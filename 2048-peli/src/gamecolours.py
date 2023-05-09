import colorsys


class Colours:
    '''Luokka, joka sisältää pelin väriyhdistelmät

    Argumentit:
                colourslist: lista baseväreistä
                colours_light: sanakirja, jossa pastellivärit
                colours_dark_list: lista tummista väreistä
                colours_dark: sanakirja, jossa tummat värit
                colours_weird_list: lista random värejä
                colours_weird: sanakirja, jossa random värit

    '''

    def __init__(self):
        '''Luokan konstruktori, joka sisältää värisanakirjan

        Args:
                colours: sanakirja, jossa laatan arvo vastaa jotain väriä

        '''

        self.colourlist = [(255, 182, 193),
                           (255, 160, 122),
                           (155, 205, 155),
                           (162, 205, 90),
                           (240, 128, 128),
                           (205, 140, 149),
                           (141, 182, 205),
                           (238, 213, 210),
                           (169, 169, 169),
                           (255, 211, 155),
                           (171, 130, 255),
                           (139, 71, 93)]
        self.colours_light = {2: self.colourlist[0],
                              4: self.colourlist[1],
                              8: self.colourlist[2],
                              16: self.colourlist[3],
                              32: self.colourlist[4],
                              64: self.colourlist[5],
                              128: self.colourlist[6],
                              256: self.colourlist[7],
                              512: self.colourlist[8],
                              1024: self.colourlist[9],
                              2048: self.colourlist[10],
                              4096: self.colourlist[11]}

        self.colours_dark = {2: self.darken_colours(self.colourlist)[0],
                             4: self.darken_colours(self.colourlist)[1],
                             8: self.darken_colours(self.colourlist)[2],
                             16: self.darken_colours(self.colourlist)[3],
                             32: self.darken_colours(self.colourlist)[4],
                             64: self.darken_colours(self.colourlist)[5],
                             128: self.darken_colours(self.colourlist)[6],
                             256: self.darken_colours(self.colourlist)[7],
                             512: self.darken_colours(self.colourlist)[8],
                             1024: self.darken_colours(self.colourlist)[9],
                             2048: self.darken_colours(self.colourlist)[10],
                             4096: self.darken_colours(self.colourlist)[11]}

        self.colours_weird = {2: self.weirder_colours(self.colourlist)[0],
                              4: self.weirder_colours(self.colourlist)[1],
                              8: self.weirder_colours(self.colourlist)[2],
                              16: self.weirder_colours(self.colourlist)[3],
                              32: self.weirder_colours(self.colourlist)[4],
                              64: self.weirder_colours(self.colourlist)[5],
                              128: self.weirder_colours(self.colourlist)[6],
                              256: self.weirder_colours(self.colourlist)[7],
                              512: self.weirder_colours(self.colourlist)[8],
                              1024: self.weirder_colours(self.colourlist)[9],
                              2048: self.weirder_colours(self.colourlist)[10],
                              4096: self.weirder_colours(self.colourlist)[11]}

    def rgb_to_hsl(self, color_rgb):
        r, g, b = color_rgb
        h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
        return int(h*255), int(s*255), int(l*255)

    def make_colour_darker(self, color_hsl, amount=1.5):
        h, s, l = color_hsl
        new_l = max(0, l - amount*100)
        r, g, b = colorsys.hls_to_rgb(h/255, new_l/255, s/255)
        return int(r*255), int(g*255), int(b*255)

    def darken_colours(self, colourlist):
        self.colours_hsl = [self.rgb_to_hsl(
            color_rgb) for color_rgb in colourlist]
        self.colours_hsl_dark = [self.make_colour_darker(
            color_hsl) for color_hsl in self.colours_hsl]
        return self.colours_hsl_dark

    def make_colour_weird(self, color_hsl, amount=0.5):
        h, s, l = color_hsl
        new_l = max(0, l - amount*100)
        return (h, s, new_l)

    def weirder_colours(self, colourlist):
        self.colours_hsl = [self.rgb_to_hsl(
            color_rgb) for color_rgb in colourlist]
        self.colours_weird = [self.make_colour_weird(
            color_hsl) for color_hsl in self.colours_hsl]
        return self.colours_weird
