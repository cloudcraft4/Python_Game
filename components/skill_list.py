import libtcodpy as libtcod
from game_messages import Message
from entity import Entity

from skill_functions import cast_throw_rock, cast_shoulder_charge, cast_quills
from components.skills import Skills



class SkillList:
    def __init__(self):
        self.skills = []
        self.owner = self

    def add_skill(self, results, skill):


        results.append({
            'skill_added': skill,
            'message': Message('You learned the ability {0}!'.format(skill), libtcod.blue)
        })

        self.skills.append(skill)

        return results

    def use(self, skill_entity, **kwargs):
        results = []

        skill_component = skill_entity.skill

        if skill_component.use_function is None:
            results.append({'message': Message(' {0} cannot be activated'.format(skill_entity.name), libtcod.yellow)})
        else:
            if skill_component.targeting and not (kwargs.get('target_x') or kwargs.get('target_y')):
                results.append({'targeting_s': skill_entity})
            else:
                kwargs = {**skill_component.function_kwargs, **kwargs}
                skill_use_results = skill_component.use_function(self.owner, **kwargs)

                results.extend(skill_use_results)

                # TODO fix this.  Why is it 'player_turn_results' in engine but just results here?)
                #results.append({'skill_used'})

        return results

    def create_skill(self, character, skill_name, **kwargs):
        results = []

        if skill_name == 'Cloak of Quills':
            skill_component = Skills(use_function=cast_quills, damage=40, maximum_range=5)
            Quills = Entity(0, 0, '*', libtcod.sky, 'Cloak of Quills', skill=skill_component)
            character.skill_list.add_skill(results, Quills)

            character.learnable_skills.remove('Cloak of Quills')
            character.learnable_skills.append('Cloak of Quills 2')

        elif skill_name == 'Shoulder Charge':
            skill_component = Skills(use_function=cast_shoulder_charge, damage=40, maximum_range=5)
            Shoulder_Charge = Entity(0, 0, '*', libtcod.sky, 'Shoulder Charge', skill=skill_component)
            character.skill_list.add_skill(results, Shoulder_Charge)

            character.learnable_skills.remove('Shoulder Charge')
            character.learnable_skills.append('Shoulder Charge 2')

        elif skill_name == 'Throw Rock':
            skill_component = Skills(use_function=cast_throw_rock, damage=40, maximum_range=3, targeting=True,
                                     targeting_message=Message('Left-click on a enemy to throw rock, or right-click to cancel.'))
            Throw_Rock = Entity(0, 0, '*', libtcod.sky, 'Throw Rock', skill=skill_component)
            character.skill_list.add_skill(results, Throw_Rock)

            character.learnable_skills.remove('Throw Rock')
            character.learnable_skills.append('Throw Rock 2')

        return results