from PIL import Image
import click
from .types import ResizeType


def pixel(color):
    r, g, b, a = color
    if a < (255 // 10):
        # If alpha is below 10%, show nothing
        return "  "
    # If alpha is below 50%, set the color as "dim"
    return click.style("  ", bg=(r, g, b), dim=a < 128)


def get_resampling_id(resampling: str):
    if resampling == "lanczos":
        return Image.Resampling.LANCZOS
    elif resampling == "bicubic":
        return Image.Resampling.BICUBIC
    elif resampling == "hamming":
        return Image.Resampling.HAMMING
    elif resampling == "bilinear":
        return Image.Resampling.BILINEAR
    elif resampling == "box":
        return Image.Resampling.BOX
    else:
        return Image.Resampling.NEAREST


@click.command()
@click.argument("image", type=click.Path(exists=True, dir_okay=False))
@click.option(
    "-r",
    "--resampling",
    type=click.Choice(["lanczos", "bicubic", "hamming", "bilinear", "box", "nearest"]),
    default="box",
)
@click.option(
    "-s",
    "--resize",
    type=ResizeType(),
    default=(20, 20),
)
def main(image, resampling, resize):

    with Image.open(image) as image:
        if isinstance(resize, float):
            resize = (int(image.width * resize), int(image.height * resize))

        resized = image.resize(
            resize, resample=get_resampling_id(resampling), reducing_gap=1.2
        ).convert("RGBA")

        for i in range(resized.width):
            for j in range(resized.height):
                try:
                    rgba = resized.getpixel((j, i))
                except IndexError:
                    rgba = (0, 0, 0, 0)
                print(pixel(rgba), end="")

            print()
