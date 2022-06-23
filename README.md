# Django REST framework

# Aula 1

## Preparação

* Abra o navegador de arquivos
* Crie uma pasta chamada `livraria` para o seu projeto
* Certifique-se de que nenhuma pasta no caminho tenha espaços ou acentos.
* Abra a pasta no vscode (repita em voz alta: *"Nunca abra um arquivo, sempre abra a pasta."*).
* Dentro do vscode, abra um terminal (`Control + Shift + '`)
  
Os comandos a seguir serão digitados no terminal que você abriu dentro do **vscode**.

Verifique se o **poetry** está instalado:

    poetry --version

Verifique se o **python** está instalado:

    python --version
ou

    python3 --version

Crie o ambiente virtual usado o **poetry**:

    poetry init


## Algumas extensões necessárias do vscode 
* Python
* SqLite Viewer
* Intellicode
* Prettier
  
----

Acrescente `'core'` na seção `INSTALLED_APPS` do arquivo `settings.py` do seu projeto.
```python
INSTALLED_APPS = [
    ...
    'core',
]
```

# Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

    pip install django
    pip install djangorestframework
    django-admin startproject example .
    ./manage.py migrate
    ./manage.py createsuperuser


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


