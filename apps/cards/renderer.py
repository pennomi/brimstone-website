"""
Render a card using the "mudblood" framework.
"""
import json
import os
import tempfile

from django.conf import settings
from jinja2 import Environment, FileSystemLoader


# Template Filters
def jsonify(s):
    return json.dumps(s)


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
    from apps.cards.serializers import CardRevisionSerializer
    s = CardRevisionSerializer(revision)
    card = s.data.copy()

    # Overwrite values strategically
    # TODO: These should be template filters
    card.update(
        id=str(revision.id).rjust(3, "0"),
        background=revision.type.background.image.path,
        image=revision.art.image.path if revision.art else "",
        subtitle=revision.type.name,
        description=revision.description.replace('\n', '\\n'),
    )

    # Set up Jinja

    # Load the template
    env = Environment(loader=FileSystemLoader(
        os.path.join(settings.BASE_DIR, 'apps', 'cards', 'templates')))
    env.filters['jsonify'] = jsonify
    env.filters['markup'] = markup
    template = env.get_template('Portrait.tml')

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
