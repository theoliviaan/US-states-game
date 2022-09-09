import turtle as t
import pandas


screen = t.Screen()
screen.title("U.S. States Game")

tim = t.Turtle()
tim.hideturtle()

image = "blank_states_img.gif"
screen.addshape(image)


t.shape(image)

# 1. change answer to title case
data = pandas.read_csv("50_states.csv")



score = 0
correct_guesses = []


# 4. A loop to allow the user to keep guessing
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 states", prompt="Whats another states name?").title()
    if answer_state == "Exit":
        not_guessed = [each_state for each_state in data["state"] if each_state not in correct_guesses]

        # not_guessed = []
        # for each_state in data["state"]:
        #     if each_state not in correct_guesses:
        #         not_guessed.append(each_state)
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("./us-states-game-start/States_not_guessed.csv")
        break


    # 2.check if answer is among the 50 states
    for each_state in data["state"]:
        if answer_state == each_state:
            score += 1
            # 5. Record the correct guesses in a list
            correct_guesses.append(answer_state)
            # 3.check correct guesses unto to the map
            get_data = data[data.state == answer_state]
            x = int(get_data.x)
            y = int(get_data.y)
            tim.penup()
            tim.goto(x, y)
            tim.write(each_state, True, font=('Arial', 7, 'normal'))




