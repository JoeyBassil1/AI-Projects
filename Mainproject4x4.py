import pygame_widgets
import pygame
from pygame_widgets.slider import Slider

pygame.init()
clock = pygame.time.Clock()
width_proportion = 0.5
width = 1100
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
difficulty = 6
slider = Slider(screen, int(width * 0.1), int(height * 0.9), int(width * 0.8), 20, min=1, max=3, step=0.01)
grid = [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]
x = [width_proportion * width - 0.3 * height, width_proportion * width - 0.1 * height,
     width_proportion * width + 0.1 * height, width_proportion * width + 0.3 * height]
y = [0.2 * height, 0.4 * height, 0.6 * height, 0.8 * height]

def drawX(screen, x, y):
    Dx = (height / 1000) * 65
    Dy = (height / 1000) * 65
    pygame.draw.line(screen, 'black', (x - Dx, y - Dy), (x + Dx, y + Dy), 7)
    pygame.draw.line(screen, 'black', (x - Dx, y + Dy), (x + Dx, y - Dy), 7)

run = True
player = [0, 0]
first_player = True  # True if X first, False if O first
f = pygame.font.Font(None, 36)

stop = True

def checkWin(grid):
    for i in range(0, 4):
        if grid[i][0] == grid[i][1] == grid[i][2] == grid[i][3] != '-':
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] == grid[3][i] != '-':
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] == grid[3][3] != '-':
        return grid[0][0]
    if grid[0][3] == grid[1][2] == grid[2][1] == grid[3][0] != '-':
        return grid[0][3]
    for row in grid:
        if '-' in row:
            return 'C'
    return 'D'

def genX(grid, alpha, beta, depth):
    current = v = -2
    x = 4
    y = 4

    for i in range(0, 4):
        for j in range(0, 4):
            if grid[i][j] == '-':
                grid[i][j] = 'X'
                tmp = value(grid, alpha, beta, depth - 1)
                v = max(v, tmp[0])
                if v > current:
                    current = v
                    x = i
                    y = j
                grid[i][j] = '-'

                if v >= beta:
                    return (v, x, y)
                alpha = max(alpha, v)
    return (v, x, y)

def genO(grid, alpha, beta, depth):
    x = 4
    y = 4
    current = v = 2
    for i in range(0, 4):
        for j in range(0, 4):
            if grid[i][j] == '-':
                grid[i][j] = 'O'
                tmp = value(grid, alpha, beta, depth - 1)
                v = min(v, tmp[0])
                if v < current:
                    current = v
                    x = i
                    y = j
                grid[i][j] = '-'
                if v <= alpha:
                    return (v, x, y)
                beta = min(beta, v)
    return (v, x, y)

def evalFunction(grid):
    rO = 0
    rX = 0
    r = [[2, 1, 1, 2], [1, 3, 3, 1], [1, 3, 3, 1], [2, 1, 1, 2]]
    for i in range(0, 4):
        for j in range(0, 4):
            if grid[i][j] != "-":
                if grid[i][j] == "O":
                    rO += r[i][j]
                else:
                    rX += r[i][j]
    if rX > rO:
        return 1
    elif rX < rO:
        return -1
    else:
        return 0

def value(grid, alpha, beta, depth):
    tour = 0
    for i in grid:
        for j in i:
            if j != '-':
                tour += 1
    c = checkWin(grid)
    if depth == 0:
        return (evalFunction(grid), 4, 4)
    elif c == 'C':
        if tour % 2 == 0:
            res = genX(grid, alpha, beta, depth)
        else:
            res = genO(grid, alpha, beta, depth)
        return res
    elif c == 'D':
        return (0, 4, 4)
    elif c == 'X':
        return (1, 4, 4)
    else:
        return (-1, 4, 4)

while run:

    screen.fill('#e4e4e4')
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == 27):
            run = False
        elif event.type == pygame.KEYDOWN and event.key == 114:
            grid = [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']]
            first_player = True
            stop = True
            diff_level = round(slider.getValue())
            if diff_level == 1:
                difficulty = 3  # Easy
            elif diff_level == 2:
                difficulty = 6  # Medium
            elif diff_level == 3:
                difficulty = 9  # Hard
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and stop:
            pos = event.pos
            if pos[0] < width_proportion * width - 0.2 * height:
                player[0] = 0
            elif pos[0] < width_proportion * width:
                player[0] = 1
            elif pos[0] < width_proportion * width + 0.2 * height:
                player[0] = 2
            elif pos[0] > width_proportion * width + 0.2 * height:
                player[0] = 3

            if pos[1] < 0.3 * height:
                player[1] = 0
            elif pos[1] < 0.5 * height:
                player[1] = 1
            elif pos[1] < 0.7 * height:
                player[1] = 2
            elif pos[1] > 0.7 * height:
                player[1] = 3

            if grid[player[1]][player[0]] == '-' and pos[1] < 0.9 * height:
                if first_player:
                    grid[player[1]][player[0]] = 'X'  
                    first_player = False
                else:
                    grid[player[1]][player[0]] = 'O' 
                    first_player = True
        elif event.type == pygame.VIDEORESIZE:
            width = event.size[0]
            height = event.size[1]
            if width < 1.2 * height:
                width = 1.2 * height
            x = [width_proportion * width - 0.3 * height, width_proportion * width - 0.1 * height,
                 width_proportion * width + 0.1 * height, width_proportion * width + 0.3 * height]
            y = [0.2 * height, 0.4 * height, 0.6 * height, 0.8 * height]
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            slider.setY(int(height * 0.9))
            slider.setX(int(width * 0.1))
            slider.setWidth(int(width * 0.8))

    pygame.draw.line(screen, "black", (width_proportion * width - 0.40 * height, 0.3 * height),
                     (width_proportion * width + 0.40 * height, 0.3 * height), 5)  # a
    pygame.draw.line(screen, "black", (width_proportion * width - 0.40 * height, 0.5 * height),
                     (width_proportion * width + 0.40 * height, 0.5 * height), 5)  # b
    pygame.draw.line(screen, "black", (width_proportion * width - 0.40 * height, 0.7 * height),
                     (width_proportion * width + 0.40 * height, 0.7 * height), 5)  # c
    pygame.draw.line(screen, "black", (width_proportion * width - 0.2 * height, 0.2 * height),
                     (width_proportion * width - 0.2 * height, 0.8 * height), 5)  # d
    pygame.draw.line(screen, "black", (width_proportion * width, 0.2 * height),
                     (width_proportion * width, 0.8 * height), 5)  # e
    pygame.draw.line(screen, "black", (width_proportion * width + 0.2 * height, 0.2 * height),
                     (width_proportion * width + 0.2 * height, 0.8 * height), 5)  # f

    for i in range(0, 4):
        for j in range(0, 4):
            if grid[i][j] == 'X':
                drawX(screen, x[j], y[i])
            elif grid[i][j] == 'O':
                pygame.draw.circle(screen, "black", (x[j], y[i]), (height / 1000) * 75, 5)

    result = checkWin(grid)

    if result == 'C':
        if not first_player:
            p, o1, o2 = value(grid, -2, 2, difficulty)
            grid[o1][o2] = 'O'
            first_player = True
    else:
        if result == 'X':
            text = f.render("X Wins the game!!", True, (255, 0, 0))
            screen.blit(text, (width / 2 - width * 0.11, height * 0.05))
            stop = False
        elif result == 'O':
            text = f.render("O Wins the game!!", True, (255, 0, 0))
            screen.blit(text, (width / 2 - width * 0.11, height * 0.05))
            stop = False
        elif result == 'D':
            text = f.render("It's a Draw :(", True, (255, 0, 0))
            screen.blit(text, (width / 2 - width * 0.11, height * 0.05))
            stop = False

    diff_level = round(slider.getValue())
    if diff_level == 1:
        difficulty_text = "Easy"
    elif diff_level == 2:
        difficulty_text = "Medium"
    elif diff_level == 3:
        difficulty_text = "Hard"

    text = f.render("Difficulty: " + difficulty_text, True, (0, 0, 0))
    screen.blit(text, (width * 0.1, 0.2 * height))
    text = f.render("Press R to reset the game and adjust the difficulty", True, (0, 0, 0))
    screen.blit(text, (width * 0.24, 0.08 * height))  
    pygame_widgets.update(pygame.event.get())
    clock.tick(120)
    pygame.display.update()