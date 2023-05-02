

class Colours:
    '''Luokka, joka sisältää pelin värit

    Argumentit:
                colours: sanakirja, jossa laatan arvo vastaa jotain väriä

    '''

    def __init__(self):
        '''Luokan konstruktori, joka sisältää värisanakirjan

        Args:
                colours: sanakirja, jossa laatan arvo vastaa jotain väriä

        '''
        self.colours = {2: (255, 182, 193),
                        4: (255, 160, 122),
                        8: (155, 205, 155),
                        16: (162, 205, 90),
                        32: (240, 128, 128),
                        64: (205, 140, 149),
                        128: (141, 182, 205),
                        256: (238, 213, 210),
                        512: (169, 169, 169),
                        1024: (255, 211, 155),
                        2048: (171, 130, 255),
                        4096: (238, 213, 210),
                        9182: (139, 71, 93)}
