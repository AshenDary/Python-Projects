import curses
import random
import time

def random_char():
    return chr(random.randint(33, 126))

def display_animation(stdscr, name_ascii):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(3)
    
    rows, cols = stdscr.getmaxyx()
    rows, cols = max(rows, 10), max(cols, 10) 
    start_y = max(0, (rows - len(name_ascii)) // 2)
    start_x = max(0, (cols - max(len(line) for line in name_ascii)) // 2)
    
    display_matrix = [[random_char() for _ in range(cols)] for _ in range(rows)]
    
    for i in range(len(name_ascii)):
        for j in range(len(name_ascii[i])):
            if name_ascii[i][j] != ' ':
                time.sleep(0.01)
                display_matrix[start_y + i][start_x + j] = name_ascii[i][j]
                
                for _ in range(1):
                    stdscr.clear()
                    for y in range(rows):
                        for x in range(cols):
                            char = display_matrix[y][x]
                            if random.random() < 0.1:
                                char = random_char()
                            try:
                                stdscr.addch(y, x, char)
                            except curses.error:
                                pass
                    stdscr.refresh()
                    time.sleep(0.00)
    
    time.sleep(1)
    stdscr.getch()

if __name__ == "__main__":
    name_ascii = [
        
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",    
    "░░░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓░░▒▓███████▓▒░░░░░░░░░▒▓███████▓▒░░░▒▓██████▓▒░░▓████████▓▒░░░▓█▓▒░░░░░░░░░",        
    "░░░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░░▒▓█▓▒░░▒▓█▓▒░░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░░▒▓█▓▒░░░░░░░░░",        
 "░░░░░░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░░▒▓█▓▒░░▒▓█▓▒░░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░░▒▓█▓▒░░░░░░░░░",        
 "░░░░░░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░░░▓█▓▒░░▒▓█▓▒░░░░░░░░░▒▓█▓▒░░▒▓█▓▒░░▓█▓▒░░▒▓█▓▒░░▓█▓███████▒░░▓█▓▒░░░░░░░░░",        
"░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░░░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░▒░▓█▓▒░░░░░░░░░",        
 "░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░░░░░░░▒░▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░",
 "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░" 
 
    ]
    curses.wrapper(display_animation, name_ascii)
