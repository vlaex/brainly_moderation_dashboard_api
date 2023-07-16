from rest_framework import serializers
from .models import Moderator


class ModeratorSerializer(serializers.ModelSerializer):
    #mentor = serializers.SerializerMethodField()

    #def get_mentor(self, moderator):
    #    if moderator.mentor:
    #        return ModeratorSerializer(moderator.mentor).data
    #    return None

    class Meta:
        model = Moderator
        exclude = ["password"]
