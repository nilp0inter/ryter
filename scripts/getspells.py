"""
Gets the list of spells of Harry Potter from Wikipedia and writes
`behave` feature files.

"""
import os
import re
import sys
import warnings

from jinja2 import Template

import wikipedia


TITLE_RE = re.compile(
    r"^(?P<incantation>.*?)\s?(?:\((?P<vernacular>.*)\))?\s===$")
KV_RE = re.compile(r"^(\S+):\s(.*)$")
FEATURE_TEMPLATE = Template("""Feature: {% if incantation %}{{ incantation }}{% endif %}{% if incantation and vernacular %} {% endif %}{% if vernacular %}({{ vernacular }}){% endif %}

    {% if description %}{{ description|wordwrap(75, False)|indent(4) }}{% endif %}

    Pronunciation:{% if pronunciation %}
        {{ pronunciation|wordwrap(71, False)|indent(8) }}{% else %} - {% endif %}
    Seen/mentioned:{% if seen_mentioned %}
        {{ seen_mentioned|wordwrap(71, False)|indent(8) }}{% else %} - {% endif %}
    Suggested etymology:{% if suggested_etymology %}
        {{ suggested_etymology|wordwrap(71, False)|indent(8) }}{% else %} - {% endif %}
    Notes:{% if notes %}
        {{ notes|wordwrap(71, False)|indent(8) }}{% else %} - {% endif %}
""")


def parse_spell(raw_spell):
    spell = {}

    lines = raw_spell.split('\n')

    title = TITLE_RE.search(lines[0])
    if title:
        spell.update(dict((k, v) for k, v in title.groupdict().items() if v))
        key = value = None
        for line in lines:
            if line.startswith('='):  # Title, skip.
                continue
            else:
                data = KV_RE.search(line)
                if data:
                    key, value = data.groups()
                    key = normalize_str(key).lower()
                elif value:  # Continuation line
                    value += line
                else:
                    continue
            spell[key] = value

    return spell 


def render_feature(spell):
    return FEATURE_TEMPLATE.render(**spell)


def normalize_str(s):
    return re.sub('\W', '_', s)


if __name__ == '__main__':
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print("argument must be the output directory")
        sys.exit(2)
    else:
        os.chdir(sys.argv[1])

    reference = wikipedia.page("List_of_spells_in_Harry_Potter")
    raw_spells = reference.content.split("\n=== ")[1:]

    for raw_spell in raw_spells:
        spell = parse_spell(raw_spell)
        if spell:
            if 'incantation' in spell:
                filename = normalize_str(spell['incantation'])
            elif 'vernacular' in spell:
                filename = normalize_str(spell['vernacular'])
            else:
                warnings.warn("Unknown spell name %r" % spell)
                continue

            filename += '.feature'
            if os.path.exists(filename):
                continue
            else:
                with open(filename, 'w') as f:
                    f.write(render_feature(spell))
