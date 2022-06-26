import os
import sys

REMOVE_PATHS = [
    '{% if cookiecutter.kicad_version != '5.x' %} kicad5 {% endiif %}',
    '{% if cookiecutter.kicad_version != '6.x' %} kicad6 {% endiif %}'
]

RENAME_PATH = [
    '{% if cookiecutter.kicad_version == '5.x' %} kicad5 {% endiif %}',
    '{% if cookiecutter.kicad_version == '6.x' %} kicad6 {% endiif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

# rename RENAME_PATH
for path in RENAME_PATH:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rename(path, 'hardware')
            


