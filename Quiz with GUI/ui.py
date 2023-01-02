from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.my_canvas = Canvas(width=300, height=250)
        self.question_text = self.my_canvas.create_text(150, 120, text="Dt", fill=THEME_COLOR, width=280, font=("Arial",
                                                                                                                20,
                                                                                                                'italic'
                                                                                                                ))
        self.my_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.yes_image = PhotoImage(file="C:/Users/Matija/Desktop/Programiranje/Quizzler/images/true.png")
        self.yes_button = Button(image=self.yes_image, highlightthickness=0, command=self.true_pressed)
        self.yes_button.grid(row=2, column=0)
        self.no_image = PhotoImage(file="C:/Users/Matija/Desktop/Programiranje/Quizzler/images/false.png")
        self.no_button = Button(image=self.no_image, highlightthickness=0, command=self.false_pressed)
        self.no_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.my_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.my_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.my_canvas.itemconfig(self.question_text, text="You reached the end of the quiz.")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.my_canvas.config(bg="green")
        else:
            self.my_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)