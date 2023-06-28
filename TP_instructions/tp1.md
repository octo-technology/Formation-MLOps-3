summary: TP1 - Découvrir l'API et faire le premier fix
id: tp1
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP1 - Découvrir l'API de prédiction et identifier un premier bug

## Vue d'ensemble

Duration: 0:01:00

### À l'issue de ce TP, vous aurez découvert

- L'API de prediction
- Identifier un bogue sur l'API
- Identifier la source du bogue dans les logs
- Rendre les erreurs utilisateurs plus user friendly avec le type hinting

## Présentation des nouveautés sur la branche de ce TP

Duration: 0:01:00

Récupérer la branche du TP :

```shell
git checkout 1_start_tp_first_bug
```

Il n'y a pas particulièrement de nouveauté sur cette branche

## Essayer l'API

Duration: 0:03:00

Dans le Swagger, essayer l'API, en mettant un niveau d'éducation (exemple : PhD), un âge et un revenu.

Normalement l'API vous retourne une prédiction

## Découvrir le premier bug

Duration: 0:03:00

La documentation propose de mettre Engineer dans le champ éducation... essayer.

L'API retourne maintenant une erreur 500 sans plus d'explications. Nous avons notre premier bug.

## Debugger et corriger

Duration: 0:15:00

- Explorer le code pour identifier la source de l'erreur.
- Rendre l'erreur plus explicite. (Conseil: Le type hinting sur fastapi permet de renvoyer une erreur 422 lorsque le
  type ne correspond pas).
- Mettre à jour la documentation (la docstring) de la route d'API

Rappel : pour les visualiser en flux, taper dans un terminal la commande : 

```shell
tail -f /home/jovyan/api_logfile.log
```

## Lien vers le TP suivant

Duration: 0:00:30 

Les instructions du TP suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp2#0)
