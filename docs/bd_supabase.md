# 22B. Utilizando um Banco de Dados externo no Supabase

Vamos criar um banco de dados no Supabase. Com isso, os dados não serão perdidos a cada nova implantação.

**Criando um projeto no Supabase**

- Acesse o site do [Supabase](https://supabase.io/) e crie uma conta.
- Crie um novo projeto no Supabase.
- Dẽ um nome ao projeto.
- Selecione a opção `Create a new organization`.
- Selecione a região `South America (São Paulo)`.
- Dẽ um nome à organização.
- Selecione a opção `Create a new database`.
- Dê um nome ao banco de dados.
- Escolha uma senha e **guarde-a** (você vai precisar dela).

**Configurando o banco de dados no projeto**

- Entre no [Dashboard](https://supabase.com/dashboard/projects) do projeto, e escolha o projeto criado.
- Escolha a opção `Project settings` e depois `Database`.
- Copia a linha de conexão do banco de dados (URI).
  - Ela deve ser parecida com isso: `postgres://postgres:[YOUR-PASSWORD]@!@db.vqcprcexhnwvyvewgrin.supabase.co:5432/postgres`.
- Troque `[YOUR-PASSWORD` pela senha que você havia guardado.
- Copie a linha de conexão e cole no arquivo `.env` do projeto, como no exemplo:

```shell
# Supabase
DATABASE_URL=postgres://postgres:Senha.123@!@db.vqcprcexhnwvyvewgrin.supabase.co:5432/postgres
```



> Altere as informações de acordo com o seu projeto.

**Configurando o arquivo `settings.py`**

- Edite o arquivo `settings.py` do projeto, e substitua o conteúdo da variável `DATABASES` pelo seguinte:

```python
...
if MODE in ["PRODUCTION", "MIGRATE"]:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

print(MODE, DATABASES)
...
```

> Note que a variável `DATABASES` foi substituída por um `if` que verifica se o `MODE` é `PRODUCTION` ou `MIGRATE`. Se for, o banco de dados será o `PostgreSQL` do `Supabase`. Caso contrário, será o `SQLite` local.

> O `print` foi incluído para que você possa verificar se o banco de dados está correto.

> Com essa configuração, podemos acessar o banco de dados do `Supabase` e fazer a migração do banco de dados.

**Instalação do suporte ao PosgreSQL**

- Para acessar o banco de dados PostgreSQL, instale o seguinte pacote:

```shell
pdm add psycopg2-binary
```

**Migração do banco de dados**

- No arquivo `.env`, altere o valor da variável `MODE` para `MIGRATE`.
- Faça a migracão do banco de dados:

```shell
pdm run python manage.py migrate
```

> Observe que o banco de dados foi migrado para o `Supabase`.

- No `Supabase`, acesse o `Table Editor` e verifique que as tabelas foram criadas.
- Você também pode ver o esquema das tabelas, em `Database`, `Schema Visualizer`.

- Faça o commit das alterações.

> Se o `MODE` estiver definido como `PRODUCTION`, no `Fl0`, o banco de dados será o do `Supabase`.

- Para testar, crie um novo autor no projeto e verifique se ele foi criado no banco de dados do `Supabase`.

> A partir de agora, sempre que você fizer uma nova implantação, os dados não serão perdidos.

- Para voltar a usar o banco de dados local, altere o valor da variável `MODE` para `DEVELOPMENT`.
