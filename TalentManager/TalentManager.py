import xml.etree.ElementTree as ET

from TalentManager.Character import Character


class TalentManager:
    def __init__(self, root):
        self.root = root
        if 'Barotrauma' not in self.root:
            return
        self.root += f'\\Content\\Talents'

        self.talents = 'TalentTrees.xml'
        self.talentsTree = None
        self.characters = {}
        self.loadAll()

    def loadAll(self):
        self.talentsTree = ET.parse(f'{self.root}\\{self.talents}')
        root = self.talentsTree.getroot()
        for talentTree in root:
            character = talentTree.attrib['jobidentifier']
            if character not in self.characters.keys():
                char = Character(character, root=self.root)
                char.parse(talentTree)
                self.characters[character] = char
        for character in self.characters.values():
            character.loadTalentDetails()
            character.verifyTalents()

    def getCount(self):
        count = 0
        for character in self.characters.values():
            count += character.getCount()
        return count

    def getTalentByName(self, name):
        talent = None
        for character in self.characters.values():
            talent = character.getTalentByName(name)
            if talent is not None:
                break
        return talent

    def move(self, input):
        sourceCharacter, sourceTree, sourceLevel, sourceTalentName, destinationCharacter, destinationTree, destinationLevel = self.parseInput(input)
        print(f"Moving {sourceTalentName} from {sourceCharacter}'s {sourceTree} tree to {destinationCharacter}'s {destinationTree} tree")

        _, _, sourceRow, sourceTalent = self.find(f'{sourceCharacter}_{sourceTree}_{sourceLevel}_{sourceTalentName}')
        _, _, destinationRow, _ = self.find(f'{destinationCharacter}_{destinationTree}_{destinationLevel}_*')

        destinationRow.append(sourceTalent)
        sourceRow.remove(sourceTalent)

        longFileTalent = self.characters[sourceCharacter].getTalentByName(sourceTalentName)
        self.characters[sourceCharacter].removeTalent(longFileTalent)
        self.characters[destinationCharacter].addTalent(longFileTalent)

        # TODO make all this saving a transaction?
        self.characters[sourceCharacter].save()
        self.characters[destinationCharacter].save()
        self.save()


    def parseInput(self, input):
        # talentManager.move('engineer:weaponsengineer:1:militaryapplications->engineer:electrician:1')
        source, destination = input.split('->')
        sourceCharacter, sourceTree, sourceLevel, sourceTalent = source.split('_')
        destinationCharacter, destinationTree, destinationLevel = destination.split('_')
        return sourceCharacter, sourceTree, sourceLevel, sourceTalent, destinationCharacter, destinationTree, destinationLevel

    def find(self, input):
        lfCharacter, lfTree, lfRow, lfTalent = input.split('_')
        try: lfRow = int(lfRow)
        except ValueError: lfRow = 0

        character, tree, row, talent = None, None, None, None
        for characterTree in self.talentsTree.getroot():
            if characterTree.attrib['jobidentifier'] == lfCharacter:
                character = characterTree
            for talentTree in characterTree:
                if talentTree.attrib['identifier'] == lfTree:
                    tree = talentTree
                rowNo = 1
                for talentRow in talentTree:
                    if rowNo == lfRow and talentTree.attrib['identifier'] == lfTree:
                        row = talentRow
                    for talentIt in talentRow:
                        if talentIt.attrib['identifier'] == lfTalent:
                            talent = talentIt
                    rowNo += 1
        return character, tree, row, talent

    def save(self):
        with open(f'{self.root}\\{self.talents}', 'wb') as f:
            self.talentsTree.write(f)

    def serialize(self):
        dict = {}
        for character in self.characters.values():
            dict[character.name] = character.serialize()
        return dict

    def __str__(self):
        output = f"TalentManager ({self.getCount()}):\n"
        for character in self.characters.values():
            output += f"\t{str(character)}\n"
        return output
