def my_print_hello():
    print("Hello world")
my_print_hello()

def my_print_name(name):
    print(name)
my_print_name("Davis") 
my_print_name("Jamal")
my_print_name("Nadj")

def add(a,b):
    print(a+b)
add(2,5)
add(3,9)
add(11,42)

def GetHello():
    return("Hello La Platforme")
print(GetHello())

def calcule(num1,operator,num2):
    operator = ""
    return(num1, operator, num2)
calcule(23,"",5)

def nombre(a):
    if a > 0:
        print("positif")
    elif a < 0:
        print("negatif")
nombre(4)
nombre(-6)
nombre(-11)

def un (langages):
    langages = ""
    if langages == "javascript":
        print("tu es developpeur web")
    elif langages == "pyton":
        print("tu es developpeur IA")
    elif langages == "java":
        print("tu es developpeur logiciel")
    elif langages == "reactjs":
        print("tu es developpeur mobile")
    else: 
        print("un jour je serai le meilleur developpeur")
un("")

def n (saison, type):
    saison = ""
    type = ""
    if type == "fruits" and saison == "hiver":
       print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise,casis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour,endive")
    elif type == "legume" and saison == "été":
        print("artichaut,aubergine,navet")

def moyenne (note1, note2, note3):
    return((note1 + note2 + note3)/3)
moyenne_etudiant = moyenne(11,13,15)
print(moyenne_etudiant)
if moyenne_etudiant <= 20 and moyenne_etudiant >=15:
    print("tres bon eleve")
elif moyenne_etudiant <= 14 and moyenne_etudiant >= 11:
    print("bon eleve")
elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8:
    print("eleve moyen")
elif moyenne_etudiant <= 0 and moyenne_etudiant >= 7:
    print("eleve devant faire des efforts")

def number(a)-> bool:
    if a%2 ==0 and a>0:
        print("pair")
    else: 
        print("imapair")
number(22)

def time_to_text(minute, console):
    console = ""
    print("heures et minutes")
time_to_text(3,10)

def mot(yes):
    yes = ""
    print("jamalmusiala")
    return yes [::-1]
add