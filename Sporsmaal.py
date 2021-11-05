class Sporsmaal:
    
    def __init__(self,line):
        self.spørsmål = line.split(':')[0]
        self.riktigSvar = line.split(':')[1]
        self.svarAlt = line.split(':')[2]

    def korrekt_svar_tekst(self):
        return str(self.riktigSvar.strip())

