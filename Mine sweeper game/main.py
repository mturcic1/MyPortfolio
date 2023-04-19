from tkinter import *
import settings
import utilities
from cell import Cell

root = Tk()
# Settings of the window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(width=False, height=False)

# Frame creation
top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utilities.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="White",
    text="Minesweeper game",
    font=("Times new roman", 40)
)

left_frame = Frame(
    root,
    bg="black",
    width=utilities.width_prct(25),
    height=settings.HEIGHT
)
left_frame.place(x=0, y=utilities.height_prct(25))

right_frame = Frame(
    root,
    bg="black",
    width=utilities.width_prct(75),
    height=utilities.height_prct(75)
)
right_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(right_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

game_title.place(
    x=utilities.height_prct(50),
    y=0
)
Cell.create_cell_btn_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines()





# Run the window
root.mainloop()


