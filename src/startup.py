from metier import (ClassManager, Classe,
                    Eleve, CarnetDeNote,
                    Matiere)


cm = ClassManager()
c1 = cm.createClasse("cp1")
cm.listClass.append(c1)

e1 = Eleve('rouse','ju')
e1.printEleve()
e2 = Eleve('toto','ti')
e2.printEleve()

cm.listClass[0].addEleve(e1)
cm.listClass[0].addEleve(e2)
cm.listClass[0].printClasse()

cdn = CarnetDeNote()
cdn.printMatiereName()
