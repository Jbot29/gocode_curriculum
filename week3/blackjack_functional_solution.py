import random

suits = ('c','s','h','d')
ranks = ('2','3','4','5','6','7','8','9','10','j','q','k','a')

def new_deck():
    return [(suit,rank) for suit in suits for rank in ranks]

def shuffle_deck(deck):
    sd = deck[:]
    random.shuffle(sd)
    return sd

def deal_one(deck):
    return deck.pop()

def deal_two(deck):
    return [deal_one(deck),deal_one(deck)]

def give_card(player,card):
    player["cards"].append(card)
    return player

def create_player(name):
    return {"name":name, "cards":[]}

def all_players(players):
    return filter(lambda name: name != "Dealer",players)

def card_value(card):
    value = card[1]
    if value in ['j','q','k']:
        return 10
    elif value == 'a':
        return 11
    return int(value)
    
def sum_cards(cards):
    return sum([card_value(c) for c in cards])

def bust(*arg):
    if sum(arg) > 21:
        return True
    return False

def calc_score(cards,cur_score=0):
    if not cards:
        return cur_score

    value = card_value(cards[0])

    remaining = sum_cards(cards[1:])
    
    if not bust(cur_score,value,remaining):
        return cur_score+value+remaining
    
    if value == 11: value = 1

    if not bust(cur_score,value,remaining):
        return cur_score+value+remaining

    return calc_score(cards[1:],cur_score+value)

def get_num_players():
    return int(raw_input("How many players? "))

def get_player_name():
    return raw_input("Player Name? ")

def user_hit():
    value = raw_input("(h)it, (s)tand:")
    if value == 'h':
        return True
    elif value == 's':
        return False
    return user_hit()

def hit_loop(deck,cards):
    print cards
    while user_hit():
        cards.append(deal_one(deck))
        print "Hand", cards
        score = calc_score(cards)
        print score
        if bust(score):
            print "Bust!"
            return

def dealer_play(deck,cards):
    cur_score = calc_score(cards)
    while cur_score < 17:
        cards.append(deal_one(deck))
        cur_score = calc_score(cards)

def game_loop():
    num_players = get_num_players()

    deck = shuffle_deck(new_deck())

    players = {"Dealer": deal_two(deck)}
    players.update({get_player_name() : deal_two(deck) for i in range(num_players)})

    for player_name in all_players(players):
        hit_loop(deck,players[player_name])

    dealer_play(deck,players['Dealer'])

    scores =[]
    for player_name in players:
        player_score = calc_score(players[player_name])
        if not bust(player_score):
            scores.append((player_name,player_score))

    scores = sorted(scores,key=lambda x:x[1])

    print scores


        


#tests
assert calc_score( [('c','a'),('c','10')]) == 21
assert calc_score( [('c','a'),('c','9'),('c','8')]) == 18 
assert calc_score( [('c','a'),('c','9'),('c','8'),('h','a')]) == 19
