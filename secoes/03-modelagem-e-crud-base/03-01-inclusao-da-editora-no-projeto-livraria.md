[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](03-02-criacao-da-api-para-autor.md)

# 3.1 Inclusão da Editora no projeto Livraria

## Objetivo da aula

Reforçar o padrão Model -> Serializer -> ViewSet -> Router -> URL criando, com mais autonomia, a API completa da entidade `Editora`.

## Introdução

Na aula anterior, a API de `Categoria` foi construída passo a passo. Agora a proposta é repetir o mesmo padrão com um pouco mais de autonomia, usando aquela experiência como referência e começando a ganhar confiança no processo.

## Desenvolvimento

### 1. Contexto

Nossa aplicação é uma livraria.

Já temos:

- `Categoria`

Agora vamos criar:

- `Editora`
- depois `Autor`
- por último `Livro`

A `Editora` representa a empresa responsável pela publicação dos livros.

Exemplos:

- Record
- Novatec
- Dark Side
- HarperCollins

Nossa `Editora` terá os seguintes campos:

- `nome`: string de no máximo 100 caracteres, obrigatório;
- `site`: URL do site da editora, opcional.

### 2. O desafio

Crie a API completa da `Editora`, repetindo o mesmo padrão utilizado em `Categoria`.

Você precisa:

1. criar a model `Editora` em `core/models/editora.py`;
2. registrar no `models/__init__.py`;
3. criar e aplicar a migração com `pdm run migrate`;
4. verificar se a tabela foi criada no banco de dados;
5. registrar no `admin.py`;
6. testar se a Editora aparece no painel administrativo;
7. criar algumas editoras para testar a exibição;
8. criar o serializer em `core/serializers/editora.py`;
9. registrar no `serializers/__init__.py`;
10. criar a viewset em `core/views/editora.py`;
11. registrar no `views/__init__.py`;
12. adicionar a rota em `urls.py`;
13. testar a API.

### 3. Implementação esperada

Depois de tentar sozinho, compare com a implementação esperada.

`models/editora.py`

```python
from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome
```

Reflita:

- Por que `site` possui `blank=True` e `null=True`?
- Faz sentido obrigar que toda editora tenha site?

`models/__init__.py`

```python
from .editora import Editora
```

### 4. Migração

Após criar a model:

```bash
pdm run migrate
```

Verifique se a tabela `core_editora` foi criada corretamente.

Se ocorrer erro:

- confira se a importação no `__init__.py` foi feita;
- confira se todos os arquivos foram salvos;
- reinicie o servidor, se necessário.

### 5. Admin, serializer, viewset e rotas

No `admin.py`:

```python
admin.site.register(models.Editora)
```

No `serializers/editora.py`:

```python
from rest_framework.serializers import ModelSerializer
from core.models import Editora


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'
```

No `serializers/__init__.py`:

```python
from .editora import EditoraSerializer
```

Pergunta importante: o que acontece se você esquecer de importar o serializer no `__init__.py`?

No `views/editora.py`:

```python
from rest_framework.viewsets import ModelViewSet
from core.models import Editora
from core.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
```

No `views/__init__.py`:

```python
from .editora import EditoraViewSet
```

Pergunta: por que não precisamos implementar manualmente métodos como `create()` ou `list()`?

No `urls.py`:

```python
from core.views import CategoriaViewSet, EditoraViewSet, UserViewSet

router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
```

Agora teste o endpoint:

```text
http://127.0.0.1:8000/api/editoras/
```

## Hora do commit

Mensagem sugerida na nova convenção:

```text
feat(3.1): cria api para editora
```

## Prática

Teste todos os métodos da API:

- GET
- POST
- PUT
- PATCH
- DELETE

Exercícios de reflexão:

1. É possível criar uma Editora sem informar `site`?
2. O que acontece se você usar PUT sem enviar todos os campos?
3. O PATCH exige todos os campos?
4. Qual código HTTP é retornado ao criar com sucesso?
5. O que acontece ao buscar um ID inexistente?

## Conclusão

Repetir o padrão em uma nova entidade reforça a arquitetura-base do projeto e ajuda a reduzir a dependência de passo a passo detalhado.

## Próxima aula

- [3.2 Criação da API para Autor](03-02-criacao-da-api-para-autor.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](03-02-criacao-da-api-para-autor.md)