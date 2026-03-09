[Início](../../README.md) | [Seção](README.md) | [Anterior](07-04-livros-com-mais-de-10-copias-vendidas.md) | [Próxima](../08-consulta-e-comportamento-da-api/README.md)

# 7.5 Ajuste de estoque de um livro

## Objetivo da aula

Criar uma action para aumentar ou diminuir estoque com validação contra valores negativos.

## Desenvolvimento

### 1. Serializer da action

```python
class LivroAjustarEstoqueSerializer(Serializer):
    quantidade = serializers.IntegerField()

    def validate_quantidade(self, value):
        livro = self.context.get('livro')
        if livro:
            nova_quantidade = livro.quantidade + value
            if nova_quantidade < 0:
                raise ValidationError('A quantidade em estoque não pode ser negativa.')
        return value
```

### 2. Action no viewset

```python
@extend_schema(
    summary='Ajusta o estoque de um livro',
    description='Aumenta ou diminui o estoque; impede resultado negativo.',
    request=LivroAjustarEstoqueSerializer,
    responses={200: OpenApiResponse(response=None, description='Estoque ajustado com sucesso.')},
)
@action(detail=True, methods=['post'])
def ajustar_estoque(self, request, pk=None):
    livro = self.get_object()
    serializer = LivroAjustarEstoqueSerializer(data=request.data, context={'livro': livro})
    serializer.is_valid(raise_exception=True)
    quantidade_ajuste = serializer.validated_data['quantidade']
    livro.quantidade += quantidade_ajuste
    livro.save()
    return Response({'status': 'Quantidade ajustada com sucesso', 'novo_estoque': livro.quantidade}, status=status.HTTP_200_OK)
```

## Hora do commit

```text
feat(7.5): documenta ajuste de estoque de livro
```

## Prática

- Teste incrementos e decrementos.
- Tente gerar estoque negativo.
- Valide a documentação no Swagger.

## Conclusão

A action amplia o controle operacional sobre o catálogo sem misturar esse comportamento às rotas padrão de atualização.

## Próxima aula

- [Seção 8. Consulta e comportamento da API](../08-consulta-e-comportamento-da-api/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](07-04-livros-com-mais-de-10-copias-vendidas.md) | [Próxima](../08-consulta-e-comportamento-da-api/README.md)