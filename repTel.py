import csv

reader = csv.DictReader(open("repTel2.csv","r"))
repTel2 = []
for row in reader:
    repTel2.append(dict(row))

#print(repTel2)

def menu():
    print("BONJOUR, HELLO, HOLÁ, HALLO")
    print(" ")
    menu = int(input("""Saisir 0 pour quittez le répertoire,
       1 pour rechercher un contact,
       2 pour ajouter un contact,
       3 pour modifier un contact,
       4 pour supprimer un contact,
       5 pour afficher tous les contacts : """))
    a = 1
    if menu > 5:
        print("Je crois que vous avez appuyé sur la mauvaise touche...")
        print(" ")
        menu = int(input("""Saisir 0 pour quittez le répertoire,
           1 pour rechercher un contact,
           2 pour ajouter un contact,
           3 pour modifier un contact,
           4 pour supprimer un contact,
           5 pour afficher tous les contacts : """))
    while a == 1:
        while menu == 1:
            print(" ")
            rechercher_contact()
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
               1 pour rechercher un contact,
               2 pour ajouter un contact,
               3 pour modifier un contact,
               4 pour supprimer un contact,
               5 pour afficher tous les contacts : """))
        if menu > 5:
            print("Je crois que vous avez appuyé sur la mauvaise touche...")
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
               1 pour rechercher un contact,
               2 pour ajouter un contact,
               3 pour modifier un contact,
               4 pour supprimer un contact,
               5 pour afficher tous les contacts : """))
        while menu == 2:
            print(" ")
            ajouter_contact()
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
               1 pour rechercher un contact,
               2 pour ajouter un contact,
               3 pour modifier un contact,
               4 pour supprimer un contact,
               5 pour afficher tous les contacts : """))
        if menu > 5:
            print("Je crois que vous avez appuyé sur la mauvaise touche...")
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
               1 pour rechercher un contact,
               2 pour ajouter un contact,
               3 pour modifier un contact,
               4 pour supprimer un contact,
               5 pour afficher tous les contacts : """))
        while menu == 3:
            print(" ")
            modifier_contact()
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
                1 pour rechercher un contact,
                2 pour ajouter un contact,
                3 pour modifier un contact,
                4 pour supprimer un contact,
                5 pour afficher tous les contacts : """))
        if menu > 5:
            print("Je crois que vous avez appuyé sur la mauvaise touche...")
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
               1 pour rechercher un contact,
               2 pour ajouter un contact,
               3 pour modifier un contact,
               4 pour supprimer un contact,
               5 pour afficher tous les contacts : """))
        while menu == 4:
            print(" ")
            supprimer_contact()
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
                1 pour rechercher un contact,
                2 pour ajouter un contact,
                3 pour modifier un contact,
                4 pour supprimer un contact,
                5 pour afficher tous les contacts : """))
        if menu > 5:
            print("Je crois que vous avez appuyé sur la mauvaise touche...")
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
               1 pour rechercher un contact,
               2 pour ajouter un contact,
               3 pour modifier un contact,
               4 pour supprimer un contact,
               5 pour afficher tous les contacts : """))
        while menu == 5:
            print(" ")
            print(afficher())
            menu = int(input("""Saisir 0 pour quittez le répertoire,
                1 pour rechercher un contact,
                2 pour ajouter un contact,
                3 pour modifier un contact,
                4 pour supprimer un contact,
                5 pour afficher tous les contacts : """))
        if menu > 5:
            print("Je crois que vous avez appuyé sur la mauvaise touche...")
            print(" ")
            menu = int(input("""Saisir 0 pour quittez le répertoire,
               1 pour rechercher un contact,
               2 pour ajouter un contact,
               3 pour modifier un contact,
               4 pour supprimer un contact,
               5 pour afficher tous les contacts : """))
        while menu == 0:
            print("")
            return "AU REVOIR, GOODBYE, HASTA LUEGO, AUF WIEDERSEHEN"

def rechercher_contact():
    a = input("Entrez le nom, le prénom ou le numéro de téléphone du contact que vous recherchez : ")
    for contact in repTel2:
        if contact["Nom"] == a or contact["Prénom"] == a or contact["Numéro de téléphone"] == a:
            print("\nNom :",contact["Nom"],", Prénom :",contact["Prénom"],", Adresse :",contact["Adresse"],", Date de naissance :",contact["Date de naissance"],", Numéro de téléphone :",contact["Numéro de téléphone"],", Notes :",contact["Notes"])
    print("Aucun contact trouvé.")

def ajouter_contact():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    adresse = input("Adresse : ")
    date = input("Date de naissance : ")
    numero = input("Numéro de téléphone : ")
    notes = input("Notes : ")
    fichier = open("repTel2.csv","a")
    fichier.write(nom)
    fichier.write(",")
    fichier.write(prenom)
    fichier.write(",")
    fichier.write(adresse)
    fichier.write(",")
    fichier.write(date)
    fichier.write(",")
    fichier.write(numero)
    fichier.write(",")
    fichier.write(notes)
    fichier.close()
    print("Le contact a été enregistré")

#print(ajouter_contact())
#print(rechercher_contact())

def modifier_contact():
    nom = input("Entrez le nom du contact que vous souhaitez modifier : ")
    prenom = input("Entrez le prénom du contact que vous souhaitez modifier : ")
    cle = input("Entrez le champ du contact que vous souhaitez modifier : ")
    modif = input("Écrivez ce que vous souhaitez : ")
    for personne in repTel2:
        if personne["Nom"] == nom and personne["Prénom"] == prenom:
            personne[cle] = modif
            print("Le contact a été modifié")
    if personne["Nom"] != nom and personne["Prénom"] != prenom:
        print("Le contact n'existe pas")

#print(modifier_contact())

def supprimer_contact():
    nom = input("Entrez le nom contact que vous voulez supprimer : ")
    prenom = input("Entrez le prénom contact que vous voulez supprimer : ")
    fichier = open("repTel2.csv","a")
    for contact in repTel2:
        if contact not in repTel2:
            print("Le contact n'existe pas")
        elif contact["Nom"] == nom and contact["Prénom"] == prenom:
            repTel2.remove(contact)
            print("Le contact a été supprimé")
    if contact["Nom"] != nom and contact["Prénom"] != prenom:
        print("Le contact n'existe pas")

#print(supprimer_contact())

def afficher():
    for contact in repTel2:
        print("\nNom : ",contact["Nom"],", Prénom : ",contact["Prénom"],", Adresse : ",contact["Adresse"],", Date de naissance : ",contact["Date de naissance"],", Numéro de téléphone : ",contact["Numéro de téléphone"],", Notes : ",contact["Notes"])

print(menu())
