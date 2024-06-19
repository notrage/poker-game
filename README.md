# Poker Game
## Description
> IMPORTANT : this is a work in progress and very not ready at all

Poker is a command-line application written in Python 3.10.6, designed to interact with a poker game. At the moment you can only generate a fully random application and see which generated hand is the best (only the best hand calculator is available)

This project aims to be a playable game, with the possibility to play versus AIs with a server side API.
## Installation
To run the Crop Farmer on your local machine, make sure you have Python 3.10.6 or later installed.
1. Clone this git repository :
```bash
git clone git@github.com:notrage/poker-game.git
```
2. Run the **Poker Game** :
```bash
python3 poker_game.py
```
or
```bash
python poker_game.py
```
If you only have one Python version on your machine.

## Usage
At the current stage, you need to put dirrectly the **game.py** functions in **poker_game.py** to make you own game, there is praticaly all the necessary functions to make a game, but you can add more if you want.
## Features
- Create a poker game
- Add players to the game
- Add atrributes to players (name, money, etc.)
- Make a player win or lose mone
- Update the community cards
- Know the best hand of a player
- Know the best hand of all players