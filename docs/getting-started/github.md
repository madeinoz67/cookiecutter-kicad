
## Initial Commit

The very first thing that should be done is to add your new project to source control, so create a git repo and push it there:

``` bash
git init
git add .
git commit -m "initial project commit"
git remote add origin git@github.com:fsmith/wireless-widget.git
git push -u origin main
```

## Github Project Settings

This template utilises [github actions](https://docs.github.com/en/actions) for the automations around release management.

!!! Note 
    To automatically publish Project Documentation to the projects "github.io" pages site, you must first enabled from github Project 
    Settings.  See this [guide](https://guides.github.com/features/pages/) for further information on how to enable this feature.

## Creating a working branch

!!! Tip
    Its not really good practice to work out of the projects Master branch for development.  This should only be reserved 
    for the stable versions of the hardware and firmware.

    Consider using working branches during your development, this is where you will add the features or bug fixes.

``` bash
git branch "some-feature"
```

e.g. `git branch "dev-rev-a"`

Any changes from now on will be committed to this branch

## Merging changes from the working branch back into the master branch

When you're ready to get the working copy back into the master branch you should use a [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests).

!!! Tip
    Don't merge directly to your master branch from your local machine.  Use Pull Requests instead
    as this keeps a detailed record of changes made and allows others to see and comment.

    Pull Requests can be directly linked to issues or feature requests from the github issue tracker.