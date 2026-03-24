[Início](../../README.md) | [Seção](README.md) | [Anterior](06-11-compra-a-partir-do-usuario-autenticado.md) | [Próxima](06-13-validacao-dos-campos-no-serializer.md)

# 6.12 Visualização de compras por perfil de usuário

## Objetivo da aula

Restringir a visualização de compras para que usuários comuns vejam apenas seus próprios registros, enquanto administradores veem todos.

## Introdução

Depois de autenticar o usuário e associar a compra ao dono correto, também é preciso controlar o que cada perfil pode enxergar. Essa etapa é importante para evitar exposição indevida de dados entre clientes diferentes.

## Desenvolvimento

Sobrescreva `get_queryset` em `CompraViewSet`:

```python
def get_queryset(self):
    usuario = self.request.user
    if usuario.is_superuser:
        return Compra.objects.all()
    if usuario.groups.filter(name='administradores'):
        return Compra.objects.all()
    return Compra.objects.filter(usuario=usuario)
```

Essa abordagem usa o próprio perfil do usuário para decidir o conjunto de compras visível.

## Hora do commit

```text
feat(6.12): implementa visualizacao de compras por perfil
```

## Prática

- Teste com um usuário comum.
- Teste com um administrador.
- Compare o retorno em `/compras/` para os dois cenários.

## Conclusão

O endpoint deixa de expor dados indevidos entre clientes diferentes e passa a respeitar melhor o perfil autenticado de cada usuário.

## Próxima aula

- [6.13 Validação dos campos no serializer](06-13-validacao-dos-campos-no-serializer.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-11-compra-a-partir-do-usuario-autenticado.md) | [Próxima](06-13-validacao-dos-campos-no-serializer.md)