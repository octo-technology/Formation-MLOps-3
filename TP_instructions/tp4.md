summary: TP4 - Envoyer automatiquement des alertes mail avec Grafana
id: tp4
status: Published
authors: OCTO Technology
Feedback Link: https://github.com/octo-technology/Formation-MLOps-3/issues/new/choose

# TP4 - Envoyer automatiquement des alertes mail avec Grafana

## Vue d'ensemble

Durée : 5 minutes

### À l'issue de ce TP, vous aurez découvert

### Présentation des nouveautés sur la branche de ce TP

## Créer un point de contact

Accéder à Grafana à
l'adresse [https://lab.aws.octo.training/grafana/alerting](https://lab.aws.octo.training/grafana/alerting)
L'identifiant est collectif à tous les formés : `admin`, le mot de passe vous sera communiqué par le formateur.

Afin de créer une alerte, nous allons créer un point de contact dans Grafana. Dans le cadre de ce TP, nous allons
utiliser un webhook disponible au sein de notre infrastructure de TP.

1. Cliquez sur le menu déroulant en haut à gauche
2. Cliquez sur `Contact points` dans la section "Alerting"
3. Cliquez sur `Add contact point`
4. Dans name fixez un nom unique `webhook_<votreprenom>`
5. Dans `Integration`, il est possible de s'intégrer à un serveur mail (SMTP), teams, slack, etc. Choisir dans le menu
   déroulant `webhook`.
6. Dans l'URL saisir http://localhost:8095/send_email/votreadresse@domain.com en remplaçant votreadresse@domain.com.
7. Vous pouvez cliquer sur `Test` pour vérifier que vous recevez bien le mail
8. Cliquez sur `Save contact point`

![contact_point.png](./images/contact_point.png)

Maintenant Grafana sait comment vous contacter, nous allons maintenant configurer quand vous contacter.

## Créer une règle d'alerte

Nous allons créer une règle pour déclencher des alertes.

1. Cliquez sur le menu déroulant en haut à gauche
2. Cliquez sur `Alert rules` dans la section "Alerting"
3. Cliquez sur `Create alert rule`
4. Dans "1 Set an alert rule name" donnez lui un nom : `alert_prenom`
5. Dans "2 Set a query and alert condition"
    - Choisir une période de `now-5m to now` (Last five minutes) : nous allons nous intéresser qu'aux 5 dernières
      minutes de données
    - Cliquez sur `Group`, les donnez vous être groupée par dateime
    - Dans column sélectionner 2 colonnes : `inference` et `datetime`. Pour inference choisir "Aggregation" `min`
    - Dans Group by col, grouper selon `datetime`
    - Dans Threshold choisir `is lower` `9000`
    - Cliquez sur Preview pour voir les alertes. Si aucun point ne s'affiche, retournez dans le Swagger pour demander
      une
      prédiction. Vous pouvez jouer sur les arguments pour déclencher une alerte (par exemple age=100 devrait permettre
      de la déclencher).
      ![alert querry screenshot](./images/tp4/alert_querry.png)
6. Dans "alert evaluation behavior" nous allons configurer un group d'alerte et au bout de combien de temps, elle se
   déclenche
    - Dans `Folder` choisir `add_new` et lui donner le nom `alert_folder_prenom`.
    - Dans `Evaluation group` l'appeler `alert_evaluation_group_prenom`
    - Dans `Evaluation interval`  choisir every `30s` (doit être un multiple de 10s). Il s'agit de la fréquence d'
      évaluation de l'alerte, il sera commun à toutes les alertes de cet "Evaluation group"
    - Dans `for` choisir `30s`, c'est le délai pendant lequel le seuil doit être dépassé pour déclencher une alerte

   NB : Dans la "vraie" vie, les noms choisis seront explicites !
   ![alert_evaluation_behavior.png](./images/alert_evaluation_behavior.png)
7. Finalement, nous allons configurer un label pour envoyer les notifications aux bonnes personnes.
    - Dans "Notifications", "Labels" dans "choose key" taper `trainee`
    - Dans "Choose value" indiquer votre prénom

   ![notification.png](./images/notification.png)
7. En haut à droite, cliquer sur `Save and exist`

Nous avons maintenant une alerte, il faut maintenant définir un envoi à de mail à vous pour cette alerte.

## Définir une notification policy

1. Cliquez sur le menu déroulant en haut à gauche
2. Cliquez sur `Notification policies` dans la section "Alerting"
3. Cliquez sur `New nested policy`
4. Dans le matching pattern configuer `trainee` `=` `prenom`

![notification_policy.png](./images/notification_policy.png)

## Recevoir une alerte

Maintenant, nous allons chercher à avoir une alerte.

Dans la vue `Alert rule` votre alert apparaît comme normale :
![normal_alert.png](./images/normal_alert.png)

Allez dans le Swagger et faire une requête (par exemple avec `age=100`) pour avoir une prédiction sous le seuil.

Attention, nous sommes tous sur la même table de monitoring des inférences, le comportement des autres formés peut-avoir
un impact sur vous, pour vous isoler, vous pouvez renommer la table de monitoring
dans `source/infrastructure/database_monitoring_handler` dans la variable `MONITORING_SELLS_FORECAST.

Retournez dans alert rules et vérifier que votre alert devient `pending` (c'est-à-dire a dépassé le seuil, mais pas
encore plus de 30s)
![pending_alert.png](./images/pending_alert.png)

Attendre un peu, elle va apparaître `firing`
![firing_alert.png](./images/firing_alert.png)

Vérifier que vous avez bien reçu le mail d'alerte.

## Pour aller plus loin

En attendant le reste du groupe, vous pouvez créer une alerte sur l'age.

## Lien vers le TP suivant

Les instructions du tp suivant sont [ici](https://octo-technology.github.io/Formation-MLOps-3/tp4#0)

# TODO Formateur
