Python War
===============
> Console simulation of the all-time favorite War card game!

## Notes
- Automatically plays through
- Prints out a summary of game stats(instances of War, rounds, etc)
- Graphically shows how each player is doing.
- Starts two players equal halves of a 54 card deck with 2 jokers.
- To avoid infinite loops I shuffle the decks between every round.

## Running the simulation
```
python war.py
```

## Potential updates
Things I might do when I get the time.

* Add support for different graphics(tkinter maybe) 
* Track time
* Take the simulation running to a higher level - be able to run thousands of games and
  track statistics.
* Add command line options for choosing 52/54 card card, and game delays.
* If I add an option to make shuffling between rounds optional, is there a way to detect an
  infinite setup loop?
