summary: TP3 - Identifier des drifts avec Deepchecks
id: tp3
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP3 - Identifier des drifts avec deepchecks

## Vue d'ensemble

Duration: 0:03:00

### À l'issue de ce TP, vous aurez découvert

- [deepchecks](https://github.com/deepchecks/deepchecks) un outil d'analyse de drift et de biais entre train et test set

### Présentation des nouveautés sur la branche de ce TP

Récupérer la branche du TP :

```shell
git checkout 3_start_tp_identifier_les_drift_avec_deepchecks
```

Les nouveautés sur cette branche sont les suivantes :

- Le `requirements.txt` contient une nouvelle dépendance : `deepchecks`

## Installer les nouvelles dépendances

Duration: 0:03:00

Dans votre terminal, avec le bon environnement activé, lancer la commande:

```shell
pip install -r requirements.txt
```

Cette commande vérifie que tout est bien installé, et installe notamment `deepchecks`

## Configurer son notebook

Duration: 0:03:00

Pour explorer l'outil deepchecks, nous allons faire une première étude dans un notebook.
1. Vérifier que l'environnement `mlops_3` est activée : `source activate mlops_3`
2. Pour utiliser votre kernel dans le notebook, lancer dans un terminal la
   commande : `python -m ipykernel install --user --name=mlops_3`
3. Cliquer sur le "➕" bleu en haut à droite
4. Cliquer sur Notebook >> Python3 (ipykernel)
5. Sélectionner votre kernel (`mlops_3`)
6. Vérifie que le notebook est fonctionnel exécutant `from deepchecks.tabular.suites import production_suite`

Si le kernel ne marche pas, essayer de redémarrer votre environnement de TP : `File` > `Hub Control Panel` > `Stop server` > `Start server`. 

## Récupérer les inférences passées

Duration: 0:03:00

Maintenant que l'on a un notebook fonctionnel, nous allons utiliser `sqlalchemy` pour réaliser des requêtes sur la base
PostGreSql de monitoring.

1. Créer une cellule d'import
   ```python
   from sqlalchemy import create_engine
   import pandas as pd
   ```
2. Créer une connection à la base de données
   ```python
   engine = create_engine('postgresql://postgres:postgres@postgres:5432/postgres')
   ```
3. Lire les données
   ```python
   monitoring_df = pd.read_sql('monitoring_sells_forecast', engine)
   ```

La table résultante ressemble au tableau suivant

| index | education   | age | income  | inference   | datetime                         |
|-------|-------------|-----|---------|-------------|----------------------------------|
| 0     | High School | 100 | 1.0     | 8437.341966 | 2023-06-23 10:30:34.466971+00:00 |
| 1     | Bachelor    | 12  | 23200.0 | 9736.099105 | 2023-06-23 12:28:40.090749+00:00 |
| 2     | Bachelor    | 12  | 23200.0 | 9736.099105 | 2023-06-23 12:28:40.932153+00:00 |

Les colonnes contiennent les informations suivantes :

- index : L'id de l'inférence
- education, age, income : les données fournies par l'utilisateur
- inference : la valeur de l'inférence retournée
- datetime : un timestamp de la prédiction en utc

## Charger les données d'entraînement

Duration: 0:03:00

Pour ce TP, les données utilisées pour l'entraînement du modèle sont disponibles dans [./data/customer_data.csv](./data/customer_data.csv)

Les charger avec `pandas` :

```python
training_df = pd.read_csv("/home/jovyan/Formation-MLOps-3/data/customer_data.csv")
```

## Comparer les deux jeux de données avec deepchecks

Duration: 0:10:00

Pour réaliser une comparaison de ces jeux de données, nous allons utiliser la suite de test `production_suite`

```python
from deepchecks.tabular.suites import full_suite
from deepchecks.tabular import Dataset

suite = full_suite()
variables = ['education', 'age', 'income']
cat_features = ['education']
result = suite.run(Dataset(training_df[variables], cat_features=cat_features), Dataset(monitoring_df[variables], cat_features=cat_features),  )
```

Deepchecks permet normalement de présenter directement un widget dans le notebook.
Malheureusement, notre infrastructure de TP ne nous permet (actuellement pas) de le visionner.
Nous allons donc sauvegarder cela sous forme `html`.

```python
result.save_as_html('deepchecks_results.html')
```

Double-cliquer, sur le fichier généré pour le visualiser. Puis cliquer dans le bandeau en haut sur `trust`. 

Finalement, explorer les résultats fournis.

## Lien vers le TP suivant

Duration: 0:01:00

Les instructions du TP suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp4#0)

