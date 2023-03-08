import threading
from PIL import Image
from pathlib import Path
from typing import Union

class Convert(threading.Thread):
    def __init__(self, game_path: Union[str, Path], color_mode: int = 3, proportions_image: bool = True, resolution: list = (300, 300), offset: list = (0, 0)):
        super().__init__()
        self.game_path: str = game_path
        self.color_mode: int = color_mode
        self.proportions_image: bool = proportions_image
        self.resolution: list = resolution
        self.offset: list = offset

        self.resolution_image: list = []

    def open_image(self) -> Image.Image:
        image: Image.open = Image.open(self.game_path)
        self.resolution_image = image.size
        return image.convert("RGB")

    def save_image(self, image: Image.Image, name_save: str = "image.png"):
        image.save(name_save)

    def convert(self, color_mode: int):
        pass

if __name__ == "__main__":
    conv = Convert("img.png")
    conv.save_image(conv.open_image(), name_save="test.png")