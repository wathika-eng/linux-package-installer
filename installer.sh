#!/bin/bash


curl -sS https://raw.githubusercontent.com/wathika-eng/linux-package-installer/main/install -o /usr/local/bin/install


chmod +x /usr/local/bin/install


ln -s /usr/local/bin/install /usr/local/bin/install

echo "Package Installer v1.0 has been installed. You can now use 'install' to run the script."
