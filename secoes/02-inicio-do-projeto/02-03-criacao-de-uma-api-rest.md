[Início](../../README.md) | [Seção](README.md) | [Anterior](02-02-criacao-de-uma-aplicacao.md) | [Próxima](02-04-conectando-a-api-ao-frontend-com-vue-3.md)

# 2.3 Criação de uma API REST

## Objetivo da aula

Criar a primeira API REST do projeto, para o recurso `Categoria`, usando Django Rest Framework.

## Introdução

Em vez de apenas consumir uma API, agora vamos criar a nossa própria API para o projeto `livraria`.

Ao final desta aula, você terá uma API completa para `Categoria`, capaz de criar, listar, buscar, atualizar e deletar registros.

## Desenvolvimento

### 1. O que é uma API REST

Uma API é uma forma de comunicação entre sistemas.

Por exemplo:

- um front-end em Vue;
- um aplicativo mobile;
- outro sistema qualquer.

Todos eles podem conversar com o backend através de requisições HTTP.

REST é um jeito organizado de construir APIs:

- cada tipo de dado é um recurso;
- cada recurso tem uma URL;
- usamos métodos HTTP como `GET`, `POST`, `PUT`, `PATCH` e `DELETE`.

### 2. Como uma API funciona no Django Rest Framework

A estrutura básica é esta:

```text
Model -> Serializer -> ViewSet -> Router -> URL
```

- O Model representa os dados no banco.
- O Serializer transforma dados em JSON e JSON em dados.
- O ViewSet implementa as ações da API.
- O Router cria as rotas automaticamente.
- A URL é o endereço acessado no navegador.

### 3. DRF já está instalado

O Django Rest Framework já está instalado no projeto:

- está listado no `pyproject.toml`;
- está no `requirements.txt`;
- já está configurado no `INSTALLED_APPS`.

### 4. Criando o serializer

Crie o arquivo `core/serializers/categoria.py`:

```python
from rest_framework.serializers import ModelSerializer

from core.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
```

No arquivo `core/serializers/__init__.py`, adicione:

```python
from .categoria import CategoriaSerializer
```

### 5. Criando a view

Crie o arquivo `core/views/categoria.py`:

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
```

No arquivo `core/views/__init__.py`, adicione:

```python
from .categoria import CategoriaViewSet
```

### 6. Criando as rotas

No arquivo `app/urls.py`, adicione:

```python
from core.views import CategoriaViewSet, UserViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'users', UserViewSet, basename='users')
```

Isso gerará rotas como:

- `/api/categorias/`
- `/api/categorias/{id}/`

### 7. Testando a API

Inicie o servidor e acesse:

```text
http://127.0.0.1:8000/api/
```

Depois teste:

- `http://127.0.0.1:8000/api/categorias/`
- `http://127.0.0.1:8000/api/categorias/1/`

### 8. Métodos HTTP e códigos de status

A API usa métodos HTTP para manipular dados:

- `GET` para buscar dados;
- `POST` para criar;
- `PUT` para atualizar completamente;
- `PATCH` para atualizar parcialmente;
- `DELETE` para remover.

Alguns códigos de status importantes:

- `200 OK`;
- `201 Created`;
- `204 No Content`;
- `400 Bad Request`;
- `404 Not Found`.

### 9. Ferramentas de teste e Swagger

Além do navegador, você pode usar:

- Thunder Client;
- RapidAPI;
- Insomnia;
- Postman.

O Swagger pode ser acessado em:

```text
http://127.0.0.1:8000/api/swagger/
```

## Hora do commit

Mensagem sugerida na nova convenção:

```text
feat(2.3): cria api rest para categoria
```

## Prática

- Crie algumas categorias.
- Liste todas.
- Atualize usando PUT.
- Atualize usando PATCH.
- Delete uma categoria.
- Crie outra.
- Liste novamente.

## Conclusão

Agora você já criou a primeira API REST do projeto e entende o fluxo básico do DRF de ponta a ponta.

## Próxima aula

- [2.4 Conectando a API ao frontend com Vue 3](02-04-conectando-a-api-ao-frontend-com-vue-3.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](02-02-criacao-de-uma-aplicacao.md) | [Próxima](02-04-conectando-a-api-ao-frontend-com-vue-3.md)