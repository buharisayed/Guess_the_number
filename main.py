import tkinter as tk
import random


# Creating a window
window = tk.Tk()

# dimension setting for window created
window.geometry('600x500')

# bg color for window
window.config(bg="#999966")

window.resizable(width=False, height=False)

# window title

window.title('Number Guessing Game')

TARGET = random.randint(0, 10)
RETRY = 0


def update_result(text):
    result.configure(text=text)


# create  a new game

def new_game():
    guess_button.config(state='normal')
    global TARGET, RETRY
    TARGET = random.randint(0, 10)
    RETRY = 0
    update_result(text="Guess a number between \n 1 and 10")


# continuing game or ending game
def play_game():
    global RETRY

    choice = int(number_form.get())

    if choice != TARGET:
        RETRY += 1

        result = "\nWrong Guess Try again"
        if TARGET < choice:
            hint = f"The required number lies between 0 and{result}"
        else:
            hint = f"The required number lies between {choice} and 10"
        result += "\n\n Hint :\n"+hint

    else:
        result = f"You Guessed the correct number and tried {RETRY} times"
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"

    update_result(result)


title = tk.Label(window, text="Guess The Number", font=("Arial", 24), fg="white", bg="#999966")

result = tk.Label(window, text="Enter between 1 to 10\n\nClick Play Game to Start again", font=("Arial", 12,'bold'), fg="White", bg="#999966", justify=tk.LEFT)

play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg="Black", bg="#29c70a",command=new_game)

guess_button = tk.Button(window, text="Guess", font=("Arial", 13), fg="#13d675", bg="Black",command=play_game)

exit_button = tk.Button(window, text="ExitGame", font=("Arial", 14), fg="white", bg="#b82741", command=exit)

guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 11), textvariable=guessed_number)

title.place(x=170, y=50)
result.place(x=180, y=210)

exit_button.place(x=300, y=400)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=400)
number_form.place(x=180, y=152)

window.mainloop()
