[Início](../../README.md) | [Seção](README.md) | [Anterior](07-03-finalizacao-da-compra-com-atualizacao-de-estoque.md) | [Próxima](07-05-ajuste-de-estoque-de-um-livro.md)

# 7.4 Livros com mais de 10 cópias vendidas

## Objetivo da aula

Criar uma action de coleção que lista livros com maior volume de vendas usando agregação no banco.

## Introdução

Nem toda rota da API precisa servir apenas para cadastro e edição. Em muitos projetos, também surgem consultas analíticas, relatórios rápidos e visões resumidas para apoiar decisões.

## Desenvolvimento

### 1. Ajustando o relacionamento reverso

```python
livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='itens_compra')
```

### 2. Serializer de resposta

```python
class LivroMaisVendidoSerializer(ModelSerializer):
    total_vendidos = IntegerField()

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'total_vendidos']
```

### 3. Action no viewset

```python
@extend_schema(
    summary='Lista os livros mais vendidos',
    description='Retorna os livros que venderam mais de 10 unidades.',
    responses={200: LivroMaisVendidoSerializer(many=True)},
)
@action(detail=False, methods=['get'])
def mais_vendidos(self, request):
    livros = Livro.objects.annotate(
        total_vendidos=Sum(
            'itens_compra__quantidade',
            filter=Q(itens_compra__compra__status=Compra.StatusCompra.FINALIZADO),
        )
    ).filter(total_vendidos__gt=10).order_by('-total_vendidos')
    serializer = LivroMaisVendidoSerializer(livros, many=True)
    if not serializer.data:
        return Response({'detail': 'Nenhum livro excedeu 10 vendas.'}, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_200_OK)
```

## Hora do commit

```text
feat(7.4): documenta livros mais vendidos
```

## Prática

- Gere compras finalizadas com volume suficiente.
- Consulte o endpoint.
- Valide o caso sem resultados.

## Conclusão

A API passa a oferecer uma consulta analítica baseada em agregação e relacionamento reverso, abrindo espaço para relatórios cada vez mais úteis.

## Próxima aula

- [7.5 Ajuste de estoque de um livro](07-05-ajuste-de-estoque-de-um-livro.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](07-03-finalizacao-da-compra-com-atualizacao-de-estoque.md) | [Próxima](07-05-ajuste-de-estoque-de-um-livro.md)