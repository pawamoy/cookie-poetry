import os
import shutil

from jinja2 import Environment, FileSystemLoader


def get_context():
    """As hooks are executed rendered, it will return a context dict."""
    context = {"cookiecutter": {
    {%- for key, value in cookiecutter.items()|sort %}
        "{{ key }}": {{ "{0!r}".format(value) }},
    {% endfor -%}
    } }
    return context


def render_template(source, target):
    """Utility function to render a source template in a target file."""
    env = Environment(loader=FileSystemLoader('.'), keep_trailing_newline=True)
    template = env.get_template(source)
    context = get_context()
    rendered = template.render(context)
    with open(target, 'w') as stream:
        stream.write(rendered)


def copy_license():
    """Copy the selected rendered license to the LICENSE file."""
    target = 'LICENSE'
    source = os.path.join(
        'licenses',
        '{{ cookiecutter.copyright_license }}'
            .replace('"', '')
            .replace("'", '')
            .replace('/', '-')
            .replace(' ', '_'))

    shutil.copyfile(source, target)
    shutil.rmtree('licenses')


copy_license()
