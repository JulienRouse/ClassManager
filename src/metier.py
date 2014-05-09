"""
Metier: Module qui gere la partie calcul de ClassManager

"""
class Eleve(object):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.eleveId = -1
        self.classeId = -1
    
    def setId(self,eleveId,classeId):
        self.eleveId = eleveId
        self.classeId = classeId
    
    def printEleve(self):
        print "name:", self.name
        print "surname:", self.surname
        print "id:", self.eleveId
        print "class:", self.classeId

class Classe(object):
    def __init__(self,name):
        self.name = name
        self.listEleves = []
        self.classeId = -1
    
    def setId(self, classeId):
        self.classeId = classeId

    def addEleve(self,eleve):
        eleveId = len(self.listEleves)
        eleve.setId(eleveId,self.classeId)
        self.listEleves.append(eleve)
        
    def removeEleve(self,eleve):
        pass

    def printClasse(self):
        for elt in self.listEleves:
            elt.printEleve()

class ClassManager(object):

    def __init__(self):
        self.listClass = []
        
    def createClasse(self, name='ClassDefault'):
        new_Classe = Classe(name)
        classeId = len(self.listClass)
        new_Classe.setId(classeId)
        return new_Classe

    def deleteClasse(self,classeToRemove):
        pass
    
