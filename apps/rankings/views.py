from typing import TypedDict
from datetime import timedelta
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ModeratorRanking
from external_services.brainly_api import BrainlyGraphQLAPI, Market, transform_graphql_id


class RankingPlace(TypedDict):
    place: int
    points: int
    user_id: int


class GetDailyRankings(APIView):
    def get(self, request):
        market = Market.US

        graphql_api = BrainlyGraphQLAPI(market=market)
        gql_res = graphql_api.execute_query("""
        query GetModeratorRanking {
        userRankings(rankingType: MODERATOR_DAILY) {
            points
            user {id}
        }
        }
        """)

        bulk_data: list[ModeratorRanking] = []
        for place in gql_res.data["userRankings"]:
            user_id = transform_graphql_id(place["user"]["id"])
            user_global_id = f"{market.value}:{user_id}"

            bulk_data.append(
                ModeratorRanking(
                    moderator_id=user_global_id,
                    value=place["points"],
                    market=market.value,
                    time=timezone.now()
                )
            )

        #moderators =

        #rows = ModeratorRanking.objects.bulk_create(bulk_data)

        #print(rows)
        return Response("OK")
        #return Response(places)
        #range = (timezone.now() - timedelta(days=1), timezone.now())

        #rankings = ModeratorRanking.timescale.select_related("moderator").filter(time__range=range).time_bucket("time", "2 hours")
        #print(rankings)
        #return Response("hello")
        # items = Item.objects.all()
        # serializer = ItemSerializer(items, many=True)
        # return Response(serializer.data)
