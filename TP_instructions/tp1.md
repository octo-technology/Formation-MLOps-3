summary: TP1 - Découvrir l'API et faire le premier fix
id: tp1
status: Published
authors: OCTO Technology
logoUrl: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAjVBMVEX////e4+lmdZOUnrPl6e6Dj6cAJFgAE1AhOGbu8PSbpbcrQWwAEVAAIVYAH1UAAEqzu8o0SnMAC04WMWHByNRBVXsAHFQIKl2FkqlKXYEAGVJ6h6DW2+MAI1cAF1IAFVH5+/wPL2HO092ps8Omrr8ABUxTY4S7w9AAIFZhcI88UXhte5YmPWkAAEVca4sJoZqqAAABt0lEQVR4AX2ShbqrMBCE0Q2SICkHCV2grrfv/3g3Gz6odyqQ/Sc+1hfZjmv9kOcDC+yvOIxiLpI0+sazXCaCL6LwMy7+0hJEVX/DDS8BQLWf8dIpFYKW6LxPS2+rXsAo/j7E4K74hGmIpa6t282Mt6vdjEnd3rbCUqaHEW9ylsCzylXkHbs0I1w0rER4VcL9bdMOeqITUw9YKM54R9Nh6g60kLTHRM4TdN1pm21a4EgOmsDa8z4uzuXI5ckbV1UroWeJqVXsT461YWg4zUm1U+QedYVH4x4ca9grWnk+8jCWadYyXTib9vai+3AEZJk1Gq7sX+YJAQJMKCJt8ErdXITzndXDcFOAfTEZbI7TgJN8DtCbs3a1YUmGvydDPRmKoDxYXo+QXIdHg9MBsgO9SHaywuAIqNYP3FRKutStTDfGD+r2YIgknZQZ079QVFMAlJuZrxfHKTfDLaf/IAEQx+0w8uJa6ma1NEnsUnpmdNqiv23s0DtcTD6kP052vZojbyXdoNrtuEx71Jw3w3MqnTF1iGge/By+5tbv5uhgyW4vnHQ4l51AQKH6mJb7Qes2r6CKL4cJ/wdeVSbK0l0WnwAAAABJRU5ErkJggg==
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP1 - Découvrir l'API de prédiction et identifier un premier bug

## Vue d'ensemble

Durée : 5 minutes

### À l'issue de ce TP, vous aurez découvert

- L'API de prediction
- Identifier un bogue sur l'API
- Identifier la source du bogue dans les logs
- Rendre les erreurs utilisateurs plus user friendly avec le type hinting

## Présentation des nouveautés sur la branche de ce TP

Récupérer la branche du TP :

```shell
git checkout 1_start_tp_first_bug
```

Il n'y a pas particulièrement de nouveauté sur cette branche

## Essayer l'API

Durée : 5 minutes

Dans le Swagger, essayer l'API, en mettant un niveau d'éducation (exemple : PhD), un âge et un revenu.

Normalement l'API vous retourne une prédiction

## Découvrir le premier bug

Durée : 5 minutes

La documentation propose de mettre Engineer dans le champ éducation... essayer.

L'API retourne maintenant une erreur 500 sans plus d'explications. Nous avons notre premier bug.

## Debugger et corriger

Durée : 15 minutes

- Explorer le code pour identifier la source de l'erreur.
- Rendre l'erreur plus explicite. (Conseil: Le type hinting sur fastapi permet de renvoyer une erreur 422 lorsque le
  type ne correspond pas).
- Mettre à jour la documentation (la docstring) de la route d'API

## Lien vers le TP suivant

Les instructions du TP suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp2#0)
