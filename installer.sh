#!/bin/bash


curl -sS https://raw.githubusercontent.com/wathika-eng/linux-package-installer/main/install.py -o /usr/local/bin/installer


chmod +x /usr/local/bin/installer


ln -s /usr/local/bin/installer /usr/local/bin/installer

echo "Package Installer v1.0 has been installed. You can now use 'installer' to run the script."
