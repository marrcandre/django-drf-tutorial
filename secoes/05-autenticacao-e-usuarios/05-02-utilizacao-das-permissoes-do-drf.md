[Início](../../README.md) | [Seção](README.md) | [Anterior](05-01-autenticacao-e-autorizacao.md) | [Próxima](05-03-autenticacao-com-o-simplejwt.md)

# 5.2 Utilização das permissões do DRF

## Objetivo da aula

Aplicar permissões no DRF tanto em uma viewset específica quanto de forma global no projeto.

## Introdução

Autenticação e permissão caminham juntas, mas não são a mesma coisa. Depois de identificar quem é o usuário, ainda precisamos decidir com bastante clareza quais ações ele pode ou não pode executar.

No DRF, esse controle pode ser aplicado em pontos diferentes: em uma viewset específica, no projeto inteiro ou por meio de classes de permissão ligadas às permissões de modelo do Django.

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

Para aplicar a mesma regra ao projeto inteiro, remova a alteração anterior da viewset e configure no `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

Com isso, todos os endpoints passam a exigir autenticação por padrão.

### 3. Usando `DjangoModelPermissionsOrAnonReadOnly`

A abordagem recomendada é usar as permissões já gerenciadas pelo Django:

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

Sugestão de mensagem:

```text
feat(5.2): implementa permissoes do drf
```

## Prática

- Teste a proteção da rota de categorias em uma viewset específica.
- Mova a configuração para o `settings.py` e repita o teste.
- Ative `DjangoModelPermissionsOrAnonReadOnly` e observe a diferença entre leitura anônima e escrita autenticada.

## Conclusão

As classes de permissão do DRF ajudam a organizar a autorização da API de um jeito mais limpo e mais próximo do que se espera em uma aplicação real, integrando esse controle ao sistema de usuários e grupos do Django.

## Próxima aula

- [5.3 Autenticação com o SimpleJWT](05-03-autenticacao-com-o-simplejwt.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](05-01-autenticacao-e-autorizacao.md) | [Próxima](05-03-autenticacao-com-o-simplejwt.md)