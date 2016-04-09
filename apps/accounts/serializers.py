from rest_framework import serializers

from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    def get_role(self, value):
        return {
            0: "Player",
            1: "Contributor",
            2: "Master",
        }[value.role]

    class Meta:
        model = User
        fields = (
            'id', 'username', 'role', 'image',
        )
