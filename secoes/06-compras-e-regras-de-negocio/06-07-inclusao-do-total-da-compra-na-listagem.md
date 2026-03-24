[Início](../../README.md) | [Seção](README.md) | [Anterior](06-06-exibicao-do-total-do-item-na-listagem.md) | [Próxima](06-08-criacao-de-compras-com-itens-aninhados-via-api.md)

# 6.7 Inclusão do total da compra na listagem

## Objetivo da aula

Calcular o total da compra e exibi-lo tanto na API quanto no Admin.

## Introdução

Se cada item já possui um subtotal, faz todo sentido consolidar essa informação no nível da compra. Assim, a API e o Admin passam a oferecer um resumo financeiro mais claro do pedido inteiro.

## Desenvolvimento

### 1. Propriedade `total` na model

```python
@property
def total(self):
    return sum(item.livro.preco * item.quantidade for item in self.itens.all())
```

> Uma propriedade (property) é uma forma elegante de calcular o total da compra sem precisar armazenar esse valor no banco, garantindo que ele esteja sempre atualizado com base nos itens associados.

### 2. Exibindo no serializer

Defina explicitamente os campos do `CompraSerializer`:

```python
fields = ('id', 'usuario', 'status', 'total', 'itens')
```

### 3. Exibindo no Admin

```python
@admin.display(description='Total')
def total_formatado(self, obj):
    return f'R$ {obj.total:.2f}'
```

Use `total_formatado` em `list_display` e `readonly_fields`:

```python
list_display = ('usuario', 'status', 'total_formatado')
readonly_fields = ('total_formatado',)
```

## Hora do commit

```text
feat(6.7): implementa total da compra na listagem
```

## Prática

- Calcule o total na model.
- Exponha o campo na API.
- Mostre o valor formatado no Admin.

## Conclusão

A compra passa a fornecer um resumo financeiro próprio, útil para operação, visualização e evolução futura das regras de negócio.

## Próxima aula

- [6.8 Criação de compras com itens aninhados via API](06-08-criacao-de-compras-com-itens-aninhados-via-api.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-06-exibicao-do-total-do-item-na-listagem.md) | [Próxima](06-08-criacao-de-compras-com-itens-aninhados-via-api.md)