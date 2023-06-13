summary: TP1 - Découvrir l'API et faire le premier fix
id: tp1
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP1 - Découvrir l'API de prédiction et identifier un premier bug

## Vue d'ensemble

Durée : 5 minutes

### À l'issue de cette section, vous aurez découvert

### Présentation des nouveautés sur la branche de ce TP

## Essayer l'API

Durée : 5 minutes

Essayer l'API, dans votre terminal réaliser un curl en remplaçant les ... pour mettre un niveau d'éducation (exemple :
PhD) et un age.

```shell
curl http://0.0.0.0:8000/predict?education=...&age=...
```

Normalement l'API vous retourne une prédiction

## Découvrir le premier bug

Durée : 5 minutes

Essayer maintenant l'API vec education=Engineer

```shell
curl http://0.0.0.0:8000/predict?education=Engineer&age=...
```

L'API retourne maintenant une erreur 500 sans plus d'explications. Nous avons notre premier bug

## Debugger et corriger

Durée : 15 minutes

- Explorez le code pour identifier la source de l'erreur.
- Rendez l'erreur plus explicite. (Conseil : Le type hinting sur fastapi permet de renvoyer une erreur 422 lorsque le
  type ne correspond pas).

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp2#0)

# TODO

Supprimer le type hinting "Eduction"
Mettre dans la doc que l'on peut entrer engineer (typiquement doc pas à jour)