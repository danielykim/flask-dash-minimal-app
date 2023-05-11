Clone this repository

For development, run the following commands:

```zsh
pip install -r requirements.txt
FLASK_APP=application.py FLASK_ENV=development flask run
```

In the development mode, the app is automatically reloaded if you modify the code.



For deployment, run the following commands:

```zsh
waitress-serve --port 8080 'application:application'
```

Open your web browser and check `http://localhost:8080/`.
