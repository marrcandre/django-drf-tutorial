[Início](../../README.md) | [Seção](README.md) | [Anterior](06-05-visualizacao-dos-itens-da-compra-na-listagem.md) | [Próxima](06-07-inclusao-do-total-da-compra-na-listagem.md)

# 6.6 Exibição do total do item na listagem

## Objetivo da aula

Calcular e mostrar o total de cada item da compra no serializer.

## Desenvolvimento

Use `SerializerMethodField` no serializer de itens:

```python
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'total')
        depth = 1
```

Essa abordagem calcula o valor dinamicamente a partir do preço do livro e da quantidade.

## Hora do commit

```text
feat(6.6): documenta total do item na listagem
```

## Prática

- Adicione o campo calculado `total`.
- Compare o retorno antes e depois da mudança.

## Conclusão

Cada item passa a carregar seu subtotal, facilitando inspeção e futura composição do total da compra.

## Próxima aula

- [6.7 Inclusão do total da compra na listagem](06-07-inclusao-do-total-da-compra-na-listagem.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-05-visualizacao-dos-itens-da-compra-na-listagem.md) | [Próxima](06-07-inclusao-do-total-da-compra-na-listagem.md)