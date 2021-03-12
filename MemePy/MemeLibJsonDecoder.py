import json, os

from PIL import ImageFont

from .MemeModel import TextZone, MemeImage
from .definitions import RESOURCE_DIR


def parse_memelib_json(source, resource_path):
    memes = {}
    for meme in source:
        memes[meme] = parse_meme_image_json(source[meme], resource_path)
    return memes

def parse_meme_image_json(source, resource_path):
    meme_image = MemeImage(None, None)
    for k in source:
        if k == "filename":
            meme_image.image_file_path = resource_path + "/ImageLibrary/" + source[k]
        elif k == "text_zones":
            text_zones = []
            for i in source[k]:
                text_zones.append(parse_text_zone_json(i, resource_path))
            meme_image.text_zones = text_zones
    return meme_image

def parse_text_zone_json(source, resource_path):
    found_font = False
    for file in os.listdir(resource_path + "/FontLibrary"):
        if file == source["font"]:
            found_font = True

    if found_font:
        font = ImageFont.truetype(resource_path + "/FontLibrary/" + source["font"], int(source["font_size"]))
    else:
        font = ImageFont.truetype(RESOURCE_DIR + "/FontLibrary/" + source["font"], int(source["font_size"]))

    zone = TextZone(
        (int(source["pos"][0]), int(source["pos"][1])),
        (int(source["dimensions"][0]), int(source["dimensions"][1])),
        font
    )
    for opt in source:
        a = source[opt]
        if opt == "angle":
            zone.angle = int(a)
        elif opt == "text_color":
            zone.text_color = (int(a[0]), int(a[1]), int(a[2]))
        elif opt == "centering":
            zone.centering = (str2bool(a[0]), str2bool(a[1]))
        elif opt == "optional":
            zone.optional = str2bool(a)
        elif opt == "outline":
            zone.outline = str2bool(a)
    return zone


def json_to_dict(files, resource_path):
    output = {}
    for f in files:
        file = open(resource_path + "/MemeLibrary/" + f, "r")
        data = json.loads(file.read())
        file.close()
        for k in data:
            output[k] = data[k]
        file.close()
    return output


def generate_meme_dict(resource_path):
    files = []
    for file in os.listdir(resource_path + "/MemeLibrary"):
        if file.endswith(".JSON"):
            files.append(file)
    return parse_memelib_json(json_to_dict(files, resource_path), resource_path)


def generate_standard_meme_dict():
    return generate_meme_dict(RESOURCE_DIR)


def str2bool(string):
    return string == "True"