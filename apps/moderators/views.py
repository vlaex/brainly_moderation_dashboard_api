from django.http import HttpRequest, JsonResponse
from .models import Moderator
from .serializers import ModeratorSerializer


def index(request: HttpRequest):
    Moderator.objects.filter(user_id__in=[18076564]).delete()
    Moderator.objects.create(
        global_id="ru:18076564",
        user_id=18076564,
        nick="andrewss",
        ranks=(2, 3),
        market="ru"
    )

    moderators = Moderator.objects.all()
    #mentees = moderator.mentees.filter(pk=2).defer("mentor", "joined_at")

    return JsonResponse(ModeratorSerializer(moderators, many=True).data, safe=False)

    # return JsonResponse(ModeratorSerializer(moderator).data)


def create(request: HttpRequest):
    Moderator.objects.filter(pk__in=[1, 2]).delete()

    moderator_1 = Moderator.objects.create(
        id=1,
        nick="andrewss",
        ranks=(2, 3),
    )
    moderator_2 = Moderator.objects.create(
        id=2,
        nick="agetnor",
        ranks=(),
        mentor=moderator_1
    )

    return JsonResponse({
        "moderator_1": ModeratorSerializer(moderator_1).data,
        "moderator_2": ModeratorSerializer(moderator_2).data
    })
