import os
import sys

class Output:
    def __init__(self):
        self.get_window_size()

    def display(self):
        sys.stdout.flush()

    def cls(self):
        print("\033[2J")
    
    def p(self, x, y, string):
        print(f"\033[{x};{y}H" + string)

    def get_window_size(self):
        self.window_width, self.window_height = os.get_terminal_size()
        return self.window_height, self.window_width
    
o = Output()
o.cls()

print(o.get_window_size())
o.p(o.window_height, o.window_width, "#")
input()