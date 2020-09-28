import math
# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

# poutre carrée
a = 15  # en mm

# poutre ronde
d = 5  # en mm

# poutre creuse
D = 15  # en mm
d = 5  # en mm


# Calcul de la section optimale

Inerties = []
Delta = []
Sections = ["rectangulaire", "carrée", "ronde", "creuse"]

I_rec = b * (h ** 3) / 12
Inerties.append(I_rec)

I_car = (a ** 4) / 12
Inerties.append(I_car)

I_ron = math.pi * (d ** 4) / 64
Inerties.append(I_ron)

I_cre = math.pi * ((D ** 4) - (d ** 4)) / 64
Inerties.append(I_cre)

for i in Inerties:
    delta_max = F * (L ** 3) / (3 * E * (10 ** 3) * i)
    Delta.append(delta_max)

Index = Delta.index(min(Delta))
Section = Sections[Index]

print ("Le type de section minimisant la déformation maximale est", Section, "avec une déformation de", (round(min(Delta)*100))/100 , "mm")