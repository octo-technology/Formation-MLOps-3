summary: TP2 - Valider les données avec Pandera
id: tp2
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP3 - Valider les données avec pandera

## Vue d'ensemble

Durée : 5 minutes

### À l'issue de ce TP, vous aurez découvert

- [Pandera](https://pandera.readthedocs.io/en/stable/index.html), un framework lightweight de validation des données
- Comment spécifier des vérifications à passer lors de la validation de vos données avec Pandera
- Comment valider vos données avec les specifications précédemment définies
- Comment gérer le resultat de l'étape de validation

### Présentation des nouveautés sur la branche de ce TP

TODO

## Installer les dépendances

TODO : Changement de branche
Ouvrir un terminal dans lequel l'environnement conda est activé puis lancer :

```
pip install pandera
```

## Rajouter des vérifications

Observer le module `source/entities/customer_data_schema`

Nous avons pré-défini un ensemble de validation en utilisant Pandera
notamment [DataFrameModel](https://pandera.readthedocs.io/en/stable/dataframe_models.html).

## Valider les données

Dans la suite, nous souhaitons définir les vérifications inhérentes à la colonne `income`, voici ce que vous
devez faire :

1. Déclarer la colonne `income` (vous pouvez inspirer de la déclaration des autres colonnes)
2. Vérifier bien que le type de la colonne est bien celui qui est attendue dans les données brutes
3. Ajouter un check custom pour vérifier à chaque fois que la valeur est compris entre 0 et 100000 (vous pouvez vous
   inspirer du check sur la colonne education)
4. Ajouter la validation sur la méthode prepare data grâce au décorateur @pa.check_input(RawCustomerSchema)
5. Dans le swagger faire un `train` pour vérifier les données : il n'y a pas d'erreur.
6. Dans le swagger faire un `predict` avec un income à -10 : Observer les logs
7. Remplacer le decorator @pa.check_input par @validate_input, celui là filtrera les erreurs de l'input

## Pour aller plus loin

Explorer les autres vérifications possibles à mettre en place.

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp4#0)

# TODO Formateur
