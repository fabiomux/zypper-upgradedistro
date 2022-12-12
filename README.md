# Zypper-Upgradedistro

Command line script which works as an assistant for the Linux openSUSE Leap distribution upgrade.

The main goal is to guide through the process step by step as in the [article from Freeaptitude blog][upgrading_with_zypper],
handling the common problems and trying to find a proper solution.

It heavily rely on the [zypper-upgraderepo application][zypper_upgraderepo] to check and upgrade repositories,
so you must install it first.

## Installation

There are several options to install the service menus listed in this repository.

### From the openSUSE Build Service repository

This application has been packaged in my personal OBS repository so you can install It
as a common RPM package:
- Add the repository URL in your list;
- install the package from Yast or Zypper.

Being the repository URL slightly changing from a version to another, I included all the steps
in the related [project page][project_page] on my blog.

### From the GitHub repository

Once cloned the repository locally:
```shell
$ git clone https://github.com/fabiomux/upgradedistro.git
```

Enter the project folder:
```shell
$ cd zypper-upgradedistro
```

Run the Makefile task to install it:
```shell
$ make install
```

Or uninstall it:
```shell
$ make uninstall
```

It will automatically install the script and the Zypper plugin with the related man page.

## Usage

```shell
$ upgradedistro [<options>]
```

Or as zypper plugin:
```shell
$ zypper upgradedistro [<options>]
```

Being an interactive script it is enough to launch the script and follow the steps.

Output messages will appear from time to time to:
- inform about the current action;
- ask for confirmations where needed;
- notice errors and provide a solution.

The messages should be helpful enough to drive through the process safely.

### Options

The optional switches provided have the sole purpose to skip one of the steps that
might block the completion of the upgrade, or the already completed tasks.

Using the `--resume` option will automatically restart the script from the latest
completed task.

This is the full list of the available options:
<dl>
  <dt>--allow-unstable (-U):</dt>
  <dd>Allow unstable releases to be considered as an option</dd>

  <dt>--no-version-check (-v):</dt>
  <dd>Skip the release version check</dd>

  <dt>--no-system-update (-s)</dt>
  <dd>Skip the system update</dd>

  <dt>--no-repository-check (-c):</dt>
  <dd>Skip the repository check procedure</dd>

  <dt>--no-repository-upgrade (-u):</dt>
  <dd>Skip the repository upgrade procedure</dd>

  <dt>--no-repository (-r)</dt>
  <dd>Skip both the repository check and upgrade procedures</dd>

  <dt>--no-packages (-p)</dt>
  <dd>Skip the download of the packages to be upgraded</dd>

  <dt>--resume</dt>
  <dd>Restart from the last step left</dd>
</dl>

Skipping the steps individually should be well ponderated, and reserved to specific situations,
for example:
- when the openSUSE server is temporarily off and doesn't provide the page where the last
  release number is served, we can skip this step if we know that a new release is available;
- A no critical repository is offline and can't get updates, instead of disable it we can decide
  to skip the update task and still upgrade it;
- A no critical package can't be upgraded without a new download, thus we can skip the upgrade
  of that package and fix it later.

### The default editor

When repositories don't get a valid URL by the *zypper-upgraderepo* script, a list of invalid but
still enabled repositories is exported in an INI file to disable or update the URLs without
interrupting the script.
To do that, the editor in the *$EDITOR* variable will be used, if none, *vim* will be the default
choice.
If you want to switch to a more familiar editor you must override this variable before lauching
the *upgradedistro* command:
```shell
$ EDITOR='nano' upgradedistro ...
```
Or
```shell
$ EDITOR='nano' zypper upgradedistro ...
```

## Get help

When this plugin is correctly installed you can see it in the list of subcommands:
```shell
$ zypper help subcommand
```

Read the man page with:
```shell
$ zypper help upgradedistro
```

For a quick help:
```shell
$ upgradedistro --help
```

## More help

More info is available at:
- the [project page][project_page] on Freeaptitude blog;
- the article [Upgrading with zypper-upgradedistro][upgrading_with_zypper_upgradedistro] on Freeaptitude blog;
- the article [Upgrading openSUSE with Zypper][upgrading_with_zypper] on Freeaptitude blog.


[upgrading_with_zypper_upgradedistro]: https://freeaptitude.altervista.org/articles/upgrading-opensuse-leap-with-zypper-upgradedistro.html "Upgrading openSUSE with Zypper-Upgradedistro"
[upgrading_with_zypper]: https://freeaptitude.altervista.org/articles/upgrading-opensuse-with-zypper.html "Upgrading openSUSE with Zypper"
[zypper_upgraderepo]: https://github.com/fabiomux/zypper-upgraderepo "Github page of the zypper-upgraderepo project"
[project_page]: https://freeaptitude.altervista.org/projects/zypper-upgradedistro.html "Zypper-Upgraderepo project page"

