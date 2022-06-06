from localization import locale

class Talent:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.element = None

    def parseDetails(self, tree):
        self.element = tree.find(f'Talent[@identifier="{self.name}"]')

    def serialize(self):
        return {
            'name': self.name,
            'localizedName': locale[self.name]['localeName'],
            'description': locale[self.name]['description'],
            'level': self.level,
        }

    def __str__(self):
        return f'\t{self.name} {self.level}'
