[Início](../../README.md) | [Seção](README.md) | [Anterior](../05-autenticacao-e-usuarios/README.md) | [Próxima](06-02-criacao-dos-itens-da-compra.md)

# 6.1 Criação da entidade compra integrada ao usuário

## Objetivo da aula

Criar a model `Compra`, associá-la ao usuário do sistema e disponibilizá-la no Admin.

## Introdução

O fluxo de compras começa com uma entidade que representa a transação principal. Ela precisa saber quem realizou a compra e em que estágio do processo essa compra está.

## Desenvolvimento

### 1. Criando a model

No arquivo `core/models/compra.py`, crie a model `Compra` com status baseados em `IntegerChoices`:

```python
from django.db import models

from .user import User


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        FINALIZADO = 2, 'Finalizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
```

### 2. Registrando a model

Exporte a model em `core/models/__init__.py`:

```python
from .compra import Compra
```

### 3. Incluindo no Admin

```python
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status')
    ordering = ('usuario', 'status')
    list_per_page = 10
```

### 4. Aplicando migrações

Crie e aplique as migrações. Depois, valide no Admin se a nova entidade já pode ser cadastrada.

## Hora do commit

```text
feat(6.1): documenta entidade compra integrada ao usuario
```

## Prática

- Crie a model `Compra`.
- Execute as migrações.
- Cadastre compras pelo Admin para validar o relacionamento com o usuário.

## Conclusão

A aplicação passa a ter a estrutura base necessária para modelar um carrinho ou pedido de compra.

## Próxima aula

- [6.2 Criação dos itens da compra](06-02-criacao-dos-itens-da-compra.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](../05-autenticacao-e-usuarios/README.md) | [Próxima](06-02-criacao-dos-itens-da-compra.md)