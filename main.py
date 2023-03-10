import configparser
import threading
import time
import glob
import math
import os

try:
    import numpy as np
    from PIL import Image
    from Convertot import Convert
except ModuleNotFoundError:
    os.system("cls")
    print("Installing the pip update")
    os.system("pip install --upgrade pip")
    os.system("cls")
    print("Installing Libraries")
    os.system("pip install pillow")
    input("Restart the program...")
    exit()

class SearchThread(threading.Thread):
    def __init__(self, config):
        super().__init__()
        self.daemon = True
        self.config = config
        self.name = "Game_search"

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
        self.config: configparser.ConfigParser = configparser.ConfigParser()

        if os.name != "nt":
            print("The script only works on Windows.")
            input("To close, press enter...")
            exit()

        os.system("cls")
        self.image_path: str = "image/"
        self.config_path: str = "config.ini"
        self.image_list: list = []
        self.mode: int = 0

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
        self.image_update: threading.Thread = threading.Thread(name="Image_update", target=self.file_image, daemon=True)

        input("To start, press Enter...")
        os.system("cls")

        self.image_update.start()
        self.select_image()

    def file_image(self):
        image_last: list = []
        image_current: list = self.image_dir()
        while True:
            image_current = self.image_dir()
            if image_current != image_last:
                image_last = image_current
                self.image_list = self.image_dir()
            time.sleep(1)


    def image_dir(self):
        extensions: list = ["png", "jpg", "jpeg"]

        files: list = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(self.image_path, f"*.{ext}")))

        return files

    def show_image_list(self, stop_event: threading.Event):
        image: list = self.image_list
        if not len(image):
            print("There are no images in the 'image/' folder.")
        while True:
            if image != self.image_list:
                os.system("cls")
                print("Select a file:")
                for i, file in enumerate(self.image_list):
                    print(f"{i} - {file}")
                print("To select a file, you must specify the image number. \n\n>>> ", end="")
                image = self.image_list

            time.sleep(1)

    def select_image(self):
        stop_show_image: threading.Event = threading.Event()

        show_image: threading.Thread = threading.Thread(name="Show_image", target=self.show_image_list, daemon=True, args=(stop_show_image,))
        show_image.start()

        while True:
            try:
                file: int = int(input())

                try:
                    if self.image_list[file] and file >= 0:
                        print(self.image_list[file])
                        break
                    else:
                        raise IndexError
                except IndexError:
                    print("Image not found \n>>> ", end="")
            except ValueError:
                print("Failed get a number. \n>>> ", end="")
        stop_show_image.set()



if __name__ == '__main__':
    main = Main()