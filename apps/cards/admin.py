from django.contrib import admin

from apps.cards import models


@admin.register(models.Deck)
class DeckAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rulebook)
class RulebookAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CardArt)
class CardArtAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CardBackground)
class CardBackgroundAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CardType)
class CardTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CardRevision)
class CardRevisionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CardComment)
class CardCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StatType)
class StatTypeAdmin(admin.ModelAdmin):
    pass
