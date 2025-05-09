# # Exercício 8: O Santuário das Constelações

# energy = 100

# gema = 2

# constellation = {1: "Andrômeda",2: "Órion",3: "Perseus",4: "Tarântula",5: "Cisne",6: "Áquila",7: "Crux",8: "Cassiopéia",9: "Eridanos", 10: "Aquário"}

# for name in constellation:
#     print(constellation.get(name))

# # coletar = print("Coletar gema >>")
# energy = 100

# point_gema = 2

# constellation = 11

# while constellation > 0:
#     constellation -= 1
#     gema = int(input(f"Quantas gemas você coletou na {constellation}° constelação? "))
    
#     force = (energy - (gema * point_gema))
#     energy = force
#     print(f"Coletou 5 gemas! Sua energia está em: {energy}")
#     if(energy <= 0):
#         print("Alex não pode mais coletar!!")
# import random

# strength = 100

# guardian = 3 * 50

# strength_points = 5

# attack_points = 10

# attack_failure = 0.3

# fight = input("Atacar? sim ou não: ")
# if fight == "sim":

#   for x in range(11): 
#     attack_aleatorio = random.randint(1, 100)
#     injured_target = attack_aleatorio * attack_failure
#     if(injured_target):
#       guardian -= 10
#       print(f"O Guardião perdeu {guardian} pontos de proteção!")
#     else:  
#       strength -= 5
#       if guardian <= 0:
#             print("Camada Destruída! Alex venceu!!!!!!!")
#       if strength <= 0:
#             print("Alex pedeu!")    
    
energy = 100

point_gema = 2

constellation = 11

while constellation > 0:
    constellation -= 1
    gema = int(input(f"Quantas gemas você coletou na {constellation}° constelação? "))
    
    force = (energy - (gema * point_gema))
    energy = force

    print(f"Coletou 5 gemas! Sua energia está em: {energy}")

    if(energy <= 0):
        print("Alex não pode mais coletar!!")
        constellation = 0
    