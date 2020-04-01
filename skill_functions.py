import libtcodpy as libtcod

from game_messages import Message
from game_states import GameStates


def cast_throw_rock(*args, **kwargs):
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    damage = kwargs.get('damage')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')
    maximum_range = kwargs.get('maximum_range')

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'message': Message('You cannot target a tile outside your field of view.', libtcod.yellow)})
        return results

    for entity in entities:
        if entity.x == target_x and entity.y == target_y and entity.fighter:
            if entity.distance(target_x, target_y) <= maximum_range:
                results.append({'skill_used': True, 'message': Message('The rock hits the {0} and damages it for {1} hit points.'.format(entity.name, damage), libtcod.orange)})
                results.extend(entity.fighter.take_damage(damage))
                break
                #TODO test the skill_used part

            else:
                results.append({'message': Message('You cannot hit anything that far away!', libtcod.orange)})
                break

        elif entity.x == target_x and entity.y == target_y:
            results.append({'message': Message('Invalid target.', libtcod.orange)})
            break

    return results

def cast_quills(*args, **kwargs):
    # TODO this skill has been coded (not tested at all).  It is never being called at moment.  Delete old way if this works.
    results = []

    if kwargs.get('attacker') is not None and kwargs.get('damage') is not None:
        attacker = kwargs.get('attacker')
        damage = kwargs.get('damage')

        quill_damage = damage//10
        results.extend(attacker.fighter.take_damage(quill_damage))

    else:
        results.append({'message': Message('This ability is used automatically when you are hit')})

    ''' OLD WAY-->
    if GameStates = SHOW_SKILL:
        results.append({'message': Message('This abitilty is used automatically when you are hit')})

    else:
        #caster = args[0]
        attacker = kwargs.get('attacker')
        damage = kwargs.get('damage')

        quill_damage = damage//10
        results.extend(attacker.fighter.take_damage(quill_damage))'''

    return results

def cast_shoulder_charge(*args, **kwargs):
    # TODO Need to impiment shoulder charge.  Not totally sure even on design
    '''Design idea- Cardinal Directions.  Move 3(?) spaces in that direction.  Bonus attack if you hit someone.  Use case: Rapidly approach dangerous enemies.
    Also run away from other enemies.  Is this WAAAAY too powerful with running away from enemies?  Maybe disable stair dancing entirely.

    Step 1:  Choose direction.  This involvs direction.  Do I need a diff targeting function?
    Step 2:  Move one position.  Check to see if anything is there.  Just use code from movement.  Repeat 3x
    Step 3:  If combat need special code for damage (extra).  OR IS ABILITY POWERFUL ENOUGH WITHOUT BONUS?'''
    caster = args[0]
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    damage = kwargs.get('damage')
    maximum_range = kwargs.get('maximum_range')

    results = []

    target = None
    closest_distance = maximum_range + 1

    for entity in entities:
        if entity.fighter and entity != caster and libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
            distance = caster.distance_to(entity)

            if distance < closest_distance:
                target = entity
                closest_distance = distance

    if target:
        results.append({'consumed': True, 'target': target, 'message': Message('A bolt of fire strikes the {0} with a boom! The damage is {1}'.format(target.name, damage))})
        results.extend(target.fighter.take_damage(damage))
    else:
        results.append({'consumed': False, 'target': None, 'message': Message('No enemy is close enough to strike.', libtcod.red)})

    return results


