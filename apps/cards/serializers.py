from rest_framework import serializers

from apps.cards import models


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
    class Meta:
        model = models.Card


class CardBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardBackground


class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardType


class CardRevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardRevision


class CardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardComment


class StatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatType
