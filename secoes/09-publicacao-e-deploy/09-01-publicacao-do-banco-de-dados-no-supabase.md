[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](09-02-publicacao-do-projeto-no-render.md)

# 9.1 Publicação do banco de dados no Supabase

## Objetivo da aula

Configurar um banco externo no Supabase para uso em produção, mantendo o SQLite local apenas para desenvolvimento.

## Desenvolvimento

### 1. Criando o projeto no Supabase

- Crie uma conta no Supabase.
- Crie um novo projeto e uma organização.
- Gere a senha do banco e guarde esse valor.
- Use a região South America, quando disponível.

### 2. Configurando o `.env`

Copie a string de conexão do `Session Pooler` e configure:

```ini
DATABASE_URL=postgresql://usuario:senha@host:5432/postgres
```

### 3. Migrando o banco remoto

Descomente `DATABASE_URL` e execute:

```shell
pdm run migrate
```

### 4. Validando o ambiente

Confira tabelas no `Table Editor` e no `Schema Visualizer`. Depois, ao voltar ao desenvolvimento local, comente novamente a variável remota para usar o SQLite.

## Hora do commit

```text
feat(9.1): documenta publicacao do banco no supabase
```

## Prática

- Crie o projeto no Supabase.
- Migre o banco remoto.
- Compare dados entre ambiente local e remoto.

## Conclusão

O projeto deixa de depender do banco efêmero do deploy e passa a ter persistência adequada em produção.

## Próxima aula

- [9.2 Publicação do projeto no Render](09-02-publicacao-do-projeto-no-render.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](09-02-publicacao-do-projeto-no-render.md)