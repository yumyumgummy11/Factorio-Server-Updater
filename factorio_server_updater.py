import requests
import os
import time
import tarfile
import shutil

def get_latest_server(server_store_fp):
    url = "https://factorio.com/get-download/stable/headless/linux64"
    filename = "/factorio-headless-stable.tar.xz"

    print("Downloading latest stable server tar file...")
    temp = requests.get(url, allow_redirects=True)

    print("Download Complete! Saving file to:", server_store_fp + filename)

    open(server_store_fp + filename, 'wb').write(temp.content)
    time.sleep(1)
    print("File saved successfully!")


def get_current_server_dir():
    while True:
        while True:
            server_store_fp = input("Enter filepath to server store location:")
            if os.path.isdir(server_store_fp):
                break
            else:
                print("Invalid file path")
        try:
            if 'factorio' not in os.listdir(server_store_fp + '/factorio/bin/x64'):
                print("Unable to locate server files")
            else:
                print("Server files found")
                break
        except OSError:
            print("Unable to locate server files")
    return server_store_fp


def extract_new_server(server_fp):
    print("Renaming existing server folder...")
    try:
        os.rename(server_fp + '/factorio', server_fp + '/factorio-backup-server')
        time.sleep(1)
        print("Server folder successfully renamed!")
    except OSError:
        print("Unable to rename existing server folder")
        quit()
    
    time.sleep(1)
    print("Extracting latest stable server...")
    with tarfile.open(server_fp + '/factorio-headless-stable.tar.xz', 'r') as tar:
        tar.extractall(server_fp)
    print("Server files successfully extracted!")
    
    time.sleep(1)
    print("Removing server tar file...")
    if os.path.exists(server_fp + '/factorio-headless-stable.tar.xz'):
        os.remove(server_fp + '/factorio-headless-stable.tar.xz')
        time.sleep(1)
        print("Server tar successfully removed!")
    else:
        print("Unable to locate server tar file")
    
    print("Copying server data to new server...")
    time.sleep(1)
    shutil.copyfile(server_fp + '/factorio-backup-server/data/server-settings.json', server_fp + '/factorio/data/server-settings.json')
    shutil.copyfile(server_fp + '/factorio-backup-server/data/server-whitelist.json', server_fp + '/factorio/data/server-whitelist.json')
    shutil.copyfile(server_fp + '/factorio-backup-server/player-data.json', server_fp + '/factorio/player-data.json')
    shutil.copyfile(server_fp + '/factorio-backup-server/achievements.dat', server_fp + '/factorio/achievements.dat')
    print("Server data successfully copied!")
    while True:
        try:
            print("It is recomended to keep the old server files until you can confirm that all server data has been copied over correctly")
            if str(input("Delete old server files? y/n:")) == 'y':
                if os.path.exists(server_fp + '/factorio-backup-server'):
                    shutil.rmtree(server_fp + '/factorio-backup-server')
                    time.sleep(1)
                    print("Old server successfully removed!")
                    print("If you find that not all server data got copied correctly after starting the server check your trash to try and recover the old files")
                    break
                else:
                    print("Unable to remove old server")
            else:
                print("Old server dir will have to be removed or renamed in order for the updater to work correctly again.")
                break
                    
        except ValueError:
            print("Invalid Input")

server_fp = get_current_server_dir()

get_latest_server(server_fp)

extract_new_server(server_fp)
