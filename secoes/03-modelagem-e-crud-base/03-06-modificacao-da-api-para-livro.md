[Início](../../README.md) | [Seção](README.md) | [Anterior](03-05-inclusao-do-relacionamento-n-para-n-no-modelo-do-livro.md) | [Próxima](../04-dados-arquivos-e-administracao/README.md)

# 3.6 Modificação da API para Livro

## Objetivo da aula

Melhorar a apresentação da API de `Livro`, criando serializadores diferentes para listagem, recuperação e operações de escrita.

## Introdução

Quando o recurso `Livro` começa a ter relacionamentos, a resposta padrão da API deixa de ser suficiente. Agora precisamos escolher melhor como os dados serão exibidos em cada contexto.

## Desenvolvimento

### 1. Observando o problema

Acesse a API do Livro e veja como está a apresentação dos autores:

```text
http://127.0.0.1:8000/api/livros/
```

No `Livro`, aparecem apenas os campos `id` da categoria, da editora e dos autores, e não as descrições.

### 2. Criação de múltiplos serializadores

Uma forma inicial de mostrar as informações detalhadas seria:

```python
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1
```

Isso resolve a listagem, mas gera problema na criação e alteração.

Para resolver, vamos criar dois serializadores:

```python
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class LivroListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1
```

Inclua o serializador `LivroListRetrieveSerializer` no arquivo `serializers/__init__.py`:

```python
from .livro import LivroListRetrieveSerializer, LivroSerializer
```

Na viewset, escolha o serializer conforme a operação:

```python
from core.serializers import LivroListRetrieveSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in {'list', 'retrieve'}:
            return LivroListRetrieveSerializer
        return LivroSerializer
```

### 3. Criação de um serializador para a listagem de livros

Também podemos criar um serializador específico para a listagem de livros, exibindo apenas `id`, `titulo` e `preco`.

```python
from core.serializers import (
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)


class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco')


class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1
```

Atualize a viewset:

```python
def get_serializer_class(self):
    if self.action == 'list':
        return LivroListSerializer
    elif self.action == 'retrieve':
        return LivroRetrieveSerializer
    return LivroSerializer
```

E atualize o arquivo `serializers/__init__.py`:

```python
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
```

## Hora do commit

Sugestão de mensagem:

```text
feat(3.6): cria multiplos serializadores para livro
```

## Prática

- Teste a listagem de livros.
- Teste a recuperação de um único livro.
- Compare a diferença entre os serializadores usados em cada caso.

## Conclusão

Você passou a controlar melhor a forma como a API expõe os dados, separando com clareza leitura detalhada, leitura resumida e escrita.

## Próxima aula

- [Seção 4. Dados, arquivos e administração](../04-dados-arquivos-e-administracao/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](03-05-inclusao-do-relacionamento-n-para-n-no-modelo-do-livro.md) | [Próxima](../04-dados-arquivos-e-administracao/README.md)