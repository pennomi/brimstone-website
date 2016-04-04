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
    icon = models.FileField(upload_to='decks/icons/')

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
    image = models.FileField(upload_to='cards/backgrounds/')
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
    image = models.FileField(upload_to='cards/stats/icons/')

    def __str__(self):
        return self.name


class Card(models.Model):
    """This represents a single card, which has many revisions."""
    deck = models.ManyToManyField(Deck, related_name='cards', blank=True)

    def __str__(self):
        try:
            return self.latest_revision.name
        except AttributeError:  # latest_revision isn't a CardRevision object
            return "Unknown"

    @property
    def latest_revision(self):
        try:
            return self.revisions.exclude(approved_at=None).latest()
        except CardRevision.DoesNotExist:
            return self.revisions.first()


def card_image_path(instance, filename):
    return 'artists/{}/art/{}'.format(instance.artist.id, filename)


class CardArt(models.Model):
    image = models.ImageField(upload_to=card_image_path, blank=True, null=True)
    artist = models.ForeignKey(Artist)

    def __str__(self):
        return "{} {}".format(self.image.url, self.artist.name)

    class Meta:
        verbose_name_plural = "card art"


class CardRevision(models.Model):
    # Data
    card = models.ForeignKey(
        Card, related_name='revisions', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    type = models.ForeignKey(CardType, on_delete=models.PROTECT)
    level = models.PositiveSmallIntegerField(
        blank=True, null=True, help_text="Only used for creatures (and items?)")
    art = models.ForeignKey(
        CardArt, null=True, blank=True, on_delete=models.PROTECT)
    stats = JSONField(default=[], blank=True)  # TODO: Add validation
    description = models.TextField(blank=True)

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
