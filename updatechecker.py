import os
import requests

# URLs for the version, update checker, and executable
version_url = "https://raw.githubusercontent.com/Aidwyd/Ni/main/version"
update_checker_url = "https://raw.githubusercontent.com/Aidwyd/Ni/main/updatechecker"
new_exe_url = "https://raw.github.com/Aidwyd/Ni/blob/main/BediumACL.exe"

# Local paths
local_version_file = "version.txt"
update_checker_file = "main.py"
new_exe_file = "new_version.exe"

# Function to download a file from a URL
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)

# Get the remote version
remote_version = requests.get(version_url).text.strip()

# Read the local version
if os.path.exists(local_version_file):
    with open(local_version_file, "r") as file:
        local_version = file.read().strip()
else:
    local_version = "0"

# Compare versions
if remote_version > local_version:
    print("A new version is available. Downloading the update...")

    # Download the update checker
    download_file(update_checker_url, update_checker_file)
    
    # Download the new executable
    download_file(new_exe_url, new_exe_file)
    
    # Update the local version file
    with open(local_version_file, "w") as file:
        file.write(remote_version)

    print(f"Update complete. New version {remote_version} downloaded.")
    
else:
    print("You are already using the latest version.")

# Proceed with the batch script (or any other operation)

