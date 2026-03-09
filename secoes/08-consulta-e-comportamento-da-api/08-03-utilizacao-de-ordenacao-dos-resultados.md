[Início](../../README.md) | [Seção](README.md) | [Anterior](08-02-utilizacao-de-busca-textual-em-campos-de-texto.md) | [Próxima](08-04-limite-de-um-carrinho-por-usuario-e-persistencia-do-total.md)

# 8.3 Utilização de ordenação dos resultados

## Objetivo da aula

Permitir ordenação controlada dos resultados da API e combinar esse recurso com filtros e busca textual.

## Desenvolvimento

No `LivroViewSet`:

```python
from rest_framework.filters import OrderingFilter, SearchFilter


class LivroViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categoria__descricao', 'editora__nome']
    search_fields = ['titulo']
    ordering_fields = ['titulo', 'preco']
    ordering = ['titulo']
```

No `CompraViewSet`, adicione ordenação e filtros por data:

```python
filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
filterset_fields = ['usuario__email', 'status', 'data']
search_fields = ['usuario__email']
ordering_fields = ['usuario__email', 'status', 'data']
ordering = ['-data']
```

Exemplos:

- `GET /api/livros/?ordering=titulo`
- `GET /api/livros/?ordering=-titulo`
- `GET /api/livros/?ordering=preco&search=python`
- `GET /api/compras/?ordering=-data`

## Hora do commit

```text
feat(8.3): documenta ordenacao dos resultados
```

## Prática

- Teste ordenação crescente e decrescente.
- Combine ordenação com filtros e busca.
- Replique a abordagem nos demais recursos do projeto.

## Conclusão

A API passa a oferecer uma camada de consulta muito mais flexível sem aumentar a quantidade de rotas.

## Próxima aula

- [8.4 Limite de um carrinho por usuário e persistência do total](08-04-limite-de-um-carrinho-por-usuario-e-persistencia-do-total.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](08-02-utilizacao-de-busca-textual-em-campos-de-texto.md) | [Próxima](08-04-limite-de-um-carrinho-por-usuario-e-persistencia-do-total.md)