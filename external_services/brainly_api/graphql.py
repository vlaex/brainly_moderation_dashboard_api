import os
import base64
from http import HTTPStatus
from httpx import Client as HttpClient
from .config import Market


GRAPHQL_SERVER_URL = "https://graphql.z-dn.net"


def transform_graphql_id(graphql_id: str) -> int:
    decoded_bytes = base64.b64decode(graphql_id)
    decoded_string = decoded_bytes.decode("utf-8")

    parts = decoded_string.split(":")
    if len(parts) != 2:
        raise ValueError(f"Invalid GraphQL ID format: {decoded_string}")

    decoded_id = int(parts[1])
    return decoded_id


class GraphQLResponse:
    def __init__(self, response: dict):
        self.data = response.get("data")
        self.errors = response.get("errors") or []


class BrainlyGraphqlAPIException(Exception):
    def __init__(self, message, response: GraphQLResponse | None = None):
        self.message = message
        self.response_errors = response.errors if response else []

        super().__init__(
            self.message if len(self.response_errors) == 0 else f"{self.message}: {self.response_errors}"
        )


class BrainlyGraphQLAPI:
    _client: HttpClient

    def __init__(
        self,
        market: Market,
        token: str | None = None,
        timeout: int = 20,
        headers: dict[str, str] | None = None
    ):
        if token is None or token == "":
            token_in_env = os.environ.get(f"BRAINLY_AUTH_TOKEN_{market.value}")
            assert token_in_env, f"Brainly auth token is required for market '{market.value}'"
            token = token_in_env

        self.token = token
        self.market = market
        self.headers = headers or {}
        self.timeout = timeout

        self._client = HttpClient(
            base_url=f"{GRAPHQL_SERVER_URL}/{self.market.value}",
            headers={
                "X-B-Token-Long": self.token,
                "X-Service-Name": "moderation_dashboard_api"
            } | self.headers,
            timeout=self.timeout,
            http2=True
        )

    def _make_http_request(self, url: str, method: str, body: dict | None = None) -> dict:
        """Make a plain HTTP request to Brainly GraphQL API"""
        response = self._client.request(method, url, json=body)

        if response.status_code == HTTPStatus.BAD_GATEWAY:
            raise BrainlyGraphqlAPIException(f"Response status is {response.status_code}")
        if response.status_code == HTTPStatus.FORBIDDEN and "captcha" in response.text:
            raise BrainlyGraphqlAPIException("403 Forbidden (captcha)")

        return response.json()

    def execute_query(self, query: str, variables: dict = None) -> GraphQLResponse:
        """Execute a GraphQL query/mutation"""
        try:
            http_response = self._make_http_request(
                url="/",
                method="POST",
                body={
                    "query": query.strip(),
                    "variables": variables
                }
            )

            response = GraphQLResponse(http_response)

            if len(response.errors) > 0:
                raise BrainlyGraphqlAPIException(message="GraphQL errors", response=response)

            return response
        except BrainlyGraphqlAPIException:
            raise
        except Exception as exc:
            raise BrainlyGraphqlAPIException(str(exc)) from exc
