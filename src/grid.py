class Grid:
    def __init__(self, width, height, divisions_x, divisions_y):
        self.width = width
        self.height = height
        self.divisions_x = divisions_x
        self.divisions_y = divisions_y
        self.color = (255, 220, 220)

    def x(self, division_x):
        if division_x < 0:
            division_x += self.divisions_x
        return self.width / self.divisions_x * division_x

    def y(self, division_y):
        if division_y < 0:
            division_y += self.divisions_y
        return self.height / self.divisions_y * division_y

    def point(self, division_x, division_y):
        return (self.x(division_x), self.y(division_y))
    
    def center_x(self):
        return self.width / 2
    
    def center_y(self):
        return self.height / 2
    
    def center(self):
        return (self.center_x(), self.center_y()) 

    
    def draw(self, draw_context):
        # draw horizontal lines
        for n in range(1, self.divisions_y):
            draw_context.line([(0, self.height / self.divisions_y * n), 
                                    (self.width, self.height / self.divisions_y * n)], 
                                    self.color,
                                    width=2)
        # draw vertical lines
        for n in range(1, self.divisions_x):
            draw_context.line([(self.width / self.divisions_x * n, 0), 
                                    (self.width / self.divisions_x * n, self.height)], 
                                    self.color, 
                                    width=2)
            
    