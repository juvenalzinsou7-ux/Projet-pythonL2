import pandas as pd
import json

def charger_json_en_df(chemin):
    """Charge les donnees JSON et les converti en DataFrame Pandas

    Args:
        chemin: chemin vers le fichier catalogue.json
    
    Returns:
        DataFrame des artistes
    """
    with open(chemin, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data)


def aplatir_albums(df):
    """Aplatir la liste des albums

    Args:
        df: dataframe retourner de la fonction charger_json_en_df
    
    Returns:
        DataFrame des artistes avec detail sur le contenu de chaque album (titre,annee,streams)
    """

    df = df.explode("albums").reset_index(drop=True)
    albums_df = pd.json_normalize(df["albums"])
    df = df.drop(columns=["albums"])
    return pd.concat([df, albums_df], axis=1)

def stats_par_artiste(df):   
    """Appliquer des agregations : groupby(), sum(), mean(), sort_values()

    Args:
        df: dataframe retourner de la fonction aplatir_albums
    
    Returns:
        DataFrame des artistes dans l'ordre croissant des streams 
    """
    result = df.groupby("nom").agg({
        "streams": "sum",
        "annee": "mean"
    }).reset_index()
    
    result = result.sort_values(by="streams", ascending=True).reset_index(drop=True)
    return result