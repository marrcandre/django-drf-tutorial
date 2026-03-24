[Início](../../README.md) | [Seção](README.md) | [Anterior](06-15-registro-da-data-da-compra.md) | [Próxima](../07-acoes-personalizadas/README.md)

# 6.16 Inclusão do tipo de pagamento na compra

## Objetivo da aula

Registrar a forma de pagamento da compra usando `IntegerChoices` e exibir o valor legível na API.

## Introdução

Uma compra não envolve apenas itens e valores. A forma de pagamento também é um dado importante, tanto para operação quanto para análises futuras sobre o comportamento dos usuários.

## Desenvolvimento

### 1. Campo `tipo_pagamento`

```python
class TipoPagamento(models.IntegerChoices):
    CARTAO_CREDITO = 1, 'Cartão de Crédito'
    CARTAO_DEBITO = 2, 'Cartão de Débito'
    PIX = 3, 'PIX'
    BOLETO = 4, 'Boleto'
    TRANSFERENCIA_BANCARIA = 5, 'Transferência Bancária'
    DINHEIRO = 6, 'Dinheiro'
    OUTRO = 7, 'Outro'


tipo_pagamento = models.IntegerField(
    choices=TipoPagamento.choices,
    default=TipoPagamento.CARTAO_CREDITO,
)
```

### 2. Exibindo na API

```python
tipo_pagamento = CharField(source='get_tipo_pagamento_display', read_only=True)
```

Atualize também os campos do serializer:

```python
fields = ('id', 'usuario', 'status', 'total', 'data', 'tipo_pagamento', 'itens')
```

### 3. Validando no shell e na API

Depois da migração, crie compras e consulte tanto o valor numérico salvo quanto o valor legível retornado pelo método `get_tipo_pagamento_display`.

## Hora do commit

```text
feat(6.16): implementa tipo de pagamento na compra
```

## Prática

- Adicione um novo tipo de pagamento, como cheque.
- Gere migração.
- Crie uma compra com esse valor e valide a resposta da API.

## Conclusão

O domínio de compras fica mais completo ao incluir a forma de pagamento como dado estruturado e pronto para consultas e estatísticas futuras.

## Próxima aula

- [Seção 7. Ações personalizadas](../07-acoes-personalizadas/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-15-registro-da-data-da-compra.md) | [Próxima](../07-acoes-personalizadas/README.md)