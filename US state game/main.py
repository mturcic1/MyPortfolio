import pandas
import turtle
screen = turtle.Screen()
state_image = turtle.Turtle()

# Screen code and turtle loading as image
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
state_image.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state
state_list = states.tolist()
guessed_country = 0
game_is_on = True
correct_guesses = []
states_to_learn = []
while game_is_on:
    guess_state = screen.textinput(title=f"{guessed_country}/50 States Correct", prompt="Enter state name: ").title()
    if guess_state == "Exit":
        break

    if guess_state in state_list:
        correct_guesses.append(guess_state)
        state_coordinates = data[data.state == guess_state]
        state_coordinate_x = int(state_coordinates.x)
        state_coordinate_y = int(state_coordinates.y)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(state_coordinate_x, state_coordinate_y)
        turtle.write(guess_state)
        guessed_country += 1

for item in state_list:
    if item not in correct_guesses:
        states_to_learn.append(item)

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("States_to_learn.csv")


