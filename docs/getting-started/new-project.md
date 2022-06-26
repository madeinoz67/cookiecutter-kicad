Let's pretend you want to create a hardware widget called "some widget". Rather than manually 
creating the project directory structures and the documentation, get cookiecutter to do all the work.


## Run Cookiecutter
Now run cookiecutter against this repo:

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

## Enter the new project and take a look around

``` bash
cd some-widget/
ls -a
```

### Install project dependencies

``` bash
make install
<or>
poetry install
```
This will proceed to download and install all project the dependencies and create a local virtual python environment for just this project so your local environment wont be pollute or get module clashes

python modules can be added at any time to the project by using poetry:

``` bash
poetry add python_module
```
!!! Important
    Always use poetry to install project python modules not pip.


you can enter the virtual environment from anywhere in your project directory by:
``` bash
poetry shell

exit (to exit)
```

or if you want to run a command in the virtual environment:

``` bash
poetry run some_command
```
### Link in personal KiCad library (optional)

If you use a custom/personal KiCad library repository that can be linked into the project library folder, you can do so by:

1.  Add the link to the library repository as a git submodule
```bash
git add submodule git@github.com:<<gitusername>>/<<library-repo>>.git hardware/library

```
!!! Important

    replace `<<gitusername>>` with your git username.

    replace `<<library-repo>>` with the name of your KiCad library repository.


2. Update the git submodule

    ```bash
    git submodule update --remote hardware/library
    ```

### Open KiCad and open the project

1. Open up your installed version of KiCAD
2. "File | Open Project"
3. Located new project directory and navigate to the 'hardware' directory
4. Select the project file.
5. press ok