import configparser
import threading
import time
import glob
import math
import os

try:
    from PIL import Image
except ModuleNotFoundError:
    os.system("cls")
    print("Installing the pip update")
    os.system("pip install --upgrade pip")
    os.system("cls")
    print("Installing Libraries")
    os.system("pip install pillow")

class SearchThread(threading.Thread):
    def __init__(self, config):
        super().__init__()
        self.config = config

    def run(self):
        drives = [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]
        folder = "GarrysMod"
        self.config["SETTINGS"] = {"game_path": ""}
        for root_dir in drives:
            if self.config["SETTINGS"]["game_path"]:
                break
            for dirpath, dirnames, filenames in os.walk(root_dir+"\\"):
                if folder in dirnames:
                    print(f"Folder found: {dirpath}\\GarrysMod\\garrysmod\\data\\e2files")
                    self.config["SETTINGS"]["game_path"] = dirpath + "\\GarrysMod\\garrysmod\\data\\e2files"
                    break
            else:
                print(f"Not found on {root_dir[:-1]}. {drives.index(root_dir) + 1}/{len(drives)} disks checked.")


class Main:
    def __init__(self):
        self.config = configparser.ConfigParser()

        if os.name != "nt":
            print("The script only works on Windows.")
            input("To close, press enter...")
            exit()

        os.system("cls")
        self.image_path = "image/"
        self.config_path = "config.ini"

        if not os.path.exists(self.image_path):
            print(f"Folder {self.config_path} not found")
            print("Folder created.")
            os.mkdir(self.image_path)

        if not os.path.exists(self.config_path):
            print("Could not find config.ini")
            print("Search for the game folder...")
            search_thread = SearchThread(self.config)
            search_thread.start()
            search_thread.join()

            with open(self.config_path, "w") as configfile:
                self.config.write(configfile)

        self.config.read(self.config_path)
        input("To start, press Enter...")
        os.system("cls")

        self.show_image_list()

    def image_dir(self):
        extensions = ["png", "jpg", "jpeg"]

        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(self.image_path, f"*.{ext}")))

        return files

    def show_image_list(self):
        def print_images(stop):
            while not stop:
                files = self.image_dir()
                print(f"Images in {self.image_path}:")
                for x, file in enumerate(files):
                    print(f"{x+1} - {file}")
                print("\n>>>", end="")

                time.sleep(3)
                os.system("cls")
        self.stop = False
        thread = threading.Thread(target=print_images, args=(self.stop,))
        thread.daemon = True
        thread.start()
        while True:
            file = int(input())
            try:
                if self.image_dir()[file-1]:
                    self.stop = True
                    print("ok")
            except IndexError:
                print("Image not found")





if __name__ == '__main__':
    main = Main()