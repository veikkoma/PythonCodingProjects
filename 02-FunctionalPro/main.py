class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"

# Tee ratkaisusi tähän:
def suorittajien_nimet(suoritukset: list):

    return map(lambda s: s.opiskelijan_nimi ,suoritukset)

def kurssien_nimet(suoritukset: list):

    return set(sorted(map(lambda s: s.kurssi, suoritukset)))

if __name__=="__main__":

    s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
    s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
    s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)

    for nimi in kurssien_nimet([s1, s2, s3]):
        print(nimi)
