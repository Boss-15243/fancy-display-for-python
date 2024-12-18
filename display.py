import os
import sys

class Output:
    def __init__(self):
        self.get_window_size()
        self.colors = {"black":30, "red":31, "green":32, "yellow":33, "blue":34, "magenta":35, "cyan":36, "white":37}
        self.reset = "\033[0m"

    def display(self):
        sys.stdout.flush()

    def cls(self):
        print("\033[2J")
    
    def printxy(self, x, y, string, **kwargs):  #draws a character with position and color

        pos = f"\033[{x};{y}H"

        if "color" in kwargs.keys():
            color = "\033[" + str(self.colors[kwargs["color"]]) + "m" 
        else:
            color = "\033[37m"

        if "flash" in kwargs.keys() and kwargs["flash"]:
            flash = "\033[5m"
        else:
            flash = ""

        if "background" in kwargs.keys():
            background = "\033[" + str(self.colors[kwargs["background"]]+10) + "m" 
        else:
            background = "\033[40m"

        print(self.reset + color + background + flash + pos + string + self.reset, end="")
    
    def move_cursor(self, x, y):
        print(f"{self.reset}\033[{x};{y}H{self.reset}")
    
    def get_window_size(self):
        self.window_width, self.window_height = os.get_terminal_size()
        return self.window_height, self.window_width
    
    def draw_pixel(self, x, y, color):  #draws solid color pixel
        self.p(x, y, "#", background=color, color=color)
    
    def draw_square(self, x, y, width, height, color, **kwargs):  #draws square
        if "character" in kwargs.keys():
            character, character_color = kwargs["character"]
        else:
            character, character_color = "#", color
        backround_color = color
        for w in range(width):
            for h in range(height):
                self.p(x+w, y+h, character, color=character_color, background=backround_color) 
    

if __name__ == "__main__":
    pass

