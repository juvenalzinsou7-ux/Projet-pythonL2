import datetime

def journaliser(action, informations):
    """Enregistre une action dans le fichier historique.log.
    
    Args:
        action: type d'action effectuée (ex: AJOUT ARTISTE, AJOUT ALBUM)
        informations: dictionnaire contenant les informations de l'action
    
    Returns:
        None
    """
    # Récupérer la date et heure actuelles
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formater la ligne
    ligne = f"[{date}] {action} | "
    ligne += " | ".join([f"{cle}: {valeur}" for cle, valeur in informations.items()])
    ligne += "\n"
    
    # Écrire dans le fichier
    with open('historique.log', 'a', encoding='utf-8') as f:
        f.write(ligne)