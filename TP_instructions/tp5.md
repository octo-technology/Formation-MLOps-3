summary: TP5 - Identifier une faille de sécurité
id: tp5
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP5 - Identifier une faille de sécurité

## Vue d'ensemble

Durée : 5 minutes

### À l'issue de ce TP, vous aurez découvert

- Qu'il est assez facile de faire prédire n'importe quoi à un modèle.
- Comment se protéger face à ce genre d'attaque

### Présentation des nouveautés sur la branche de ce TP

Récupérer la branche du TP :

```shell
git checkout 5_start_tp_faille_de_securite
```

Les nouveautés sur cette branche sont les suivantes :

- Le fichier [source/domain/entities/prediction_schema.py](source/domain/entities/prediction_schema.py) qui contient un
  template de schema pour valider les prédictions

## Trouver une faille

En tant qu'attaquant, nous souhaitons faire prédire une valeur négative à notre modèle.

Manipulez les données fournies en entrée, essayer des valeurs extrêmes jusqu'à ce que le modèle prédise une valeur
négative.

## Empêcher la faille de se reproduire

Comme nous avons identifié une règle métier (l'inférence ne peut pas être négative), nous vous proposons de
l'implémenter comme contrôle qualité de notre inférence.

En utilisant `pandera` il est possible de contrôler également les outputs.

Pour cela décorer la fonction `predict_model` avec le décorateur

```python
@pa.check_output(PredictionSchema)
def predict_model(df: pd.DataFrame, model_handler: ModelHandler) -> pd.DataFrame:
    ...
```

Puis définir un `PredictionSchema` en s'inspirant du schema RawCustomerSchema

## Enrichir le schéma des inputs

Nous avons également identifié une faille dans les inputs, nous n'avons pas fixé de limites sur les valeurs pour l'âge
des clients alors que le métier nous dit qu'ils ont entre 18 et 125 ans.

Implémenter ce contrôle dans le schéma.

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp4#0)

# TODO Formateur
