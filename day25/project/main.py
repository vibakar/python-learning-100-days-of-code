import pandas
from turtle import Turtle, Screen

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("Name the states")
turtle = Turtle()
turtle.shape(image)
correct_answer = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

def display_missed_states():
    missed_states = [state for state in all_states if state not in guessed_states]
    data_dict = {
        "missed_states": missed_states
    }
    print(missed_states)
    df = pandas.DataFrame(data_dict)
    df.to_csv("missed_states.csv")
    exit()

for _ in range(len(data) + 1):
    answer = screen.textinput(title=f"{correct_answer}/50 States Correct", prompt="What's the state name?")
    user_answer = answer.title() if answer else display_missed_states()
    row = data[data['state'] == user_answer]

    if len(row) > 0:
        correct_answer += 1
        guessed_states.append(user_answer)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(row.x), int(row.y))
        turtle.write(user_answer, font=("Courier", 14, "normal"))
    else:
        print("State name doesn't exist")

screen.exitonclick()
