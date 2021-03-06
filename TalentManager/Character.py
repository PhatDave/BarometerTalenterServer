import xml.etree.ElementTree as ET

from TalentManager.TalentTree import TalentTree


class Character:
    def __init__(self, name, root):
        self.characterSubstitutionTable = {
            'securityofficer': "Security",
            'captain': "Captain",
            'assistant': "Assistant",
            'engineer': "Engineer",
            'mechanic': "Mechanic",
            'medicaldoctor': "Doctor",
        }

        self.name = name

        alternateName = self.characterSubstitutionTable[self.name]
        self.root = root
        self.fileName = f'{self.root}\\{alternateName}\\Talents{alternateName}.xml'
        self.afflictionsFile = f'{self.root}\\{alternateName}\\Afflictions{alternateName}.xml'

        self.fileTree = None
        self.afflictionFileTree = None

        self.talentTrees = []

    def parse(self, tree):
        for talentTree in tree:
            treeName = talentTree.attrib['identifier']
            ttree = TalentTree(treeName)
            ttree.parse(talentTree)
            self.talentTrees.append(ttree)

    def loadTalentDetails(self):
        self.fileTree = ET.parse(self.fileName)
        root = self.fileTree.getroot()
        self.afflictionFileTree = ET.parse(self.afflictionsFile)
        rootAffli = self.afflictionFileTree.getroot()

        for talentTree in self.talentTrees:
            talentTree.parseTalentDetails(root)
            talentTree.parseAfflictionDetails(rootAffli)

    def verifyTalents(self):
        for tree in self.talentTrees:
            tree.verifyTalents()

    def getCount(self):
        count = 0
        for tree in self.talentTrees:
            count += tree.getCount()
        return count

    def getTalentByName(self, name):
        talent = None
        for tree in self.talentTrees:
            talent = tree.getTalentByName(name)
            if talent is not None:
                break
        return talent

    def removeTalent(self, talent):
        root = self.fileTree.getroot()
        element = root.find(f'Talent[@identifier="{talent.element.attrib["identifier"]}"]')
        root.remove(element)
        if talent.afflictionElement is not None:
            rootAffli = self.afflictionFileTree.getroot()
            elementAffli = rootAffli.find(f'Affliction[@identifier="{talent.afflictionElement.attrib["identifier"]}"]')
            rootAffli.remove(elementAffli)

    def addTalent(self, talent):
        self.fileTree.getroot().append(talent.element)
        if talent.afflictionElement is not None:
            self.afflictionFileTree.getroot().append(talent.afflictionElement)

    def save(self):
        with open(self.fileName, 'wb') as f:
            self.fileTree.write(f)
        with open(self.afflictionsFile, 'wb') as f:
            self.afflictionFileTree.write(f)

    def serialize(self):
        return {
            'name': self.name,
            'count': self.getCount(),
            'trees': [tree.serialize() for tree in self.talentTrees]
        }

    def __str__(self):
        output = f'{self.characterSubstitutionTable[self.name]} ({self.getCount()}):\n'
        for tree in self.talentTrees:
            output += f'\t{str(tree)}\n'
        return output
