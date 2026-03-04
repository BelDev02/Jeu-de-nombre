from random import randint

def choisir_difficulte():
    print("Choisissez un niveau :")
    print("1 - Facile (1-50, 15 essais)")
    print("2 - Moyen (1-100, 10 essais)")
    print("3 - Difficile (1-500, 7 essais)")
    
    while True:
        try:
            choix = int(input("Votre choix : "))
            if choix == 1:
                return 50, 15
            elif choix == 2:
                return 100, 10
            elif choix == 3:
                return 500, 7
            else:
                print("Choix invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def jouer():
    max_nombre, max_essais = choisir_difficulte()
    nombre_secret = randint(1, max_nombre)
    score = 0
    
    print(f"\nDevinez le nombre entre 1 et {max_nombre}")
    
    for tentative in range(1, max_essais + 1):
        try:
            proposition = int(input(f"Tentative {tentative}/{max_essais} : "))
        except ValueError:
            print("Entrée invalide.")
            continue
        
        if proposition < nombre_secret:
            print("C'est plus !")
        elif proposition > nombre_secret:
            print("C'est moins !")
        else:
            score = max_essais - tentative + 1
            print(f"🎉 Bravo ! Vous avez trouvé en {tentative} tentatives.")
            print(f"🏆 Score : {score}")
            return
        
    print(f"❌ Perdu ! Le nombre était {nombre_secret}")

if __name__ == "__main__":
    jouer()
