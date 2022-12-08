CIRCLE CI PIPELINE STATUS
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/FuzzyParrabellum/OPENCP13Clone/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/FuzzyParrabellum/OPENCP13Clone/tree/master)

## Résumé
Projet cloné de OPENCP13


Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Instructions pour un Déploiement sur Heroku via CircleCI, monitoré par Sentry

### Prérequis

- Un compte Github
- Un compte CircleCI
- Un compte Heroku
- Un compte Sentry

### Fonctionnement

Grâce au contenu de ce repository sur github, en incluant .circleci/config.yml,
heroku.yml et le Dockerfile, il est possible de créer un pipeline de CI/CD,
en utilisant CircleCI qui va créer un pipeline en 3 étapes:
1 - Compiler et testerle code, pour voir si il est correctement formaté et qu'il
n'y a pas d'erreurs en local.
2 - Créer une image de l'application qu'il va pusher vers le DockerHub, afin
que l'application fonctionne de la même manière dans n'importe quel 
environnement.
3 - Déployer l'application via l'image crée vers Heroku, qui va fournir un lien
https pour y accéder.

Sentry va ensuite être alerté et vous notifier si votre application rencontre
des erreurs lors de son utilisation après son déploiement, par exemple si vous
essayez d'aller sur la route `/sentry-debug/` qui est là à titre d'exemple
pour montrer le comportement de l'application lors d'une erreur.

Si vous voulez accéder à votre application en utilisant uniquement Docker, après
avoir pushé l'image de votre application via CircleCI et avoir installé docker
localement sur votre ordinateur, vous pouvez effecter la commande :

`docker run -d -p 8000:8000 DOCKER_USERNAME/project13:CIRCLE_SHA1`
en remplaçant DOCKER_USERNAME par votre nom d'utilisateur sur docker et en
remplaçant CIRCLE_SHA1 par le tag que vous pouvez voir à la fin du registry
de votre projet, project13, sur votre compte docker.

#### Instructions Django

Dans les settings de l'application, une méthode est importée pour founir une **SECRET_KEY** si vous n'en donnez pas ensuite à Heroku ou CircleCI. Vous pouvez
bien sûr en générer une vous-même que vous utiliserez par la suite.

#### Instructions Sentry

Créez un compte sur Sentry, puis un projet Django, et notez la **clé dsn** qui
vous ait fourni.

#### Instructions Docker

Créez un compte sur Dockerhub et notez votre **nom d'utilisateur** et votre 
**mot de passe**.
Créez ensuite un projet appelé project13.

#### Instructions Heroku

Créez un compte sur Heroku et notez le **nom de votre application** et notez
également votre **API KEY** que vous vouvez générer dans les settings de votre
compte.

Allez ensuite dans les settings de votre projet, cliquez sur "Config Vars" et 
renseignez deux champs :

SECRET_KEY -- avec comme valeur votre clé secrète django, si vous en avez
généré une.
SENTRY_DSN -- avec comme valeur la clé dsn fournie par sentry.

#### Instructions CircleCI

Après avoir cloné le site et l'avoir pushé vers votre repository github,
créez un compte CircleCI et indiquez vouloir relier ce repository à CircleCI.
Quand il vous ai demandé si vous avez besoin d'un template de fichier de  configuration, indiquez plutôt que vous en avez déjà un qui est joint à
ce repo dans .circleci/ 

Normalement, tout commit sur la branche master entrainera un push vers votre
repo Docker, puis un déploiement vers votre application Heroku.
Pour se faire, vous devez aller dans les settings de votre projet et renseigner
plusieurs champs dans le volet "Environment variables":

DOCKERHUB_USERNAME -- avec comme valeur votre nom d'utilisateur sur docker.
DOCKERHUB_PASSWORD -- avec comme valeur votre mot de passe sur docker.
HEROKU_APP_NAME -- avec comme valeur le nom de votre app sur heroku.
HEROKU_API_KEY -- avec comme valeur votre API KEY sur heroku.
SECRET_KEY -- avec comme valeur votre clé secrète django, si vous en avez
généré une.
SENTRY_DSN -- avec comme valeur la clé dsn fournie par sentry.



