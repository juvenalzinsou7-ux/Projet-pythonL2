Application console Python pour gerer un catalogue d'artistes et d'albums, avec persistance en JSON et statistiques via `pandas`.

## Apercu

Le projet permet de :

- consulter le catalogue complet des artistes ;
- rechercher un artiste par nom ou par genre ;
- afficher le detail d'un artiste via son identifiant ;
- ajouter un nouvel artiste ;
- ajouter un album a un artiste existant ;
- generer des statistiques et exporter un rapport CSV.

Le catalogue fourni contient actuellement **12 artistes** et **33 albums**.

## Structure du projet

- `main.py` : point d'entree et gestion des menus console ;
- `label.py` : logique metier, validation et sauvegarde des donnees ;
- `analyse.py` : traitement statistique avec `pandas` ;
- `catalogue.json` : base de donnees du catalogue ;
- `requirements.txt` : dependances Python ;
- `rapport.csv` : fichier genere a la demande depuis le menu statistiques.

## Prerequis

- Python 3.10 ou plus recent
- `pip`

Dependance principale :

```txt
pandas>=2.0
```

## Installation

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer le projet

```bash
python main.py
```

## Fonctionnalites

### 1. Consultation du catalogue

Depuis le menu principal, vous pouvez :

- afficher tous les artistes ;
- rechercher par nom ;
- rechercher par genre ;
- afficher le detail d'un artiste a partir de son ID.

### 2. Ajout d'un artiste

L'application demande :

- un identifiant unique, par exemple `ART-013` ;
- le nom de scene ;
- le genre musical ;
- le pays d'origine ;
- un nombre optionnel d'albums a ajouter tout de suite.

Les donnees sont sauvegardees immediatement dans `catalogue.json`.

### 3. Ajout d'un album

Vous pouvez rattacher un album a un artiste existant en renseignant :

- l'ID de l'artiste ;
- le titre ;
- l'annee ;
- le nombre de streams.

### 4. Statistiques

Le menu statistiques permet de produire :

- le top 5 des artistes par nombre total de streams ;
- la moyenne des streams par genre ;
- le nombre d'albums par annee ;
- un export `rapport.csv` encode en UTF-8 avec BOM.

Si `pandas` n'est pas installe, l'application affiche un message explicite.

## Format des donnees

Chaque artiste est stocke sous la forme suivante :

```json
{
  "id": "ART-001",
  "nom": "Nom Artiste",
  "genre": "Afrobeat",
  "pays": "RDC",
  "albums": [
    {
      "titre": "Titre Album",
      "annee": 2022,
      "streams": 5100000
    }
  ]
}
```

## Points techniques

- application 100 % console ;
- persistance des donnees en JSON ;
- validation des saisies numeriques ;
- verification de l'unicite de l'identifiant artiste ;
- gestion des erreurs de chargement et de saisie ;
- organisation separee entre interface, logique metier et analyses.

## Utilisation rapide

```text
1) Consulter le catalogue
2) Ajouter un artiste
3) Ajouter un album
4) Statistiques & rapport
5) Quitter
```

## Ameliorations possibles

- ajouter des tests automatises ;
- proposer la suppression ou la modification d'un artiste ;
- ajouter des graphiques avec `matplotlib` ;
- filtrer les statistiques par pays ou par genre.
