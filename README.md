# Django com DRF

Tutorial para desenvolvimento de APIs REST usando o Django, com DRF (Django Rest Framework).

# 1 - Preparação do ambiente

**Criação da pasta**

-   Abra o navegador de arquivos
-   Crie uma pasta chamada `livraria` para o seu projeto
-   Certifique-se de que **nenhuma pasta** no caminho tenha **espaços** ou **acentos** (_se você não fizer isso, terá que recriar todo o projeto_).
-   Abra a **pasta** no vscode (repita em voz alta: _"Nunca abra um arquivo, sempre abra a pasta."_).
-   Dentro do vscode, abra um terminal (`Control+Shift+'`)

**Instalação de extensões**

Instale algumas extensões para o **vscode**:

-   Python
-   SqLite Viewer
-   Intellicode
-   Prettier

**Instalação do poetry**

Os comandos a seguir serão digitados no terminal que você abriu dentro do **vscode**.

Verifique se o **poetry** está instalado:

    poetry --version

Se não estiver instalado, siga o próximo passo:

Baixe o [programa de instalação](./bin/poetry_install.sh) e o execute em um terminal.

Execute os seguintes comandos no terminal:

    poetry completions bash >> ~/.bash_completion

e

    pip install -U pip setuptools

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

# 2 - Criando uma app

Apague o projeto criado na passada e vamos criá-lo novamente.

**Resumo da criação de um projeto Django**

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

**Criando um app**

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

# 3 - Criando um segundo projeto

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

# 4 - Colocando o projeto no **github**

Antes de mais nada, seguem **3 regras** a serem consideradas ao seguir as instruções:

-   **Antes de clicar ou responder, leia atentamente as instruções.**
-   **Leia atentamente as instruções antes de clicar ou responder.**
-   **Nunca clique ou responda sem antes ler atentamente as instruções.**

As 3 regras falam a mesma coisa? Sim, você entendeu o recado. ;-)

**Configure o projeto git**

-   Verifique se já não existe uma conta conectada ao github no **vscode**, clicando no ícone **Contas** na barra lateral esquerda. Deve ser o penúltimo ícone da baixo pra cima. Se houver, **desconecte primeiro**.
-   Inicialize o repositório **git**. Clique no ícone do **git** no painel lateral esquerdo. Deve ser o segundo ícone, de cima pra baixo. Opcionalmente, tecle (`Control+Shift+G`). Depois, clique no botão `Initialize repository`.
-   Se aparecer uma bolinha azul no ícone do git com um número, o repositório foi ativado. Esse número indica o número de arquivos que foram criados ou alterados.

Se aparecem muitos arquivos alterados (10 mil, por exemplo), é provável que exista um repositório **git** criado na pasta raiz do usuário. Apague esse repositório assim:

    rm -Rf ~/.gitconfig

Recarregue o **vscode** (`Control+Shift+P + "Recarregar a Janela"`) e verifique se o número mudou para algo mais razoável (em torno de 100 arquivos).

**Configure as variáveis do git**

Para isso, digite no terminal, substituindo por suas informações pessoais (colocando as suas informações no lugar):

    git config user.name "Marco André Mendes"
    git config user.email "marcoandre@gmail.com"

Para verificar se as informações estão corretas, digite:

    git config -l

Se aparecer outro nome de usuário ou outras informações estranhas, remova o arquivo com as configurações globais do git:

    rm ~/.gitconfig

Repita o processo de configuração de nome e email.

**Crie o arquivo `.gitignore`**

-   Vá no site [gitignore.io](https://gitignore.io/)
-   Escolha a opção `Django`.
-   Clique em `Criar`.
-   Selecione todo o texto (`Control+A`) e copie (`Control+C`).
-   Crie um arquivo novo na raiz do projeto e dê o nome de `.gitignore`.
-   Cole o conteúdo copiado (`Control+V`).
-   Encontre as linhas que se referem "`db.sqlite3`" e comente-as (`Control+/`).

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

-   Abra o **vscode** na pasta (_Você já sabe fazer isso. 1, lembra?_).
-   Vá no projeto no **github**, clique no botão **Code** e copie a url dele. Deve ser algo no seguinte formato: `https://github.com/marrcandre/livraria.git`
-   Tecle `Control+Shift+P+"Git Clone"`
-   Ao ser solicitado o endereço do projeto, informe a url que você copiou de lá.
-   Se tudo correu bem, o projeto foi baixado e está no seu computador.
-   Abra um terminal.
-   Reinstale os pacotes necessários para o seu projeto e ative o ambiente virtual:

Digite no terminal:

    poetry install && poetry shell

-   Feito isso, execute o servidor do seu projeto e teste no navegador.

Pronto! Seu projeto está de volta no computador e rodando.

# 5 - Colocando o projeto livraria no github

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
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.titulo} ({self.quantidade})'
```

Antes de efetivarmos as alterações no banco de dados, vamos incluir duas chaves estrangeiras no modelo `Livro`.

**Incluindo chaves estrangeiras no modelo**

Nosso livro terá uma categoria e uma editora. Para isso, vamos incluir campos que serão chaves estrageiras, referenciando as tabelas `Categoria` e `Editora`.

**Campo `categoria`**

Inclua a linha a seguir no `model Livro`, logo após o atributo `preco`:

```python
...
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
...
```

Vamos entender cada parte:

-   `models.ForeignKey`: define o campo como sendo uma chave estrangeira.
-   `Categoria`: o model (tabela) que será associado a esse campo.
-   `on_delete=models.PROTECT`: impede de apagar uma categoria que possua livros associados.
-   `related_name='livros'`: cria um atributo `livros` na classe `Categoria`, permitindo acessar todos os livros de uma categoria.

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

-   Cadastre algumas categorias, editoras, autores e livros.
-   Note como os livros acessam as categorias e editoras já cadastradas.
-   Tente apagar uma editora ou categoria **com** livros associados.
-   Tente apagar uma editora ou categoria **sem** livros associados.

<!--
No django shell, é possível testar o acesso a todos os livros de uma categoria usando algo parecido com isso:
Categoria.objects.get(id=1).livros.all()
-->

# 6 - Criando uma API Rest com o Django REST framework (DRF)

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

[http://localhost:8000/categorias/](http://localhost:8000/categorias/)

Isso deve trazer todas as categorias do banco, no formato **json**.

Para acessar um único registro, use o seguinte formato:

[http://localhost:8000/categorias/1/](http://localhost:8000/categorias/1/)

Nesse caso, `1` é o `id` do registro no banco de dados.

**Opções de manipulação do banco de dados**

As opções disponíveis para manipulação dos dados são:

-   **GET**:

    -   para **listar** **todos** os registros:

            http://localhost:8000/categorias/

    -   para **listar** **apenas 1** registro:

            http://localhost:8000/categorias/<id>/

-   **POST** (para **criar** um **novo** registro):

          http://localhost:8000/categorias/

-   **PUT** (para **alterar** um registro existente):

          http://localhost:8000/categorias/<id>/

-   **PATCH** (para **alterar parcialmente** um registro):

          http://localhost:8000/categorias/<id>/

-   **DELETE** (para **remover** um registro):

          http://localhost:8000/categorias/<id>/

**Outras ferramentas para testar a API**

A interface do DRF é funcional, porém simples e limitada. Algumas opções de ferramentas para o teste da API são:

-   [Insomnia](https://docs.insomnia.rest/insomnia/install)
-   [Postman](https://www.postman.com/downloads/)
-   [Thunder Client](https://www.thunderclient.com/) (extensão do **vscode**)

**Testando a API e as ferramentas**

Instale uma ou mais das ferramentas sugeridas.

Experimente as seguintes tarefas:

-   Criar uma ou mais categorias;
-   Listar todas as categorias;
-   Alterar uma ou mais categorias, utilizando PUT e PATCH;
-   Listar a categoria alterada;
-   Remover uma categoria;
-   Incluir outra categoria;
-   Listar todas as categorias.

# 7 - API Rest com DRF

**Criação da API para a classe Editora**

Repita os passos utilizados para a criação da API da `Categoria` e crie a API para a `Editora`.

Os passos são:

-   Criar o serializador em `serializers.py`
-   Criar a viewset em `views.py`.
-   Incluir a nova rota em `urls.py`

Os arquivos ficarão assim:

**`serializers.py`**

```python
from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
```

**`views.py`**

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora
from core.serializers import CategoriaSerializer, EditoraSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
```

**`urls.py`**

```python
...

from core.views import CategoriaViewSet, EditoraViewSet

...

router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)

...
```

**Teste da API da Editora**

-   Teste todas as operações da `Editora`.
-   Verifique se é possível incluir novas editoras sem incluir todos os campos.
-   Tente utilizar o PUT e o PATCH sem informar todos os campos.
-   Tente remover uma editora com livros associados a ela.

**Criação da API para Autor e Livro**

-   Repita os passos para a criação da API para `Autor` e `Livro`.
-   Teste o funcionamento.
-   Observe que no Livro, aparecem apenas os campos `id` da categoria e da editora.

**Apresentação das informações de categoria e editora no livro**

Uma forma de mostrar essas informações é essa, em `serializers.py`:

```python
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
```

Teste e você verá que isso resolve a listagem (GET), mas gera problema no criação e alteração (POST, PUT e PATCH).

Para resolver isso, podemos criar dois (ou mais) serializadores, como no exemplo:

```python
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
```

Na viewset, escolhemos o serializador conforme a operação:

```python
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroDetailSerializer
        return LivroSerializer
```

# 8 - Aplicação frontend e Django CORS Headers

**Executando uma aplicação _frontend_ de exemplo**

Clone o repositório https://github.com/marrcandre/livraria-vue-3 e execute os seguintes comandos:

```shell
npm install
npm run dev
```

Se tudo correu bem, execute a aplicação:

http://localhost:3000

Se os dados não aparecerem, entre na opção **Inspecionar** do seu navegador (`Control`+`Shift`+I ou **botão direto - Inspecionar**.)

Na opção `Console`, verifique se aparece um erro de **CORS**. Se isso ocorrer, siga o tutorial a seguir.;

**Inclusão do Django CORS headers no projeto**

Adicionar o Django CORS headers permite que seu projeto seja acessado de outros domínios. Isso é necessário, por exemplo, para acessar a API através de uma aplicação de _frontend_ feita em _vuejs_.

Instale o pacote no `poetry`:

```python
poetry add django-cors-headers
```

Depois, faça algumas modificações no `settings.py'. Primeiro, adicione o pacote recém adicionado nas suas aplicações instaladas:

```python
INSTALLED_APPS = [
    ...,
    "corsheaders",
    "rest_framework",
    "core",
    ...,
]
```

Não esqueça da vírgula no final da linha e procure manter nessa mesma ordem.

Você também vai precisar adicionar uma classe de _middleware_ para ouvir suas respostas:

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```

A ordem aqui também é importante.

Por fim, adicione a seguinte linha ao final do arquivo `settings.py`:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

Feito isso, reinicie o servidor e tudo deve funcionar.

# 9 - API Rest do projeto Garagem

-   Volte ao projeto `Garagem`
-   Crie as classes, baseadas no arquivo `models.py` abaixo.
-   Depois, crie a API REST com o Django Rest Framework para todas as entidades.
-   Não esqueça de adicionar o DRF ao seu projeto.
-   Depois, teste tudo!

```python
class Categoria(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="carros")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="carros"
    )
    ano = models.IntegerField(null=True, blank=True)
    cor = models.CharField(max_length=50, null=True, blank=True)
    preco = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.cor} ({self.ano})"
```

# 10 - Deploy no Heroku

**Instalação e configuração do gunicorn**

O **gunicorn** é um servidor web. Adicione-o ao seu projeto assim:

    poetry add gunicorn

Crie o arquivo `Procfile` na raiz do projeto e adicione esse conteúdo:

    web: gunicorn livraria.wsgi

Lembrando que `livraria` é o nome do projeto e precisa ser alterado a cada projeto criado.

**Instalação do whitenoise**

O **whitenoise** é um servidor de arquivos estáticos. Adicione-o ao seu projeto assim:

    poetry add whitenoise

Edite seu arquivo `settings.py` e faça as alterações abaixo.

Adicione o **whitenoise** ao final da lista de `MIDDLEWARE`:

```python
MIDDLEWARE = [
    ...
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]
```

<!-- Adicione também a seguinte linha ao final do arquivo:

```python
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
``` -->

Modifique a linha do `ALLOWED_HOSTS`, para que fique assim:

```python
ALLOWED_HOSTS = ["*"]
```

Import o módulo `os` no início do arquivo:

```python
import os
```

E adicione a seguinte linha ao final do arquivo:

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Por fim, execute o seguinte comando no terminal, para coletar os arquivos estáticos:

    python manage.py collectstatic --noinput

**Criação do arquivo `requirements.txt`**

Execute o seguinte comando no _poetry shell_:

    poetry export --without-hashes > requirements.txt

Isso irá criar o arquivo `requirements.txt` na raiz do projeto a partir dos pacotes que foram instalados no projeto e que estão listados no arquivo `pyproject.toml`. Esse arquivo contém a lista de pacotes necessários para que o projeto funcione corretamente.

**Criação do projeto no heroku**

-   Garanta que a última versão do seu projeto esteja no **github**.
-   Entre no [Heroku](https://dashboard.heroku.com/) e crie uma nova aplicação.
-   Escolha a opção **Conectar no GitHub**
-   Selecione o repositório desejado.
-   Clique na opção **Enable Automatic Deploy**
-   Clique na opção **Deploy Branch**.
-   Se tudo der certo, aparecerá uma opção **View** para você entrar na aplicação.
-   O link para aplicação é https://livraria.herokuapp.com/

# 11 - Relacionamento n para n

**Model com ManyToManyField - Livros com vários autores**

Um livro pode ter vários autores, por isso criaremos agora um relacionamento n para n entre `Livro` e `Autor`. Para isso utilizaremos um campo do tipo `ManyToManyField`.

Inclua o seguinte atributo na _model_ `Livro`:

```python
...
autores = models.ManyToManyField(Autor, related_name="livros")
...
```

Como sempre que alteramos um modelo precisamos fazer a migração das tabelas do banco de dados, precisamos executar os seguintes comandos no terminal:

    python manage.py makemigrations

e

    python manage.py migrate

Feito isso, observe no banco de dados que esse campo não foi criado na tabela de livros. Ao invés disso uma **tabela associativa** foi criada, com o nome `core_livro_autores`, contendo os campos `livro_id` e `autor_id`. É assim que é feito um relacionamento n para n no Django.

**Tarefa**: Entre no **Admin** agora e cadastre alguns livros e autores.

# 12 - Permissões de acesso

Vamos trabalhar agora os conceitos de segurança relacionados a autenticação e permissão (autorização). Utilizaremos aquilo que o Django
já oferece, em termos de usuários e grupos.

Uma estratégia muito utilizada para a definição de permissões de acesso é:

-   criar grupos para perfis de usuários específicos
-   definir as permissões que esse grupo de usuários terá
-   criar um usuários para cada pessoa
-   incluir os usuários nos grupos, dando assim as permissões
-   No caso de mudanças nas permissões, elas são sempre feitas nos grupos, refletindo nos usuários
-   Se um usuário possui mais do que um perfil de permissões, ele deve ser incluído em vários grupos
-   Quando um usuário sai de um cargo ou deve perder seus privilégios, ele é removido do grupo específico

**Resumindo: toda a estratégia de permissões parte da criação de grupos e inclusão ou remoção de usuários desses grupos.**

Observe no **Admin**, para cada usuário em **Usuários (Users)**, as opções de **Permissões do usuário**.

## Criando grupos

Vamos começar criando 2 grupos e dando a eles permissões distintas:

**Grupo compradores**

Crie um grupo chamado `compradores`, com as seguintes permissões:

-   Visualizar autor, categoria e editora
-   Adicionar, editar e visualizar livro

**Grupo administradores**

Crie também um grupo chamado `administradores`, dando a ele **todas** as permissões em categorias, editoras, autores e livros.

## Criando usuários e adicionando aos grupos

-   Crie um usuário `admin1` e o inclua no grupo `administradores`.
-   Crie um usuário `comprador1` e o inclua no grupo `compradores`.

# 13 - Usando as permissões do DRF

## Autenticação e permissão

_A **autenticação** ou **identificação** por si só geralmente não é suficiente para obter acesso à informação ou código. Para isso, a entidade que solicita o acesso deve ter **autorização**._ [(Permissões no DRF)](https://www.django-rest-framework.org/api-guide/permissions/)

**Autenticação** significa que um usuário foi **identificado** em um sistema, portanto ele é **conhecido**. Isso se dá, normamente por um sistema de **_login_**.

**Permissão (autorização)** se dá por um esquema de **conceder privilégios**, seja a usuários ou grupos.

Por padrão, qualquer usuário, mesmo sem autenticação, tem acesso irrestrito e permissão de fazer qualquer coisa em uma aplicação.

As permissões podem ser definidas a nível de objeto (nas _views_ ou _viewsets_, por exemplo) ou de forma global, no arquivo `settings.py`.

## Exemplo de uso de permisssão na viewset

Como ilustração, modifique o arquivo `views.py`, da seguinte forma.

Importe a seguinte função:

```python
from rest_framework.permissions import IsAuthenticated
```

Inclua também a seguinte linha na `CategoriaViewSet`:

```python
permission_classes = [IsAuthenticated]
```

Para testar:

-   Encerre a sessão do **Admin**
-   Tente acessar as **categorias** pelo DRF.
-   Você deve receber um erro.
-   Agora entre novamente pelo **Admin**.
-   Tente acessar as **categorias** pelo DRF.
-   Você deve conseguir.

## Exemplo de uso de permisssão no `settings.py`

Outra forma de gerencimento de permissões é feita no arquivo `settings.py`. Para isso, utilizá-la, comente as últimas alterações feitas no arquivo `views.py`.

Uma forma de conseguir o mesmo resultado de forma padrão para todo o projeto, isto é, só permitir acesso a todos os _endpoints_ para usuários autenticados é configurar desse modo o arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

Inclua o códio acima e teste novamente o acesso aos _endpoints_ do DRF (categorias, editoras, etc.) com e sem uma sessão autenticada.

## Permissões com o DjangoModelPermissions

A forma que iremos adotar para o gerenciamento de permissões será com o uso do [DjangoModelPermissions](https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions).

Esta classe de permissão está ligada às permissões do modelo `django.contrib.auth` padrão do Django. Essa permissão deve ser aplicada apenas a visualizações que tenham uma propriedade `.queryset` ou método `get_queryset()` (exatamente o que temos).

A autorização só será concedida se o usuário estiver autenticado e tiver as permissões de modelo relevantes atribuídas, da seguinte forma:

-   As solicitações `POST` exigem que o usuário tenha a permissão de adição (`add`) no modelo.
-   As solicitações `PUT` e `PATCH` exigem que o usuário tenha a permissão de alteração (`change`) no modelo.
-   As solicitações `DELETE` exigem que o usuário tenha a permissão de exclusão (`remove`) no modelo.

Para isso, teremos que alterar a classe de autenticação:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    ...
}
```

**Resumindo, utilizaremos a estrutura de usuários, grupos e permissões que o próprio Django já nos fornece.**

Para utilizar essa estrutura de permissões corretamente, precisaremos de um sistema de autenticação (`login`) no nosso projeto, de forma a enviar essas informações via a `URL`. Utilizaremos o **SimpleJWT**.

# 14 - Uso do SimpleJWT para autenticação no DRF

## Um resumo sobre autenticação e autorização

Relembrando o que estudamos até aqui em termos de autenticação e autorização:

-   Como criar grupos e usuários e inserir os usuários nesses grupos
-   Como dar permissões nas models (via **Admin**) para visualização (`view`), adição (`add`), alteração (`change`) e exclusão (`remove`).
-   Como utilizar diversas formas de gerenciamento de permissões no Django, incluindo as permissões em cada `view` ou as permissões padrão no `settings.py`.
-   Como utilizar o `DjangoModelPermissions` para fazer uso do gerenciamento de permissões já incluído no **Django Admin**.

Agora, vamos utilizar o **SimpleJWT** para a autenticação no **Django REST Framework**.

**Resumindo, utilizaremos o SimpleJWT para autenticação e a estrutura de permissões do Django para autorização.**

## O SimpleJWT

O [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) é um plug-in de autenticação JSON Web Token para o Django REST Framework.

**Instalação**

Para instalar, execute o seguinte comando no _poetry shell_:

```shell
poetry add djangorestframework-simplejwt
```

**Configuração**

Adicione a forma de autenticação no arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}
```

Inclua também as rotas no arquivo `urls.py`:

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```

Por fim, adicione o **SimpleJWT** a lista de `INSTALLED_APPS`, no `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]
```

Feitas essa aterações, coloque o servidor do Django novamente em execução.

Pata testar se tudo deu certo, utilizaremos algum cliente HTTP, como **Postman**, **Insomnia**, **Thunder Client** ou **RapidAPI**.

# 15 - Testando as permissões dos endpoints usando um cliente HTTP

## Colocando as informações do token na requisição

Feita a instalação e a configuração do SimpleJWT, podemos testar seu funcionamento. Para isso utilize um cliente HTTP.

**Dica: se sua ferramenta permitir, crie várias requisições separadas para cada tipo de requisição, como autenticação, consulta, inclusão, etc.**

Ao tentar acessar, por exemplo, o seguinte _endpoint_:

```
http://localhost:8000/categorias/
```

Você deverá receber uma resposta parecida com essa:

```json
{
    "detail": "As credenciais de autenticação não foram fornecidas."
}
```

Para fazer a autenticação, precisamos enviar as informações de usuário e senha. Faremos isso enviando uma requisição do tipo `POST`, com as seguintes informações:

```json
{
    "username": "admin1",
    "password": "minhasenha1"
}
```

O endereço é o seguinte:

```
http://localhost:8000/token/
```

Não esqueça da barra (`/`) final no endereço e lembre-se que essa é uma requisição do tipo `POST`.

Você deve receber uma resposta semelhante a essa:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTcyNDUxMCwiaWF0IjoxNjYxNjM4MTEwLCJqdGkiOiJiN2RhNWZkMjEwYTI0NjliOWE0MjgxZjQxZDcwNjZhMCIsInVzZXJfaWQiOjN9.lATd6io76oVa6nW5zuBEtsa8htvsL6wVhp-KzXMK-rk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNjM4NDEwLCJpYXQiOjE2NjE2MzgxMTAsImp0aSI6ImRhYTBmNDcyZDI3YTQ5ZTM4M2I4ZjJhOTcwYjhlMWNmIiwidXNlcl9pZCI6M30.HY2j0L6eQBaPxAoHrPz_KFK_sWyb9lHmR7dQ1sOPTNY"
}
```

A cada chamada ao sistema, precisaremos enviar no cabeçalho da requisição um campo com o nome `Authorization` (autorização) com tipo `Bearer ` com essa chave que foi definida no campo `access`.

Para fazer isso, inclua em `Headers` um nova entrada, com se seguintes informações:

-   KEY (Header Name): `Authorization`
-   Value: `Bearer` + `valor da chave accesss`. (O valor desse token muda a cada nova autenticação.)
-   -   Por exemplo: `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNjM4NDEwLCJpYXQiOjE2NjE2MzgxMTAsImp0aSI6ImRhYTBmNDcyZDI3YTQ5ZTM4M2I4ZjJhOTcwYjhlMWNmIiwidXNlcl9pZCI6M30.HY2j0L6eQBaPxAoHrPz_KFK_sWyb9lHmR7dQ1sOPTNY`

Para testar, acesse com `GET` o seguinte endereço:

```
[GET] ​http://localhost:8000/categorias/
```

Você deverá conseguir visualizar todas as categorias cadastradas.

## Token expirado

```json
{
    "detail": "O token informado não é válido para qualquer tipo de token",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "O token é inválido ou expirado"
        }
    ]
}
```

## Testando com outro usuário

Repita o processo de autenticação e consulta com o usuário `comprador1` que criamos anteriormente.

Resumindo, você vai precisar:

-   Criar uma requisição de autenticação, do tipo `POST`, para a URL `token`, enviando as informações de usuário e senha.
-   Copiar a chave do tipo `access` e colocá-la no cabeçalho `Authorization` da requisição do tipo `GET` que vocẽ fará.

## Tentando alterar uma informação

```
[POST] ​http://localhost:8000/categorias/10/
```

```json
{
    "descricao": "Cobol"
}
```

```json
{
    "detail": "Método \"POST\" não é permitido."
}
```

Com isso, fizemos um sistema básico de autenticação (login) e autorização (permissões) usando o próprio sistema já fornecido pelo Admin do Django.

<!-- Aulas futuras -->

<!-- Reestruturação inicial das pastas para as models, views e serializers -->
criar a pasta
criar o __init__.py
separar as informações

<!-- Adicionando campos ao usuário padrão -->
- Explicar que essa é uma estratégia mais simples, mas que dá de fazer sem perder os dados.
- Editar settings.py e models.py 
- Apagar as migrations e dbsqlite
- makemigrations core && migrate
- Editar admin.py incluindo as informaçoes de BaseAdmin e incluindo os campos adicionais

<!-- Settings para dev e produção -->

<!-- Configuração do isort (junto com black). -->

<!-- Vuejs com autenticação e autorização. -->

<!-- Upload e associação de Imagens -->

1a etapa
- baixar pasta media e utils (remover referencias de backend)
- instalar python-magic e Pillow
- settings.py
  - INSTALLED_APPS
  - configurações de MEDIA
  - urls.py
- makemigrations media && migrate

2a etapa
- Adicionar campo Image na model
- Referenciar no serializer

<!-- # Uso do Django Shell para acessar as models -->

<!-- Populate script  -->

<!-- # Model de compras integrando com Model User do Django  -->

<!-- # Criar model StatusCompra -->

<!-- Criar model ItensCompra -->

<!-- # Uso de TabularInline no Admin para Itens da Compra -->

<!-- Endpoint para listagem básica de Compras -->

<!-- #  Ajustes na visualização do status de compra e itens de compra -->
