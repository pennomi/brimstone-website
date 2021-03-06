import base64

from django.db import transaction
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from apps.cards import models
from apps.cards import serializers
from apps.cards import permissions
from apps.cards.renderer import generate_image


class CardRevisionViewSet(viewsets.ModelViewSet):
    """##Filters:
     - `?card=<id>` Filter by card id
    """
    queryset = models.CardRevision.objects.all()
    serializer_class = serializers.CardRevisionSerializer
    permission_classes = [permissions.CardRevisionPermission]

    def get_queryset(self):
        q = super().get_queryset()

        # Apply filters
        params = self.request.query_params
        if params.get('card'):
            q = q.filter(card_id=params.get('card'))
        return q

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            # If no Card is given, this is a new suggestion. Add the Card first.
            if not request.data.get('card'):
                c = models.Card.objects.create()
                request.data['card'] = c.id

            # Continue as normal
            return super().create(request, *args, **kwargs)

    @list_route(methods=['POST'])
    def preview(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = generate_image(serializer.data)
        b64 = base64.b64encode(data)
        return HttpResponse(b"data:image/PNG;base64," + b64, status=200)

    @detail_route(
        methods=['POST'],
        permission_classes=[permissions.CardRevisionApprovalPermission])
    def approve(self, request, pk=None):
        revision = self.get_object()
        revision.approver = request.user
        revision.approved_at = timezone.now()
        revision.save()
        return Response({}, status=200)

    @detail_route(
        methods=['POST'],
        permission_classes=[permissions.CardRevisionApprovalPermission])
    def reject(self, request, pk=None):
        revision = self.get_object()
        revision.rejector = request.user
        revision.rejected_at = timezone.now()
        revision.save()
        return Response({}, status=200)


class CardCommentViewSet(viewsets.ModelViewSet):
    queryset = models.CardComment.objects.all()
    serializer_class = serializers.CardCommentSerializer
    permission_classes = [permissions.CardCommentPermission]

    def get_queryset(self):
        q = super().get_queryset()

        # Apply filters
        params = self.request.query_params
        if params.get('card'):
            q = q.filter(card_id=params.get('card'))
        return q


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
