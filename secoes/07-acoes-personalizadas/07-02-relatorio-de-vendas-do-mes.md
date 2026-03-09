[Início](../../README.md) | [Seção](README.md) | [Anterior](07-01-alteracao-do-preco-de-um-livro.md) | [Próxima](07-03-finalizacao-da-compra-com-atualizacao-de-estoque.md)

# 7.2 Relatório de vendas do mês

## Objetivo da aula

Criar uma action de coleção para gerar um resumo mensal de vendas.

## Desenvolvimento

Em `CompraViewSet`, implemente:

```python
@extend_schema(
    request=None,
    responses={200: None},
    description='Gera um relatório de vendas do mês atual.',
    summary='Relatório de vendas do mês',
)
@action(detail=False, methods=['get'])
def relatorio_vendas_mes(self, request):
    agora = timezone.now()
    inicio_mes = agora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    compras = Compra.objects.filter(status=Compra.StatusCompra.FINALIZADO, data__gte=inicio_mes)
    total_vendas = sum(compra.total for compra in compras)
    quantidade_vendas = compras.count()
    return Response(
        {
            'status': 'Relatório de vendas deste mês',
            'total_vendas': total_vendas,
            'quantidade_vendas': quantidade_vendas,
        },
        status=status.HTTP_200_OK,
    )
```

O endpoint resultante é `GET /compras/relatorio_vendas_mes/`.

## Hora do commit

```text
feat(7.2): documenta relatorio de vendas do mes
```

## Prática

- Gere compras finalizadas no mês atual.
- Consulte o endpoint.
- Compare o total reportado com os dados persistidos.

## Conclusão

As actions de coleção permitem expor relatórios e estatísticas sem deformar os endpoints de CRUD.

## Próxima aula

- [7.3 Finalização da compra com atualização de estoque](07-03-finalizacao-da-compra-com-atualizacao-de-estoque.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](07-01-alteracao-do-preco-de-um-livro.md) | [Próxima](07-03-finalizacao-da-compra-com-atualizacao-de-estoque.md)