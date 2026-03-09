[Início](../../README.md) | [Seção](README.md) | [Anterior](08-01-utilizacao-de-filtros-para-listagem-de-recursos.md) | [Próxima](08-03-utilizacao-de-ordenacao-dos-resultados.md)

# 8.2 Utilização de busca textual em campos de texto

## Objetivo da aula

Permitir busca textual em campos como título de livro usando `SearchFilter`.

## Introdução

Filtrar por categoria e editora já ajuda bastante, mas ainda falta um comportamento muito comum em catálogos: pesquisar por texto digitado pelo usuário. Essa etapa aproxima a API de uma experiência de busca mais natural.

## Desenvolvimento

```python
from rest_framework.filters import SearchFilter


class LivroViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['categoria__descricao', 'editora__nome']
    search_fields = ['titulo']
```

Exemplo de uso:

```text
GET /api/livros/?search=python
```

Esse filtro pode ser combinado com os filtros declarativos já configurados.

## Hora do commit

```text
feat(8.2): documenta busca textual
```

## Prática

- Faça buscas por título.
- Combine busca textual com filtros de categoria e editora.

## Conclusão

A API ganha uma forma simples de pesquisa textual, útil para interfaces de catálogo, administração e experiências de busca mais amigáveis.

## Próxima aula

- [8.3 Utilização de ordenação dos resultados](08-03-utilizacao-de-ordenacao-dos-resultados.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](08-01-utilizacao-de-filtros-para-listagem-de-recursos.md) | [Próxima](08-03-utilizacao-de-ordenacao-dos-resultados.md)