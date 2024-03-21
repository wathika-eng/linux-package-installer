# AUTHORS - WATHIKA
# DATE - 2024-03-21
# VERSION - 1.0
# LANGUAGE - PYTHON
# ABOUT - A simple package installer that searches for a package in APT and Snap, checks if it is already installed, and installs it if it is not.


import subprocess
import argparse
from colorama import init, Fore, Style
from tqdm import tqdm


def search_package(package_name):
    """Search for a package in APT and Snap.

    Args:
        package_name (str): The name of the package to search for.

    Returns:
        tuple: A tuple containing the search results from APT and Snap.
    """
    apt_process = subprocess.Popen(
        ["apt", "search", package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    apt_output, _ = apt_process.communicate()

    snap_process = subprocess.Popen(
        ["snap", "find", package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    snap_output, _ = snap_process.communicate()

    return apt_output.decode(), snap_output.decode()


def check_package_installed(package_name):
    """Check if a package is already installed.

    Args:
        package_name (str): The name of the package to check.

    Returns:
        bool: True if the package is installed, False otherwise.
    """
    apt_check_process = subprocess.Popen(
        ["dpkg", "-l", package_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    apt_check_output, _ = apt_check_process.communicate()

    snap_check_process = subprocess.Popen(
        ["snap", "list", package_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    snap_check_output, _ = snap_check_process.communicate()

    return (
        "Status: install ok installed" in apt_check_output.decode()
        or package_name in snap_check_output.decode()
    )


def install_package(package_name):
    """Install a package using APT or Snap.

    Args:
        package_name (str): The name of the package to install.
    """
    if check_package_installed(package_name):
        print(
            f"{Fore.YELLOW}Package '{package_name}' is already installed.{Style.RESET_ALL}"
        )
        return

    apt_output, snap_output = search_package(package_name)

    if package_name.encode() in apt_output.encode():
        print(f"{Fore.GREEN}Package found in APT!{Style.RESET_ALL}")
        install_process = subprocess.Popen(
            ["sudo", "apt", "install", "-y", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        with tqdm(
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            miniters=1,
            desc=f"Downloading {package_name}",
        ) as progress:
            for line in install_process.stdout:
                progress.update(len(line))
        install_output, _ = install_process.communicate()
        print(install_output.decode())
    elif package_name.encode() in snap_output.encode():
        print(f"{Fore.GREEN}Package found in Snap!{Style.RESET_ALL}")
        install_process = subprocess.Popen(
            ["sudo", "snap", "install", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        with tqdm(
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            miniters=1,
            desc=f"Downloading {package_name}",
        ) as progress:
            for line in install_process.stdout:
                progress.update(len(line))
        install_output, _ = install_process.communicate()
        print(install_output.decode())
    else:
        print(f"Package '{package_name}' not found.")


def main():
    """Main function to parse command-line arguments and install packages.
    Initialize colorama and print a welcome message.
    """
    init()
    print(
        f"{Fore.BLUE}Welcome to Package Installer v1.0\n Support the developer!{Style.RESET_ALL}"
    )
    parser = argparse.ArgumentParser(description="Install packages")
    parser.add_argument(
        "package_name", nargs="?", help="Name of the package to install"
    )
    args = parser.parse_args()

    if args.package_name:
        install_package(args.package_name)
    else:
        while True:
            package_name = input("Enter the name of the package to install: ")
            if package_name:
                install_package(package_name)
                break
            else:
                print("Please enter a package name.")


if __name__ == "__main__":
    main()
