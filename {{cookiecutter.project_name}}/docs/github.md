
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

## Github Actions

This project uses github actions to manage the release process.  The actions are defined in the `.github/workflows` directory.

### troubleshooting

If you're having problems with the actions failing, you can view the logs by clicking on the "Actions" tab in your repository.  You'll see a list of all the actions that have been run for this projec

A common problem is the actions do not have write permissions to the repository. The error reported in the actions will be something along the lines of "fatal: unable to access 'https://github.com/your_repository_url/': The requested URL returned error: 403"

You can fix this by doing either of the following:

1. Adding a [Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to the repository secrets.  You can add this token by going to the repository settings, then "Secrets" tab.
2. You can also fix this by allowing actions read/write access from the repository settings | Actions | general | Workflows permissions.  The default is Read Only, Change this to Read and Write.

Once resolved you can rerun the failed action by clicking on the "Re-run jobs" button.

## Versioning

The versioning scheme is based on [Semantic Versioning](https://semver.org/).  This means that the version number is incremented in the following order: Major, Minor, Patch.

## Changelog

The changelog is generated using [changelog-maker](https://github.com/michaelbausor/changelog-maker).  This tool will automatically generate a new changelog based on the commits since the last tag.

## Release Process

The release process is managed by [Github Actions](https://docs.github.com/en/actions).  When a new tag is pushed to master, the following steps will be performed:

 1. Bump the version number in the `pyproject.toml` file to next version number. This is done by manually editing the file.
 2. Commit Changes and push them back up to github
 3. Pull the latest changes from the master branch into the working copy as will autogenerate CHANGELOG.md
 4. Tag the latest commit with the new version number and push it back to github.  The action looks for a tag that matches `v*.*.*` e.g. `v1.0.0` or `v2025.1.1` tags not having the `v` prefix will be ignored.
 5. The release process will also build documentation and push to the projects github.io pages site.
