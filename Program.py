from Sporsmaal import Sporsmaal


def spmObjList():

    file1 = open(r'C:\Users\Ny Bruker\Documents\GitHub\Oving_10\sporsmaalsfil.txt', 'r', encoding="utf-8")
    lines = file1.readlines()
 
    sporsmalObjList = []
    for line in lines:
        sporsmalObjList.append(Sporsmaal(line))
    
    return sporsmalObjList



spmList = spmObjList()

teller1 = 0
teller2 = 0
for spm in spmList:
    print("\n\n")
    print(spm.spørsmål)
    
    t = 0
    for alt in spm.svarAlt.split(','):
        print(str(t) + ". " + alt.replace('[', '').replace(']', '').strip())
        t += 1
        
    svar1 = input("Velg et svaralternativ for spiller 1: ")
    svar2 = input("Velg et svaralternativ for spiller 2: ")
    print("\nKorrekt svar: " + spm.riktigSvar + "\n")
    
    if(svar1 == spm.korrekt_svar_tekst()):
        print("Spiller 1: Korrekt")
        teller1 += 1
    else:
        print("Spiller 1: Feil")
        
    if(svar2 == spm.korrekt_svar_tekst()):
        print("Spiller 2: Korrekt")
        teller2 += 1
    else:
        print("Spiller 2: Feil")

print("\n\n----------------------------")
print("Spiller 1 fikk " + str(teller1) + " rette.")
print("Spiller 2 fikk " + str(teller2) + " rette.")
print("----------------------------" )