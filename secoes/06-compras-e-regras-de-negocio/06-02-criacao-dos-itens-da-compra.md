[Início](../../README.md) | [Seção](README.md) | [Anterior](06-01-criacao-da-entidade-compra-integrada-ao-usuario.md) | [Próxima](06-03-uso-de-tabularinline-no-admin-para-itens-da-compra.md)

# 6.2 Criação dos itens da compra

## Objetivo da aula

Modelar a entidade associativa entre compra e livro, permitindo armazenar quantidade por item.

## Introdução

Uma compra pode conter vários livros, e cada um desses livros pode aparecer com uma quantidade diferente. Por isso, em vez de usar um `ManyToManyField` simples, faz mais sentido criar uma estrutura própria para representar cada item da compra.

## Desenvolvimento

### 1. Criando `ItensCompra`

No mesmo arquivo `core/models/compra.py`:

```python
from .livro import Livro


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField(default=1)
```

### 2. Ajustes importantes

- `CASCADE` remove os itens quando a compra é excluída.
- `PROTECT` impede apagar um livro já vinculado a um item.
- `related_name='+'` evita criar acesso reverso desnecessário em `Livro`.

### 3. Exportando a model

Adicione a exportação em `core/models/__init__.py`:

```python
from .compra import Compra, ItensCompra
```

### 4. Finalizando

Execute as migrações, confira a tabela criada e registre `ItensCompra` no Admin.

## Hora do commit

```text
feat(6.2): implementa criacao dos itens da compra
```

## Prática

- Crie a entidade associativa.
- Gere as migrações.
- Verifique a nova tabela no banco e o cadastro no Admin.

## Conclusão

A compra deixa de ser apenas um cabeçalho e passa a representar, de fato, o que o usuário colocou no carrinho, com itens e quantidades reais.

## Próxima aula

- [6.3 Uso de TabularInline no Admin para itens da compra](06-03-uso-de-tabularinline-no-admin-para-itens-da-compra.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-01-criacao-da-entidade-compra-integrada-ao-usuario.md) | [Próxima](06-03-uso-de-tabularinline-no-admin-para-itens-da-compra.md)