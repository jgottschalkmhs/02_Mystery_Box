from tkinter import *
from functools import partial


class Start:
    def __init__(self, parent):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        self.temp_Converter_label = Label(self.start_frame,
                                          text="Mystery Box Game",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="please enter a dollar amount "
                                          "(Between $5 and $50). in the box "
                                          "below. Then choose the stakes."
                                          "The higher the stakes the more "
                                          "you can win!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        self.entry_error_frame = Frame(self.start_frame, width=10)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame,
                                        font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.entry_error_frame,
                                       font="Arial 19 bold",
                                       text="Add Funds",
                                       command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1)

        self.amount_error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Orange low stakes button
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="#FF9933")
        self.low_stakes_button.grid(row=0, column=0, pady=10)

        # Yellow Medium stakes button
        self.medium_stakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="#FFFF33")
        self.medium_stakes_button.grid(row=0, column=1, pady=10)

        # Green High Stakes button
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)",
                                       command=lambda: self.to_game(3),
                                       font=button_font, bg="#99FF33")
        self.high_stakes_button.grid(row=0, column=2, pady=10)

        # Disabling buttons
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # help button
        self.help_button = Button(self.stakes_frame, text="How to Play",
                                       font=button_font, bg="#808080", fg="white")
        self.help_button.grid(row=1, column=1, pady=10)

    # Number checking function
    def check_funds(self):
        starting_balance = self.start_amount_entry.get()
        # Game(self, stakes, starting_balance)

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # Disabling buttons
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you " \
                                 "can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high!  The most you can risk in " \
                                 "This game is $50"

            elif starting_balance >= 15:
                # Enable all buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)

            elif starting_balance >= 10:
                # Enable 2 buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)

            else:
                # Enable low stakes button
                self.low_stakes_button.config(state=NORMAL)

        except ValueError:
            has_errors= "yes"
            error_feedback = "Please enter a dollar amount(no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):

        starting_balance = self.starting_funds.get()

        Game(self, stakes, starting_balance)

        # hide start up menu disabled for testing purposes
        # root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        self.balance = IntVar()

        self.balance.set(starting_balance)

        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=3)

        self.play_button = Button(self.game_frame, text="Gain",
                                   padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=4)

    def reveal_boxes(self):
        # retrieval the balance from the initial function
        current_balance = self.balance.get()

        # adjust balance
        current_balance +=2

        # set balance to new balance
        self.balance.set(current_balance)

        # Edit label so user can see balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
