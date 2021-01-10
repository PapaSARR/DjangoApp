# Appli Django dockerisé

## Installation et lancement du projet

1. git clone https://github.com/PapaSARR/user-auth
2. cd user-auth
3. docker-compose up -d   
NB: Si le serveur ne trouve pas la bd MySQL au premier coup, réexécuter la commande une seconde fois
4. docker exec -it container_id python manage.py migrate
5. Ouvrir le lien http://127.0.0.1:8000
