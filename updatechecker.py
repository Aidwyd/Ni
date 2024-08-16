import requests

def check_for_update(current_version):
    version_url = "https://raw.githubusercontent.com/Aidwyd/Ni/main/version"
    
    try:
        response = requests.get(version_url)
        latest_version = response.text.strip()

        if latest_version > current_version:
            print(f"New version {latest_version} is available! Downloading the update...")
            download_update()
        else:
            print("You are using the latest version.")
    except Exception as e:
        print(f"Failed to check for updates: {e}")

def download_update():
    update_url = "https://raw.githubusercontent.com/Aidwyd/Ni/main/BediumACL.exe"

    try:
        update_response = requests.get(update_url)
        with open("new_update.exe", "wb") as f:
            f.write(update_response.content)
        print("Update downloaded successfully.")
    except Exception as e:
        print(f"Failed to download the update: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        current_version = sys.argv[1]
    else:
        current_version = "0.0"

    check_for_update(current_version)
