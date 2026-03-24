[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](07-02-relatorio-de-vendas-do-mes.md)

# 7.1 Alteração do preço de um livro

## Objetivo da aula

Criar uma action em um recurso específico para alterar o preço de um livro com validação dedicada.

## Introdução

As ações padrão do DRF cobrem muito bem o CRUD, mas nem todo comportamento interessante de uma aplicação cabe nesses métodos. Nesta aula, a API começa a ganhar endpoints mais expressivos, voltados para necessidades específicas do domínio.

## Desenvolvimento

### 1. Serializer da action

```python
class LivroAlterarPrecoSerializer(Serializer):
    preco = DecimalField(max_digits=7, decimal_places=2)

    def validate_preco(self, preco):
        if preco <= 0:
            raise ValidationError('O preço deve ser um valor positivo.')
        return preco
```

### 2. Action no `LivroViewSet`

```python
@extend_schema(
    request=LivroAlterarPrecoSerializer,
    responses={200: None},
    description='Altera o preço de um livro específico.',
    summary='Alterar preço do livro',
)
@action(detail=True, methods=['patch'])
def alterar_preco(self, request, pk=None):
    livro = self.get_object()
    serializer = LivroAlterarPrecoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    livro.preco = serializer.validated_data['preco']
    livro.save()
    return Response({'detail': f'Preço do livro "{livro.titulo}" atualizado para {livro.preco}.'}, status=status.HTTP_200_OK)
```

### 3. Teste no Swagger

Use o endpoint `PATCH /livros/{id}/alterar_preco/` enviando um novo preço no corpo.

## Hora do commit

```text
feat(7.1): implementa alteracao do preco de um livro
```

## Prática

- Crie o serializer específico.
- Exponha a action no viewset.
- Teste valores válidos e inválidos.

## Conclusão

O projeto passa a ter um primeiro exemplo claro de action aplicada a um recurso individual, o que ajuda bastante a entender como o DRF pode ir além do CRUD básico.

## Próxima aula

- [7.2 Relatório de vendas do mês](07-02-relatorio-de-vendas-do-mes.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](07-02-relatorio-de-vendas-do-mes.md)