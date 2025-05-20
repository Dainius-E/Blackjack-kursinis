# 🃏 Blackjack

How to run the program?
1. Clone the repository  
2. type "cd Blackjack-kursinis" in console (command prompt)
3. Install Python 3.10+ (if not already available)  
4. "py -m unittest discover"  to run the unit tests  
5. "py Main.py"  to launch the game  

How to use the program?  
At startup you can change the default number of decks (1–8) or keep the previous value stored in config.json.  
Follow on‐screen prompts to Hit or Stand.  
After each round your hand, the dealer’s hand, totals, and outcome are printed and logged.

 OOP pillars  
1. Encapsulation: (from hand_class.py)
 `Hand` keeps `_cards` private.
`
class Hand:
    def __init__(self):
        self._cards = []
    def add_card(self, card):
        self._cards.append(card)
`
   
3. Abstraction: (from Shoe_class_with_Factory_method.py)
    The `Shoe_Factory_method` abstract base class defines `build_cards()`;
   
`  class Shoe_Factory_method(ABC):
    @abstractmethod
    def build_cards(self, num_decks: int) -> list:
        ...
class StandardShoe_Factory_Method(Shoe_Factory_method):
    def build_cards(self, num_decks: int) -> list:
        cards = []
        for _ in range(num_decks):
            for r in Deck.ranks:
                for s in Deck.suits:
                    cards.append(Card(r, s))
        return cards
     `
5. Inheritance: (from dealer_class.py and player_class.py) 
   - `Player` and `Dealer` both subclass `Hand`.

    ` class Dealer(Hand):
    def decide_hit_or_stand(self):
        return self.best_value() < 17

     class Player(Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name `
     `
 
6. Polymorphism: (from dealer_class.py and player_class.py)
   - Both `Player` and `Dealer` implement `decide_hit_or_stand()` differently.
`class Dealer(Hand):
    def decide_hit_or_stand(self):
        return self.best_value() < 17 (calls the decide_hit_or_stand method for the dealer)
     `
`class Player(Hand):
    def __init__(self, name):
        super().__init__()
        self.name = name
     `

   ` def decide_hit_or_stand(self):
        while True:
            choice = input(f"{self.name}, Hit or Stand? [h/s]: ").strip().lower()  (promtps the actual user to type in to hit or stand)
            if choice in ('h','s'):
                return choice == 'h'
`
### Design pattern  
Factory Method:  
  - `class Shoe_Factory_method(ABC)` declares `build_cards()`.  
  - `class StandardShoe_Factory_method(ShoeFactory)` provides the concrete N-deck implementation.  
  - `Shoe` takes any factory method and builds the needed shoe.

Composition / Aggregation  
- `BlackjackGame` uses aggregation for the Shoe_factory_method. when you remove the blackjack game, the factory still exists without it.

class StandardShoe_Factory_Method(Shoe_Factory_method):
  `  def build_cards(self, num_decks: int) -> list:
        cards = []
        for _ in range(num_decks):
            for r in Deck.ranks:
                for s in Deck.suits:
                    cards.append(Card(r, s))
        return cards
  `
- `hand_class.py` implements composition and if we take away a hand, the cards go with it.

class Hand:
    def __init__(self):
        self._cards = []

    def add_card(self, card):
        self._cards.append(card)

    def values(self):
        totals = [0]
        for card in self._cards:
            new_totals = []
            for v in card.value():
                for t in totals:
                    new_totals.append(t + v)
            totals = set(new_totals)
        return totals
  


File I/O  
- `config.json` is read/written to store and update default deck count. (from Main.py)
`
def load_config():
    defaults = {"num_decks": 1}
    if not os.path.exists(CONFIG_FILE):
        return defaults
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {k: data.get(k, defaults[k]) for k in defaults}
    except (json.JSONDecodeError, IOError):
        return defaults
`
- `blackjack_log.txt` is appended after each round with timestamp, hands, totals, and outcome. (from blackjack_game_controller.py)
`
def log_result(self, line, filename="blackjack_log.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)
`
Testing  
All core classes have `unittest` in `tests/`.


Conclusions:
1. The game works (on cmd and on visual studio code)
2. It was a challenge to learn how to use VScode and use it efficiently, how to create separate files and import them (they wouldnt work for me withhout src.). It also was a challenge to figure out how to start nad from where to start, but it got easier along the way as I was coding and getting the general idea off how to implement each thing.
3. The game could definitely be better, some visuals could be made for it, some gamemodes could exist with different decks ect. But it works as a solid way to play blackjack.
