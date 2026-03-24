[Início](../../README.md) | [Seção](README.md) | [Anterior](07-02-relatorio-de-vendas-do-mes.md) | [Próxima](07-04-livros-com-mais-de-10-copias-vendidas.md)

# 7.3 Finalização da compra com atualização de estoque

## Objetivo da aula

Criar uma action que finaliza a compra, valida estoque e atualiza múltiplos registros com segurança transacional.

## Introdução

Até aqui, a compra ainda podia existir sem fechar de fato o processo de venda. Nesta aula, você transforma esse fluxo em uma operação mais realista, com validação de estoque e alteração consistente dos dados envolvidos.

## Desenvolvimento

```python
@extend_schema(
    request=None,
    responses={200: None, 400: None},
    description='Finaliza a compra, atualizando o estoque dos livros.',
    summary='Finalizar compra',
)
@action(detail=True, methods=['post'])
def finalizar(self, request, pk=None):
    compra = self.get_object()
    if compra.status == Compra.StatusCompra.FINALIZADO:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'status': 'Compra já finalizada'})
    with transaction.atomic():
        for item in compra.itens.all():
            if item.quantidade > item.livro.quantidade:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'status': 'Quantidade insuficiente',
                        'livro': item.livro.titulo,
                        'quantidade_disponivel': item.livro.quantidade,
                    },
                )
            item.livro.quantidade -= item.quantidade
            item.livro.save()
        compra.status = Compra.StatusCompra.FINALIZADO
        compra.save()
    return Response(status=status.HTTP_200_OK, data={'status': 'Compra finalizada'})
```

## Hora do commit

```text
feat(7.3): implementa finalizacao da compra com estoque
```

## Prática

- Finalize uma compra válida.
- Tente finalizar uma compra já finalizada.
- Tente finalizar com estoque insuficiente.

## Conclusão

A action concentra uma regra de negócio mais próxima do mundo real e mostra por que actions são úteis para fluxos que vão além do CRUD tradicional.

## Próxima aula

- [7.4 Livros com mais de 10 cópias vendidas](07-04-livros-com-mais-de-10-copias-vendidas.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](07-02-relatorio-de-vendas-do-mes.md) | [Próxima](07-04-livros-com-mais-de-10-copias-vendidas.md)