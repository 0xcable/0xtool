import random
import os

def ajouter_chiffres_aleatoires_au_lien(lien):
    chiffres_aleatoires = random.randint(1, 1000000000)
    lien_modifie = f"{lien}{chiffres_aleatoires}"
    return lien_modifie

# Nom du fichier texte
nom_fichier = "give.txt"

# Vérifier si le fichier existe
if not os.path.exists(nom_fichier):
    # Créer le fichier s'il n'existe pas
    with open(nom_fichier, "w"):
        pass

# Demander à l'utilisateur s'il veut supprimer le contenu actuel
supprimer_contenu = input("Voulez-vous supprimer le contenu actuel du fichier (O/N) ? ").upper()

# Si l'utilisateur choisit de supprimer le contenu actuel
if supprimer_contenu == "O":
    # Ouvrir le fichier en mode écriture pour supprimer le contenu
    with open(nom_fichier, "w"):
        pass

# Demander le nombre de liens à générer
nombre_de_liens = int(input("Entrez le nombre de liens que vous souhaitez générer : "))

# Prendre le lien d'origine en entrée de l'utilisateur
lien_original = input("Entrez le lien d'origine : ")

# Ouvrir le fichier en mode ajout pour écrire les nouveaux liens
with open(nom_fichier, "a") as fichier:
    # Boucle pour générer et écrire les liens dans le fichier
    for _ in range(nombre_de_liens):
        lien_modifie = ajouter_chiffres_aleatoires_au_lien(lien_original)
        fichier.write(lien_modifie + "\n")
        print(lien_modifie)

print(f"Les liens ont été ajoutés au fichier {nom_fichier}.")
