import os
import requests
import subprocess
import sys

def get_desktop_path():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def read_local_version(version_file_path):
    if os.path.exists(version_file_path):
        with open(version_file_path, "r") as f:
            return f.read().strip()
    return "0.0"  # Default version if the file doesn't exist

def write_local_version(version_file_path, version):
    with open(version_file_path, "w") as f:
        f.write(version)

def check_for_update(current_version, version_file_path):
    version_url = "https://raw.githubusercontent.com/Aidwyd/Ni/main/version"
    
    try:
        response = requests.get(version_url)
        latest_version = response.text.strip()

        if latest_version > current_version:
            print(f"New version {latest_version} is available! Downloading the update...")
            download_update()
            write_local_version(version_file_path, latest_version)
        else:
            print("You are using the latest version.")
    except Exception as e:
        print(f"Failed to check for updates: {e}")

def download_update():
    update_url = "https://raw.githubusercontent.com/Aidwyd/Ni/main/BediumACL.exe"

    try:
        # Open the browser to download the file
        subprocess.run(['start', update_url], shell=True)
        print("Update is being downloaded in your browser.")
    except Exception as e:
        print(f"Failed to open the browser for the update: {e}")

if __name__ == "__main__":
    version_file_path = os.path.join(get_desktop_path(), "current_version.txt")

    current_version = read_local_version(version_file_path)

    check_for_update(current_version, version_file_path)
