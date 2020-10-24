import pygame

class Grid:
    def __init__(self):
        #simple lines
        self.gridLines = [ ((1,80),  (720,80)),
                           ((1,160),(720,160)),
                           ((1,320),(720,320)),
                           ((1,400),(720,400)),
                           ((1,560),(720,560)),
                           ((1,640),(720,640)),
                           ((80,1),  (80,720)),
                           ((160,1),(160,720)),
                           ((320,1),(320,720)),
                           ((400,1),(400,720)),
                           ((560,1),(560,720)),
                           ((640,1),(640,720)),]
        #wide bold lines
        self.gridWideLines = [((1,1),    (720,1)),
                              ((1,240),(720,240)),
                              ((1,480),(720,480)),
                              ((1,720),(720,720)),
                              ((1,1),    (1,720)),
                              ((240,1),(240,720)),
                              ((480,1),(480,720)),
                              ((720,1),(720,720)),]
    def drawSuccess(self,surface):
        pass
    #draw lines of the grid
    def draw(self, surface):
        pygame.draw.rect(surface, (200,200,200),(723,0,900,722))
        pygame.display.update()
        for line in self.gridLines:
            pygame.draw.line(surface, (200,200,200), line[0], line[1], 2)

        for line2 in self.gridWideLines:
            pygame.draw.line(surface, (200,200,200), line2[0], line2[1], 5)