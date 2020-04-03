import libtcodpy as libtcod

from core.game_messages import Message

from core.game_states import GameStates

from core.render_functions import RenderOrder
from components.custom_tiles import CustomTile


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = CustomTile.SKULL
    monster.color = libtcod.white
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message
