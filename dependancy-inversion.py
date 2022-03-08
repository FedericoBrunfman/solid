from abc import ABC, abstractmethod


class Wizard:

    def __init__(self):
        self.name = ''
        self.life = 100
        self.attack = 0
        self.defense = 0
        self.spells = []
        self.extra_attack = 0
        self.extra_defense = 0

    def add_wizard(self, name, life, attack, defense, spells):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.spells = spells


class SpellHandler(ABC):

    @abstractmethod
    def damage(self, w, name, damage):
        pass

class SpellHandler_Message(SpellHandler):

    @abstractmethod
    def damage(self, w, name, damage):
        pass

    @abstractmethod
    def message(self, message):
        pass


class Increase(SpellHandler_Message):
    def damage(self, w, name, damage):
        spell = next((spell for spell in w.spells if spell['name'] == name), None)
        spell['damage'] = int(spell['damage']) + damage

    def message(self, message):
        print(message)

class Decrease(SpellHandler):
    def damage(self, w, name, damage):
        spell = next((spell for spell in w.spells if spell['name'] == name), None)
        spell['damage'] = int(spell['damage']) - damage


spell_list = [
    {
        "name": "earthquake",
        "damage": "20"
    },
    {
        "name": "blast",
        "damage": "50"
    }
]

wizard = Wizard()

wizard.add_wizard("Merlin", 80, 15, 11, spell_list)

increase = Increase()
increase.message('You are going to increase your damage')
increase.damage(wizard, 'blast', 20)

print(wizard.spells)


