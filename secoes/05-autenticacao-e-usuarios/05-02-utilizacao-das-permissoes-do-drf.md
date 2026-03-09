[Início](../../README.md) | [Seção](README.md) | [Anterior](05-01-autenticacao-e-autorizacao.md) | [Próxima](05-03-autenticacao-com-o-simplejwt.md)

# 5.2 Utilização das permissões do DRF

## Objetivo da aula

Aplicar permissões no DRF tanto em uma viewset específica quanto de forma global no projeto.

## Introdução

Autenticação identifica o usuário. Permissão determina o nível de acesso que esse usuário terá sobre a API.

No DRF, isso pode ser feito por view, globalmente no `settings.py` ou com classes de permissão ligadas às permissões de modelo do Django.

## Desenvolvimento

### 1. Exemplo de permissão na viewset

No arquivo `views/categoria.py`, importe:

```python
from rest_framework.permissions import IsAuthenticated
```

Em seguida, configure a `CategoriaViewSet`:

```python
permission_classes = [IsAuthenticated]
```

Teste o comportamento com e sem sessão autenticada no Admin. Sem autenticação, a API deve responder com erro de credenciais ausentes.

### 2. Exemplo global no `settings.py`

Para aplicar a mesma regra ao projeto inteiro, remova a alteração anterior da viewset e configure:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

Com isso, os endpoints passam a exigir autenticação por padrão.

### 3. Usando `DjangoModelPermissionsOrAnonReadOnly`

No projeto reorganizado, a abordagem recomendada é usar as permissões já gerenciadas pelo Django:

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly', ),
    ...
}
```

Esse modo funciona assim:

- `POST` exige permissão `add`;
- `PUT` e `PATCH` exigem permissão `change`;
- `DELETE` exige permissão `delete`;
- usuários não autenticados ficam com acesso somente leitura.

## Hora do commit

Mensagem sugerida na nova convenção:

```text
feat(5.2): documenta permissoes do drf
```

## Prática

- Teste a proteção da rota de categorias em uma viewset específica.
- Mova a configuração para o `settings.py` e repita o teste.
- Ative `DjangoModelPermissionsOrAnonReadOnly` e observe a diferença entre leitura anônima e escrita autenticada.

## Conclusão

As classes de permissão do DRF permitem centralizar a autorização da API e integrar esse controle com o sistema de usuários e grupos do Django.

## Próxima aula

- [5.3 Autenticação com o SimpleJWT](05-03-autenticacao-com-o-simplejwt.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](05-01-autenticacao-e-autorizacao.md) | [Próxima](05-03-autenticacao-com-o-simplejwt.md)