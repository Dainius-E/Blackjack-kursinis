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

### Functional requirements  
File I/O: `config.json` for persisting default decks; `blackjack_log.txt` for logging round results.

 OOP pillars  
1. Encapsulation:  
 `Hand` keeps `_cards` private and only exposes `add_card()`, `best_value()`, `is_bust()`.    
2. Abstraction:  
   - The `Shoe_Factory_method` abstract base class defines `build_cards()`;
3. Inheritance:  
   - `Player` and `Dealer` both subclass `Hand`.  
4. Polymorphism:  
   - Both `Player` and `Dealer` implement `decide_hit_or_stand()` differently.

### Design pattern  
Factory Method:  
  - `class Shoe_Factory_method(ABC)` declares `build_cards()`.  
  - `class StandardShoe_Factory_method(ShoeFactory)` provides the concrete N-deck implementation.  
  - `Shoe` takes any factory, decoupling shoe‐construction from shoe‐behavior.

Composition / Aggregation  
- `BlackjackGame` aggregates a `Shoe`, a `Player`, and a `Dealer`.

File I/O  
- `config.json` is read/written to store and update default deck count.  
- `blackjack_log.txt` is appended after each round with timestamp, hands, totals, and outcome.

Testing  
All core classes have `unittest` coverage in `tests/`.
