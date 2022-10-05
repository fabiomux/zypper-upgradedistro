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

The optional switches provided have the sole purpose to skip one of the steps that
block the completion of the upgrade.

Of course the reason to do that should be well ponderated, for example:
- the openSUSE server is temporarily off and doesn't provide the page where the last
  release number is served, we can skip this step if we know that a new release is available;
- A no critical repository is offline and can't get updates, instead of disable it we can decide
  to skip the last update but still upgrade it;
- A no critical package can't be upgraded without a new download, but having switched to
  the console mode we can skip the upgrade of that package and fix it later.

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
$ zypper upgradedistro --help
```

## More help

More info is available at:
- the [project page][project_page] on Freeaptitude blog;
- the article [Upgrading with zypper_upgradedistro][upgrading_with_zypper_upgradedistro] on Freeaptitude blog;
- the article [Upgrading openSUSE with Zypper][upgrading_with_zypper] on Freeaptitude blog.


[upgrading_with_zypper_upgradedistro]: https://freeaptitude.altervista.org/articles/upgrading-opensuse-leap-with-zypper-upgradedistro.html "Upgrading openSUSE with Zypper-Upgradedistro"
[upgrading_with_zypper]: https://freeaptitude.altervista.org/articles/upgrading-opensuse-with-zypper.html "Upgrading openSUSE with Zypper"
[zypper_upgraderepo]: https://github.com/fabiomux/zypper-upgraderepo "Github page of the zypper-upgraderepo project"
[project_page]: https://freeaptitude.altervista.org/projects/zypper-upgradedistro.html "Zypper-Upgraderepo project page"

