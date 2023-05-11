import pygame


class Ending():

    '''Luokka, joka luo pelin päättymisnäytön

    Kertoo pelaajalle, että hän on hävinnyt sekä miten tämä voi aloittaa uuden pelin

    Argumentit:
                font: fontti
                screen: näyttö
                game_ends: luo ja piirtää päättymisnäytön

    '''

    def __init__(self,connection):
        '''Luokan konstruktori, joka alustaa lopetuksen

        Args:
                    font: fontti
                    screen: näyttö
                    run: pitää lopetusnäyttöä yllä kunnes peslaaja painaa välilyöntiä

        '''
        pygame.init()
        self.font = pygame.font.SysFont("Comic Sans", 20)
        self.screen = pygame.display.set_mode((500, 400))
        self.run = True
        self._connection = connection
        cursor = self._connection.cursor()
        cursor.execute("SELECT h.player, h.result FROM Highscores h ORDER BY result DESC LIMIT 3;")
        rows = cursor.fetchall()
        self.highest_scores = ""
        for i, row in enumerate(rows):
            player = row[0]
            result = row[1]
            score_str = f"{i+1}. {player}: {result}"
            self.highest_scores += score_str
            print(self.highest_scores)
            if i != len(rows) - 1:
                self.highest_scores += "\n"
            
    def game_ends(self, ending_matrix):
        '''Luokan metodi, joka luo ja piirtää päättysmisnäytön

        Args:
                    you_lost: häviämisteksti
                    restart_instuctions: aloitusohjeet

        '''
        if not self.highest_scores:
            self.highest_scores = "No high scores yet!"
        while self.run:
            self.screen.fill((155, 205, 155))
            you_lost = self.font.render("You Lost!", True, (0, 0, 0))
            restart_instructions = self.font.render(
                "Press space to restart", True, (0, 0, 0))
            yeet = self.font.render(
                str(self.highest_scores), True, (0, 0, 0))
            self.screen.blit(you_lost, (200, 160))
            self.screen.blit(restart_instructions, (140, 210))
            self.screen.blit(yeet, (90, 300))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.run = False
                    ending_matrix = [[0 for _ in range(4)] for _ in range(4)]
                    self.screen.fill((125, 158, 192))
                    return ending_matrix
                if event.type == pygame.QUIT:
                    pygame.quit()
