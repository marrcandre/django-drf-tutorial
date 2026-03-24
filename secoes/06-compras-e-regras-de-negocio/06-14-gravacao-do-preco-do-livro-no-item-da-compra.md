[Início](../../README.md) | [Seção](README.md) | [Anterior](06-13-validacao-dos-campos-no-serializer.md) | [Próxima](06-15-registro-da-data-da-compra.md)

# 6.14 Gravação do preço do livro no item da compra

## Objetivo da aula

Preservar o preço histórico da compra, gravando o valor do livro no próprio item no momento da criação ou atualização.

## Introdução

Uma compra não pode depender do preço atual do catálogo para continuar fazendo sentido no futuro. Se o valor do livro mudar depois, o histórico da compra precisa continuar fiel ao momento em que ela foi feita.

## Desenvolvimento

### 1. Novo campo em `ItensCompra`

```python
preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
```

### 2. Gravando o preço no `create`

```python
def create(self, validated_data):
    itens = validated_data.pop('itens')
    compra = Compra.objects.create(**validated_data)
    for item in itens:
        item['preco'] = item['livro'].preco
        ItensCompra.objects.create(compra=compra, **item)
    compra.save()
    return compra
```

### 3. Gravando também no `update`

```python
def update(self, compra, validated_data):
    itens = validated_data.pop('itens')
    if itens:
        compra.itens.all().delete()
        for item in itens:
            item['preco'] = item['livro'].preco
            ItensCompra.objects.create(compra=compra, **item)
    compra.save()
    return super().update(compra, validated_data)
```

### 4. Ajustando cálculos

Passe a usar `instance.preco` no total do item e `item.preco * item.quantidade` no total da compra.

## Hora do commit

```text
feat(6.14): implementa gravacao do preco do livro no item
```

## Prática

- Crie uma compra.
- Altere depois o preço do livro.
- Verifique que o histórico da compra anterior permanece inalterado.

## Conclusão

O sistema deixa de recalcular compras antigas com base no preço atual do catálogo, preservando o histórico da compra de forma muito mais correta.

## Próxima aula

- [6.15 Registro da data da compra](06-15-registro-da-data-da-compra.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-13-validacao-dos-campos-no-serializer.md) | [Próxima](06-15-registro-da-data-da-compra.md)