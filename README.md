# 🎯 Jeu du Nombre Mystère en Python

## 📌 Description

Ce projet est une implémentation avancée du jeu du Nombre Mystère en Python, jouable en ligne de commande.

Le programme génère un nombre aléatoire et le joueur doit le deviner en un nombre limité de tentatives, selon le niveau de difficulté choisi.

Cette version inclut une structure modulaire avec fonctions, un système de score et plusieurs niveaux de difficulté.

---

## 📝 Sujet du projet

### Instructions de base :

- Importer la fonction `randint` du module `random`
- Générer un nombre entier aléatoire
- Créer une boucle permettant au joueur de deviner le nombre
- Utiliser un bloc `try...except ValueError` pour sécuriser la saisie
- Indiquer si le nombre recherché est plus grand ou plus petit
- Afficher un message de félicitations lorsque le nombre est trouvé

### Extensions ajoutées :

- Ajout d’un choix de niveau de difficulté
- Limitation du nombre d’essais
- Système de score
- Structuration du programme avec fonctions

---

## 🎮 Fonctionnalités implémentées

✔ Génération d’un nombre aléatoire  
✔ Gestion des erreurs de saisie utilisateur  
✔ Indications dynamiques : "C'est plus !" / "C'est moins !"  
✔ Choix du niveau de difficulté  
✔ Nombre d’essais limité  
✔ Système de score basé sur les tentatives restantes  
✔ Code structuré avec fonctions  

---

## 🧠 Niveaux de difficulté

| Niveau     | Intervalle      | Tentatives |
|------------|----------------|------------|
| Facile     | 1 – 50         | 15         |
| Moyen      | 1 – 100        | 10         |
| Difficile  | 1 – 500        | 7          |

---

## 🏆 Système de score

Le score est calculé comme suit :

Score = nombre d’essais restants

Plus le joueur trouve rapidement le nombre secret, plus son score est élevé.

---

## 🛠️ Technologies utilisées

- Python 3
- Module `random`
- Boucle `for`
- Gestion d’exceptions (`try/except`)
- Fonctions
- Structure conditionnelle

---

## 📂 Structure du code

Le programme est organisé de manière modulaire :

- `choisir_difficulte()` → Gestion du niveau
- `jouer()` → Logique principale du jeu
- `if __name__ == "__main__"` → Point d’entrée du programme

Cette organisation rend le code plus clair, maintenable et évolutif.

---

## ▶️ Exécution

Cloner le repository puis exécuter :

```bash
python nombre_mystere.py
