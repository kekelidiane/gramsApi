#ENVIRONNEMENT
- Installation de python si cela n'a pas été prealablement fait
- Installation de django et django rest framework


#BASE DE DONNEES
- PostgreSQL
    _ Installer postgreSQL et PgAdmin en fonction du systeme d'explication
    _ Configurer la base de données dans le fichier "settings.py" du projet
    _ Configurer le fichier C:\Program Files\PostgreSQL\15\data\pg_hba.conf en ajoutant cette ligne 
        " host    gramsdb         diane           127.0.0.1/32            md5 "
    _ Creer la base de données "gramsdb"
    _ Executer psql en tant qu'administrateur et renseigner le nom d'utilisateur, mot de passe, de la base de donnée

#EXECUTION 
- Executer python manage.py runserver pour acceder au serveur django