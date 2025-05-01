import turtle
import pandas

screen =turtle.Screen()
screen.title("U.S States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

# print(all_states)
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state" , prompt="What's another states's name").title()
    if answer_state == "Exit":
        
        ## list comprehenstion
        states_to_know =[state for state in all_states if state not in guessed_state]
        state_name = pandas.DataFrame(states_to_know)
        state_name.to_csv("State_names_to_know.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t= turtle.Turtle()
        t.up()
        t.hideturtle
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

