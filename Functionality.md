# MemePy

*Meme generator library for your everyday needs*

Python meme generator originally made for the discord-chat-bot [HydroBot](https://github.com/julianbrandt/Hydrobot3), but migrated to its own package for increased modularity and ease of use.

## How it works

MemePy uses the Python Imaging Library *PIL* to edit existing templates of memes and return them to the user.

MemePy has a list of defined `MemeImage` templates that are fed to a `MemeFactory`. The factory then produces an image with all the arguments, given by the user, pasted onto the image in the correct formats of the specific meme.

In addition to just text-based memes, MemePy also supports substituting the text-argument with an image. Just supply an image-link in `< ... >` angle brackets as an argument, and the text will be substituted for the image. ENDLESS POTENTIAL!!!

The available meme templates can be found in the [Image Library](./MemePy/Resources/ImageLibrary). The specifications of each meme template can be found in the [Meme Library](./MemePy/Resources/MemeLibrary). Where `builtin.JSON` is the place for default templates. You can define your own templates as well, which is described below.

## Usage

### Importing MemePy into your own project

If you wish to import the meme-generation functionality into your own project, usually all you will need can be found in [MemePy/MemeGenerator.py](./MemePy/MemeGenerator.py). 

#### The functions available in this file are:

* `save_meme_to_disk(template, path, args)`

  * Generates a meme of the given template, with given args and saves it to disk at the given path.

* `get_meme_image(template, args)`

  * Generates a meme of the given template, with given args and returns it as a `PIL`Image object. Used if you wanna pass an image to your own project instead of saving it.

* `get_meme_image_bytes(template, args)`

  * Generates a meme of the given template, with given args and returns it as a BytesIO object. This allows for treating the output image as a file, and thus making it possible to open as other objects (e.g. `discord.py File` objects).

* `get_meme_factory(template, args)`

  * Generates a meme factory with the given template and args. This exposes more of the specifications of the factory, in case you need more rich details.

* `add_external_resource_dir(resource_path)`

  * Allows you to add your own external resource library without having access to the package's internal resource directory. The given resource directory *HAS* to follow the following rules for resource directories:

    ```
    <resources>
    +---FontLibrary
    |       <font>.ttf
    |
    +---ImageLibrary
    |       <image>.png
    |
    \---MemeLibrary
            <meme-definition>.JSON
    ```

    In other words. The folders inside the given directory *MUST* be named **FontLibrary**, **ImageLibrary** and **MemeLibrary**. The font you choose to use in your extension can be left out of the fonts directory, if it already exists internally in the package resources.



## Creating memes on the Command-Line

Using the command-line, you can generate images from templates and save them to disk.

#### Generating a meme:

```console
MemePy <path> <template> <*args> <*options>
```

- __path__ is where on your computer you want to save the meme.
- __template__ is the underlying template to use for the meme (not case sensitive).
- __\*args__ are all arguments to be placed onto the template.
  - Multi-word arguments must be surrounded by "" quotation marks
  - Arguments can be images, pasted onto the template. Image-links should be given in '<>' angle brackets.
- __\*options__ are the options that modify behavior of the generation.
  - Options are passed with '{}' curly braces.
  - Currently supported options: "stretch".