# Cookiecutter for KiCAD Projects

Powered by [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/), Cookiecutter KiCad generates boilerplate for production-ready [KiCad](https://www.kicad.org) projects.

See the [Project Documentation](https://madeinoz67.github.io/cookiecutter-kicad/) for more details.

## Features

The project you create from this template has a few features to be aware of
including:

- [x] Kicad v5.x supported.
- [x] Kicad v6.x supported.
- [x] KiCad v8.x supported.
- [x] A [KiCAD](https://www.kicad.org/) project structure to get you going.
- [x] A starting project document structure using [Mkdocs-Materials](https://squidfunk.github.io/mkdocs-material/) that automatically publishes to the projects github.io pages site on release. Inspiration for the document structure is based on the <https://hutscape.com/pine/> by Sayanee Basu <https://github.com/sayanee> and her great YouTube video around hardware documentation <https://youtu.be/uPitFGqjyPU>.
- [x] Automated Release and Changelog management.
- [ ] Automated asset generation that incorporates into the documentation build, e.g. BOM, Schematics, PCB, 3D Board Images.
- [ ] CICD pipeline for Hardware and Firmware testing.
- [x] [Poetry](https://python-poetry.org/) Python Virtual Environment and dependency management for the project.
- [x] [mermaid](https://mermaid-js.github.io/mermaid/#/) diagrams using markdown syntax.
- [ ] [wavedrom](https://github.com/wavedrom/wavedrom) waveform diagrams using markdown syntax.

## Usage

Let's pretend you want to create a hardware widget called "some widget". Rather than manually 
creating the project directory structures and the documentation, get cookiecutter to do all the work.

First, get Cookiecutter:

``` bash
pip install "cookiecutter>=1.4.0"`
```

Now run it against this repo:

``` bash
cookiecutter https://github.com/madeinoz67/cookiecutter-kicad
```

You'll be prompted for some values. Provide them, then a project structure will be created for you.

Warning: After this point, change 'Fred Smith', 'fsmith', etc to your own
information.

Answer the prompts with your own desired options. For example:

``` bash
Cloning into 'cookiecutter-kicad'...
remote: Counting objects: 550, done.
remote: Compressing objects: 100% (310/310), done.
remote: Total 550 (delta 283), reused 479 (delta 222)
Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
Resolving deltas: 100% (283/283), done.
project_name [Project Name]: Some Widget
project_repo_name [repo-name]: some-widget
project_description [This is my Kicad Project]: A Hardware Widget
author_name [my_name]: Fred Smith
author_email [my_email@somewhere.com]: fsmith@nowhere.com
github_user [my_gihub_username]: fsmith
Select kicad_version:
1 - 6.x
2 - 5.x
Choose from 1, 2 [1]: 1
Select license:
1 - CC-A-SA
2 - CC-A
3 - MIT
4 - BSD
5 - OSHD
6 - TAPR
7 - CERN-OHL-P
Choose from 1, 2, 3, 4, 5, 6, 7 [1]:
```

Enter the project and take a look around:

``` bash
cd some-widget/
ls -a
```

Create a git repo and push it there:

``` bash
git init
git add .
git commit -m "initial project commit"
git remote add origin git@github.com:fsmith/wireless-widget.git
git push -u origin master
```

## Open KiCad and open the project

If you have performed the steps above, you should now be able to open KiCad and open the new project.

## Resources

Would you like to learn more?  Check out the links below!

* [Cookiecutter Project
  Documentation](https://cookiecutter.readthedocs.io/en/latest/)
* [Cookiecutter: Project Templates Made
  Easy](https://www.pydanny.com/cookie-project-templates-made-easy.html)
* [KiCAD](https://www.kicad.org)
* [mkdocs-materials](https://squidfunk.github.io/mkdocs-material/)
* [poetry](https://python-poetry.org/)

## Author

This program was created by [Stephen Eaton](https://github.com/madeinoz67).

This project is [hosted on GitHub](https://github.com/madeinoz67/cookiecutter-kicad). Please feel free to submit pull requests.

## License

Copyright © 2021 Stephen Eaton. This program is released under the GPLv3 license, which you can find in the file [LICENSE](LICENSE).
