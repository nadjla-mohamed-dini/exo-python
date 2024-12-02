def l():
    fruits = ["pomme","cerise","orange"]
    return fruits
print(l())

def m ():
    fruits = ["pomme",'cerise',"orange"]
    return fruits
print(m()[1])

def p ():
    fruits = ["pomme", "cerise","orange"]
    fruits.append("Melon")
    return fruits
print(p())

def f ():
    fruits = ["pomme","cerise","orange","melon"]
    fruits.insert(2,"mangue")
    return fruits
print(f())

L = [2,6,11,9,5]
print(L[2])
def un ():
    L [3]=16 
    return L
print(un())
print(un()[4])

number = [1,2,3,4,5]
print(number)
print(number[::-1])

mul = [8,24,48,2,16]
for num in mul:
   if num % 3 ==0:
    print(num)

liste = [8,24,2,74,82,16,9,7,84,91]
somme = 0
for paire in liste:
   if paire % 2 ==0:
      somme += paire
      print(somme)


ciao = [8,24,27,48,2,16,9,102,7,84,91]
for n in ciao:
   if n >= 102:
      print(f"la valeur max est {n}")
   elif n <= 2:
      print(f"la valuer min est {n}") 

lei = [8,24,27,48,2,16,9,102,7,84,91]
nun = 1
for t in lei:
   if t >25 and t <90:
     nun *= t 
   print(nun)

liste = [7,11,42,39,2]
add = [x + 1 for x in liste]
print(add)

def i():
   number = [3,7,12,42,14,66]
   tri_selection(number)