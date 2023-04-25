WIDTH = 1440
HEIGHT = 720
starting_index_counter = 4
starting_player_placement_counter = 33
starting_dealer_placement_counter = 31


def height_percent(percentage):
    return (HEIGHT / 100) * percentage


def width_percent(percentage):
    return (WIDTH / 100) * percentage


def create_card_values():
    values = []
    for i in range(0, 4):
        values.append("A")
        for j in range(2, 11):
            values.append(j)
        values.append("J")
        values.append("Q")
        values.append("K")

    return values


# --------------------------------------------------Calculate value of hand---------------------------------------------
def determine_total(hand):
    total = 0
    ace_11s = 0
    for card in hand:
        if card in range(11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total



