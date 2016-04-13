"""
Render a card using the "mudblood" framework.
"""
import json
import os
import tempfile

from django.conf import settings
from jinja2 import Environment, FileSystemLoader
from apps.cards.models import StatType, CardType, CardArt
from apps.cards.serializers import CardRevisionSerializer


# Template Filters
def jsonify(s):
    return json.dumps(s)


def escape_newlines(s):
    return s.replace('\n', '\\n')


def type_name(s):
    return CardType.objects.get(id=s).name


def stat_name(s):
    return StatType.objects.get(id=s).name


def stat_icon(s):
    return StatType.objects.get(id=s).image.path


def background_image(s):
    t = CardType.objects.get(id=s)
    return t.background.image.path


def art_image(s):
    art = CardArt.objects.get(id=s)
    return art.image.path


def rjust(s, number, character):
    return str(s).rjust(number, character)


def markup(s):
    """Replaces [] with a background color tag and {} with fontawesome icons.
    """
    # [] Tags
    s = s.replace(
        '[', '<span font="DroidSans Bold 20" rise="1000" '
             'background="#212121" foreground="#FFFFFF"'
             'gravity="south"> '
    ).replace(']', ' </span>')

    # {} Tags
    s = s.replace(
        '{', '<span font="FontAwesome Normal">').replace('}', '</span>')
    return s


# Driver
def generate_image(revision):
    # Use the serializer to get a JSON representation of the card
    s = CardRevisionSerializer(revision)
    revision_data = s.data.copy()

    # Set up Jinja and load the template
    env = Environment(loader=FileSystemLoader(
        os.path.join(settings.BASE_DIR, 'apps', 'cards', 'templates')))
    env.filters['jsonify'] = jsonify
    env.filters['markup'] = markup
    env.filters['rjust'] = rjust
    env.filters['type_name'] = type_name
    env.filters['stat_name'] = stat_name
    env.filters['stat_icon'] = stat_icon
    env.filters['background_image'] = background_image
    env.filters['art_image'] = art_image
    env.filters['escape_newlines'] = escape_newlines
    template = env.get_template('Portrait.tml')

    # Render the image using squib
    # TODO: Can we do this without subprocess?
    filename = os.path.join(
        settings.MEDIA_ROOT, 'cards', 'renders', "{}.png".format(revision.id))

    with tempfile.TemporaryDirectory() as tmpdir:
        out_filepath = os.path.join(tmpdir, 'template.tml')
        with open(out_filepath, 'w') as outfile:
            # Render the template using jinja
            outfile.write(template.render(rev=revision_data))

        # Execute the renderer
        cmd = 'python generate_image.py {} {} {} {}'.format(
            out_filepath, 825, 1125, filename)
        os.system(cmd)
