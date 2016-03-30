from rest_framework import viewsets

from apps.cards import models
from apps.cards import serializers


# TODO: Permissions
class CardRevisionViewSet(viewsets.ModelViewSet):
    queryset = models.CardRevision.objects.all()
    serializer_class = serializers.CardRevisionSerializer

    def create(self, request, *args, **kwargs):
        # If no Card is given, this is a new suggestion. Add the Card first.
        if not request.data.get('card'):
            c = models.Card.objects.create()
            request.data['card'] = c.id

        # Continue as normal
        return super().create(request, *args, **kwargs)

    # TODO: approve/reject detail routes


# TODO: Permissions
class CardCommentViewSet(viewsets.ModelViewSet):
    queryset = models.CardComment.objects.all()
    serializer_class = serializers.CardCommentSerializer


# Read-only ViewSets Below here
class CardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer


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


class CardArtViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CardArt.objects.all()
    serializer_class = serializers.CardArtSerializer


class StatTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.StatType.objects.all()
    serializer_class = serializers.StatTypeSerializer
