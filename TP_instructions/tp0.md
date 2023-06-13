summary: TP0 - Setup de l'environnement de travail
id: tp0
categories: setup
tags: setup
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP0 - Préparation de l'environnement de travail

## Vue d'ensemble

Durée : 15 min

Cette partie permet de préparer l'environnement de travail pour les TPs.

## Prise en main de Jupyterhub, l'environnement de TP

Durée : 3 min

Pour vous connecter sur l'interface de TP, l'instructeur vous aura donné votre identifiant/mot de passe :
![Connection](images/tp0/connection.png)

Une fois connecté, une page de chargement apparaît, temps pendant lequel votre environnement de TP est créé :
![StartingServer](images/tp0/starting_server.png)

Cela peut prendre 1 à 2 minutes, mais pas plus. Si votre environment ne démarre pas, vous pouvez essayer d'actualiser
puis faire appel à votre formateur.

Une fois que le serveur est démarré, vous êtes redirigé vers la page principale :
![HomePage](docs/tp0/homepage.png)

Depuis cette page, vous pouvez ouvrir :

- Un terminal : dans other / terminal
- Un éditeur de code en ligne : dans Notebook / VS Code
- Airflow et MLFlow que nous manipulerons

Vous pouvez également changer votre mot de passe [ici](https://lab.aws.octo.training/jupyter/hub/auth/change-password).

## Préparer son environnement et cloner le repo

Durée : 3min

Rendez-vous sur votre environnement de développement.

Ouvrez un terminal afin d'y cloner le repository de code des TPs avec la commande `$> git clone <url>;`.
Vous trouverez l'URL de clonage en HTTPS sur github, dans le repo que vous avez forké :

Pour ouvrir un terminal il faut cliquer sur les 2 barres parallèles en haut à droite puis `terminal`
puis `new terminal`.
![bouton clonage](docs/tp0/github-clone-button.png)

En tapant la commande `git branch` vous pourrez constater que vous êtes sur la branche `0_initial_state`

Ensuite, nous allons créer un environnement de travail Python avec Conda et installer les dépendances :

```bash
conda create -yqf python=3.10 --name mlops_3
source activate mlops_3
pip install -r requirements.txt
```

## Accéder au Swagger de l'api

Durée : 5min

Swagger est un langage de description d'interface permettant de décrire des API exprimées à l'aide de JSON. Swagger est
utilisé avec toute une série d'outils logiciels open source pour concevoir, créer, documenter et utiliser des services
Web.

Nous allons accéder à cette interface pour voir les routes d'API et interagir avec elles.

Pour pouvoir y accéder, nous devons faire une configuration liée à l'environnement de TP.

Ouvrir le fichier `/home/jovyan/api_conf.ini`, il contient deux sections de configuration :

```shell
[server] # Ce qui concerne notre serveur de TP
address = https://lab.aws.octo.training/jupyter/user/admin/swagger/  # TODO Remplacer admin par votre username (visible dans l'url)
python_path = python3 # TODO Insérer le path vers votre env conda (que vous pouvez trouver en tapant which python, le résultat sera sans doute /opt/conda/envs/mlops_3/bin/python)

[api] # Ce qui concerne le TP
run_dot_py_file_path = run.py  # TODO Insérer le path vers le fichier run.py du TP soit `Formation-MLOps-3.py`
```

Une fois cela fait, vous pouvez cliquer sur l'icône API dans le launcher, puis ajouter /docs pour voir le swagger.

Tester la route `/health` pour vérifier que tout marche bien.

NB : En background, l'API a été lancé en auto reload, ce qui fait que toutes les modifications que l'on apportera
relancerons l'API.

Les logs de l'API sont visibles dans `/home/jovyan/api_logfile.log`

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp1#0)

## TODO pour créer branche de TP :

- Garder uniquement un run.py et un main.py qui lance l'API avec les route / et /health