import threading
import numpy as np
from PIL import Image
from pathlib import Path
from typing import Union


class Convert(threading.Thread):
    def __init__(self, image_path: Union[str, Path], game_path: Union[str, Path], color_mode: int = 3,
                 quantize: int = 64, proportions_image: bool = True, resolution: complex = complex(300, 300),
                 offset: complex = complex(0, 0)):
        super().__init__()

        self.image_path: str = image_path
        self.game_path: str = game_path
        self.color_mode: int = color_mode
        self.proportions_image: bool = proportions_image
        self.resolution: complex = resolution
        self.offset: complex = offset
        self.quantize: int = quantize

        self.resolution_image: list = []
        self.image: Image.Image = Image.Image()

        self.open_image()
        self.size_image(self.resolution)
        self.show_image("quantized_image.png")

    def open_image(self):
        image: Image.open = Image.open(self.image_path)
        self.resolution_image = image.size
        self.image = image.convert("RGB")
        image = image.quantize(colors=self.quantize)  # уменьшаем количество цветов
        self.image = image

    def size_image(self, resolution: complex) -> Image.Image:
        if self.proportions_image:
            aspect_ratio: float = self.resolution_image[1] / self.resolution_image[0]
            width: int = int(resolution.real)
            new_width: int = width
            new_height: int = int(new_width * aspect_ratio)

            return self.image.resize((new_width, new_height))
        else:
            width: int = int(resolution.real)
            height: int = int(resolution.imag)
            return self.image.resize((width, height))

    def arr_colors(self) -> np.ndarray:
        colors: np.ndarray = np.array(self.image)
        colors = colors.flatten()
        colors = np.concatenate([colors[::3], colors[1::3], colors[2::3]])

        return colors

    def convert(self, color_mode: int):
        rgb_colors: list = self.arr_colors()
        rgb2digi: list = []
        match color_mode:
            case 0:
                print(rgb_colors[0])
                print(rgb_colors[1])
                print(rgb_colors[2])
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass

    def show_image(self, name_save: Union[str, Path] = ""):
        if name_save:
            self.image.save(name_save)

        self.image.show()


if __name__ == "__main__":
    conv = Convert("img.png", "")
    conv.convert(0)
