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


class Increase(SpellHandler):
    def __init__(self, extra_attack):
        self.extra_attack = extra_attack
    def damage(self, w, name, damage):
        spell = next((spell for spell in w.spells if spell['name'] == name), None)
        spell['damage'] = int(spell['damage']) + damage
        print(f"This wizard has {self.extra_attack} extra attack")


class Decrease(SpellHandler):
    def __init__(self, extra_defense):
        self.extra_defense = extra_defense
    def damage(self, w, name, damage):
        spell = next((spell for spell in w.spells if spell['name'] == name), None)
        spell['damage'] = int(spell['damage']) - damage
        print(f"This wizard has {self.extra_defense} extra defense")


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

decrease = Decrease(5)
decrease.damage(wizard, 'blast', 50)

print(wizard.spells)


