from enum import Enum

from PIL import ImageFont

from src.MemeModel import MemeImage, TextZone


class MemeImages(Enum):
    def __str__(self):
        return str(self.value)

    MeAlsoMe = MemeImage(
        "mealsome.png",
        [TextZone(
            pos=(60, 0),
            dimensions=(400, 95),
            font=ImageFont.truetype("arial.ttf", 24),
        ),
            TextZone(
            pos=(120, 100),
            dimensions=(350, 100),
            font=ImageFont.truetype("arial.ttf", 24),
        )]
    ),
    ItsRetarded = MemeImage(
        "itsretarded.png",
        [TextZone(
            pos=(253, 3),
            dimensions=(220, 90),
            font=ImageFont.truetype("arial.ttf", 20),
            centering=(False, True)
        )]
    ),
    Headache = MemeImage(
        "headache.png",
        [TextZone(
            pos=(250, 490),
            dimensions=(400, 50),
            font=ImageFont.truetype("impact.ttf", 54),
            centering=(True, False)
        )]
    ),
    ItsTime = MemeImage(
        "itstime.png",
        [TextZone(
            pos=(60, 50),
            dimensions=(200, 150),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(True, True)
        ),
        TextZone(
            pos=(95, 380),
            dimensions=(110, 75),
            font=ImageFont.truetype("arial.ttf", 24),
            centering=(True, True)
        )]
    ),
    ClassNote = MemeImage(
        "classnote.png",
        [TextZone(
            pos=(585, 545),
            dimensions=(175, 140),
            angle=30,
            font=ImageFont.truetype("arial.ttf", 24),
            centering=(True, True)
        )]
    ),
    FirstWord = MemeImage(
        "firstword.png",
        [TextZone(
            pos=(100, 30),
            dimensions=(500, 50),
            font=ImageFont.truetype("comic.ttf", 60),
        ),
        TextZone(
            pos=(100, 485),
            dimensions=(500, 200),
            font=ImageFont.truetype("comic.ttf", 60),
            centering=(False, True)
        )],
    ),
    NutButton = MemeImage(
        "nutbutton.jpg",
        [TextZone(
            pos=(133, 300),
            dimensions=(175, 100),
            angle=10,
            font=ImageFont.truetype("arial.ttf", 56),
            centering=(False, True)
        )]
    ),
    SwuUok = MemeImage(
        "swuuok.png",
        [TextZone(
            pos=(20,22),
            dimensions=(220, 220),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(True, True)
        ),
        TextZone(
            pos=(20, 285),
            dimensions=(220, 220),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(True, True)
        )]
    ),
    Pills = MemeImage(
        "pills.jpg",
        [TextZone(
            pos=(235, 290),
            dimensions=(230, 40),
            font=ImageFont.truetype("arial.ttf", 20),
            centering=(True, False)
        )]
    ),
    Balloon = MemeImage(
        "balloon.jpg",
        [TextZone(
            pos=(30, 300),
            dimensions=(200, 200),
            font=ImageFont.truetype("arial.ttf", 40),
            centering=(True, True)
        ),
        TextZone(
            pos=(470, 100),
            dimensions=(300, 250),
            font=ImageFont.truetype("arial.ttf", 40),
            centering=(True, True)
        ),
        TextZone(
            pos=(10, 750),
            dimensions=(200, 250),
            font=ImageFont.truetype("arial.ttf", 40),
            centering=(True, True)
        )]
    ),
    Classy = MemeImage(
        "classy.jpg",
        [TextZone(
            pos=(310, 20),
            dimensions=(370, 210),
            font=ImageFont.truetype("arial.ttf", 40),
            centering=(True, True)
        ),
        TextZone(
            pos=(310, 270),
            dimensions=(370, 210),
            font=ImageFont.truetype("MemePy/FontLibrary/BLKCHCRY.ttf", 45),
            centering=(True, True)
        )]
    ),
    Cola = MemeImage(
        "cola.jpg",
        [TextZone(
            pos=(180, 425),
            dimensions=(200, 200),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(True, True),
            text_color=(255, 255, 255)
        ),
        TextZone(
            pos=(600, 350),
            dimensions=(180, 100),
            font=ImageFont.truetype("arial.ttf", 36),
            angle=30,
            centering=(True, True)
        )]
    ),
    Loud = MemeImage(
        "loud.jpg",
        [TextZone(
            pos=(850, 600),
            dimensions=(200, 200),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(True, False)
        ),
        TextZone(
            pos=(860, 800),
            dimensions=(200, 190),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(True, False),
            optional=True
        )]
    ),