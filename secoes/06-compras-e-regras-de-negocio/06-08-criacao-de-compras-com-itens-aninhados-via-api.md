[Início](../../README.md) | [Seção](README.md) | [Anterior](06-07-inclusao-do-total-da-compra-na-listagem.md) | [Próxima](06-09-atualizacao-de-compras-e-seus-itens-via-api.md)

# 6.8 Criação de compras com itens aninhados via API

## Objetivo da aula

Permitir a criação de compras com itens aninhados em uma única requisição.

## Introdução

Até aqui, já existe estrutura suficiente para representar compras e itens. O problema é que o DRF não grava automaticamente esse tipo de estrutura aninhada do jeito que gostaríamos. Nesta aula, você vai resolver exatamente esse ponto.

## Desenvolvimento

### 1. Serializers de entrada

```python
class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')


class CompraCreateUpdateSerializer(ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('usuario', 'itens')
```

### 2. Selecionando o serializer na viewset

```python
def get_serializer_class(self):
    if self.action in ('create', 'update', 'partial_update'):
        return CompraCreateUpdateSerializer
    return CompraSerializer
```

### 3. Implementando `create`

```python
def create(self, validated_data):
    itens_data = validated_data.pop('itens')
    compra = Compra.objects.create(**validated_data)
    for item_data in itens_data:
        ItensCompra.objects.create(compra=compra, **item_data)
    compra.save()
    return compra
```

## Hora do commit

```text
feat(6.8): documenta criacao de compras com itens aninhados
```

## Prática

- Envie um `POST` com compra e itens.
- Observe o erro inicial sem `create` customizado.
- Implemente o método e teste novamente.

## Conclusão

Com isso, o fluxo de criação fica muito mais útil para clientes reais da API, que passam a conseguir enviar a compra completa em uma única operação.

## Próxima aula

- [6.9 Atualização de compras e seus itens via API](06-09-atualizacao-de-compras-e-seus-itens-via-api.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-07-inclusao-do-total-da-compra-na-listagem.md) | [Próxima](06-09-atualizacao-de-compras-e-seus-itens-via-api.md)