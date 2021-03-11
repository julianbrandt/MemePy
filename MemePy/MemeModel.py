class TextZone:
    def __init__(self, pos, dimensions, font, angle=0, text_color=(0,0,0), centering=(False, False), outline=False, optional=False):
        self.pos = pos
        self.dimensions = dimensions
        self.font = font
        self.angle = angle
        self.text_color = text_color
        self.centering = centering
        self.outline = outline
        self.optional = optional

class MemeImage:
    def __init__(self, image_file_path, text_zones):
        self.image_file_path = image_file_path
        self.text_zones = text_zones

    def count_non_optional(self):
        count = 0
        for z in self.text_zones:
            if not z.optional:
                count += 1
        return count