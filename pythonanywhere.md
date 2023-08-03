# 21. Configurando variáveis de ambiente

É importante manter informações sensíveis, como chaves de API e senhas, longe de olhares indiscretos. A melhor maneira de fazer isso é não colocá-los no **GitHub**! Para isso, vamos usar o arquivo `.env` para armazenar essas informações.

-   Instale o pacote `django_environ`:

```shell
pdm add django-environ
```

-   Edite o arquivo `config/settings.py`:

```python
...
import environ
...
# Carrega as variáveis de ambiente do sistema operacional e as prepara para usá-las
env = environ.Env()
environ.Env.read_env((os.path.join(BASE_DIR, '.env')))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')
DATABASES = {'default': env.db()}
```

IMPORTANTE: Após incluir essas variáveis, remova as outras referências a elas no arquivo `settings.py`.

-   Crie o arquivo `.env`:

```shell
touch .env
```

-   Edite o arquivo `.env`:

```python
SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

**IMPORTANTE**:

-   Adicione o arquivo `.env` ao arquivo `.gitignore`.
-   Feito isso, esse arquivo não será mais versionado pelo Git.
-   Para ter um modelo de arquivo `.env`, crie um arquivo `.env.example` e adicione-o ao Git.

```shell
cp .env .env.example
```

# 22. Publicação no PythonAnywhere

O PythonAnywhere é um serviço de hospedagem de aplicações Python. Ele permite que você hospede seu projeto Django gratuitamente. Para isso, você precisa criar uma conta no PythonAnywhere e seguir os passos abaixo. Para publicar seu projeto no PythonAnywhere, você precisa ter uma conta no **GitHub**.

**Atualização do arquivo `requirements.txt`**

Atualize o arquivo `requirements.txt`:

```shell
pdm export -o requirements.txt -v --without-hashes
```

Faça um commit e um push para o **GitHub** antes de continuar.

**Criação da conta no PythonAnywhere**

-   Crie uma conta no https://www.pythonanywhere.com/

**Criação do banco de dados no PythonAnywhere**

-   Crie o banco de dados em https://www.pythonanywhere.com/dashboard/, na opção `Databases`.
-   Anote as informações de conexão com o banco de dados:
    -   Host: `sua_conta.mysql.pythonanywhere-services.com`
    -   Database name: `seu_usuario_bd$seu_bd`
    -   Username: `seu_usuario_bd`
    -   Password: `sua_senha_bd`

**IMPORTANTE:**

-   Substitua `seu_usuario` pelo seu usuário do **GitHub**.
-   Substitua `seu_projeto` pelo nome do seu projeto no **GitHub**.
-   Substitua `sua_conta` pelo nome da sua conta no PythonAnywhere.
-   Substitua `seu_bd` pelo nome do seu banco de dados.
-   Substitua `seu_usuario_bd` pelo nome do seu usuário no banco de dados.
-   Substitua `sua_senha_bd` pela sua senha no banco de dados.

**Instalação do módulo `mysqlclient`**

-   Instale o pacote `libmysqlclient-dev`:

```shell
sudo apt install libmysqlclient-dev
```

-   Caso você esteja usando Manjaro:

```shell
sudo pacman -S gcc mysql
```

O pacote `libmysqlclient-dev` é necessário para instalar o módulo `mysqlclient`.

-   Instale o módulo `mysqlclient`:

```shell
pdm add mysqlclient
```

O módulo `mysqlclient` é necessário para conectar o Django ao banco de dados MySQL.

**Configuração das variáveis de ambiente**

-   Crie um arquivo `.env` na pasta raiz (`/`) do seu usuario no PythonAnywhere. Você pode fazer isso pelo console ou pela interface web, na opção `Files`.

```python
SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DEBUG=False
ALLOWED_HOSTS=sua_conta.pythonanywhere.com
DATABASE_URL=mysql://seu_usuario_bd:sua_senha_bd@sua_conta.mysql.pythonanywhere-services.com/seu_usuario_bd$seu_bd
```

-   Inclua o seguinte conteúdo no arquivo .virtualenvs/postactivate:

```shell
echo "Copiando o arquivo .env para a pasta do projeto..."
cp ~/.env ~/sua_conta.pythonanywhere.com/
```

Esse comando copia o arquivo `.env` dentro da pasta do seu projeto no PythonAnywhere.

**Geração da SECRET_KEY**

-   Para gerar uma nova SECRET_KEY (chave secreta), a ser colocada no arquivo `.env`, execute o comando:

```shell
python -c "import secrets; print(secrets.token_urlsafe())"
```

-   Você também pode gerar uma nova chave secreta em https://djecrety.ir/
-   Para saber mais sobre a chave secreta, acesse a [documentação](https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key) do Django.

IMPORTANTE:

-   Não esqueça de substituir a chave secreta pelo valor gerado.
-   Não esqueça de substituir os valores das variáveis de ambiente pelos seus valores.

**Criação da API Token**

-   Crie uma API Token em `Account` > `API Token` em https://www.pythonanywhere.com/dashboard/.

**Instalação do cliente do PythonAnywhere**

-   Acesse o console (terminal) do PythonAnywhere em https://www.pythonanywhere.com/consoles/

-   Instale o cliente do PythonAnywhere no console:

```shell
pip install pythonanywhere --user
```

**Criação do projeto no PythonAnywhere**

O script `pa_autoconfigure_django.py` autoconfigura o projeto Django no PythonAnywhere a partir de um repositório do **GitHub**:

-   Faz o clone do repositório do **GitHub**.
-   Cria um virtualenv.
-   Instala as dependências do projeto.
-   Cria uma webapp.
-   Cria o arquivo de configuração `wsgi.py`.
-   Adiciona os arquivos estáticos.

-   No console do PythonAnywhere, execute o comando abaixo, substituindo `https://github.com/seu_usuario/seu_projeto.git` pelo link do seu repositório no **GitHub** (aquele mesmo que você usou para clonar o projeto):

```shell
pa_autoconfigure_django.py --python=3.8 --nuke https://github.com/seu_usuario/seu_projeto.git
```

**Ativando o virtualenv (se necessário)**

-   Se necessário, no console, ative o `virtualenv`:

```shell
workon marcoandre.pythonanywhere.com
```

**Migrando o banco de dados**

-   No console, execute o comando abaixo para migrar o banco de dados:

```shell
python manage.py migrate
```

**Configuração do banco de dados no PythonAnywhere**

-   Carregue os dados iniciais:

```shell
python manage.py loaddata livraria.json
```

**Remoção do banco de dados local (se necessário)**

Para remover um banco de dados, acesse https://www.pythonanywhere.com/dashboard/, na opção `Databases` e digite:

```shell
drop database seu_usuario$seu_bd;
```

**IMPORTANTE:** Não esqueça de substituir `seu_usuario` e `seu_bd` pelos seus valores.

**Baixar novamente o projeto do **GitHub** (se necessário)**

-   Se você precisar atualizar o projeto do **GitHub**, sem precisar executar todo o processo novamente execute o comando:

```shell
git pull
```

-   Em caso de erro, execute o comando:

```shell
git checkout -- .
git clean -f -d
git pull
```

-   Se houverem alterações no arquivo `requirements.txt`, execute o comando:

```shell
pip install -r requirements.txt
```

-   Se houverem alterações nos modelos, faça a migração:

```shell
python manage.py migrate
```

