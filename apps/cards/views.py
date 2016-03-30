from rest_framework import viewsets

from apps.cards import models
from apps.cards import serializers


class CardViewSet(viewsets.ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer


class CardRevisionViewSet(viewsets.ModelViewSet):
    queryset = models.CardRevision.objects.all()
    serializer_class = serializers.CardRevisionSerializer


class CardCommentViewSet(viewsets.ModelViewSet):
    queryset = models.CardComment.objects.all()
    serializer_class = serializers.CardCommentSerializer


# Read-only ViewSets Below here
class DeckViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Deck.objects.all()
    serializer_class = serializers.DeckSerializer


class RulebookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Rulebook.objects.all()
    serializer_class = serializers.RulebookSerializer


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class CardBackgroundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CardBackground.objects.all()
    serializer_class = serializers.CardBackgroundSerializer


class CardTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CardType.objects.all()
    serializer_class = serializers.CardTypeSerializer


class StatTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.StatType.objects.all()
    serializer_class = serializers.StatTypeSerializer
