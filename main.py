import label

def menu_consulter(catalogue):
    """
    Affiche le menu de consultation du catalogue et gere les interactions utlisateur.

    Cette fonction permet à l'utilisateur de choisir entre lister les artistes, rechercher par critere ou 
    voir le détail d'un artiste spécifique.

    Args:
        catalogue (list): La liste des artistes dans le catalogue.

    Returns:
        None
    """

    print("\n1.CONSULTER LE CATALOGUE")
    print("a.Afficher tous les artistes")
    print("b.Rechercher un artiste par genre ou nom")
    print("c.Afficher le détail d'un artiste")
    
    choix= input("Votre choix (a/b/c):").lower()

    if choix == 'a':
        liste=label.liste_artistes(catalogue)
        


    elif choix =='b':
        critere= input("Rechercher par(nom/genre):").lower()
        valeur=input("Valeur recherchee:")
    
        resultats= label.rechercher_artiste(catalogue, critere, valeur)
        if resultats:
            for artiste in resultats:
                print(f"Nom:{artiste['nom']}| Genre:{artiste['genre']}")
       

    elif choix =='c':
        nom_art= input ("Entrez le nom de l'artiste:").lower()
        #afficher la liste des albums d'artiste avec ses streams
        artiste_trouve = None
        for artiste in catalogue:
            if artiste['nom'].lower() == nom_art:
                artiste_trouve = artiste
                break
        if artiste_trouve:
            print(f"Albums de {artiste_trouve['nom']}:")
            for album in artiste_trouve['albums']:
                print(f"Titre: {album['titre']} | Streams: {album['streams']}")
        else:
            print("Artiste introuvable")


def menu_ajouter_artiste(catalogue):
    """
    Affiche le menu pour ajouter un artiste au catalogue.

    Args:
        catalogue (list): La liste des artistes dans le catalogue.
        artiste (dict): Les informations de l'artiste à ajouter.

    Returns:
        None
    """
    print("\n Formulaire d'ajout d'artiste")
    #saisie des infos
    id_artiste = input("Entrez l'ID (ex:ART-001):").strip()
    nom = input("Nom de l'artiste:").strip()
    genre = input("Genre de musical:").strip()
    pays = input("Pays de l'artiste:").strip()


    nouvel_artiste = {
        "id": id_artiste,
        "nom": nom, 
        "genre": genre,
        "pays": pays,
        
        "albums": []
    }

    if label.ajouter_artiste(catalogue, nouvel_artiste):
        label.sauvegarder_catalogue(catalogue, "catalogue.json")
        print(" Artiste ajouté et sauvegardé avec succes")
    else:
        print("Echec de l'ajout.Verifiez les informations saisies")

def menu_ajouter_album(catalogue):
    """
    Affiche le menu pour ajouter un album à un artiste du catalogue.

    Args:
        catalogue (list): La liste des artistes dans le catalogue.

    Returns:
        None
    """
    print("\n Formulaire d'ajout d'album")# saisie des infos
    mon_artiste = input("ID de l'artiste(ex:ART-001):").strip()
    titre_album = input("Titre de l'album:").strip()
    streams = input("Nombre de streams:")
    annee= input("Année de sortie:")

    
    nouvel_album = {
            "titre": titre_album,
            "streams": streams,
            "annee": annee
        }
    
    if label.ajouter_album(catalogue,mon_artiste,nouvel_album):
        label.sauvegarder_catalogue(catalogue, "catalogue.json")
        print(" Album ajouté et sauvegardé avec succes")
    else:
        print("Erreur lors de l'ajout de l'album")



    


def main():
    catalogue= label.charger_catalogue("catalogue.json")

    while True:
        print("\nMENU PRINCIPAL")
        print("1.Consulter le catalogue")
        print("2.Ajouter un artiste")
        print("3.Ajouter un album")
        print("4.Statisques et rapport")
        print("5.Quitter")

        choix= input("Choix(1-5):")

        if choix == "1":
            menu_consulter(catalogue)

        elif choix =="2":
            menu_ajouter_artiste(catalogue)
            
        
            
        elif choix =="3":
            menu_ajouter_album(catalogue)
            

        elif choix =="5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 