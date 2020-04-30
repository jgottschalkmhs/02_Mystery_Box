import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    # prize = ""
    round_winnings = 0

    for thing in range(0,3):

        prize_num = random.randint(1,100)
        # prize += " "
        if prize_num == 10:
            # get gold if its 1 < one in ten chance>
            # prize += "gold"
            round_winnings += 5
        elif 1 < prize_num <= 25:
            # get silver if its 2,3
            # prize += "silver"
            round_winnings += 2
        elif 3 < prize_num <= 65:
            # copper if its 4,5,6,7, <40% chance of copper>
            # prize += "copper"
            round_winnings += 1
        '''else:
            prize += "lead"'''

    # print("You won {} which is worth {}".format(prize, round_winnings))
    winnings += round_winnings

print("Paid In: ${}".format(cost))
print("Pay Out: ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings - cost))
else:
    print("Sorry, you lost ${}".format(cost-winnings))