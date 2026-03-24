[Início](../../README.md) | [Seção](README.md) | [Anterior](06-04-endpoint-para-a-listagem-basica-de-compras.md) | [Próxima](06-06-exibicao-do-total-do-item-na-listagem.md)

# 6.5 Visualização dos itens da compra na listagem

## Objetivo da aula

Exibir os itens da compra no endpoint de listagem de compras.

## Introdução

Listar apenas a compra, sem mostrar seus itens, ainda deixa a resposta muito pobre para quem consome a API. Nesta etapa, a ideia é começar a transformar essa listagem em algo realmente informativo.

## Desenvolvimento

Crie um serializer para `ItensCompra`, em `core/serializers/compra.py`:

```python
class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')
        depth = 1
```

> O parâmetro `depth = 1` é uma forma rápida de incluir os dados relacionados do livro, como título e preço, sem precisar criar um serializer específico para isso.

Depois, aninhe esse serializer em `CompraSerializer`:

```python
itens = ItensCompraSerializer(many=True, read_only=True)
```

Com isso, a listagem de compras passa a retornar também os livros associados e as respectivas quantidades.

> O parâmetro `many=True` indica que `itens` é uma lista de objetos, e `read_only=True` garante que esses dados sejam apenas para leitura, evitando problemas de escrita complexa.

## Hora do commit

```text
feat(6.5): implementa itens da compra na listagem
```

## Prática

- Adicione o serializer dos itens.
- Teste o endpoint de compras.
- Ajuste `depth` e compare o nível de detalhamento retornado.

## Conclusão

A compra deixa de mostrar apenas o cabeçalho e passa a expor a composição dos itens, o que torna a resposta muito mais útil para leitura e integração.

## Próxima aula

- [6.6 Exibição do total do item na listagem](06-06-exibicao-do-total-do-item-na-listagem.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-04-endpoint-para-a-listagem-basica-de-compras.md) | [Próxima](06-06-exibicao-do-total-do-item-na-listagem.md)