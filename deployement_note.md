Mise en production
==================

## Après le premier deploy :

- `createsuperuser`
- `migrate`
- modifier le nom du site par le nom de domaine.
- Rajouter des medias car ne fonctionne pas avec loaddata :
    - des archives de démonstrations.
    - des actualités avec des images.

## Après chaque deploy :

Voir le release du Procfile pour voir l'ensemble des commandes lancées automatiquement après chaque deploy.

_Charger les fixtures_

Les fixtures chargés sont le résultat de la commande suivante :

`python manage.py dumpdata flatpages actualites > fixtures/dump-data.json`

Attention : on dump les actualités mais veiller à ne pas leur attribuer d'image, car elles ne seront pas correctement uploadées lors du loaddata. Pour cette même raison on ne dump pas l'app archives.
