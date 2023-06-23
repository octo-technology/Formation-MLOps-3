summary: TP3 - Identifier des drifts avec Deepchecks
id: tp3
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP3 - Identifier des drifts avec deepchecks

## Vue d'ensemble

Durée : 5 minutes

### À l'issue de ce TP, vous aurez découvert

- [deepcheck](https://github.com/deepchecks/deepchecks) un outil d'analyse de drift et de biais entre train et test set

### Présentation des nouveautés sur la branche de ce TP


## Installer les nouvelles dépendances

Dans votre terminal, avec le bon environnement activé lancer la commande
```shell
pip install -r requirements.txt
```

Cette commande va vérifier que tout est bien installé, et notamment installer `deepcheck`

## Récupérer les inférences passées

Pour explorer l'outil deepchecks nous allons faire une première exploration dans un notebook. 
1. Cliquer sur le "➕" bleu en haut à droite
2. Cliquer sur Notebook >> Python3 (ipykernel)
3. 


from deepchecks.tabular.suites import production_suite

suite = full_suite()

suite.run(df, df)

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp4#0)

# TODO Formateur
