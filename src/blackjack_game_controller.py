from src.Shoe_class_with_Factory_method import Shoe
from src.player_class import Player
from src.dealer_class import Dealer
from src.Shoe_class_with_Factory_method import Shoe_Factory_method
from src.Shoe_class_with_Factory_method import StandardShoe_Factory_Method
from datetime import datetime
import time

class BlackjackGame:
    def __init__(self, num_decks: int = 1, shoe_factory: Shoe_Factory_method = StandardShoe_Factory_Method()):
        self.num_decks = num_decks
        self.shoe_factory = shoe_factory
        self.player = Player("You")
        self.dealer = Dealer()
        self._reset_shoe()

    def _reset_shoe(self):
        self.shoe = Shoe(self.num_decks)
        time.sleep(1)
        print(f"\n Reshuffled {self.num_decks} deck(s). Cards in shoe: {self.shoe.cards_left()}")

    def deal_card(self, hand):
        card = self.shoe.deal_one()
        if card is None:
            time.sleep(1)
            input("Shoe empty and the game must restart — press Enter to reshuffle ")
            self._reset_shoe()
            card = self.shoe.deal_one()
        hand.add_card(card)
        return card

    def initial_deal(self):
        # Deal in the order: dealer, player, dealer, player 
        # 1) Dealer up‐card
        up = self.deal_card(self.dealer)
        print("Dealer receives: ", up)
        time.sleep(1)

        # 2) Player first card
        c = self.deal_card(self.player)
        print("You receive:", c)
        time.sleep(1)

        # 3) Dealer hole‐card (face‐down)
        hole = self.deal_card(self.dealer)
        print("Dealer receives:  ?")
        time.sleep(1)

        # 4) Player second card
        c = self.deal_card(self.player)
        print("You receive:", c)
        time.sleep(1)


    def play_round(self):
        print(f"\nCards left in shoe: {self.shoe.cards_left()}")
        print("Dealing cards…")
        self.initial_deal()
        time.sleep(1)
        print()
        # Now show only the dealer’s up‐card
        up = self.dealer._cards[0]
        print(f"Dealer shows: ?   {up}")
        print(f"Your hand: {self.player._cards}   Total: {self.player.best_value()}")

        # Player turn
        while not self.player.is_bust() and self.player.decide_hit_or_stand():
            card = self.deal_card(self.player)
            time.sleep(1)
            print("You drew:", card,
                  "| Your hand:", self.player._cards,
                  "| Total:", self.player.best_value())

        # Dealer turn
        while not self.player.is_bust() and self.dealer.decide_hit_or_stand():
            card = self.deal_card(self.dealer)
            time.sleep(1)
            print("Dealer drew:", card,
                  "| Dealer total:", self.dealer.best_value(),
                  "| Left in shoe:", self.shoe.cards_left())

        self.show_result()

    def show_result(self):
        p_cards = self.player._cards
        d_cards = self.dealer._cards
        p_val = self.player.best_value()
        d_val = self.dealer.best_value()

    # 1) Check for blackjack 
        if len(p_cards) == 2 and p_val == 21:
            time.sleep(1)
            print(f"\nYour hand: {p_cards} ({p_val})  Dealer reveals: {d_cards} ({d_val})")
            print("Blackjack! Congratulations, you hit 21!")
            line = (f"{datetime.now():%Y-%m-%d %H:%M:%S} | BLACKJACK | You: {p_cards} ({p_val})  | "
                    f"Dealer: {d_cards} ({d_val}) | Player wins with Blackjack!\n")
            self.log_result(line)
            return

    # 2) dealer Blackjack: house wins or pushes
        if len(d_cards) == 2 and d_val == 21:
            time.sleep(1)
            print(f"\nDealer reveals: {d_cards} ({d_val})")
            print("Dealer has Blackjack! Dealer wins.")
            line = (f"{datetime.now():%Y-%m-%d %H:%M:%S} | BLACKJACK | "
                    f"You: {p_cards} ({p_val}) | Dealer: {d_cards} ({d_val}) | Dealer wins with Blackjack!\n")
            self.log_result(line)
            return

        print(f"\nFinal Hands -> You: {p_cards} ({p_val}), Dealer: {d_cards} ({d_val})")
        if self.player.is_bust():
            time.sleep(1)
            outcome = "Dealer won (player busted)"
        elif self.dealer.is_bust():
            time.sleep(1)
            outcome = "Player won (dealer busted)"
        elif p_val > d_val:
            time.sleep(1)
            outcome = "Player won"
        elif p_val < d_val:
            time.sleep(1)
            outcome = "Dealer won"
        else:
            time.sleep(1)
            outcome = "Push (tie)"

        print(outcome)


        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = (f"{timestamp} | You: {self.player._cards} ({p_val}) | "
                f"Dealer: {self.dealer._cards} ({d_val}) | {outcome}\n")

        self.log_result(line)

    def log_result(self, line, filename="blackjack_log.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)