# bot code goes here
from os import walk
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import (
    defense_actions,
    attack_actions,
    jump_boost,
    projectile_actions,
    super_saiyan,
)
from Game.gameSettings import (
    HP,
    LEFTBORDER,
    RIGHTBORDER,
    LEFTSTART,
    RIGHTSTART,
    PARRYSTUN,
)
from ScriptingHelp.usefulFunctions import *


# PRIMARY CAN BE: Teleport, Super Saiyan, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = TeleportSkill
SECONDARY_SKILL = Hadoken

# constants, for easier move return
# movements
JUMP = ("move", (0, 1))
FORWARD = ("move", (1, 0))
BACK = ("move", (-1, 0))
JUMP_FORWARD = ("move", (1, 1))
JUMP_BACKWARD = ("move", (-1, 1))
MOVEMENTS = [JUMP, FORWARD, BACK, JUMP_FORWARD, JUMP_BACKWARD]

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)
B_ATTACK = [LIGHT, HEAVY]

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)

CANCEL = ("skill_cancel",)

# no move, aka no input
NOMOVE = "NoMove"
# for testing
moves = (SECONDARY,)
moves_iter = iter(moves)


# TODO FOR PARTICIPANT: WRITE YOUR WINNING BOT
class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL

    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary

    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])

        if distance < 3:
            return LIGHT

        return FORWARD


# ---------------------------------------------------
# Use MCTS markov chain to solve this problem.
# ---------------------------------------------------
import sys
from pathlib import Path
import random
import importlib
import json
from Game.GameManager import startGame

# Manually choose bot files to test
SUBMISSIONPATH = "Submissions"
PATH1 = "Bot1"
PATH2 = "Bot2"


def GameEnd(player1, player2, tick):  # Return Bool,
    if get_hp(player1) <= 0 or get_hp(player2) <= 0 or tick == 120:
        return True


def win_game(
    player1, player2, tick
):  # 1 for win, -1 for lose, 0 for tie, None for not ended
    # First, check if the game has ended
    if not GameEnd(
        player1, player2, tick
    ):  # Assuming game_end() is a function that checks if the game has ended
        return 0  # Game has not ended, no result yet

    # Retrieve players' HP once to avoid multiple function calls
    hp1 = get_hp(player1)
    hp2 = get_hp(player2)

    # Determine the game outcome
    if hp1 <= 0 and hp2 <= 0:
        print("Tie - Both players have been defeated.")
        return None  # Tie due to both players losing
    elif hp1 <= 0:
        print("Player 2 wins")
        return -1
    elif hp2 <= 0:
        print("Player 1 wins")
        return 1
    elif tick == 120:  # Assuming 'tick' is a global variable tracking time or turns
        if hp1 > hp2:
            print("Player 1 wins by HP advantage at final tick")
            return 1
        elif hp1 < hp2:
            print("Player 2 wins by HP advantage at final tick")
            return -1
        else:
            print("Tie - Equal HP at final tick")
            return 0  # Tie due to equal HP at the final tick

    # If none of the above conditions are met, return None (indeterminate)
    return None


def full_assault(player, enemy, primary, secondary):
    # Player and Enemy Positions
    player_x, player_y = get_pos(player)
    enemy_x, enemy_y = get_pos(enemy)

    # Check for secondary skills if not on cooldown
    if not secondary_on_cooldown(player):
        if (
            secondary == "Hadoken"
            and player_y == enemy_y
            and abs(player_x - enemy_x) <= 7
        ):
            return secondary
        elif secondary == "Grenade":
            return secondary
        elif secondary == "BearTrap" and abs(player_x - enemy_x) < 2:
            return secondary
        elif secondary in ["super_saiyan", "jump_boost"]:
            return secondary
    else:
        pass

    # Check for primary skills if not on cooldown
    if not primary_on_cooldown(player):
        if primary == "teleport" or primary == "meditate":
            return primary
        elif primary == "dash_attack" and abs(player_x - enemy_x) <= 5:
            return primary
        elif (
            primary == "uppercut"
            and abs(player_x - enemy_x) <= 1
            and player_y == enemy_y
        ):
            return primary
    else:
        pass

    # TODO: Implement Movement and Block logic

    # Check for basic attack condition
    if player_y == enemy_y and abs(player_x - enemy_x) == 1:
        return "HEAVY"  # Assuming HEAVY is a constant defined somewhere

    # Default action if no abilities are available
    return "LIGHT"  # Assuming LIGHT is a constant defined somewhere
