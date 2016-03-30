import itertools

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models


class Rulebook(models.Model):
    version = models.IntegerField()
    download = models.FileField(upload_to='rules/downloads/')

    def __str__(self):
        return "Version {}".format(self.version)


class Deck(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='decks/icons/')

    def __str__(self):
        return self.name


# TODO: Take this logic and move it into a CardType fixture
TYPES = tuple(" ".join(v).strip() for v in itertools.chain(
    itertools.product(
        ('Basic', 'Passive', ''),
        ('Combat Power', 'Noncombat Power')
    ),

    # Creatures
    ('Creature', ),

    # Items
    itertools.product(
        ('Mundane', 'Rare', 'Epic', ),
        ('Consumable',
         'Wearable Head', 'Wearable Neck', 'Wearable Shoulder', 'Wearable Arm',
         'Wearable Hand', 'Wearable Chest', 'Wearable Belt', 'Wearable Leg',
         'Wearable Foot', 'Wearable Ring', ),
        ('Item', )
    ),
))


class Artist(models.Model):
    """The attribution info needed for card art."""
    name = models.CharField(max_length=64)
    attribution_instructions = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CardBackground(models.Model):
    """Each unique card background is uploaded here."""
    name = models.CharField(max_length=16)
    image = models.ImageField(upload_to='cards/backgrounds/')
    has_art = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CardType(models.Model):
    """The card's subtitle is generated off of this."""
    name = models.CharField(max_length=32)
    background = models.ForeignKey(CardBackground)

    def __str__(self):
        return self.name


class StatType(models.Model):
    """A name and icon for each of the unique stat block types on the card."""
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='cards/stats/icons/')

    def __str__(self):
        return self.name


class Card(models.Model):
    """This represents a single card, which has many revisions."""
    deck = models.ManyToManyField(Deck, related_name='cards', blank=True)

    def __str__(self):
        try:
            return self.revisions.latest().name
        except CardRevision.DoesNotExist:
            return "Unknown"


def card_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cards/images/<id>/<filename>
    return 'cards/images/{}/{}'.format(instance.id, filename)


class CardRevision(models.Model):
    # Data
    card = models.ForeignKey(
        Card, related_name='revisions', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    type = models.ForeignKey(CardType, on_delete=models.PROTECT)
    level = models.PositiveSmallIntegerField(
        blank=True, null=True, help_text="Only used for creatures (and items?)")
    image = models.ImageField(upload_to=card_image_path, blank=True, null=True)
    artist = models.ForeignKey(
        Artist, null=True, blank=True,
        help_text="Required if an image is uploaded.")
    stats = JSONField(default={})  # TODO: Add validation

    # Audit Trail
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='cards_submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    approver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='cards_approved',
        blank=True, null=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    rejector = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='cards_rejected',
        blank=True, null=True)
    rejected_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-approved_at', )
        get_latest_by = "approved_at"

    def __str__(self):
        return self.name


class CardComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    card = models.ForeignKey(Card, related_name='comments')
    text = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
