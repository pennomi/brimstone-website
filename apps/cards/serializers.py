from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.cards import models


class CardRevisionSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(
        read_only=True, default=CurrentUserDefault())

    # TODO: `level` validator
    # TODO: `stats` validator
    # TODO: `art` validator

    class Meta:
        model = models.CardRevision
        read_only_fields = (
            'approved_at', 'approver', 'rejected_at', 'rejector'
        )


class CardCommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=CurrentUserDefault())

    class Meta:
        model = models.CardComment


# Below this are all generic serializer implementations
class CardArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardArt


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deck


class RulebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rulebook


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist


class CardSerializer(serializers.ModelSerializer):
    # TODO: Audit this for performance
    latest_revision = CardRevisionSerializer()
    pending_revisions = serializers.SerializerMethodField()
    approved_revisions = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_pending_revisions(self, card):
        return card.revisions.filter(approved_at=None, rejected_at=None).count()

    def get_approved_revisions(self, card):
        return card.revisions.exclude(approved_at=None).count()

    def get_comments(self, card):
        return card.comments.count()

    class Meta:
        model = models.Card


class CardBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardBackground


class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardType


class StatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatType
