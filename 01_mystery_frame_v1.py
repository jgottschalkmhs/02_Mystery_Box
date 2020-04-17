from tkinter import *
from functools import partial


class Start:
    def __init__(self, parent):

        background_color = "white"

        self.start_frame = Frame(bg=background_color, pady=10)
        self.start_frame.grid()

        self.temp_Converter_label = Label(self.start_frame,
                                          text="Mystery Box Game",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=1)

        self.lowstakes_button = Button(self.start_frame,
                                       text="Low($5)",
                                       padx=10,
                                       pady=10,
                                       command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=2)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        partner.lowstakes_button.config(state=DISABLED)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
