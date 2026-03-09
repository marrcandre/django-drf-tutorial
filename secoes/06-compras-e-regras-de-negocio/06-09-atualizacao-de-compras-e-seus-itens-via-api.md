[Início](../../README.md) | [Seção](README.md) | [Anterior](06-08-criacao-de-compras-com-itens-aninhados-via-api.md) | [Próxima](06-10-serializer-especifico-para-listagem-de-compras.md)

# 6.9 Atualização de compras e seus itens via API

## Objetivo da aula

Permitir a atualização de compras com itens aninhados, tratando explicitamente o método `update`.

## Desenvolvimento

Sem sobrescrever `update`, o DRF retorna erro ao tentar gravar campos aninhados. A solução é remover os itens antigos e recriá-los a partir do payload recebido:

```python
def update(self, compra, validated_data):
    itens_data = validated_data.pop('itens', [])
    if itens_data:
        compra.itens.all().delete()
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
    return super().update(compra, validated_data)
```

Depois disso, teste operações `PUT` e `PATCH` variando usuário, livro e quantidade.

## Hora do commit

```text
feat(6.9): documenta atualizacao de compras com itens
```

## Prática

- Atualize uma compra completa com `PUT`.
- Faça testes parciais com `PATCH`.
- Verifique o comportamento dos itens antigos ao reenviar a lista.

## Conclusão

A atualização de estruturas aninhadas exige regra explícita. O serializer deixa esse fluxo sob controle da aplicação.

## Próxima aula

- [6.10 Serializer específico para listagem de compras](06-10-serializer-especifico-para-listagem-de-compras.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-08-criacao-de-compras-com-itens-aninhados-via-api.md) | [Próxima](06-10-serializer-especifico-para-listagem-de-compras.md)