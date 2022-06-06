from localization import locale

class Talent:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.element = None
        self.afflictionName = None
        self.afflictionElement = None

    def parseDetails(self, tree):
        self.element = tree.find(f'Talent[@identifier="{self.name}"]')
        try: self.afflictionName = self.element.find("AbilityGroupInterval").find("Abilities").find("CharacterAbilityApplyStatusEffects").find("StatusEffects").find("StatusEffect").find("Affliction").attrib['identifier']
        except AttributeError: pass

    def serialize(self):
        return {
            'name': self.name,
            'localizedName': locale[self.name]['localeName'],
            'description': locale[self.name]['description'],
            'level': self.level,
        }

    def parseAfflictionDetails(self, tree):
        self.afflictionElement = tree.find(f'Affliction[@identifier="{self.afflictionName}"]')

    def __str__(self):
        return f'\t{self.name} {self.level}'
