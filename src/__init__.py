import sys
from src.MemeGenerator import save_meme_to_disk


def h():
    print("Usage: MemePy <template> <path> <*args> <*options>\n"
          "Visit https://github.com/julianbrandt/src for detailed instructions")
    sys.exit()


def main(args):
    if args.__contains__("MemePy"):
        args.remove("MemePy")
    if len(args) <= 2:
        h()
    try:
        path = args[1]
        template = args[0]
        save_meme_to_disk(template, path, args[2:])
    except ValueError as e:
        print(str(e))
        h()
    except FileNotFoundError:
        print("No such directory: " + path)

if __name__ == "__main__":
    main(sys.argv)