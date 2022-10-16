
'''
Checkers non gui
Edward Abel Guobadia
10-15-2022
'''
from checkers_class_info import gameboard

def main():
    board1 = gameboard.Board(6, 6)
    print(f"Board is ->\n{board1}")


if __name__ == "__main__":
    main()
