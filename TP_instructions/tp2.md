summary: TP2 - Réaliser un tir de performance sur l'API
id: tp1
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP2 - Réaliser un tir de performance sur l'API

## Vue d'ensemble

Durée : 5 minutes

## Configuration de votre machine personnel

Pour réaliser ce TP les tirs de performance se feront depuis votre PC personnel.

Pour cela

1. Cloner le repository `git clone https://github.com/octo-technology/Formation-MLOps-3.git`
2. Installez locust en local `pip install locust`

## Ajouter l'authentification pour réaliser vos tirs de performance

Pour pouvoir faire un tir de performance sur une machine déployée, il faut s'authentifier

Dans le cas de notre machine de TP, l'authentification se fait avec un header `Cookie`, nous allons le récupérer dans
notre navigateur :

1. Aller sur l'interface Swagger,
2. Clic droit, inspecter
3. Aller dans l'onglet "Network" qui est apparu
4. Lancer une requête /health
5. Cliquer sur la requête health qui est apparue
6. Dans Request Headers copier le contenu de `Cookie`
7. Le coller dans la variable `YOUR_COOKIE` in `locustfile.py`

![Comment récupérer un cookie](./images/tp2/reccuperer_le_cookie.png)

## Lancer le tir de performance

Pour lancer le tir de performance

1. Dans votre terminal taper `locust`
2. Accéder à http://0.0.0.0:8089
   Vous verrez alors l'interface de configuration suivante :
   ![Configuration locust](./images/tp2/interface_config_locust.png)
3. Pour configurer :
    - Number of user : nombre d'utilisateurs simulés. Commençons par 10.
    - Spawn rate : nombre de créations d'utilisateurs par seconde. Commençons par 1.
    - Host : route du server sur lequel faire le test. `https://lab.aws.octo.training/jupyter/admin/swagger/` ⚠️
      Remplacez `admin` par votre user.
4. Cliquez sur start swarming.
5. Verifier que cela fonctionne :
    - Est-ce que les appels finissent en succès ?
    - Dans le fichier de log `logfile.log` sur le lab, est-ce que les appels apparaissent ?

## Faire des tirs de performance sur la route predict

1. Modifier le fichier `locustfile.py` en remplaçant l'appel sur la route `/health` par un appel sur la route `/predict`
   avec les bons querry paramets.

   Par exemple : `/predict?education=PhD&age=12`

2. Arrêtez et relancer locust dans votre terminal
3. Réaliser un test de performance
4. Jouez sur le nombre d'utilisateurs pour tirer des conclusions sur le fonctionnement de la route et ses limites.

## Auditer le code de predict et l'améliorer

Parcourez le code de prediction et trouver des améliorations pour accélérer la route.

Implémentez votre idée, et réaliser un nouveau tir de performance pour vérifier le résultat.

Si vous n'avez pas d'idée voir la section d'après.

## Si vous n'avez pas d'idée pour accélérer

Comme idée d'amélioration, nous vous proposons de charger le modèle au marriage de l'application plutôt que à chaque
prédiction.

## Pour aller plus loin

Avec des tirs de performance as-code, il est possible de configurer de nombreux scenarios.

- Explorez la documentation de [locust](https://docs.locust.io/en/stable/writing-a-locustfile.html)
- Changez l'implémentation de notre tir de performance pour générer aléatoirement les variables age et éducation.

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp3#0)

# TODO
