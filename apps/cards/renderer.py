"""
Render a card using the "mudblood" framework.
"""
import json
import os
import tempfile

from django.conf import settings
from jinja2 import Template


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
    # Convert the revision into something we care about using
    card = dict(
        id=str(revision.id).rjust(3, "0"),
        background=revision.type.background.image.path,
        image=revision.art.image.path if revision.art else "",
        artist="{}" + revision.art.artist.name if revision.art else "",
        stats=revision.stats,
        title=revision.name,
        subtitle=revision.type.name,
        description=revision.description.replace('\n', '\\n'),
        deck="{}",
        table=json.dumps(revision.table),
        table_y=revision.table_y,
    )

    # Parse Markup
    _replace_markup(card, 'description')
    # _replace_markup(card, 'table')
    _replace_markup(card, 'artist')
    _replace_markup(card, 'deck')

    # Load the template
    template_file = os.path.join(
        settings.BASE_DIR, 'apps', 'cards', 'templates', 'Portrait.tml')
    with open(template_file, 'r') as infile:
        template = Template(infile.read())

    # Render the image using squib
    # TODO: Can we do this without subprocess?
    filename = os.path.join(
        settings.MEDIA_ROOT, 'cards', 'renders', "{}.png".format(revision.id))

    with tempfile.TemporaryDirectory() as tmpdir:
        out_filepath = os.path.join(tmpdir, 'template.tml')
        with open(out_filepath, 'w') as outfile:
            # Render the template using jinja
            outfile.write(template.render(card=card))

        # Execute the renderer
        cmd = 'python generate_image.py {} {} {} {}'.format(
            out_filepath, 825, 1125, filename)
        os.system(cmd)
