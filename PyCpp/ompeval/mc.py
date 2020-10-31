import build.ompeval

def equity(my_cards, cards_on_table, player_numbers):
    my_cards = "".join(my_cards[0])
    cards_on_table = "".join(cards_on_table)
    random_player = ['44+,A2s+,K2s+,Q4s+,J7s+,T7s+,97s+,87s,A3o+,K7o+,Q8o+,J8o+,T8o+']*(player_numbers-1)
    eval_equity = build.ompeval.equity([my_cards]+random_player, cards_on_table,1000)
    return eval_equity

def main():
    my_cards = [['AD', '2S']]
    cards_on_table = ['5S', '3S', '4S', 'KS', 'AS']
    print(equity(my_cards, cards_on_table, 2))

    my_cards = [['QC', 'QD']]
    cards_on_table = ['TS', '3C', '8C', '9H', 'JC']
    print(equity(my_cards, cards_on_table, 4))

if __name__ == "__main__":
    main()