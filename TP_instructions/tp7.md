summary: TP7 - Mesurer le carbone émis par l'entraînement
id: tp7
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP7 - Mesurer le carbone émis par l'entraînement

## Vue d'ensemble

Durée : 5 minutes

### À l'issue de ce TP, vous aurez découvert

- L'outil code carbone

### Présentation des nouveautés sur la branche de ce TP

TODO

## Intégrer la mesure du coût carbone de l'entraînement du modèle

Pour réaliser la mesure du coût carbone d'un entraînement, nous allons utiliser le package `codecarbon`

Pour cela mettre à jour les dépendances en lançant la commande :

```shellp
pip install -r requirements.txt
```

Cela va installer en particulier le package `codecarbon`

Ce package est configurable avec un fichier `.codecarbon.config`, nous vous avons fourni la configuration, allez
l'explorer pour voir ce qu'il est possible de configurer.

Ensuite, il faut ajouter un décorateur sur la méthode à mesurer. Ajouter le décorateur suivant :

```python
@track_emissions(project_name='...', offline=True, country_iso_code='FRA')
```

Il convient d'importer `track_emissions` de `codecarbon`

Ce décorateur permet de spécifier

- `project_name` : un nom unique retrouvable parmi les emissions calculées. Choisissez en un.
- `offline` : Pour préciser si un appel API est réalisé pour récupérer les émissions CO2e/kWh de votre pays
- `country_iso_code` : Le pays dans lequel vous êtes

Pour finir, allez dans le Swagger et lancez un entraînement sur la route train pour que l'on commence à logger

## Analyser les résultats

Code carbon a produit un fichier `/home/jovyan/emissions.csv`

Ouvrir le csv (soit directement, soit avec `pandas` dans un notebook pour explorer les résultats).
