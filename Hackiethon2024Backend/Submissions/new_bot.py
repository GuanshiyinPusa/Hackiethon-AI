# TODO是我们要关注的。
# 第一个TODO选择主要和次要技能。
# 第二个TODO是写你的bot。get_move()
# 输赢判断规则：
# 1. 击败对手
# 2. 时间到，剩余血量多的玩家获胜
# 3. 时间到，剩余血量相同，硬币翻转决定胜负
# -----------------------------------------------------------
# - There are three ways to win a match:
# - Knockout: Defeat the opponent by reducing their character's health to zero.
# - Time Limit: If the match reaches the time limit, the player with more
# - remaining health wins.
# - Coin Flip: If both players have the same amount of health when the time runs
# - out, the winner will be determined by a coin flip.
# -----------------------------------------------------------
# 运行Backend
# python3 Game/GameManager.py
# 会生成一个新的文件夹，jsonfiles/Round_1,把里面的p1,p2,round
# json文件贴到FrontEnd/StreamingAssests/Round_1文件夹里面
# -----------------------------------------------------------

# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN


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

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)

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

    # TODO MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        distance = abs(get_pos(player)[0] - get_pos(enemy)[0])

        if distance == 1:
            return LIGHT

        return FORWARD