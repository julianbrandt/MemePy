from src.MemeGenerator import MemeGenerator


def get_meme_generator(template, texts):
    return MemeGenerator.generator_from_template(template, texts)


def save_meme_to_disk(template, path, texts):
    MemeGenerator.generator_from_template(template, texts).image.save(path + "\meme.png")
    return "Image saved to " + path