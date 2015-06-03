# Mac OSX Versions Cleaner

A script that scrubs the document version history from Mac OSX systems

## Instructions

### Get the Script

You can manually download a [zip file](https://github.com/chrissimpkins/macosx-versions-cleaner/archive/master.zip) or [tar archive file](https://github.com/chrissimpkins/macosx-versions-cleaner/archive/master.tar.gz)

or pull the repository to your machine with git:

```sh
git clone https://github.com/chrissimpkins/macosx-versions-cleaner.git
```

### Usage

Navigate to the `version_cleaner.py` file in the repository and execute the command:

```sh
sudo python version_cleaner.py
```

The script will ask if you would like to reboot to complete the cleanup process.  Enter `y` or `n` to complete the cleaning process.

If you choose not to reboot your system at the completion of the cleanup, you will not be able to save document versions in applications that use them until you perform a manual reboot.


