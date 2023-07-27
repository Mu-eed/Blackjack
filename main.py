import random

class Card:
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return self.rank["rank"] + " of " + self.suit

class Deck:
	def __init__(self):
		self.cards = []
		suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
		ranks = [
			{"rank": "A", "value": 11},
			{"rank": "2", "value": 2},
			{"rank": "3", "value": 3},
			{"rank": "4", "value": 4},
			{"rank": "5", "value": 5},
			{"rank": "6", "value": 6},
			{"rank": "7", "value": 7},
			{"rank": "8", "value": 8},
			{"rank": "9", "value": 9},
			{"rank": "10", "value": 10},
			{"rank": "J", "value": 10},
			{"rank": "Q", "value": 10},
			{"rank": "K", "value": 10},
			]

		for suit in suits:
			for rank in ranks:
				self.cards.append([suit, rank])

	def shuffle(self):
		if len(self.cards) > 1:
			random.shuffle(self.cards)

	def deal(self, number):
		cards_dealt = []
		for x in range(number):
			if len(self.cards) > 0:
				card = self.cards.pop()
				cards_dealt.append(card)
		return cards_dealt
	
card1 = Card("Hearts", {"rank": "Q", "value": 10})
print(card1)
# deck1 = Deck()
# deck2 = Deck()
# deck2.shuffle()
# print(deck1.cards)
# print(deck2.cards)


	# shuffle()
	# card = deal(1)[0]

	# print(card[1]["value"])
# cards_dealt = deal(2)
# card = cards_dealt[0]
# rank = card[1]

# if rank == "A":
#     value = 11
# elif rank == "J" or rank == "Q" or rank == "K":
#     value = 10
# else:
#     value = rank

# rank_dict = {"rank": rank, "value": value}

# print(rank_dict["rank"], rank_dict["value"])