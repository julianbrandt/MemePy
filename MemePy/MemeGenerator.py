from io import BytesIO

from .MemeFactory import MemeFactory, MemeLib
from .MemeLibJsonDecoder import generate_meme_dict


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


def add_external_resource_dir(resource_path):
    try:
        meme_dict = generate_meme_dict(resource_path)
        for i in meme_dict:
            MemeLib[i] = meme_dict[i]
    except FileNotFoundError as e:
        error_message = "Could not identify external resource directory.\n" + str(e)
        print(error_message)