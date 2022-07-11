# Django com DRF

Tutorial para desenvolvimento de APIs REST usando o Django, com DRF (Django Rest Framework).

# Aula 1

## Preparação do ambiente

-   Abra o navegador de arquivos
-   Crie uma pasta chamada `livraria` para o seu projeto
-   Certifique-se de que **nenhuma pasta** no caminho tenha **espaços** ou **acentos** (_se você não fizer isso, terá que recriar todo o projeto_).
-   Abra a **pasta** no vscode (repita em voz alta: _"Nunca abra um arquivo, sempre abra a pasta."_).
-   Dentro do vscode, abra um terminal (`Control+Shift+'`)

Instale algumas extensões para o **vscode**:

-   Python \*
-   SqLite Viewer \*
-   Intellicode
-   Prettier

Os comandos a seguir serão digitados no terminal que você abriu dentro do **vscode**.

Verifique se o **poetry** está instalado:

    poetry --version

Verifique se o **python** está instalado:

    python --version
    python3 --version

Informe ao **poetry** para criar a pasta do ambiente virtual dentro da pasta do projeto:

    poetry config virtualenvs.in-project true

**Criação do ambiente virtual**

Crie o ambiente virtual usado o **poetry**:

    poetry init

Você passará por uma tela semelhante a essa:

```bash
This command will guide you through creating your pyproject.toml config.

Package name [livraria]:
Version [0.1.0]:
Description []:
Author [Marco André Mendes <marcoandre@gmail.com>, n to skip]:
License []:
Compatible Python versions [^3.10]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "livraria"
version = "0.1.0"
description = ""
authors = ["Marco André Mendes <marcoandre@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.10"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
```

Ative o ambiente virtual recèm criado:

    poetry shell

Para verificar o tamanho da pasta do ambiente virtual:

    du -sh .venv

**Instalação do django**

Instale o **django** no ambiente virtual:

    poetry add django

Verifique se o **django** está instalado:

    django-admin

Se tudo der certo, ele mostrará as opções do `django-admin` na tela.

**Criação do projeto no django**

    django-admin startproject livraria .

O projeto criado ficará assim:

```
.
├── livraria
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── poetry.lock
└── pyproject.toml
```

Para executar o projeto, digite no terminal:

    python manage.py runserver

Verifique se o projeto está rodando:

-   Página inicial: [http://localhost:8000](http://localhost:8000)

-   `Admin`: [http://localhost:8000/admin](http://localhost:8000/admin)

Ao rodar o projeto pela primeira vez, o arquivo `db.sqlite3` é criado.
Também aparecem mensagens de erro importantes.

-   Abra o arquivo `db.sqlite3` dentro do **vscode**.
-   Verifique que ele não possuem nenhuma tabela ainda.

Vamos abrir cada um desses arquivos e verificar para que eles servem, principalmente os seguintes:

-   `manage.py`
-   `settings.py`
-   `urls.py`
-   `db.sqlite3`

**Configurando o interpretador Python**

-   Ao abrir um arquivo `.py`, verifique se o interpretador Python correto está configurado. Clique na opção do interpretador Python na barra inferior do **vscode**, ao lado da palavra `Python`. O correto seria algo como `.'venv/':poetry`.
-   Se não estiver assim, clique e configure.
-   Opcionalmente, configure a variavel `Venv Path` nos configurações do **vscode**. Tecle `Control+,` e procure por `venv`.
-   Com essas configurações feitas, feche todos os terminais e abra novamente. O ambiente virtual deve ser ativado automaticamente cada vez que você abrir um terminal a partir de agora.

**Executando o servidor**

Desse ponto em diante, abra um outro terminal no **vscode**, mantendo sempre o django em execução (`runserver`) no outro terminal.

Se precisar parar a execução do projeto, aperte `Control+C` e depois o execute novamente.

**Criando a base de dados inicial**

Para resolver o erro informado no momento de rodar o projeto, execute o seguinte comando:

    python manage.py migrate

Verifique se o projeto continua rodando e se o [Admin](http://localhost:8000) está em execução.

**Criando o superusuário**

Crie o super usuário para poder fazer o login:

    python manage.py createsuperuser

Agora sim, seu projeto está rodando e você consegue entrar no `admin`:

-   Crie mais 2 usuários de teste.
-   Entre no arquivo de banco de dados, e verifique se os registros foram criados.

---

# Aula 2

Apague o projeto criado na aula passada e vamos criá-lo novamente.

## Resumo da criação de um projeto Django

Siga as seguintes instruções para criar novamente o projeto.

-   Crie uma pasta
-   Abra a pasta no **vscode**
-   Abra um terminal no **vscode**

Digite os seguintes comandos, um a um, no terminal dentro do vscode.

    poetry
    poetry shell
    poetry add django
    django-admin startproject livraria .
    python manage.py migrate
    python manage.py createsuperuser

## Criando um app

Para criar seu primeiro app, digite: 

    python manage.py startapp core

Acrescente o app `'core'` na seção `INSTALLED_APPS` do arquivo `settings.py` do seu projeto.

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

Após criar o app, sua pasta deve parecer com isso:

```
.
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── livraria
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── poetry.lock
└── pyproject.toml

```

Dentro da pasta `core` foram criados alguns arquivos.
Vamos abrir cada um desses arquivos e verificar para que eles servem, principalmente os seguintes:

-   `admin.py`
-   `models.py`
-   `views.py`

Posteriormente, iremos modificar esses arquivos, bem como incluir alguns arquivos novos.

Nesse ponto, temos:

-   O ambiente virtual **Python** criado;
-   O projeto `livraria` criado;
-   O app `core` criado e instalado no projeto.

---

**Criação da primeira model**

Uma `model` no **Django** é uma classe que representa uma tabela no banco de dados. Cada atributo (variável) dessa classe representa um campo da tabela.

Para maiores informações consulte a [documentação](https://docs.djangoproject.com/en/4.0/topics/db/models/) do **Django** sobre `models`.

Altere o arquivo `models.py`, desse jeito:

```python
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
```

Nesse código, você:

-   Importou o pacote necessário para criar a `model`;
-   Criou a classe `Categoria`;
-   Incluiu o campo `descricao`.

**Efetivando a criação da tabela**

Precisamos agora efetivar essa criação da tabela no banco de dados. Para isso, abra um novo terminal, deixando o terminal antigo executando o servidor do projeto, e execute os seguintes comandos:

    python manage.py makemigrations

e

    python manage.py migrate

-   Acesse o banco de dados e verifique se a tabela `core_categoria` foi criada.
-   Acesse o [Admin](http://localhost:8000) do projeto e verifique se a nova tabela aparece lá.

**Inclusão no Admin**

A tabela ainda não apareceu, pois ainda precisamos informar ao [Admin](http://localhost:8000) da sua existência.

Para isso, inclua as seguintes linhas no arquivo `admin.py`:

```python
from django.contrib import admin

from core.models import Categoria

admin.site.register(Categoria)
```

Acesse novamente o [Admin](http://localhost:8000) e inclua algumas editoras no banco de dados.

**Mudando a língua e time zone**

Encontre e edite as seguintes linhas no arquivo no arquivo `settings.py`:

    LANGUAGE_CODE = "pt-br"
e

    TIME_ZONE = "America/Sao_Paulo"

Acesse novamente o [`Admin`](http://localhost:8000) e verifique que agora ele está em português.

**Mudando a descrição dos registros criados**

Você perceberá que a descrição dos informações que você inclui está meio estranha. Para resolver, isso, vamos fazer uma pequena modificação na `model Categoria`.

```python
...

    def __str__(self):
        return self.descricao
```
Volte ao [`Admin`](http://localhost:8000) verifique o que mudou na apresentação da model `Categoria`.

---

**Criação da segunda model**

Crie a segunda model, incluindo as seguintes informações no arquivo `models.py`:

```python
...

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
```

Não esqueça de que a cada criação de novas models é necessário:

-   Registrar a model no arquivo `admin.py`;
-   Fazer as migrações (`makemigrations`);
-   Efetivar as migrações (`migrate`);

Seu arquivo `admin.py` ficará assim:

```python
from django.contrib import admin

from core.models import Categoria, Editora

admin.site.register(Categoria)
admin.site.register(Editora)
```

Após fazer isso tudo, inclua algumas editoras na tabela e veja como ficou o seu banco de dados.

---

# Aula 3

## Criando um segundo projeto

Seguindo aquilo que você já aprendeu, crie um **novo projeto** chamado **garagem**. Crie os seguintes modelos nesse projeto e inclua dados nas tabelas.

```python
from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
```

---

# Aula 4

## Colocando o projeto no **github**

Antes de mais nada, seguem **3 regras** a serem consideradas ao seguir as instruções:

-   **Antes de clicar ou responder, leia atentamente as instruções.**
-   **Leia atentamente as instruções antes de clicar ou responder.**
-   **Nunca clique ou responda sem antes ler atentamente as instruções.**

As 3 regras falam a mesma coisa? Sim, você entendeu o recado. ;-)

**Configure o projeto git**

-   Verifique se já não existe uma conta conectada ao github no **vscode**, clicando no ícone **Contas** na barra lateral esquerda. Deve ser o penúltimo ícone da baixo pra cima. Se houver, **desconecte primeiro**.
-   Inicialize o repositório **git**. Clique no ícone do **git** no painel lateral esquerdo. Deve ser o segundo ícone, de cima pra baixo. Opcionalmente, tecle (`Control+Shift+G`). Depois, clique no botão `Initialize repository`.
-   Se aparecer uma bolinha azul no ícone do git com um número, o repositório foi ativado. Esse número indica o número de arquivos que foram criados ou alterados.

**Configure as variáveis do **git****

Para isso, digite no terminal, substituindo por suas informações pessoais (colocando as suas informações no lugar):

    git config user.name "Marco André Mendes"
    git config user.email "marcoandre@gmail.com"

Para verificar se as informações estão corretas, digite:

    git config -l

**Crie o arquivo `.gitignore`**

-   Vá no site [gitignore.io](https://gitignore.io/)
-   Escolha as opções `Django` e `VisualStudioCode`.
-   Clique em `Criar`.
-   Selecione todo o texto (`Control+A`) e copie (`Control+C`).
-   Crie um arquivo novo na raiz do projeto e dê o nome de `.gitignore`.
-   Cole o conteúdo copiado (`Control+V`).

**Faça a publicação**

-   Escreva uma descrição para o commit (`"commit Inicial"`).
-   Tecle `Control+ENTER` para fazer o envio para o servidor do github.
-   Leia atentamente as instruções relacionadas a autenticação no **github** e criação do projeto.
-   Ao final, seu projeto será incluído no **github** e você poderá visulizá-lo lá.

**Fazendo alterações no projeto e enviando novamente**

Vamos agora realizar algumas mudanças no projeto e enviá-lo novamente para o **github**.

-   Abra o arquivo `models.py` (Um atalho útil é teclar `Control+P` e então digitar o nome do arquivo.)
-   Selecione todo o texto (`Control+A`) e mande formatar o código (`Control+Shift+I` ou `Control+Shift+P+"Formatar o Documento"`).
-   Deve aparecer uma mensagem pedindo para instalar um **formatador de código** (`black`). Concorde com a instalação.
-   Após a instalação, execute o comando anterior novamente. O arquivo deve ser formatado.
-   Faça a mesma coisa com o arquivo `admin.py`.
-   Altere outros arquivos. Por exemplo: apague os comentários iniciais dos arquivos `settings.py` e `urls.py`.
-   Nesse ponto, você já deve ter vários arquivos modificados.
-   Vá para a aba do **github** no **vscode** e coloque o nome do **commit** como sendo `Instalação do black`.
-   Confirme o **commit** teclando `Control+ENTER`.
-   Faça o envio (`push`), clicando no ícone de envio.
-   Vá no seu projeto no github, atualize a página e verifique as modificações.

**Baixando novamente o projeto**

Agora que seu projeto está no **github**, você pode baixá-lo onde quiser. Vamos testar isso.

  **A partir desse ponto, vamos repetir uma série de passos que já fizemos nas aulas anteriores. Em caso de dúvidas, volte nessas aulas para mais detalhes.**

-   Apague todo o projeto do seu computador (_isso mesmo, coragem_).
-   Crie novamente uma pasta vazia para hospedá-lo.

-   Abra o **vscode** na pasta (_Você já sabe fazer isso. Aula 1, lembra?_).
-   Vá no projeto no **github**, clique no botão **Code** e copie a url dele. Deve ser algo no seguinte formato: `https://github.com/marrcandre/livraria.git`
-   Tecle `Control+Shift+P+"Git Clone"`
-   Ao ser solicitado o endereço do projeto, informe a url que você copiou de lá.
-   Se tudo correu bem, o projeto foi baixado e está no seu computador. 
-   Abra um terminal.
-   Reinstale os pacotes necessários para o seu projeto e ative o ambiente virtual: 

Digite no terminal:

    poetry install && poetry shell

- Feito isso, execute o servidor do seu projeto e teste no navegador.

Pronto! Seu projeto está de volta no computador e rodando.

# Aula 5

## Continuando o projeto livraria

**Colocando o projeto livraria no github**

Agora que você conseguiu colocar o projeto `garagem` no **github**, coloque também o projeto `livraria`.

**Criando as tabelas `Autor` e `Livro`**

Vamos agora criar mais duas tabelas na nossa livraria, as tabelas `Autor` e `Livro`.

No arquivo `models.py`. inclua a seguinte informação:

```python
...

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
 
    def __str__(self):
        return f'{self.titulo} ({self.quantidade})'
```

Antes de efetivarmos as alterações no banco de dados, vamos incluir duas chaves estrangeiras no modelo `Livro`.

**Incluindo chaves estrangeiras no modelo**

Nosso livro terá uma categoria e uma editora. Para isso, vamos incluir campos que serão chaves estrageiras, referenciando as tabelas `Categoria` e `Editora`.

**Campo `categoria`**

Inclua a linha a seguir no `model Categoria`, logo após o atributo `preco`:

```python
...
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
...
```

Vamos entender cada parte:

- `models.ForeignKey`: define o campo como sendo uma chave estrangeira.
- `Categoria`: o model (tabela) que será associado a esse campo.
- `on_delete=models.PROTECT`: impede de apagar uma categoria que possua livros associados.
- `related_name='livros'`: cria um atributo `livros` na classe `Categoria`, permitindo acessar todos os livros de uma categoria.

De forma semelhante, vamos associar o livro a uma editora, incluindo logo em seguida à categoria, a seguinte linha:

```python
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
```

Feito isso, inclua as classe criadas no arquivo `admin.py`:

```python
from django.contrib import admin

from core.models import Autor, Categoria, Editora, Livro

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
```

O próximo passo é migrar a base de dados para efetivarmos essas mudanças no banco de dados podermos testar na interface de administração. Lembra dos comandos? Aqui estão eles, mais uma vez:

    python manage.py makemigrations

e

    python manage.py migrate

Feito isso, verifique se tudo funcionou.

- Cadastre algumas categorias, editoras, autores e livros. 
- Note como os livros acessam as categorias e editoras já cadastradas.
- Tente apagar uma editora ou categoria **com** livros associados.
- Tente apagar uma editora ou categoria **sem** livros associados.

<!-- 
No django shell, é possível testar o acesso a todos os livros de uma categoria usando algo parecido com isso:
Categoria.objects.get(id=1).livros.all() 
-->

# Aula 6

## Criando uma API Rest com o Django REST framework (DRF)

**Instalação do DRF**

Instale o DRF via poetry:

    poetry add djangorestframework

Adicione-o aos applicativos instalados, no arquivo `settings.py`:

```python
INSTALLED_APPS = [
...
    "rest_framework",
    "core",
]
```

**Criação do serializer**

Para criar o serializer da `Categoria`, crie o arquivo `serializers.py` na pasta `core`:

```python
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
```

**Criação da view**

Para criar a view da `Categoria`, edite o arquivo `views.py` na pasta `core`. Substitua o seu conteúdo por esse:

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
```

**Criação das rotas(urls)**

Para criar as rotas da `Categoria`, edite o arquivo `urls.py` na pasta `livraria`. Substitua o seu conteúdo por esse:

```python
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
```

**Testando a API**

Para acessar a interface gerada pelo DRF, acesse:

    http://localhost:8000

Se tudo correu bem, você deve ver a interface do DRF.

Você pode acessar diretamente a rota da `Categoria`:

    http://localhost:8000/categorias

Isso deve trazer todas as categorias do banco, no formato **json**.

Para acessar um único registro, use o seguinte formato:

  http://localhost:8000/categorias/1/

Nesse caso, `1` é o `id` do registro no banco de dados.

**Opções de manipulação do banco de dados**

As opções disponíveis para manipulação dos dados são:

- GET: para listar todos ou apenas 1 registro.
- POST: para criar um novo registro.
- PUT: para alterar um registro.
- PATCH: para alterar campos de um registro.
- DELETE: para remover registros.

**Outras ferramentas para testar a API**

A interface do DRF é funcional, porém simples e limitada. Algumas opções de ferramentas para o teste da API são:

- **Insomnia**
- **Postman**
- **Thunder Client** (extensão do **vscode**)

---
```python
print("That's all, folks!")
```
