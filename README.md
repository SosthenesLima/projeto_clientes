## Como utilizar

Após clonar o projeto, acessar o diretório e ativar a branch 
`problema-com-deploy-no-heroku`:

- Copie o arquivo `contrib/env-sample` para a pasta raiz do projeto e renomeio-o para `.env`

```
cp contrib/env-sample .env
```

- Crie um novo ambiente virtual

```
python -m venv .venv
```

- Instale as dependências

```
pip install -r requirements.txt
```

- Faça as migrações

```
python manage migrate
```

- Crie o superusuário:

```
python manage createsuperuser
```

## Deploy no Heroku

- Crie a app no Heroku

```
heroku create
```

- Crie e configure as variáveis de ambiente no Heroku

```
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com
heroku config:set SECRET_KEY=minha-secret-key
```

- Faça o deploy da app

```
git push heroku problema-com-deploy-no-heroku:main
```

- Fazendo as migrações no Heroku

```
heroku run python manage.py migrate
```

- Criando o superuser no Heroku

```
heroku run python manage.py createsuperuser
```
