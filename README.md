# MemePy
Python meme generator originally made for the discordbot [Hydrobot](https://github.com/julianbrandt/Hydrobot3), but migrated to its own project as it could have several uses.

Welcome to MemePy!
Importing this library allows passing PIL objects to

Using the command-line, you can generate images from templates and save them to disk.
These templates are defined in MemeLib.JSON.
Generating a meme:
>MemePy <path> <template> <*args> <*options>
Path is the destination for the generated image file on disk.
Templates define the image to use as base for the meme.
Args are the text or image elements to be inserted into the template.
Options are additional arguments to modify the behavior of the meme generation.
Adding your own templates to AdditionalTemplates.JSON, and putting the corresponding images and fonts to ImageLibrary and FontLibrary respectively, automatically adds your image to the available templates.