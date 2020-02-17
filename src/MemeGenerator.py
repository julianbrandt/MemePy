from src.MemeFactory import MemeFactory
from io import BytesIO


def get_meme_factory(template, args):
    return MemeFactory.factory_from_template(template, args)


def get_meme_image(template, args):
    return get_meme_factory(template, args).output_image


def get_meme_image_bytes(template, args):
    image_bytes = BytesIO()
    meme = MemeFactory.factory_from_template(template, args)
    meme.output_image.save(image_bytes, format="PNG")
    image_bytes.seek(0)
    return image_bytes


def save_meme_to_disk(template, path, args):
    MemeFactory.factory_from_template(template, args).output_image.save(path + "\meme.png")
    return "Image saved to " + path