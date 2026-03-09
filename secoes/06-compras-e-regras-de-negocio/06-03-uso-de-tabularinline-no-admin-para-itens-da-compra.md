[Início](../../README.md) | [Seção](README.md) | [Anterior](06-02-criacao-dos-itens-da-compra.md) | [Próxima](06-04-endpoint-para-a-listagem-basica-de-compras.md)

# 6.3 Uso de TabularInline no Admin para itens da compra

## Objetivo da aula

Melhorar o fluxo de edição de compras no Admin, exibindo os itens diretamente no formulário da compra.

## Introdução

Quando compra e itens são editados separadamente, o fluxo fica artificial. O `TabularInline` resolve isso aproximando a interface da estrutura real do domínio.

## Desenvolvimento

No `admin.py`, configure:

```python
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    extra = 1


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status')
    search_fields = ('usuario', 'status')
    list_filter = ('usuario', 'status')
    ordering = ('usuario', 'status')
    list_per_page = 10
    inlines = [ItensCompraInline]
```

Você também pode comparar esse comportamento com `StackedInline`.

## Hora do commit

```text
feat(6.3): documenta tabularinline para itens da compra
```

## Prática

- Edite uma compra no Admin.
- Adicione itens diretamente no formulário principal.
- Compare com a experiência anterior sem inline.

## Conclusão

O Admin passa a refletir melhor a relação entre compra e itens, reduzindo atrito na operação manual.

## Próxima aula

- [6.4 Endpoint para a listagem básica de compras](06-04-endpoint-para-a-listagem-basica-de-compras.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-02-criacao-dos-itens-da-compra.md) | [Próxima](06-04-endpoint-para-a-listagem-basica-de-compras.md)