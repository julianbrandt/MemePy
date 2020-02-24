import sys

from .MemeGenerator import save_meme_to_disk, add_external_resource_dir


def h():
    print("Usage: MemePy <template> <path> <*args> <*options>\n"
          "Visit https://github.com/julianbrandt/src for detailed instructions")
    sys.exit()


def main(args):
    if len(args) <= 2:
        h()
    try:
        args = args[1:]
        template = args[0]
        path = args[1]
        save_meme_to_disk(template, path, args[2:])
    except ValueError as e:
        print(str(e))
        h()
    except FileNotFoundError:
        print("No such directory: " + path)