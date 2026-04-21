
















































def albums_par_annee(df, annee_min=None):

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


def exporter_rapport(df, chemin_csv="rapport.csv"):
    
    top5       = top5_artistes_streams(df)
    par_genre  = moyenne_streams_par_genre(df)
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