#!/bin/bash


curl -sS https://raw.githubusercontent.com/wathika-eng/linux-package-installer/main/install -o /usr/local/bin/package_installer.py


chmod +x /usr/local/bin/package_installer.py


ln -s /usr/local/bin/package_installer.py /usr/local/bin/package-installer

echo "Package Installer v1.0 has been installed. You can now use 'install' to run the script."
