[Início](../../README.md) | [Seção](README.md) | [Anterior](05-02-utilizacao-das-permissoes-do-drf.md) | [Próxima](05-04-inclusao-da-foto-de-perfil-no-usuario.md)

# 5.3 Autenticação com o SimpleJWT

## Objetivo da aula

Configurar autenticação com JWT e testar registro, login, renovação de token e acesso a endpoints protegidos.

## Introdução

Nesta aula, o projeto ganha um fluxo de autenticação mais próximo do que aparece em muitas APIs modernas. A ideia é entender não só como obter e usar o token, mas também como esse processo se encaixa no restante da segurança da aplicação.

## Desenvolvimento

### 1. Ativando o SimpleJWT

No `settings.py`, mantenha a autenticação e as permissões padrão desta forma:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",),
    ...
}
```

Confirme também as rotas já previstas no `urls.py`:

- `/api/token/`
- `/api/token/refresh/`
- `/api/token/verify/`
- `/api/registro/`

### 2. Endpoints usados na aula

- `POST /api/registro/`: cria um novo usuário;
- `POST /api/token/`: autentica e devolve `access` e `refresh`;
- `POST /api/token/refresh/`: gera novo `access token`;
- `POST /api/token/verify/`: verifica se um token é válido.

### 3. Criando um usuário

Use o endpoint abaixo:

```text
[POST] http://0.0.0.0:19003/api/registro/
```

Envie:

```json
{
    "email": "comprador1@a.com",
    "name": "Comprador 1",
    "password": "teste.123"
}
```

### 4. Fazendo login

Primeiro teste uma rota protegida sem token:

```text
[GET] http://0.0.0.0:19003/api/categorias/
```

Depois autentique o usuário:

```text
[POST] http://0.0.0.0:19003/api/token/
```

```json
{
    "email": "comprador1@a.com",
    "password": "teste.123"
}
```

A resposta deve conter `refresh` e `access`.

### 5. Obtendo o token pela linha de comando

```shell
curl -s -X POST http://127.0.0.1:19003/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"email": "comprador1@a.com", "password": "teste.123"}'
```

Para exibir somente o `access token`:

```shell
curl -s -X POST http://127.0.0.1:19003/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"email": "comprador1@a.com", "password": "teste.123"}' | awk -F'"' '/access/ {print $4}'
```

### 6. Usando o token em endpoints protegidos

Cole o `access token` como `Bearer` no cliente HTTP e teste:

```text
[GET] http://0.0.0.0:19003/api/categorias/
```

Você também pode consultar:

```text
[GET] http://0.0.0.0:19003/api/usuarios/me/
```

### 7. Renovando e verificando tokens

Renovação:

```text
[POST] http://0.0.0.0:19003/api/token/refresh/
```

```json
{
    "refresh": "<refresh_token>"
}
```

Verificação:

```text
[POST] http://0.0.0.0:19003/api/token/verify/
```

```json
{
    "token": "<access_token>"
}
```

### 8. Simulando logout

No modelo atual, o logout é feito no cliente, removendo:

- o `access token`;
- o `refresh token`;
- o cabeçalho `Authorization: Bearer <token>`.

### 9. Testando permissões com usuários diferentes

Repita operações autenticadas com perfis distintos para observar a diferença entre:

- autenticação via JWT;
- autorização via permissões do Django e do DRF.

## Hora do commit

Sugestão de mensagem:

```text
feat(5.3): implementa   autenticacao com simplejwt
```

## Prática

- Registre um usuário novo.
- Faça login e use o token em uma rota protegida.
- Force a renovação do token.
- Remova o token e confirme o retorno para acesso não autenticado.

## Conclusão

Com o SimpleJWT, o projeto passa a separar de forma mais clara duas responsabilidades importantes: o JWT cuida da autenticação do usuário, enquanto as permissões do Django e do DRF continuam definindo o que esse usuário pode fazer.

## Próxima aula

- [5.4 Inclusão da foto de perfil no usuário](05-04-inclusao-da-foto-de-perfil-no-usuario.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](05-02-utilizacao-das-permissoes-do-drf.md) | [Próxima](05-04-inclusao-da-foto-de-perfil-no-usuario.md)