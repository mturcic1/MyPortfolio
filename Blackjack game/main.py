from tkinter import *
import settings
import random
from PIL import Image, ImageTk


# ---------------------------------------------------------Button creation----------------------------------------------
def create_deal_button():
    btn = Button(
        root,
        width=int(settings.width_percent(0.8)),
        height=int(settings.height_percent(0.4)),
        text="Deal",
        bg="DarkSalmon",
        fg="DarkSlateBlue",
        command=lambda : deal_cards()

    )
    btn.place(x=0, y=settings.height_percent(53))


def create_hit_me_button():
    btn = Button(
        root,
        width=int(settings.width_percent(0.8)),
        height=int(settings.height_percent(0.4)),
        text="Hit me",
        bg="DarkSalmon",
        fg="DarkSlateBlue",
        command=lambda : hit_me()

    )
    btn.place(x=settings.width_percent(7), y=settings.height_percent(53))


def create_stand_button():
    btn = Button(
        root,
        width=int(settings.width_percent(0.8)),
        height=int(settings.height_percent(0.4)),
        text="Stand",
        bg="DarkSalmon",
        fg="DarkSlateBlue",
        command=lambda: stand()
    )
    btn.place(x=settings.width_percent(14), y=settings.height_percent(53))


# -------------------------------------------------------Card dealing and adding cards----------------------------------
def deal_cards():
    player_left_card.create_image(image_width / 2, image_height / 2, image=card_list[0])
    player_right_card.create_image(image_width / 2, image_height / 2, image=card_list[1])
    dealer_right_card.create_image(image_width / 2, image_height / 2, image=card_list[2])


def hit_me():
    player_next_card = Canvas(
        root,
        width=image_width,
        height=image_height
    )
    player_next_card.place(x=settings.width_percent(settings.starting_player_placement_counter),
                           y=settings.height_percent(60))
    player_next_card.create_image(image_width / 2, image_height / 2, image=card_list[settings.starting_index_counter])
    player_hand.append(deck[card_list[settings.starting_index_counter]])
    settings.starting_index_counter += 1
    settings.starting_player_placement_counter += 14


def stand():
    disable_hit_me()
    dealer_left_card.create_image(image_width / 2, image_height / 2, image=card_list[3])
    dealer_draw()
    check_result()


def disable_hit_me():
    label = Label(root,
                  width=int(settings.width_percent(0.8)),
                  height=int(settings.height_percent(0.4)),
                  text="Hit me",
                  bg="DarkSalmon",
                  fg="Gray")
    label.place(x=settings.width_percent(7), y=settings.height_percent(53))


def dealer_draw():
    while settings.determine_total(dealer_hand) <= 16:

        dealer_next_card = Canvas(
            root,
            width=image_width,
            height=image_height
        )
        dealer_next_card.place(x=settings.width_percent(settings.starting_dealer_placement_counter),
                               y=settings.height_percent(-12))
        dealer_next_card.create_image(image_width / 2, image_height / 2,
                                      image=card_list[settings.starting_index_counter])
        dealer_hand.append(deck[card_list[settings.starting_index_counter]])
        settings.starting_index_counter += 1
        settings.starting_dealer_placement_counter -= 14


def check_result():
    if settings.determine_total(dealer_hand) > 21:
        label = Label(root,
                      width=int(settings.width_percent(3)),
                      height=int(settings.height_percent(2)),
                      text="House has gone bust. YOU WIN!",
                      bg="DarkSalmon",
                      fg="DarkGreen",
                      font=("Arial Black", 15)
                      )
        label.place(x=settings.width_percent(18), y=settings.height_percent(25))
    elif settings.determine_total(player_hand) == 21 == settings.determine_total(dealer_hand):
        label = Label(root,
                      width=int(settings.width_percent(3)),
                      height=int(settings.height_percent(2)),
                      text="It's a push!",
                      bg="DarkSalmon",
                      fg="Black",
                      font=("Arial Black", 15)
                      )
        label.place(x=settings.width_percent(18), y=settings.height_percent(25))
    elif settings.determine_total(dealer_hand) < 21 < settings.determine_total(player_hand):
        label = Label(root,
                      width=int(settings.width_percent(3)),
                      height=int(settings.height_percent(2)),
                      text="Over 21. YOU LOSE",
                      bg="DarkSalmon",
                      fg="DarkRed",
                      font=("Arial Black", 15)
                      )
        label.place(x=settings.width_percent(18), y=settings.height_percent(25))
    elif settings.determine_total(dealer_hand) < settings.determine_total(player_hand) <= \
            settings.determine_total(player_hand) <= 21:
        label = Label(root,
                      width=int(settings.width_percent(3)),
                      height=int(settings.height_percent(2)),
                      text="YOU WIN!",
                      bg="DarkSalmon",
                      fg="DarkGreen",
                      font=("Arial Black", 15)
                      )
        label.place(x=settings.width_percent(18), y=settings.height_percent(25))
    elif settings.determine_total(player_hand) < settings.determine_total(dealer_hand) <= \
            settings.determine_total(dealer_hand) <= 21:
        label = Label(root,
                      width=int(settings.width_percent(3)),
                      height=int(settings.height_percent(2)),
                      text="YOU LOSE!",
                      bg="DarkSalmon",
                      fg="DarkRed",
                      font=("Arial Black", 15)
                      )
        label.place(x=settings.width_percent(18), y=settings.height_percent(25))
    elif settings.determine_total(player_hand) == settings.determine_total(dealer_hand) <= \
            settings.determine_total(dealer_hand) <= 21:
        label = Label(root,
                      width=int(settings.width_percent(3)),
                      height=int(settings.height_percent(2)),
                      text="It's a push!",
                      bg="DarkSalmon",
                      fg="Black",
                      font=("Arial Black", 15)
                      )
        label.place(x=settings.width_percent(18), y=settings.height_percent(25))


# -------------------------------------------------------Starting window------------------------------------------------
root = Tk()
# -------------------------------------------------------Image file-----------------------------------------------------
back_side_image = PhotoImage(file="Card_back.PNG")
image_width = back_side_image.width()
image_height = back_side_image.height()
table_top_image = PhotoImage(file="Table_top.PNG")
top_width = table_top_image.width()
top_height = table_top_image.height()

root.geometry(f"{top_width}x{top_height}")
root.configure(bg="black")
root.title("Blackjack")
root.resizable(width=False, height=False)
# -------------------------------------------------------Deck creation--------------------------------------------------
colors = ["c", "d", "h", "s"]
card_list = []


for color in colors:
    for value in range(1, 14):
        card = Image.open(f"Classic/{color}{value}.png")
        card = card.resize((image_width, image_height), Image.LANCZOS)
        card = ImageTk.PhotoImage(card)
        card_list.append(card)

deck = dict(zip(card_list, settings.create_card_values()))

# -----------------------------------------------------Shuffling and dealing--------------------------------------------
random.shuffle(card_list)
player_hand = [deck[card_list[0]], deck[card_list[1]]]
dealer_hand = [deck[card_list[2]], deck[card_list[3]]]

# ------------------------------------------------------Table frame creation-------------------------------------------
top_of_table = Canvas(
    root,
    width=top_width,
    height_=top_height
)
top_of_table.place(x=0, y=0)
top_of_table.create_image(top_width/2, top_height/2, image=table_top_image)

# -------------------------------------------------------Card frame creation--------------------------------------------
dealer_left_card = Canvas(
    root,
    width=image_width,
    height=image_height
)
dealer_left_card.place(x=settings.width_percent(45), y=settings.height_percent(-12))
dealer_left_card.create_image(image_width/2, image_height/2, image=back_side_image)

dealer_right_card = Canvas(
    root,
    width=image_width,
    height=image_height
)
dealer_right_card.place(x=settings.width_percent(59), y=settings.height_percent(-12))
dealer_right_card.create_image(image_width/2, image_height/2, image=back_side_image)

player_left_card = Canvas(
    root,
    width=image_width,
    height=image_height
)
player_left_card.place(x=settings.width_percent(5), y=settings.height_percent(60))
player_left_card.create_image(image_width/2, image_height/2, image=back_side_image)

player_right_card = Canvas(
    root,
    width=image_width,
    height=image_height
)
player_right_card.place(x=settings.width_percent(19), y=settings.height_percent(60))
player_right_card.create_image(image_width/2, image_height/2, image=back_side_image)

create_deal_button()
create_hit_me_button()
create_stand_button()
# ----------------------------------------------------------Run the window----------------------------------------------
root.mainloop()


