import os
import sys

REMOVE_PATHS = [
    '{% if cookiecutter.kicad.version != '5' %} kicad5 {% endiif %}',
    '{% if cookiecutter.kicad.version != '6' %} kicad6 {% endiif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)