import json
import re

#fonction pour charger le JSON
def charger_catalogue(chemin):

    """Charge et retourne le catalogue depuis un fichier JSON.
    
    Args:
        chemin: chemin vers le fichier catalogue.json
    
    Returns:
        liste des artistes ou None en cas d'erreur
    """

    try:
        with open(chemin,'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier catalogue.json n'existe pas")
    except  json.JSONDecodeError:
        print("Le fichier est corrompu ou vide")
    except PermissionError:
        print("Désolé vous n'avez pas l'autorisation d'ouvrir ce fichier")

#fonction pour sauvegarder le catalogue
def sauvegarder_catalogue(data,chemin):

    """Sauvegarde le catalogue dans le fichier JSON.
    
    Args:
        data: liste des artistes à sauvegarder
        chemin: chemin vers le fichier catalogue.json
    
    Returns:
        None
    """

    try:
        with open(chemin,'w',encoding='UTF-8') as f:
            return json.dump(data,f ,ensure_ascii=False ,indent=4)
    except PermissionError:
        print("Impossible d'écrire : fichier utilisé par un autre programme.")
    except TypeError:
        print("Les données contiennent un format non sauvegardable.")

#fonction pour retourner la liste des artistes
def liste_artistes(catalogue):

    """Retourne la liste complète des artistes du catalogue.
    
    Args:
        catalogue: liste des artistes chargée depuis le JSON
    
    Returns:
        liste des artistes ou None si le catalogue est vide
    """

    if not catalogue :
        print("Liste vide")
        return None
    return catalogue

#fonction pour rechercher un artiste(nom ou genre)
def rechercher_artiste(catalogue,critere,valeur):

    """Recherche des artistes par nom ou par genre.
    
    Args:
        catalogue: liste des artistes chargée depuis le JSON
        critere: critère de recherche, soit 'nom' soit 'genre'
        valeur: valeur à rechercher
    
    Returns:
        liste des artistes correspondants ou None en cas d'erreur
    """

    if critere not in ['nom','genre']:
        print("Critére invalide, choisissez entre nom ou genre")
        return None
    
    if not valeur.strip():
        print("La valeur ne peut pas être vide")
        return None
    
    resultats=[result for result in catalogue if valeur.lower() in result[critere].lower()]
    if resultats==[]:
        print("Désolé mais aucun artiste ne correspond à votre recherche")

    return resultats

#fonction pour ajouter un artiste
def ajouter_artiste(catalogue,artiste):
    """Ajoute un nouvel artiste au catalogue après validation.
    
    Args:
        catalogue: liste des artistes chargée depuis le JSON
        artiste: dictionnaire contenant les informations du nouvel artiste
    
    Returns:
        True si l'ajout est réussi, False sinon
    """
    #Vérifier que l'ID est dans le bon format
    if not re.match(r'^ART-[0-9]{3}$',artiste['id']):
        print("L'id doit être au format ART-XXX(exemple: ART-001)")
        return False
    

    #Vérifier si tout les champs sont bien remplis
    champ=['id','nom','pays','genre']
    for c in champ:
        if not artiste[c].strip():
            print(f"Le champ {c} ne peut pas être vide")
            return False
        
    #Vérifier si les ids n'existent pas
    id_actu=[a['id'] for a in catalogue]
    if artiste['id'] in id_actu:
        print("Cet utilisateur existe déja")
        return False
    
    #Quand tout est bon, ajouter
    catalogue.append(artiste)
    return True


#Fonction pour ajouter un album
def ajouter_album(catalogue,id_artiste,album):
    """Ajoute un album à un artiste existant dans le catalogue.
    
    Args:
        catalogue: liste des artistes chargée depuis le JSON
        id_artiste: identifiant de l'artiste au format ART-XXX
        album: dictionnaire contenant titre, annee et streams de l'album
    
    Returns:
        True si l'ajout est réussi, False sinon
    """
    #s'assurer d'avoir trouver l'artiste
    mon_artiste=None
    for id in catalogue:
        if id['id']==id_artiste:
            mon_artiste=id
            break
    
    if mon_artiste is None:
        print("Cet artiste n'existe pas chez nous merci")
        return  False
    
    #s'assure que le titre n'est pas vide
    if not album['titre'].strip():
        print("L'album doit avoir obligatoirement un titre")

    #Réglage pour l'année
    try:
        annee=int(album['annee'])
        if annee<1900 or annee>2026:
            print("L'album doit être entre 1900 et 2026")
            return False
    except ValueError:
        print("Veuillez entrer une valeur correcte")
        return False
    
    #Réglage pour les streams
    stream=int(album['streams'])
    if stream<0:
        print("Les streams ne peuvent pas être négatif")
        return False
    else:
        #Validé quand tout est bon
        mon_artiste['albums'].append(album)
        return True





        


     