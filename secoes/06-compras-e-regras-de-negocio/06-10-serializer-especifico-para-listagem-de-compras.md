[Início](../../README.md) | [Seção](README.md) | [Anterior](06-09-atualizacao-de-compras-e-seus-itens-via-api.md) | [Próxima](06-11-compra-a-partir-do-usuario-autenticado.md)

# 6.10 Serializer específico para listagem de compras

## Objetivo da aula

Criar serializers enxutos para a listagem de compras, retornando apenas os campos realmente úteis nesse contexto.

## Desenvolvimento

Crie serializers dedicados:

```python
class ItensCompraListSerializer(ModelSerializer):
    livro = CharField(source='livro.titulo', read_only=True)

    class Meta:
        model = ItensCompra
        fields = ('quantidade', 'livro')


class CompraListSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    itens = ItensCompraListSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')
```

Na viewset:

```python
def get_serializer_class(self):
    if self.action == 'list':
        return CompraListSerializer
    if self.action in ('create', 'update', 'partial_update'):
        return CompraCreateUpdateSerializer
    return CompraSerializer
```

## Hora do commit

```text
feat(6.10): documenta serializer de listagem de compras
```

## Prática

- Compare o retorno da listagem antes e depois.
- Garanta que o detalhe continue usando serializer mais completo.

## Conclusão

Listagem e detalhe passam a ter responsabilidades distintas, deixando a API mais clara e econômica.

## Próxima aula

- [6.11 Compra a partir do usuário autenticado](06-11-compra-a-partir-do-usuario-autenticado.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-09-atualizacao-de-compras-e-seus-itens-via-api.md) | [Próxima](06-11-compra-a-partir-do-usuario-autenticado.md)