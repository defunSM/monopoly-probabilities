from random import randint
from collections import Counter
import operator

def board(number_of_properties, jail_position, go_to_jail_position):

    # This will set the board up.

    n = number_of_properties
    jail = jail_position
    go_jail = go_to_jail_position

    properties = []
    for i in range(1, n+1):
        properties.append(i)

    return [properties, jail, go_jail]

def roll():

    return randint(1, 6) + randint(1, 6)

def determine_property_density(board, iterations):

    # This is the probability that a given player will land on a property.

    # Assumption is made that for sack of simplicity after in jail you do not need to roll a double to get out however this may effect probabilities we are considering it will be insignificant. However this assumption may be wrong. However for the time being this assumption will be made for the sack of time consumption of writing the code.

    player_pos = 1

    n = board[0]
    jail = board[1]
    go_jail = board[2]
    maximum = max(n)


    distribution = []
    for i in range(0, iterations):


        dice_roll = roll()
        player_pos = player_pos + dice_roll


        if player_pos == go_jail:

            distribution.append(go_jail)
            player_pos = jail
            distribution.append(jail)

        elif player_pos > max(n):
            player_pos = player_pos - maximum
            distribution.append(player_pos)

        else:
            distribution.append(player_pos)

    return distribution

def main():

    mboard = board(40, 11, 31)
    probability = determine_property_density(mboard, 100000)

    total = 0
    for value in Counter(probability).values():
        total += value

    print(total)

    for v, k in sorted(dict(Counter(probability)).items(), key=operator.itemgetter(1)):
        print(v, "-->", round((k/total)*100, 4), "%")



if __name__ == "__main__":
    main()
