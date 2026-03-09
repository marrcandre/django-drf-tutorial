[Início](../../README.md) | [Seção](README.md) | [Anterior](09-01-publicacao-do-banco-de-dados-no-supabase.md) | [Próxima](09-03-armazenamento-de-arquivos-no-cloudinary.md)

# 9.2 Publicação do projeto no Render

## Objetivo da aula

Publicar a aplicação no Render usando build script, variáveis de ambiente e servidor ASGI compatível com produção.

## Desenvolvimento

### 1. Teste local do servidor de produção

```shell
pdm run python -m gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker
```

### 2. Configuração do serviço

No Render, crie um `Web Service` a partir do repositório Git e configure:

- `Build command`: `./build.sh`
- `Start command`: `python -m gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker`
- `Runtime`: Python
- `Branch`: `main`

### 3. Variáveis de ambiente

Inclua valores como:

```ini
MODE=PRODUCTION
DEBUG=False
SECRET_KEY=sua_chave
WEB_CONCURRENCY=4
DATABASE_URL=sua_database_url
CLOUDINARY_URL=cloudinary://...
```

## Hora do commit

```text
feat(9.2): documenta publicacao do projeto no render
```

## Prática

- Teste o comando de produção localmente.
- Configure o serviço no Render.
- Valide as variáveis de ambiente antes do primeiro deploy.

## Conclusão

A aplicação passa a ter um fluxo de publicação consistente e repetível em ambiente hospedado.

## Próxima aula

- [9.3 Armazenamento de arquivos no Cloudinary](09-03-armazenamento-de-arquivos-no-cloudinary.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](09-01-publicacao-do-banco-de-dados-no-supabase.md) | [Próxima](09-03-armazenamento-de-arquivos-no-cloudinary.md)