# 22A. Implantando no Fl0

Vamos implantar o projeto no Fl0.

**Criando uma conta no Fl0**

Acesse o site do [Fl0](https://fl0.com/) e crie uma conta.

**Criando um novo projeto no Fl0**

-  Crie um novo projeto no Fl0.
-  Dẽ um nome ao projeto.
-  Selecione o repositório do projeto.
-  Habilite a opção `Automatic deployments`.
-  Selecione a branch `main`.

**Configurando o projeto no Fl0**

- Na aba `Environment variables`, inclua as variáveis de ambiente definidas no arquivo `.env`:

| Configuração   | Valor               |
|----------------|---------------------|
| PORT           | 8080                |
| SECRET_KEY     | [gere uma chave secreta](#geração-da-secret_key). |
| DEBUG          | False               |
| MODE           | PRODUCTION          |

**Configurações no projeto**

- Adicione o pacote `gunicorn`:

```shell
pdm add gunicorn
```

> O `gunicorn` é um servidor HTTP WSGI para Python. Ele é necessário para que o projeto possa ser executado no Fl0.

- Crie um arquivo `Procfile` na raiz do projeto, com o seguinte conteúdo:

```shell
web: gunicorn config.wsgi
```

**Configuração de arquivos estáticos**

Websites geralmente precisam servir arquivos adicionais, como imagens, JavaScript e CSS. No Django, esses arquivos são chamados de arquivos estáticos, e ele fornece um módulo dedicado para coletá-los em um único local para servir em produção.

Nesta etapa, vamos configurar o `WhiteNoise`, que é uma solução muito popular para esse problema.

- Adicione o `WhiteNoise` como uma dependência (adicionar suporte para `Brotli` é opcional, mas recomendado):

```shell
pdm add 'whitenoise[brotli]'
```

- Abra o arquivo `settings.py`, encontre a lista `MIDDLEWARE` e adicione o middleware `WhiteNoise` logo após o `SecurityMiddleware`:

```python
MIDDLEWARE = [
    ...
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ....
]
```

-   Edite o arquivo `settings.py`, incluindo o seguinte código:

```python
...
if MODE == "PRODUCTION":
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

> O `STATIC_ROOT` é o diretório onde os arquivos estáticos serão coletados. O `STATICFILES_STORAGE` é o armazenamento de arquivos estáticos que será utilizado.

> Essas configurações só serão utilizadas no modo `PRODUCTION`.


**Finalizando**

- Assegure-se de que o arquivo `requirements.txt` está atualizado. Caso ele não exista, [siga esses passos](#a3-gerando-o-arquivo-requirementstxt-automaticamente).

- Faça o commit das alterações. O projeto deve ser implantado automaticamente no Fl0.
- Acompanhe o processo na aba `Deployments`, escolhendo o deployment mais recente, e clicando em `View logs`.
- Se tudo der certo, o projeto estará disponível na URL que você definiu, algo parecido com https://livraria-marrcandre-dev.fl0.io/.


# 22B. Utilizando um Banco de Dados externo no Fl0

Vamos criar um banco de dados externo no Fl0. Assim, não utilizaremos mais o SQLite3, que vinhamos usando no desenvolvimento. Com isso, os dados não serão perdidos a cada nova implantação.

**Configurando o arquivo `settings.py`**

- Edite o arquivo `settings.py` do projeto, e substitua o conteúdo da variável `DATABASES` pelo seguinte:

```python
...
if MODE in ["PRODUCTION", "MIGRATE"]:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

print(MODE, DATABASES)
...
```

> Note que a variável `DATABASES` foi substituída por um `if` que verifica se o `MODE` é `PRODUCTION` ou `MIGRATE`. Se for, o banco de dados será o `PostgreSQL` do `Fl0`. Caso contrário, será o `SQLite` local.

> O `print` foi incluído para que você possa verificar se o banco de dados está correto.

**Instalação do suporte ao PosgreSQL**

- Para acessar o banco de dados PostgreSQL, instale o seguinte pacote:

```shell
pdm add psycopg2-binary
```

**Criando um Banco de Dados no Fl0**

- Nas configurações do projeto, clique em `Add New` e em `Postgres database`.
- Escolha a localização mais perto de sua casa.
- O Banco de Dados será criado.

**Utilizando as informações do Banco de Dados criado**

- Clique no Banco de Dados criado e entre na opção `Conection Info`.
- Copie as informações de conexão, e coloque no seu arquivo `.env`:

```shell
# Fl0 Database
DATABASE_NAME=fl0db
DATABASE_USER=fl0user
DATABASE_PASSWORD=senha_do_bd
DATABASE_HOST=url.do.bd.flo.com
DATABASE_PORT=5432
```
> Altere as informações de acordo com o seu projeto.

- Inclua as informações do Banco de Dados no Fl0, na aba `Environment variables`, incluindo as variáveis de ambiente definidas no arquivo `.env` referentes ao banco de dados.

**Migração do banco de dados**

- No arquivo `.env`, altere o valor da variável `MODE` para `MIGRATE`.
- Faça a migracão do banco de dados:

```shell
pdm run python manage.py migrate
```

> Observe que o banco de dados foi migrado para o `Fl0`.

- Crie um super usuário:

```shell
pdm run python manage.py createsuperuser
```

**Configurando o Banco de Dados externo no Fl0**

- Na aba `Environment variables`, certifique-se de que o valor da variável `MODE` é `PRODUCTION`.
- Faça o commit das alterações.
- Sua aplicação deve estar funcionando normalmente, utilizando o banco de dados do `Fl0`.

**Observações**

- Para testar, crie um novo autor no projeto e verifique se ele foi criado no banco de dados do `Fl0`.

- Opcionalmente, você pode utilizar um dump do banco de dados local e carregá-lo no banco de dados do `Fl0`:

```shell
pdm run python manage.py loaddata livraria.json
```

> A partir de agora, sempre que você fizer uma nova implantação, os dados não serão perdidos.

- Para voltar a usar o banco de dados local, altere o valor da variável `MODE` no arquivo `.env` para `DEVELOPMENT`.
