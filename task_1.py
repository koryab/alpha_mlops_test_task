class Parallelepiped():
    def __init__(self):
        introduction = ("Count parallelepiped:\n"
                "\tThis programm counts parallelepiped "
                "sides squares and figure volume.\n"
                "\n"
                "\t   _________\n"
                "\t /|        /|\n"
                "\t/_|_______/ |c\n"
                "\t| |_______|_|\n"
                "\t|/        |/ b\n"
                "\t|_________|\n"
                "\t     a\n")

        print(introduction)
        print("Let's set sizes:")
        
        for edge in ["a", "b", "c"]:
            setattr(self, edge, self._get_side(edge))

        self._count_squares()
        self._count_volume()
        print()
        print(f"Side \'ac\' square {self.square_a_c}")
        print(f"Side \'ab\' square {self.square_a_b}")
        print(f"Side \'bc\' square {self.square_b_c}")
        print(f"Sum square {self.square}")
        print(f"Volume {self.volume}")

    def _get_side(self, edge):
        value = 0
        while float(value) <= 0:
            value = input(f"Input edge \'{edge}\' size: ")
            if value.lower() == "stop":
                exit("Execution stopped.")
            if value.isalpha():
                print("Incorrect value. Must be a positive number.")
                continue
            if float(value) <= 0:
                print("Incorrect value. Must be a positive number.")
                continue

        return float(value)

    def _count_squares(self):
        self.square_a_b = self.a * self.b
        self.square_a_c = self.a * self.c
        self.square_b_c = self.b * self.c
        self.square = self.square_a_b * 2 +\
                      self.square_a_c * 2 +\
                      self.square_b_c * 2

    def _count_volume(self):
        self.volume = self.a * self.b * self.c


if __name__=="__main__":
    Parallelepiped()
