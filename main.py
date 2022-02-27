from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('King of the Dice')
root.iconbitmap('Img/Bitmap_icon.ico')
root.configure(bg='#127115')
root.geometry('701x960')
root.resizable(False, False)

# Permanent labels top

# Title and slogan
title_app = Label(root, text='King of the Dice', font='Courier 36 bold', 
                  bg='#127115', fg='red',)

slogan_app = Label(root, text='"Dare the Dice to win the Price"', 
                   font='Courier 18 bold', bg='#127115', fg='darkred')

# Game explanantions
explanation_1 = Label(root, text='Gooi 3 maal 6 voor een Jackpot van 100' + 
                      'euro!!!!!', font='Verdana 11 bold', bg='#127115', 
                      fg='red')
explanation_2 = Label(root, text='Gooi met minmaal 4 tot maximaal 6! ' + 
                      'dobbelstenen', font='Verdana 11 bold', bg='#127115', 
                      fg='red')
explanation_3 = Label(root, text='Is bij verlies je score boven hoger dan ' + 
                      'onder dan is je beurt gratis!!', font='Verdana 11 bold',
                      bg='#127115', fg='red')
explanation_4 = Label(root, text='Inleg is één euro per dobbelsteen', 
                      font='Verdana 11 bold', bg='#127115', fg='red')

# Used Images
start_game = ImageTk.PhotoImage(Image.open('Img/Welkom.jpg'))
win_game = ImageTk.PhotoImage(Image.open('Img/Winner.jpg'))
loose_game = ImageTk.PhotoImage(Image.open('Img/Looser.jpg'))

# Variable label for cartoon 
cartoon_app = Label(image=start_game, borderwidth=0)

title_app.grid(row=0, column=0, columnspan=6)
slogan_app.grid(row=1, column=0, columnspan=6)
cartoon_app.grid(row=2, column=0, columnspan=6)
explanation_1.grid(row=3, column=0, columnspan=6)
explanation_2.grid(row=4, column=0, columnspan=6)
explanation_3.grid(row=5, column=0, columnspan=6)
explanation_4.grid(row=6, column=0, columnspan=6)

###############################################################################

# Labels which show up in the game

# Label to show if input dice is right (must be 4 - 6 dice)
validate_input = Label(root, text='', font='Verdana 18 bold', bg='#127115', 
                       fg='red')
validate_input.place(x=185, y=700)

# Labels for dice
result_1 = Label(root, image='', bg='#127115')
result_2 = Label(root, image='', bg='#127115')
result_3 = Label(root, image='', bg='#127115')
result_4 = Label(root, image='', bg='#127115')
result_5 = Label(root, image='', bg='#127115')
result_6 = Label(root, image='', bg='#127115')

result_1.place(x=58, y=660)
result_2.place(x=165, y=660)
result_3.place(x=272, y=660)
result_4.place(x=379, y=660)
result_5.place(x=486, y=660)
result_6.place(x=593, y=660)

# Label for outcome game
outcome_game = Label(root, text='', bg='#127115' )
outcome_game.place(x=40, y=725)

# Label for total top of the dice
total_above = Label(root, pady=10, text='', font='Verdana 10 bold underline', 
                    justify='left', bg='#127115', fg='darkred')
total_above.place(x=10, y=820)

# Label for total bottom of the dice
total_beneath = Label(root, pady=10, text='', font='Verdana 10 bold underline', 
                      bg='#127115', fg='darkred')
total_beneath.place(x=467, y=820)

# Label for confirmation free turn
extra_turn = Label(root, text='', font='Verdana 10 bold', bg='#127115', 
                   fg='gold')
extra_turn.place(x=220, y=915)

# Label to ask to throw again
restart_game = Label(root, text='', font='Courier 18 bold',bg='#127115', 
                     fg='red')
restart_game.place(x=470, y=872)

###############################################################################

# Variables for the game

score_0 = ""
score_1 = PhotoImage(file='Img/Dobbel1 (50x50).png')
score_2 = PhotoImage(file='Img/Dobbel2 (50x50).png')
score_3 = PhotoImage(file='Img/Dobbel3 (50x50).png')
score_4 = PhotoImage(file='Img/Dobbel4 (50x50).png')
score_5 = PhotoImage(file='Img/Dobbel5 (50x50).png')
score_6 = PhotoImage(file='Img/Dobbel6 (50x50).png')

score_list = [score_0, score_1, score_2, score_3, score_4, score_5, score_6]

turn = 0
price = 0

# Functions used in game

# Bet calculation for a turn with 4 dice

def turn_4_dice():
    global turn

    turn = turn + 4

    turn_count.config(text=turn)

# Bet calculation for a turn with 5 dice

def turn_5_dice():
    global turn

    turn = turn + 5

    turn_count.config(text=turn)

# Bet calculation for a turn with 6 dice

def turn_6_dice():
    global turn

    turn = turn + 6

    turn_count.config(text=turn)

# Subtract turn on free turn won

def turn_free():
    global turn
    global aantal_dobbelstenen

    turn = turn - number_dice

    turn_count.config(text=turn)

# Calculation total money won

def prize_money():
    global price

    price = price + 100

    price_count.config(text=price)

#  Calculation balance buy-in - prize money. This is shown with background
#  colors in the buy-in label and prize money label

def profit():
    if turn > price:
        turn_count.config(bg='red', fg='white')
        price_count.config(bg='red', fg='white')

    else:
        turn_count.config(bg='green', fg='white')
        price_count.config(bg='green', fg='white')

# Function to restart the game

def reset_game():
    button_start.config(state=NORMAL)
    cartoon_app.config(image=start_game, borderwidth=0)
    result_1.config(image='')
    result_2.config(image='')
    result_3.config(image='')
    result_4.config(image='')
    result_5.config(image='')
    result_6.config(image='')
    validate_input.config(text='')
    outcome_game.config(text='')
    total_above.config(text='')
    total_beneath.config(text='')
    extra_turn.config(text='')
    restart_game.config(text='')
    restart_yes.config(state=DISABLED)
    restart_no.config(state=DISABLED)
    input_dice.config(state=NORMAL)

###############################################################################

# Function to play the game

def game():

    # Check if input is 4, 5, or 6 dice
    try:
        float(input_dice.get())
        validate_input.config(text="")

        global number_dice
        number_dice = int(input_dice.get())

        if number_dice < 4 or number_dice > 6:
            validate_input.config(text="Invoer is onjuist")

        # Throw dice
        else:
            def throw_dice():
                input_dice.delete(0, END)
                input_dice.config(state=DISABLED)

                # Possible result dice. (Extra 6 for more chance to win and an
                # extra 1 for less chance to win an extra turn)
                dice = (1, 1, 2, 3, 4, 5, 6, 6)
                return(random.choice(dice))

            dice_1 = throw_dice()
            dice_2 = throw_dice()
            dice_3 = throw_dice()
            dice_4 = throw_dice()
            dice_5 = throw_dice()
            dice_6 = throw_dice()

            # Result 4 dice and build array to check win and free turn and 
            # udate buy-in

            if number_dice == 4:
                result_2.config(image=score_list [dice_2])
                result_3.config(image=score_list [dice_3])
                result_4.config(image=score_list [dice_4])
                result_5.config(image=score_list [dice_5])
                button_start.config(state=DISABLED)

                total = [dice_2, dice_3, dice_4, dice_5]
                turn_4_dice()

            # Result 5 dice and build array to check win and free turn and 
            # udate buy-in

            if number_dice == 5:
                result_1.config(image=score_list [dice_1])
                result_2.config(image=score_list [dice_2])
                result_3.config(image=score_list [dice_3])
                result_4.config(image=score_list [dice_4])
                result_5.config(image=score_list [dice_5])
                button_start.config(state=DISABLED)

                total = [dice_1, dice_2, dice_3, dice_4, dice_5]
                turn_5_dice()

            # Result 6 dice and build array to check win and free turn and 
            # udate buy-in

            if number_dice == 6:
                result_1.config(image=score_list [dice_1])
                result_2.config(image=score_list [dice_2])
                result_3.config(image=score_list [dice_3])
                result_4.config(image=score_list [dice_4])
                result_5.config(image=score_list [dice_5])
                result_6.config(image=score_list [dice_6])
                button_start.config(state=DISABLED)

                total = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]
                turn_6_dice()

            # Check jackpotwin

            jackpot = (total.count(6))

            if jackpot >= 3:
                cartoon_app.config(image=win_game, borderwidth=0)
                outcome_game.config(pady= 30, text='WINNER!!!!!!!!!', 
                                    font='Verdana 44 bold', fg='gold')
                prize_money()

            else:
                cartoon_app.config(image=loose_game, borderwidth=0)
                outcome_game.config(pady= 3, text='      LOST :(', 
                                    font='Verdana 44 bold', fg='red',)

                # Check in case of loss if total top is higher then 
                # total bottom to get the last turn for free.

                total_top = sum(total)
                total_bottom = int(number_dice * 7) - (sum(total))

                total_above.config(text='Totaal bovenkant = ' + format(total_top))

                total_beneath.config(text='Totaal onderkant = ' + 
                                          format(total_bottom))

                if total_top >= total_bottom:
                        extra_turn.config(text='Deze beurt was gratis!', fg='gold')
                        turn_free()

                if total_top < total_bottom:
                        extra_turn.config(text='')

            # Update colors in the labels for buy-in and prize money 
            
            profit()

            restart_game.config(text='OPNIEUW?')
            restart_yes.config(state=NORMAL)
            restart_no.config(state=NORMAL)

    except  ValueError: 
        validate_input.config(text="Invoer is onjuist")

###############################################################################

# Labels for input dice

# Label to ask number of dice
entry_dice = Label(root, padx=10, pady=25, text='Aantal Stenen', 
                   font='Courier 16 bold', bg='#127115', fg='red')
entry_dice.grid(row=7, column=0, columnspan=2, stick=W)

# Input dice
input_dice = Entry(root, width=5, font='Courier 16 bold', justify='center', 
                   fg='red')
input_dice.place(x=310, y=595)

# Button restart game
button_start = Button(root, padx=50, text='ROLL', font='Courier 16 bold', 
                      bg='gold',  fg='red',
                            bd=8, relief=RAISED, command=game)
button_start.place(x=490, y=580)

###############################################################################

# Permanent labels bottom

# Label for costs with image
turn_count = Label(root, width=5, text=turn, font='Courier 16 bold', bg='red', 
                   fg='white', bd=5, relief="sunken")
turn_count.place(x=10, y=910)

turn_img = ImageTk.PhotoImage(Image.open('Img/Munt.jpg'))
cartoon_costs = Label(image=turn_img, borderwidth=0)
cartoon_costs.place(x=42, y=872)

# Label for profit with image
price_count = Label(root, width=5, text=price, font='Courier 16 bold', 
                    bg='white', fg='darkgreen', bd=5, relief="sunken")
price_count.place(x=120, y=910)

price_img = ImageTk.PhotoImage(Image.open('Img/Geldzak.jpg'))
cartoon_profit = Label(image=price_img, borderwidth=0)
cartoon_profit.place(x=147, y=865)

# Buttons restart or cash
restart_yes = Button(root, text='Opnieuw', font='Courier 10 bold',
                     bg='gold', fg='darkgreen', bd=4, relief=RAISED, 
                     state=DISABLED, command=reset_game)
restart_yes.place(x=450, y=910)

restart_no = Button(root, text='Uitbetalen', font='Courier 10 bold', 
                    bg='gold',  fg='red', bd=4, relief=RAISED, 
                    state=DISABLED, command=root.quit)
restart_no.place(x=575, y=910)

root.mainloop()