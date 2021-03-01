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

!!! Warning
    After this point, change 'Fred Smith', 'fsmith', etc. to your own
    information.

Answer the prompts with your own desired options. For example:

``` bash
Cloning into 'cookiecutter-kicad'...
remote: Counting objects: 550, done.
remote: Compressing objects: 100% (310/310), done.
remote: Total 550 (delta 283), reused 479 (delta 222)
Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
Resolving deltas: 100% (283/283), done.
project_name [my-kicad-project]: some widget 
project_github_repo_name [repo-name]: some-widget
project_description [This is my Kicad Project]: A hardware widget based on an ESP32
author_name [my_name]: Fred Smith
author_email [my_email@somewhere.com]: fsmith@somewhere.com
Select license:
1 - CC-A-SA
2 - CC-A
3 - MIT
4 - BSD
5 - OSHD
6 - TAPR
7 - CERN-OHL-P
Choose from 1, 2, 3, 4, 5, 6, 7 [1]:
github_user [my_github_user]: fsmith
```

Enter the project and take a look around:

``` bash
cd some-widget/
ls -a
```

## Open KiCad and open the project

1. Open up your installed version of KiCAD
2. "File | Open Project"
3. Located new project directory and navigate to the 'kicad_pcb' directory
4. Select the 'some-widget.pro' file.
5. press ok