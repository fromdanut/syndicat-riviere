# syndicat-riviere
Basic website demonstration for a river syndicate association

## Presentation

Site de démonstration réalisé en Python avec le Framework Django.

Il contient l'ensemble des fonctionnalités basiques pour un syndicat de rivière :

- différentes pages pour présenter les problématiques
- une section actualité pour la partie communication
- une partie document pour poster des documents en ligne
- une partie administration pour ajouter/modifier facilement l'ensemble des éléments cités

## Mise en production

__Après le premier deploy :__

- `createsuperuser`
- `migrate`
- modifier le nom du site par le nom de domaine.
- Rajouter des medias car ne fonctionne pas avec loaddata :
    - des archives de démonstrations.
    - des actualités avec des images.

__Après chaque deploy :__

Voir le release du Procfile pour voir l'ensemble des commandes lancées automatiquement après chaque deploy.

_Charger les fixtures_

Les fixtures chargés sont le résultat de la commande suivante :

`python manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude admin.logentry --exclude archives --exclude sites.site -o fixtures/dump-data.json`

- Exclure le site permet de garder le site configuré en production. Attention à n'avoir qu'un site avec l'id 1 (peut nécessiter de mofidier la BDD si d'autre ont été créés entre temps.)
- Exclure les archives car elles ne seront pas correctement uploadées lors du loaddata.
- Garder les actualités mais veuiller à ne pas leur attribuer d'image, car elles ne seront pas correctement uploadées lors du loaddata.
