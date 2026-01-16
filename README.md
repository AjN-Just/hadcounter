**HadCounter**

Petit projet Django pour la gestion d'une application municipale (structure du projet fournie).

SECOND README

**Aperçu**:
- **But**: Fournir une application Django minimaliste (app `mairie`) pour démonstration et développement.

**Prérequis**:
- **Python**: 3.8+ recommandé
- **Virtualenv**: optionnel mais conseillé

**Installation**:
- Créer et activer un environnement virtuel:

```
python -m venv .venv
source .venv/bin/activate
```

- Installer les dépendances (ajoutez `requirements.txt` si nécessaire):

```
pip install -r requirements.txt
```

- Appliquer les migrations et créer la base SQLite (déjà fournie `db.sqlite3` si présent):

```
python manage.py migrate
python manage.py makemigrations
```

- Créer un superutilisateur:

```
python manage.py createsuperuser
```

**Exécution en développement**:

```
python manage.py runserver
```

Puis ouvrir http://127.0.0.1:8000/ dans le navigateur.

**Tests**:

- Lancer les tests Django:

```
python manage.py test
```

**Structure importante**:
- **hadcounter/**: configuration Django (settings, urls, wsgi, asgi)
- **mairie/**: application principale (models, views, admin, migrations)
- `db.sqlite3`: base de données SQLite (si présente)

**Contribuer / Suivi**:
- Ouvrir une issue ou proposer une PR pour des améliorations.

**Contact**:
- Indiquez ici votre e-mail ou canal de contact.

---

Souhaitez-vous que j'ajoute une section `requirements.txt`, des exemples d'API, ou un guide de déploiement ?
