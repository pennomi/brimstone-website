"""
Render a card using the "mudblood" framework.
"""
import json
import os

from django.conf import settings
from jinja2 import Template
from mudblood.mudblood import render_string


def _replace_markup(card, key):
    """Replaces [] with a background color tag and {} with fontawesome icons.
    """
    # [] Tags
    card[key] = card[key].replace(
        '[', '<span font="DroidSans Bold 20" rise="1000" '
             'background="#212121" foreground="#FFFFFF"'
             'gravity="south"> '
    ).replace(']', ' </span>')

    # {} Tags
    card[key] = card[key].replace(
        '{', '<span font="FontAwesome Normal">').replace('}', '</span>')


def generate_image(revision):
    print("Rendering card data...")

    # Convert the revision into something we care about using
    card = dict(
        id=str(revision.id).rjust(3, "0"),
        background=revision.type.background.image.path,
        image=revision.art.image.path if revision.art else "",
        artist="{}" + revision.art.artist.name if revision.art else "",
        stats=revision.stats,
        description=revision.description.replace('\n', '\\n'),
        deck="{}",
        table_data="",  # TODO: json.dumps(revision.table_data)
        table_y=0,  # TODO: revision.table_y
    )

    # Parse Markup
    _replace_markup(card, 'description')
    _replace_markup(card, 'table_data')
    _replace_markup(card, 'artist')
    _replace_markup(card, 'deck')

    # Load the template
    template_file = os.path.join(
        settings.BASE_DIR, 'apps', 'cards', 'templates', 'Portrait.tml')
    with open(template_file, 'r') as infile:
        template = Template(infile.read())

    # Iterate over each card and render it
    # Render the template using jinja
    layout = template.render(card=card)

    # Render the image using squib
    filename = os.path.join(
        settings.MEDIA_ROOT, 'cards', 'renders', "{}.png".format(card['id']))
    render_string(layout, 825, 1125, filename)
