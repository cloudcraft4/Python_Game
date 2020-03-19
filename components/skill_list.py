import libtcodpy as libtcod

from game_messages import Message

class SkillList:
    def __init__(self):
        self.skills = []

    def add_skill(self, skill):
        results = []

        results.append({
            'skill_added': skill,
            'message': Message('You learned the ability {0}!'.format(skill), libtcod.blue)
        })

        self.skills.append(skill)

        return results
