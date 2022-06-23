# Django com DRF

# Aula 1

## Preparação

* Abra o navegador de arquivos
* Crie uma pasta chamada `livraria` para o seu projeto
* Certifique-se de que nenhuma pasta no caminho tenha espaços ou acentos.
* Abra a pasta no vscode (repita em voz alta: *"Nunca abra um arquivo, sempre abra a pasta."*).
* Dentro do vscode, abra um terminal (`Control + Shift + '`)

Instale algumas extensões para o **vscode**:
* Python *
* SqLite Viewer *
* Intellicode
* Prettier
  
Os comandos a seguir serão digitados no terminal que você abriu dentro do **vscode**.

Verifique se o **poetry** está instalado:

    poetry --version

Verifique se o **python** está instalado:

    python --version
    python3 --version

Informe ao **poetry** para criar a pasta do ambiente virtual dentro da pasta do projeto:

    poetry config virtualenvs.in-project true

## Criação do ambiente virtual

Crie o ambiente virtual usado o **poetry**:

    poetry init

Você passará por uma tela semelhante a essa:

```bash
This command will guide you through creating your pyproject.toml config.

Package name [livraria]:  
Version [0.1.0]:  
Description []:  
Author [Marco André Mendes <marcoandre@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [^3.10]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "livraria"
version = "0.1.0"
description = ""
authors = ["Marco André Mendes <marcoandre@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.10"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
```

Ative o ambiente virtual recèm criado:

    poetry shell

Para verificar o tamanho da pasta do ambiente virtual:

    du -sh .venv

## Instalação do django

Instale o **django** no ambiente virtual:

    poetry add django

Verifique se o **django** está instalado:

    djago-admin

Se tudo der certo, ele mostrará as opções do `django-admin` na tela.

## Criação do projeto no django

    django-admin startproject livraria .


O projeto criado ficará assim:

```
.
├── livraria
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── poetry.lock
└── pyproject.toml
```

Para executar o projeto, digite no terminal:

    python manage.py runserver

Verifique o projeto rodando no navegador:

    http://localhost:8000

Verifique também se o `admin` está rodando:

    http://localhost:8000/admin

Ao rodar o projeto pela primeira vez, o arquivo `db.sqlite3` é criado.
Também aparecem mensagens de erro importantes.

* Abra o arquivo `db.sqlite3` dentro do **vscode**.
* Verifique que ele não possuem nenhuma tabela ainda.

Vamos abrir cada um desses arquivos e verificar para que eles servem, principalmente os seguintes:

* `manage.py`
* `settings.py`
* `urls.py`
* `db.sqlite3`

Desse ponto em diante, abra um outro terminal no **vscode**, mantendo sempre o django em execução (`runserver`) no outro terminal.

Se precisar parar a execução do projeto, aperte `Control + C` e depois o execute novamente.

Para resolver o erro informado no momento de rodar o projeto, execute o seguinte comando:

    python manage.py makemigrations

Verifique se o projeto continua rodando e se o `admin` roda.

Crie o super usuário para poder fazer o login:

    python manage.py creatsuperuser

Agora sim, seu projeto está rodando e você consegue entrar no `admin`:

* Crie mais 2 usuários de teste.
* Entre no arquivo de banco de dados, e verifique se os registros foram criados.

----
# Aula 2
Acrescente o app `'core'` na seção `INSTALLED_APPS` do arquivo `settings.py` do seu projeto.
```python
INSTALLED_APPS = [
    ...
    'core',
]
```

# Resumo da criação de um projeto Django:

Abra um terminal na pasta onde você deseja criar o projeto e digite:

    
    mkdir livraria
    poetry -n
    poetry shell
    poetry add django
    django-admin startproject livraria .
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py starapp core    

Now edit the `example/urls.py` module in your project:

```python
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

We'd also like to configure a couple of settings for our API.

Add the following to your `settings.py` module:

```python
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

```

That's it, we're done!

    ./manage.py runserver

You can now open the API in your browser at `http://127.0.0.1:8000/`, and view your new 'users' API. If you use the `Login` control in the top right corner you'll also be able to add, create and delete users from the system.


