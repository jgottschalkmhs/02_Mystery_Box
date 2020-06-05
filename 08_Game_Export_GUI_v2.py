from tkinter import *
from functools import partial
import random


class Game:
    def __init__(self):

        # Formatting variables
        self.game_stats_list = [50, 6]

        self.round_stats_list = ['lead ($0) | lead ($0) | lead ($0) - Cost: $15 |Payback: $0 | Current Balance: $11',
                                 'lead ($0) | copper ($1) | lead ($0) - Cost: $5 |Payback: $1 | Current Balance: $4',
                                 'lead ($0) | lead ($0) | copper ($1) - Cost: $5 |Payback: $1 | Current Balance: $3',
                                 'lead ($0) | copper ($1) | copper ($1) - Cost: $5 |Payback: $2 | Current Balance: $3']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # History Button (row 1)
        self.stats_button = Button(self.game_frame,
                                   text="Game Stats",
                                   font="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)


class GameStats:
    def __init__(self, partner, game_history, game_stats):

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = " Arial 12 bold"
        content= "Arial 12"

        # Sets up child window(ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,
                                                            partner))

        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up help heading (row 0)
        self.stats_heading = Label(self.stats_frame, text="Game Statistics",
                                   font="arial 19 bold")
        self.stats_heading.grid(row=0)

        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics."
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting Balance (Row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting balance (row 2)
        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value = Label(self.details_frame, font=content,
                                         text="${}".format(game_stats[0]), anchor="w")
        self.start_balance_value.grid(row=0, column=1, padx=0)

        # Current Balance (row 2.2)
        self.current_balance_label = Label(self.details_frame, font=heading,
                                           text="Current Balance:",
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_label = Label(self.details_frame, font=content,
                                           text="${}".format(game_stats[1]), anchor="e")
        self.current_balance_label.grid(row=1, column=1, padx=1)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost (row 2.3)
        self.wind_loss_label = Label(self.details_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame, font=content,
                                           text="${}".format(amount),
                                           fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=heading,
                                              text="Games Played:",
                                              anchor="e")
        self.games_played_value_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content,
                                              text=len(game_history),
                                              anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # Dismiss Button (Row 3)
        self.dismiss_export = Frame(self.stats_frame)
        self.dismiss_export.grid(row=3)

        self.dismiss_btn = Button(self.dismiss_export, text="Dismiss", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=7,
                                  command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=6, column=0, pady=10, padx=5)

        self.export_btn = Button(self.dismiss_export, text="Export", fg="white",
                                  bg="#003366", font="Arial 15 bold", width=7,
                                  command=lambda: self.to_export(game_history, game_stats))
        self.export_btn.grid(row=6, column=1, pady=10, padx=5)

    def close_stats(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def to_export(self, game_history, game_stats):
        Export(self, game_history, game_stats)


class Export:
    def __init__(self, partner, game_history, all_game_stats):

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300,)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / "
                                                         "Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the "
                                                         "box below and press the "
                                                         "Save button to save your "
                                                         "calculation history to a "
                                                         "text file. ",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning Text Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="If the filename you "
                                                         "enter below already "
                                                         "exists, its contents "
                                                         "will be replaced with "
                                                         "your calculation history ",
                                 justify=LEFT, bg='#ffafaf', fg='maroon',
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        self.save_error_label = Frame(self.export_frame)
        self.save_error_label.grid(row=5, pady=10)

        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4)

        # Save and Canel Buttons (row 0 of save_cancel_frame
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(lambda: self.close_export(partner)))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history, game_stats):

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"
        problem = ""

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            elif letter == ".":
                problem = "(no .'s allowed"

            else:
                problem = "(the filename you chose is not valid)"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.filename_entry.config(bg="#ffafaf")
            self.save_error_label.config(text=problem)

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt
            filename += ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # Heading for stats
            f.write("Game Statistics\n\n")

            # Game stats
            f.write("Starting Balance : ${:.2f}\n".format(game_stats[0]))
            f.write("Current Balance : ${:.2f}\n".format(game_stats[1]))
            f.write("Amount Won / Lost : ${:.2f}\n".format(game_stats[1] - game_stats[0]))

            # heading for rounds
            f.write("\n\nRound Details\n\n")

            for item in game_history:
                f.write(item + "\n")

            f.close()

    def close_export(self, partner):
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Game()
    root.mainloop()