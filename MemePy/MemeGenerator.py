from io import BytesIO

from .MemeFactory import MemeFactory, MemeLib
from .MemeLibJsonDecoder import generate_meme_dict


def get_meme_factory(template, args):
    return MemeFactory.factory_from_template(template, args)


def get_meme_image(template, args):
    return get_meme_factory(template, args).output_image


def get_meme_image_bytes(template, args):
    image_bytes = BytesIO()
    meme_img = MemeFactory.factory_from_template(template, args).output_image
    if hasattr(meme_img, "is_animated") and meme_img.is_animated:
        frames = []
        for i in range(0, meme_img.n_frames):
            meme_img.seek(i)
            frames.append(meme_img.copy())
        frames[0].save(image_bytes, format="GIF", save_all=True, append_images=frames[1:], duration=meme_img.info['duration'], loop=0)
    else:
        meme_img.save(image_bytes, format="PNG")
    image_bytes.seek(0)
    return image_bytes


def save_meme_to_disk(template, path, args):
    image_bytes = get_meme_image_bytes(template, args)
    format = MemeLib[template].image_file_path.split(".")[-1]
    with open(path + "/meme." + format, "wb") as f:
        f.write(image_bytes.getbuffer())
        return "Image saved to " + path


def add_external_resource_dir(resource_path):
    try:
        meme_dict = generate_meme_dict(resource_path)
        for i in meme_dict:
            MemeLib[i] = meme_dict[i]
    except FileNotFoundError as e:
        error_message = "Could not identify external resource directory.\n" + str(e)
        print(error_message)