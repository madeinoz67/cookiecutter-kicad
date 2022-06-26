import os
from shutil import rmtree

REMOVE_PATHS = [
    '{% if cookiecutter.kicad_version != '5.x' %} kicad5 {% endif %}',
    '{% if cookiecutter.kicad_version != '6.x' %} kicad6 {% endif %}'
]

RENAME_PATH = [
    '{% if cookiecutter.kicad_version == '5.x' %} kicad5 {% endif %}',
    '{% if cookiecutter.kicad_version == '6.x' %} kicad6 {% endif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            rmtree(path)
        else:
            os.unlink(path)

# rename RENAME_PATH
for path in RENAME_PATH:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rename(path, 'hardware')
            


