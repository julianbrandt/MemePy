from PIL import Image
from MemePy import MemeFactory

memes = MemeFactory.MemeLib

config = {l.split(":")[0]:l.split(":")[1] for l in open("./Docs/docsettings.config", "r").readlines()}

def resize_images(memes):
    max_size = int(config["image_max_size"])
    imgs = []
    for m in memes:
       try:
            img = Image.open(memes[m].image_file_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((max_size, max_size), Image.ANTIALIAS)
            img.save("./Docs/Img/" + m + ".jpg")
       except:
            print("Failed to resize image: " + memes[m].image_file_path)


def build_thumbnails():
    resize_images(memes)


def build_markdown_table():
    table = "| Template name          | Arguments       | Image |\n" \
            "| ------------- | --------------- | ----- |\n"
    for m in memes:
        required = memes[m].count_non_optional()
        opt = len(memes[m].text_zones) - required
        arguments = "**Required**: %i<br>**Optional**: %i" % (required, opt)
        img = "./Docs/Img/" + m + ".jpg"
        table += "| %s | %s | ![%s](%s) |\n" % (m, arguments, m, img)

    return table

def write_to_md():
    f = open("./Docs/FuncTable.md", "w")
    f.write(build_markdown_table())
    f.close()


def compile_readme():
    functionality = open("Functionality.md", "r").read()
    func_table = open("./Docs/FuncTable.md", "r").read()
    readme = open("README.md", "w")
    readme.write("%s\n## Built-In template docs\n%s" % (functionality, func_table))

def build_docs():
    build_thumbnails()
    write_to_md()
    compile_readme()