import libtcodpy as libtcod

from game_messages import Message

class skill_list:
    def __init__(self):
        self.skill_list = []

    def add_skill(self, skill):
        results = []

        results.append({
            'skill_added': skill,
            'message': Message('You learned the ability {0}!'.format(skill.name), libtcod.blue)
        })

           self.skill.append(skill)

        return results

