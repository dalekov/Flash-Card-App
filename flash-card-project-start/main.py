from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Loading the data:
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/spanish_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}
# ---------------------------- CREATE NEW FLASHCARDS -------------------------------- #
def next_card():
    global current_card
    current_card = random.choice(to_learn)

    spanish_word = current_card["Spanish"]

    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=f"{spanish_word}", fill="black")
    canvas.itemconfig(canvas_background, image=card_front_image)
    flip_timer = root.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()
# ---------------------------- UI SETUP --------------------------------------------- #
root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas attributes, images for the front and back of the card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Wrong button:
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

# Right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

next_card()

root.mainloop()
