## Directory uses
hardware - KiCad hardware design files

firmware - firmware source files for the hardware

cad - CAD files for the hardware

docs - MkDocs project documentation

datasheets - downloaded data sheets references of parts used in th eproject

output - generated output files such as BOM, PDF, etc

### Linking external kicad libraries

A good way to link in your personal KiCad libraies is to have them in a git repository.
and add them as a submodule

```bash
git submodule add <git-repository-url> hardware/library
```
This will add a new library directory under hardware and link it as a git submodule

The benefits is that you can still manage the libraries independently of the main project and use them across multiple projects.

## Generated Project files and directories
```
.
├── AUTHORS.rst
├── LICENSE
├── Makefile
├── README.md
├── datasheets
├── docs
│   ├── authors.md
│   ├── bom.md
│   ├── changelog.md
│   ├── checklists
│   │   ├── sample.md
│   │   └── sample2.md
│   ├── design
│   │   └── design.md
│   ├── firmware
│   │   └── overview.md
│   ├── hardware
│   │   ├── mechanical.md
│   │   └── overview.md
│   ├── index.md
│   ├── license.md
│   └── references.md
├── firmware
├── hardware
│   ├── Some Widget.kicad_pcb
│   ├── Some Widget.kicad_prl
│   ├── Some Widget.kicad_pro
│   ├── Some Widget.kicad_sch
│   └── library (git submodule)
├── mkdocs.yml
├── output
│   ├── bom
│   ├── cad
│   ├── gerber
│   └── img
├── poetry.lock
└── pyproject.toml
```
