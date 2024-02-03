import random
from tkinter import *
# constants
w1_Width = 1200
w1_Height = 800
spase_size = 10
snake_lenght = 3
speed = 25
background_color = 'black'
food_color = 'brown'
head_color = 'white'
body_color = 'white'
class Snake:
    def __init__(self):
        self.snake_lenght = snake_lenght
        self.coord = [[0, 0]] * 3
        self.squares = []

        for x, y in self.coord:
            square = c.create_rectangle(x, y, x + spase_size, y + spase_size, fill=body_color)
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (w1_Width/spase_size) - 1) * spase_size  # 1200/25 = 48
        y = random.randint(0, (w1_Height/spase_size) - 1) * spase_size  # 800/25 = 32


        self.coord = [x, y]
        c.create_rectangle(x, y, x + spase_size, y + spase_size, fill=food_color)

def move (snake, food):
    for x, y in snake.coord:
        square = c.create_rectangle(x, y, x + spase_size, y + spase_size, fill=body_color)
    x, y = snake.coord[0]

    if (direction == 'down'):
        y += spase_size
    elif (direction == 'up'):
        y -= spase_size
    elif (direction == 'left'):
        x -= spase_size
    elif (direction == 'right'):
        x += spase_size

    snake.coord.insert(0, (x, y))
    square = c.create_rectangle(x, y, x + spase_size, y + spase_size, fill=head_color)
    snake.squares.insert(0, square)

    if (x == food.coord[0] and y == food.coord[1]):
        global score
        score += 1
        Label_score.config(text = 'Счёт: {}'.format(score))

        c.delete('food')
        food = Food()
    else:
        x, y = snake.coord[-1]
        square = c.create_rectangle(x, y, x + spase_size, y + spase_size, fill=background_color)

        del snake.coord[-1]
        c.delete(snake.squares[-1])
        del snake.squares[-1]

    if (check_collisions(snake)):
        pass
        # game_over()
    else:
        w1.after(speed, move, snake, food)

def cange_direction(new_dir):
    global direction

    if (new_dir == 'down'):
        if(direction != 'up'):
            direction = new_dir
    elif (new_dir == 'up'):
        if (direction != 'down'):
            direction = new_dir
    elif (new_dir == 'left'):
        if (direction != 'right'):
            direction = new_dir
    elif (new_dir == 'right'):
        if (direction != 'left'):
            direction = new_dir

def check_collisions(snake):
    x, y = snake.coord[0]

    if (x < 0 or x >= w1_Width):
        return True
    elif (y < 0 or y >= w1_Height):
        return True

    for snake_lenght in snake.coord[1:]:
        if (x == snake_lenght[0] and y == snake_lenght[1]):
            return True

def game_over():
    c.delete(ALL)
    c.create_text(c.winfo_width()/2, c.winfo_height()/2, font=('Futurs PT', 50), text = 'Вы проиграли', fill='red')
    c.create_text(c.winfo_width() / 2, c.winfo_height() / 2, font=('Futurs PT', 50), text='\n\nПопробуйте снова', fill='green')

w1 = Tk()
w1.title('Змейка  :D, автор Шляхта')
w1.resizable(False, False)
w1.geometry('1200x870')

w1.bind('<Down>', lambda event: cange_direction('down'))
w1.bind('<Up>', lambda event: cange_direction('up'))
w1.bind('<Left>', lambda event: cange_direction('left'))
w1.bind('<Right>', lambda event: cange_direction('right'))


score = 0
direction = 'down'
Label_score = Label(w1, text='Счёт: {}'.format(score), font=('Arial', 40))
Label_score.pack()

c = Canvas(w1, height=w1_Height, width=w1_Width, bg=background_color)
c.pack()
snake = Snake()
food = Food()
move(snake, food)
w1.mainloop()