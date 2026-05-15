# Pokemon Blueish

## Description

A Fan made version of Pokemon Blue. I made this as a passion project in High School. This project took a year to make so I hope you like it. This is a complete remake of Pokemon Blue with a few additions.

## Table of Contents

- [Pokemon Blueish](#pokemon-blueish)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Additions](#additions)
  - [Automatic Install Instructions](#automatic-install-instructions)
    - [Install.sh](#installsh)
    - [Start.sh](#startsh)
  - [Manual Install Instructions](#manual-install-instructions)
    - [GH CLI](#gh-cli)
    - [Git Clone](#git-clone)
    - [Run Game](#run-game)
  
## Additions

- 2 new Bosses at end of Game
- Ability to gain all 151 Kanto Pokemon
- Fixed Previous Gen 1 errors(Ghost vs Psychic, 256 Glitch, Focus Energy,etc)
- Flashing lights with some Move Animations
- Patched the bad references to match the real filename casing for Lady3
- renamed Requirments.txt to Requirements.txt
- updated to use Player_Info.txt as save state
- fixed exit not working
- added Install.sh and Start.sh for automatic install and game running
- Updated README.md for clarity and operations

## Automatic Install Instructions

### Install.sh

  Ensure [Install.sh](/Install.sh) has executable permissions:

    chmod +x Install.sh

  Run [Install.sh](/Install.sh) to automatically create Python Virtual Environment and install [Requirements.txt](/Requirements.txt)

    ./Install.sh

### Start.sh

  Ensure [Start.sh](/Start.sh) has executable permissions:

    chmod +x Start.sh

  Run [Start.sh](/Start.sh) to start game.

    ./Start.sh

  *you can keep using Start.sh after virtual env has been created*

## Manual Install Instructions

### GH CLI

    gh repo clone Bunnzulu/Pokemon-Blueish

### Git Clone

    git clone https://github.com/Bunnzulu/Pokemon-Blueish.git

### Run Game

1. Change directory to cloned repo

    `cd <current-directory>/Pokemon-Blueish`
    *replace `current-directory>` with working directory repo was downloaded to*

2. (Optional) Create Python Virtual Environment

    `python3 -m venv <venv-name>`
    *replace `<venv-name>` with actual virtual environment name*
    *(e.g. `python3 -m venv .blue-venv` )*

    - Activate Virtual Environment

        `source .<venv-name>/bin/activate`
        *replace `<venv-name>` with actual virtual environment name*
        *(e.g. `source .blue-venv/bin/activate` )*

3. Install [Requirements.txt](/Requirements.txt) (renamed from Requirments.txt)

    `pip3 install -r Requirements.txt`

4. Run [Main.py](/Main.py) to enjoy game!!

    `python3 Main.py`
