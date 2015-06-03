# Mac OSX Versions Cleaner

A script that scrubs the document version history from Mac OSX systems.

**Warning**: This script deletes all previous versions of all documents for all applications that use Mac OSX document versioning.  Please understand what you are doing and confirm that you do not need prior versions before you use this script.  A Time Machine backup is highly recommended prior to use.

It **does not** delete the current versions of these documents.

## Background

The Mac OSX Versions feature provides an automatic document versioning tool that allows you to recover up to *hundreds* of prior document changes in commonly used applications such as Pages, Preview, Numbers, as well as in many third party applications.  Not all users require this feature and [in certain cases](https://medium.com/thomasdegry/how-sketch-took-over-200gb-of-our-macbooks-cb7dd10c8163) it leads to the loss of a significant amount of storage space on your system (hundreds of GB).  This feature was introduced in Mac OSX Lion and Apple documentation is available [here](https://support.apple.com/en-us/HT202255).

This script eliminates all stored document versions from your Mac OSX v 10.7+ system (OSX Lion through current).

## Instructions

### Dependency

Requires Python v2.x or v3.x

### Get the Script

You can manually download a [zip archive](https://github.com/chrissimpkins/macosx-versions-cleaner/archive/master.zip) or [tar archive](https://github.com/chrissimpkins/macosx-versions-cleaner/archive/master.tar.gz) of the repository

or pull the repository to your machine with git:

```sh
git clone https://github.com/chrissimpkins/macosx-versions-cleaner.git
```

### Usage

Navigate to the `version_cleaner.py` file in the repository and execute the command:

```sh
sudo python version_cleaner.py
```

The script will ask if you would like to reboot to complete the cleanup process.  Enter `y` or `n`.

If you choose not to reboot your system, you will not be able to save document versions in applications that use them until you perform a manual reboot.


### Discontinue Future Versioning in Applications

Use the following command in your terminal application:

```sh
defaults write -app ‘<appname>’ ApplePersistence -bool no
```

replacing `<appname>` with the application that uses the Versions feature.

### Cleanup

You can safely delete the entire Mac OSX Versions Cleaner repository after use.  Or, keep it around to use down the road when document versions pile up again.


