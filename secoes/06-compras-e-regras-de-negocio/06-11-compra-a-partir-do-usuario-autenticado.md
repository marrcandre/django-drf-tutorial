[Início](../../README.md) | [Seção](README.md) | [Anterior](06-10-serializer-especifico-para-listagem-de-compras.md) | [Próxima](06-12-visualizacao-de-compras-por-perfil-de-usuario.md)

# 6.11 Compra a partir do usuário autenticado

## Objetivo da aula

Parar de receber o usuário no corpo da compra e vincular automaticamente a compra ao usuário autenticado.

## Desenvolvimento

No `CompraCreateUpdateSerializer`, use `HiddenField` com `CurrentUserDefault`:

```python
from rest_framework.serializers import CurrentUserDefault, HiddenField


class CompraCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')
```

Assim, o cliente deixa de informar o campo `usuario` manualmente e a API usa o usuário do token atual.

## Hora do commit

```text
feat(6.11): documenta compra a partir do usuario autenticado
```

## Prática

- Faça um `POST /compras/` autenticado sem o campo `usuario`.
- Confirme que a compra foi criada com o usuário do token.

## Conclusão

A API fica mais segura e mais coerente com o conceito de compra do usuário logado.

## Próxima aula

- [6.12 Visualização de compras por perfil de usuário](06-12-visualizacao-de-compras-por-perfil-de-usuario.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-10-serializer-especifico-para-listagem-de-compras.md) | [Próxima](06-12-visualizacao-de-compras-por-perfil-de-usuario.md)