import json
from src.MemeFactory import MemeImage
from src.MemeModel import TextZone
from PIL import ImageFont
from definitions import RESOURCE_DIR

def parse_memelib_json(source):
    memes = {}
    for meme in source:
        memes[meme] = parse_meme_image_json(source[meme])
    return memes

def parse_meme_image_json(source):
    meme_image = MemeImage(None, None)
    for k in source:
        if k == "filename":
            meme_image.image_file_name = source[k]
        elif k == "text_zones":
            text_zones = []
            for i in source[k]:
                text_zones.append(parse_text_zone_json(i))
            meme_image.text_zones = text_zones
    return meme_image

def parse_text_zone_json(source):
    zone = TextZone(
        (int(source["pos"][0]), int(source["pos"][1])),
        (int(source["dimensions"][0]), int(source["dimensions"][1])),
        ImageFont.truetype(RESOURCE_DIR + "/FontLibrary/" + source["font"], int(source["font_size"]))
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
            zone.optional = str2bool(bool(a))
    return zone


def json_to_dict(files):
    output = {}
    for f in files:
        file = open(f, "r")
        data = json.loads(file.read())
        file.close()
        for k in data:
            output[k] = data[k]
    return output


def generate_meme_dict():
    files = [
        RESOURCE_DIR + "/MemeLibrary/builtin.JSON",
        RESOURCE_DIR + "/MemeLibrary/extension.JSON"
    ]
    return parse_memelib_json(json_to_dict(files))


def str2bool(string):
    return string == "True"