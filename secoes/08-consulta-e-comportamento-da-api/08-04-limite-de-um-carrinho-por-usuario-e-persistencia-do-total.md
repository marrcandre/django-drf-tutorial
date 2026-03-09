[Início](../../README.md) | [Seção](README.md) | [Anterior](08-03-utilizacao-de-ordenacao-dos-resultados.md) | [Próxima](../09-publicacao-e-deploy/README.md)

# 8.4 Limite de um carrinho por usuário e persistência do total

## Objetivo da aula

Restringir cada usuário a um carrinho ativo e armazenar o total da compra no banco para melhorar performance e consistência.

## Introdução

Quando o projeto começa a amadurecer, alguns comportamentos precisam deixar de ser apenas funcionais e passar a ser mais consistentes. É o caso do carrinho único por usuário e do total persistido para evitar recálculos desnecessários.

## Desenvolvimento

### 1. Um carrinho por usuário

No serializer de criação e atualização de compras, use `get_or_create` para reaproveitar o carrinho aberto do usuário:

```python
def create(self, validated_data):
    itens = validated_data.pop('itens')
    usuario = validated_data['usuario']
    compra, criada = Compra.objects.get_or_create(
        usuario=usuario,
        status=Compra.StatusCompra.CARRINHO,
        defaults=validated_data,
    )
    for item in itens:
        item_existente = compra.itens.filter(livro=item['livro']).first()
        if item_existente:
            item_existente.quantidade += item['quantidade']
            item_existente.preco = item['livro'].preco
            item_existente.save()
        else:
            item['preco'] = item['livro'].preco
            ItensCompra.objects.create(compra=compra, **item)
    compra.save()
    return compra
```

### 2. Persistindo o total no modelo

Adicione o campo:

```python
total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
```

Depois, sobrescreva `save`:

```python
def save(self, *args, **kwargs):
    if self.pk:
        self.total = sum(item.preco * item.quantidade for item in self.itens.all())
    super().save(*args, **kwargs)
```

Remova a property antiga `total`, gere migrações e recalcule os registros já existentes pelo shell.

## Hora do commit

```text
feat(8.4): documenta carrinho unico e persistencia do total
```

## Prática

- Adicione o mesmo livro duas vezes ao carrinho e observe o incremento de quantidade.
- Garanta que o usuário não tenha múltiplos carrinhos em aberto.
- Salve compras existentes para recalcular o campo `total` persistido.

## Conclusão

O comportamento do carrinho fica mais previsível e o total da compra passa a estar pronto para filtros, ordenações e relatórios sem recálculo contínuo.

## Próxima aula

- [Seção 9. Publicação e deploy](../09-publicacao-e-deploy/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](08-03-utilizacao-de-ordenacao-dos-resultados.md) | [Próxima](../09-publicacao-e-deploy/README.md)