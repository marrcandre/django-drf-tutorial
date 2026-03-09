[Início](../../README.md) | [Seção](README.md) | [Anterior](06-14-gravacao-do-preco-do-livro-no-item-da-compra.md) | [Próxima](06-16-inclusao-do-tipo-de-pagamento-na-compra.md)

# 6.15 Registro da data da compra

## Objetivo da aula

Armazenar automaticamente a data de criação da compra e expor essa informação na API e no Admin.

## Desenvolvimento

### 1. Campo `data`

```python
data = models.DateTimeField(auto_now_add=True)
```

### 2. Exibindo no serializer

```python
from rest_framework.serializers import DateTimeField


class CompraSerializer(ModelSerializer):
    data = DateTimeField(read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'data', 'itens')
```

### 3. Exibindo no Admin

Inclua `data` em `list_display`, `ordering`, `list_filter` e `readonly_fields`.

### 4. Exercício sugerido

Como evolução, vale renomear `data` para `data_criacao` e adicionar `data_atualizacao` com `auto_now=True`.

## Hora do commit

```text
feat(6.15): documenta registro da data da compra
```

## Prática

- Faça a migração com o novo campo.
- Teste a criação de compras e confira o timestamp gerado.
- Exponha a data na resposta da API e no Admin.

## Conclusão

A compra passa a ter rastreabilidade temporal, algo importante para auditoria e relatórios.

## Próxima aula

- [6.16 Inclusão do tipo de pagamento na compra](06-16-inclusao-do-tipo-de-pagamento-na-compra.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-14-gravacao-do-preco-do-livro-no-item-da-compra.md) | [Próxima](06-16-inclusao-do-tipo-de-pagamento-na-compra.md)