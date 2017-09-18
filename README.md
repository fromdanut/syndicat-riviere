# syndicat-riviere
Basic website demonstration for a river syndicate association

# Deploy :
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude admin.logentry -o fixtures/dump-data.json


1. Après le premier deploy :

- `createsuperuser`
- `migrate`

2. Dump data :

`python manage.py dumpdata --excludeuth.permission --exclude contenttypes --exclude admin.logentry --exclude sites.site -o fixtures/dump-data.json`

Exclure le site permet de garder le site configurer sur heroku. Attention à n'avoir qu'un site avec l'id 1 (peut nécessiter de mofidier la BDD si d'autre ont été créés entre temps.)

Ces données sont chargé à chaque deploy (cf. release dans le Procfile)
