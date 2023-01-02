from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    new_window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_box_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps == 0 or reps % 2 == 0:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN )
        reps += 1
    elif reps % 2 == 1 and reps < 8:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
        reps += 1
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
        reps = 0


#------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = new_window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check_box_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
new_window = Tk()
new_window.title("Pomodoro")
new_window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
slika_paradajza = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=slika_paradajza)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"))
timer_label.config(bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check_box_label = Label(font=(FONT_NAME, 20, "bold"))
check_box_label.config(bg=YELLOW, fg=GREEN)
check_box_label.grid(column=2, row=3)


new_window.mainloop()