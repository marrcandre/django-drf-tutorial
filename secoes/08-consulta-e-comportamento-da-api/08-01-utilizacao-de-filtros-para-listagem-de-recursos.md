[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](08-02-utilizacao-de-busca-textual-em-campos-de-texto.md)

# 8.1 Utilização de filtros para listagem de recursos

## Objetivo da aula

Habilitar filtros declarativos na API para consultas por campos específicos e relacionamentos.

## Introdução

Até aqui, a API já consegue cadastrar e devolver muita coisa. O próximo passo é torná-la mais agradável de usar no dia a dia, permitindo consultas mais úteis e menos genéricas.

## Desenvolvimento

No `LivroViewSet`:

```python
from django_filters.rest_framework import DjangoFilterBackend


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria__descricao', 'editora__nome']
```

Com isso, a API aceita parâmetros como:

- `GET /api/livros/?categoria__descricao=Python`
- `GET /api/livros/?editora__nome=Novatec`
- `GET /api/livros/?categoria__descricao=Python&editora__nome=Novatec`

## Hora do commit

```text
feat(8.1): implementa filtros para listagem de recursos
```

## Prática

- Adicione filtros em `LivroViewSet`.
- Replique o mesmo padrão em outros viewsets do projeto.

## Conclusão

Os filtros tornam a API mais útil para consumo real sem exigir endpoints específicos para cada tipo de consulta.

## Próxima aula

- [8.2 Utilização de busca textual em campos de texto](08-02-utilizacao-de-busca-textual-em-campos-de-texto.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](08-02-utilizacao-de-busca-textual-em-campos-de-texto.md)