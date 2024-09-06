# Requirements

Pour installer le projet vous devez avoir:

- Python

# Installation

Pour installer l’application bureautique, commencez par cloner le repository github :

```bash
git clone https://github.com/jason-heng/soigne-moi-desktop
```

Ensuite dupliquez le fichier .env.example et renommez le en .env puis remplissez les variables d’environements avec les votres.

<aside>
:bulb: La variable d’environement “API_URL” est le lien vers l’api du site
Si vous faites tourner le site en local ca sera: http://localhost:3000/api
Sinon c’est: https://soigne-moi-web.vercel.app/api

</aside>

Apres ca, installez les modules necessaires a l’execution du site en faisant:

```bash
pip install -r requirements.txt
```

Finalement vous pouvez lancer l’application via:

```bash
python main.py
```