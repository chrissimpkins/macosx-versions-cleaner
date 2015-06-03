# Mac OSX Versions Cleaner

A script that scrubs the document version history from Mac OSX systems

**Warning**: This script deletes all previous versions of all documents for all applications that use Mac OSX document versioning.  Please understand what you are doing and confirm that you do not need prior versions before you use this script.  A Time Machine backup is highly recommended before the use of this script.

## Instructions

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

If you choose not to reboot your system at the completion of the cleanup, you will not be able to save document versions in applications that use them until you perform a manual reboot.


