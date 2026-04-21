def charger_et_aplatir(chemin):
    """Charge le fichier JSON et retourne un DataFrame aplati avec les albums.

    Args:
        chemin: chemin vers le fichier catalogue.json
    
    Returns:
        DataFrame des artistes avec detail sur le contenu de chaque album (titre, annee, streams)
        ou None en cas d'erreur
    """
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        df = pd.DataFrame(data)
        
        if df.empty:
            print("Le catalogue est vide")
            return None
        
        df = df.explode("albums").reset_index(drop=True)
        albums_df = pd.json_normalize(df["albums"])
        df = df.drop(columns=["albums"])
        return pd.concat([df, albums_df], axis=1)

    except FileNotFoundError:
        print("Le fichier catalogue.json est introuvable")
        return None
    except json.JSONDecodeError:
        print("Le fichier est corrompu ou vide")
        return None
    except PermissionError:
        print("Accès refusé au fichier")
        return None
    except KeyError as e:
        print(f"Colonne manquante : {e}")
        return None
    except ValueError:
        print("Erreur lors du traitement des données")
        return None

def stats_par_artiste(df):   
    """Appliquer des agregations : groupby(), sum(), mean(), sort_values()

    Args:
        df: dataframe retourner de la fonction aplatir_albums
    
    Returns:
        DataFrame des artistes dans l'ordre croissant des streams 
    """
    
    try:
        if df is None:
            print("Aucune donnée disponible")
            return None
        
        if df.empty:
            print("Le DataFrame est vide")
            return None

        result = df.groupby("nom").agg({
            "streams": "sum",
        }).reset_index()
        
        #Convertir les streams en entier
        result["streams"] = result["streams"].astype(int)

        result = result.sort_values(by="streams", ascending=False).reset_index(drop=True)
        return result.head(5)
  
    except KeyError as e:
        print(f"Colonne manquante : {e}")
        return None

def strams_genre(df):
    """Calcule la moyenne des streams par genre musical.
    
    Args:
        df: DataFrame retourné par la fonction charger_et_aplatir
    
    Returns:
        DataFrame avec les genres triés par moyenne de streams décroissante
        ou None en cas d'erreur
    """
    try:
        if df is None:
            print("Aucune donnée disponible")
            return None
        
        if df.empty:
            print("Le DataFrame est vide")
            return None

        result = df.groupby("genre").agg({
            "streams": "mean",
        }).reset_index()
       
       #Affichage normal du résultats et retrait des NaN éventuels
        result = result.dropna(subset=["streams"])
        result["streams"] = result["streams"].round(0).astype(int)

        result = result.sort_values(by="streams", ascending=False).reset_index(drop=True)
        return result
  
    except KeyError as e:
        print(f"Colonne manquante : {e}")
        return None

def albums_par_annee(df, annee_min=None):
    """Compte le nombre d'albums (titres) par année de sortie.
        
        Args:
            df: DataFrame des artistes
            annee_min: année minimale pour filtrer les données (optionnel)
        
        Returns:
            DataFrame avec deux colonnes : 'annee' et 'nombre_albums' """
    
    try:
        if df is None:
            print("Aucune donnée disponible")
            return None
        
        if df.empty:
            print("Le DataFrame est vide")
            return None
        

        masque = df["annee"].notna()
        
        if annee_min is not None:
            masque = masque & (df["annee"] >= annee_min)
        
        df_filtre = df[masque]
        
        # pour compter le nombre de titres par année
        par_annee = (
            df_filtre.groupby("annee")["titre"]
                    .count()
                    .reset_index()
                    .sort_values("annee")
        )
        
        par_annee.columns = ["annee", "nombre_albums"]
        par_annee["annee"] = par_annee["annee"].astype(int)
        return par_annee
  
    except KeyError as e:
        print(f"Colonne manquante : {e}")
        return None
    except ValueError:
        print("Erreur lors du traitement des données")
        return None


def exporter_rapport(df, chemin_csv="rapport.csv"):
    """Génère et exporte un rapport complet d'analyse en fichier CSV.
        Compile trois sections : le top 5 des artistes par streams,
        la moyenne des streams par genre, et le nombre d'albums par année.

        Args:
            df: DataFrame des artistes
            chemin_csv: chemin du fichier CSV de sortie (défaut: 'rapport.csv')

        Returns:
            None — écrit le rapport dans le fichier CSV et affiche le chemin
        """
    
    top5 = stats_par_artiste(df)
    par_genre  = strams_genre(df)
    par_annee  = albums_par_annee(df)
    
    with open(chemin_csv, "w", encoding="utf-8-sig", newline="") as f:
        
        f.write(" TOP 5 ARTISTES PAR STREAMS \n")
        top5.to_csv(f, index=False)
        f.write("\n")
        
        f.write("MOYENNE DES STREAMS PAR GENRE\n")
        par_genre.to_csv(f, index=False)
        f.write("\n")
        
        f.write(" NOMBRE D'ALBUMS PAR ANNÉE \n")
        par_annee.to_csv(f, index=False)
    
    print(f"Rapport exporté dans : {chemin_csv}")