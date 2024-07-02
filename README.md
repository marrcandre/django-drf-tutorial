# Django com DRF - 2023

Tutorial para desenvolvimento de APIs REST usando o [Django](https://www.djangoproject.com/) com [DRF](https://www.django-rest-framework.org/) (Django Rest Framework). Esse tutorial foi construído a partir do curso em vídeo [Django com DRF](https://www.youtube.com/playlist?list=PL6u1VNwqZdJZT5lCMbBQA1UHVWy0FOYOl) do [Eduardo da Silva](https://github.com/eduardo-da-silva).

Este tutorial está em constante desenvolvimento. Envie sugestões e correções para meu [email](mailto:marcoandre@gmail.com). Se preferir, faça uma [solicitação de contribuição ao projeto](#contribua).

## Trilha do Curso

Esse curso é parte de uma trilha de aprendizado. Siga os links abaixo para acessar os outros cursos da trilha:

- **[Programação I](https://github.com/ldmfabio/Programacao)**  ([Prof. Fábio Longo de Moura](https://github.com/ldmfabio))
    - Lógica de Programação usando JavaScript
- **[Desenvolvimento Web II](https://eduardo-da-silva.github.io/aula-desenvolvimento-web/)** ([Prof. Eduardo da Silva](https://github.com/eduardo-da-silva))
  - Desenvolvimento front-end com VueJS
- **[Desenvolvimento Web III](https://github.com/marrcandre/django-drf-tutorial)** ([Prof. Marco André Lopes Mendes](https://github.com/marrcandre/))
  - Desenvolvimento back-end com Django e DRF.

Bons estudos!

---

# 1. Preparação do ambiente

A preparação do ambiente será feita apenas uma vez em cada computador. Ela consiste em instalar e configurar o **VS Code**, o **PDM** e o **Python**.

- [Instale ou atualize o VS Code](#a0-instalação-do-vs-code).
- [Instale e sincronize as extensões do VS Code.](#a0-instalação-e-sincronização-de-extensões-do-vs-code)
- [Instale e configure o PDM](#a0-instalação-e-configuração-do-pdm)

<!-- TODO: Inserir na seção de resolução de erros. -->

<!-- **1.2.6 Instalação de plugins do PDM**

**1.2.7 Instalação do plugin pdm-autoexport**

Instale o plugin `pdm-autoexport`, que atualiza automaticamente o arquivo `requirements.txt`, cada vez que você instalar um pacote:

```shell
pdm plugin add pdm-autoexport
```

Para configurar o plugin, edite o arquivo `pyproject.toml` e adicione a seguinte linha:

```toml
[[tool.pdm.autoexport]]
filename = "requirements.txt"
without-hashes = "true"
```
-->

<!-- **1.2.8 Configuração do Navegador de Arquivos**

-   No **Gnome Shell**, inclua o VS Code no menu de contexto do navegador de arquivos (_"Abrir com Code"_):

```shell
wget -qO- https://raw.githubusercontent.com/cra0zy/code-nautilus/master/install.sh | bash
``` -->

<!-- **1.3 Instalação do Python**

-   Verifique se o **python** está instalado:

```shell
python -V
```

-   Se o python não estiver instalado, verifique se o python3 está instalado:

```shell
python3 -V
```

-   Nesse caso, você pode criar um link simbólico para o python3:

```shell
sudo ln -s /usr/bin/python3 /usr/bin/python
```

-   Ou ainda, criar um `alias` (apelido) para o python3:

```shell
echo "alias python=python3" >> ~/.bashrc
``` -->

# 2. Criação do projeto

**2.0 O projeto Livraria**

**Modelo Entidade Relacionamento**

![Modelo ER](diagramas/livraria_MER.png "Modelo ER")

**Diagrama de Classes**

![Diagrama de Classes](diagramas/livraria_classes.png "Diagrama de Classes")

**2.1 Criação da pasta do projeto**

-   Abra o navegador de arquivos:

    `Windows + E`

-   Entre na pasta **Documentos** ou crie uma pasta **projetos**.
-   Crie uma pasta chamada `livraria` (ou outro nome de sua preferência) para o seu projeto.
-   **IMPORTANTE**:
    -   Não trabalhe na `Área de Trabalho` ou na pasta `Downloads`.
    -   Certifique-se de que **nenhuma pasta** no caminho tenha **espaços** ou **acentos** (**se você não fizer isso, terá que recriar todo o projeto**).
-   Dentro dessa pasta, abra um terminal:

    _Botao direito do mouse -> Abrir terminal aqui_

**2.2 Criação do projeto no PDM**

-   Crie uma pasta chamada `livraria` para o seu projeto.

```shell
mkdir livraria
```

-   Entre na pasta do projeto:

```shell
cd livraria
```

-   Crie o projeto com o **PDM**:

```shell
pdm init
```

-   Você passará por uma tela semelhante a essa:

```shell
Creating a pyproject.toml for PDM...
Please enter the Python interpreter to use
1. /usr/bin/python (3.10)
2. /usr/bin/python3.10 (3.10)
3. /home/marco/.local/share/pdm/venv/bin/python (3.10)
Please select (0):
Using Python interpreter: /usr/bin/python (3.10)
Would you like to create a virtualenv with /usr/bin/python? [y/n] (y): n
You are using the PEP 582 mode, no virtualenv is created.
For more info, please visit https://peps.python.org/pep-0582/
Is the project a library that will be uploaded to PyPI [y/n] (n): n
License(SPDX name) (MIT):
Author name (Marco André Mendes):
Author email (marcoandre@gmail.com):
Python requires('*' to allow any) (>=3.10):
Changes are written to pyproject.toml.
```

-   Verifique se o **PDM** criou o arquivo `pyproject.toml`:

```shell
ls -l pyproject.toml
```

**2.3 Abrindo o projeto no VS Code**

-   Abra o projeto no VS Code:

```shell
code .
```

Você pode abrir o projeto no VS Code de duas formas:

-   Digitando o comando `code .` no terminal.
-   Pelo gereciador de arquivos, clicando com o botão direito do mouse na pasta do projeto e selecionando a opção **Abrir com o VS Code**.
-   Clicando no botão **Abrir pasta** e selecionando a pasta do projeto.

**IMPORTANTE:**

-   Sempre abra a **pasta raiz do projeto** no VS Code (repita em voz alta: _"**Nunca** abra um **arquivo**, **sempre** abra a **pasta**."_).
-   O VS Code precisa dessa informação de qual é a pasta raiz do projeto para funcionar corretamente.

**2.4 Instalação do Django**

-   Abra o terminal do VS Code:

    Ctrl + Shift + `

-   Instale o **Django** no seu projeto:

```shell
pdm add django
```

-   Verifique se o arquivo `pdm.lock` foi criado:

```shell
ls -l pdm.lock
```

-   Verifique a versão do **Django** instalado:

```shell
pdm run django-admin --version
```

**2.5 Criação do projeto no Django**

Um projeto no **Django** é uma pasta com um conjunto de arquivos e pastas que contém o código do seu site. Vamos criar um projeto chamado `config`.

-   Crie o projeto no **Django**:

```shell
pdm run django-admin startproject config .
```

**IMPORTANTE**: o ponto no final é importante. Ele indica que o projeto será criado na pasta atual.

O projeto criado ficará assim:

```
.
├── .vscode
│   ├── settings.json
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pdm.lock
├── pyproject.toml
└── requirements.txt
```

**2.6 Rodando o servidor de desenvolvimento**

-   Para executar o projeto, digite no terminal:

```shell
pdm run python manage.py runserver
```

-   Verifique se o projeto está rodando:

    -   Página inicial: http://localhost:8000
    -   `Admin`: http://localhost:8000/admin

-   Ao rodar o projeto pela primeira vez, o arquivo `db.sqlite3` é criado.
-   Também aparecem mensagens de erro importantes.
-   Abra o arquivo `db.sqlite3` dentro do **VS Code**.
-   Verifique que ele ainda não possui nenhuma tabela.

-   Vamos abrir cada um desses arquivos e verificar para que eles servem, principalmente os seguintes:

    -   `manage.py`: é o arquivo que você usa para executar comandos do **Django**.
    -   `settings.py`: é o arquivo de configuração do projeto.
    -   `urls.py`: é o arquivo de configuração das rotas do projeto.
    -   `db.sqlite3`: é o arquivo de banco de dados do projeto.

**2.7 Executando o servidor**

Desse ponto em diante, abra um outro terminal lado a lado no **VS Code**, mantendo sempre o django em execução (`runserver`) no outro terminal.

Se precisar parar a execução do projeto, aperte `Control+C` e depois o execute novamente.

**2.8 Criando a base de dados inicial**

-   Para resolver o erro informado no momento de rodar o projeto, execute o seguinte comando:

```shell
pdm run python manage.py migrate
```

Verifique se o projeto continua rodando e se o [Admin](http://localhost:8000) está em execução.

**2.9 Criando o superusuário**

-   Crie o super usuário para poder fazer o login:

```shell
pdm run python manage.py createsuperuser
```

-   Agora sim, seu projeto está rodando e você consegue entrar no `Admin`:

-   Crie mais 2 usuários de teste.
-   Entre no arquivo de banco de dados (`db.sqlite3`), e verifique se os registros foram criados.

**2.10 Exercício**

-   Apague o projeto e crie novamente, seguindo as instruções acima.
-   Verifique se o projeto está rodando e se o `Admin` está em execução.
-   Observe que configurações precisam ser feitas novamente e quais não foram mais necessárias.

# 3. Criação de uma aplicação

Uma aplicação no **Django** é um conjunto de arquivos e pastas que contém o código de uma funcionalidade específica do seu site.

**3.1 Criando uma aplicação**

-   Para criar uma aplicação, execute o seguinte comando:

```shell
pdm run python manage.py startapp livraria
```

**3.2 Instalando a aplicação**

-   Acrescente a aplicação `livraria` na seção `INSTALLED_APPS` do arquivo `settings.py` do seu projeto.

```python
INSTALLED_APPS = [
    ...
    "livraria",
]
```

Após criar a aplicação, sua pasta deve parecer com isso:

```
.
├── config
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── livraria
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── pdm.lock
└── pyproject.toml
```

Dentro da pasta `livraria` foram criados alguns arquivos, mas os mais importantes são:

-   `admin.py`: é o arquivo de configuração do `Admin`, uma ferramenta que permite que você gerencie os dados do seu site.
-   `models.py`: é o arquivo de configuração dos modelos (entidades) da aplicação.
-   `views.py`: é o arquivo de configuração das `views` da aplicação.
-   `migrations`: é a pasta de migrações de banco de dados da aplicação.

Posteriormente, iremos modificar esses arquivos, bem como incluir alguns arquivos novos.

**3.3 Resumo**

Nesse ponto, temos:

-   O projeto criado no `PDM`;
-   O projeto django chamado `config` criado;
-   A aplicação `livraria` criada e instalada no projeto.

**3.4 Criação do primeiro modelo de dados**

Um modelo (`model`) no **Django** é uma classe que representa uma tabela no banco de dados. Cada atributo (variável) dessa classe representa um campo da tabela.

Para maiores informações consulte a [documentação](https://docs.djangoproject.com/en/4.0/topics/db/models/) do **Django** sobre `models`.

-   Vamos começar criando o modelo de dados `Categoria`, que representa uma categoria de livro, como por exemplo: `Ficção`, `Terror`, `Romance`, etc.

-   Abra o arquivo `models.py` da aplicação `livraria` e adicione o seguinte código:

```python
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
```

Nesse código, você:

-   Importou o pacote necessário para criar a `model`;
-   Criou a classe `Categoria`;
-   Incluiu o campo `descricao`.

**3.5 Efetivando a criação da tabela**

Precisamos agora efetivar a criação da tabela no banco de dados.

-   Abra um novo terminal, deixando o terminal antigo executando o servidor do projeto.

-   Crie as migrações:

```shell
pdm run python manage.py makemigrations
```

-   Execute as migrações:

```shell
pdm run python manage.py migrate
```

-   Acesse o arquivo do banco de dados (`db.sqlite3`) e verifique se a tabela `livraria_categoria` foi criada.
-   Acesse o [Admin](http://localhost:8000) do projeto e verifique se a nova tabela aparece lá.

**3.6 Inclusão no Admin**

A tabela ainda não apareceu, certo? Isso acontece poque ainda não incluímos a `model` no `Admin`.

-   Vamos incluir a `model` no `Admin`. Abra o arquivo `admin.py` da aplicação `livraria` e adicione o seguinte código:

```python
from django.contrib import admin

from .models import Categoria

admin.site.register(Categoria)
```

Acesse novamente o [Admin](http://localhost:8000/admin) e inclua algumas categorias no banco de dados.

**3.7 Mudando a língua e time zone**

Encontre e edite as seguintes linhas no arquivo no arquivo `settings.py`:

```python
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
```

Acesse novamente o [`Admin`](http://localhost:8000) e verifique que agora ele está em português.

**3.8 O campo `id`**

O campo `id` é criado automaticamente pelo **Django**. Ele é o identificador único de cada registro da tabela.

**3.9 Mudando a forma de exibição dos registros criados**

-   Inclua algumas categorias no banco de dados.
-   Você perceberá que a descrição dos informações que você inclui está meio estranha.
-   Para resolver, isso, vamos fazer uma pequena modificação na `model Categoria`.

**3.10 O método `__str__`**

O método `__str__` é um método especial que é chamado quando você tenta imprimir um objeto. Ele é utilizado no `Admin` e em outros locais para definir como o objeto será exibido.

-   Vamos incluir o método `__str__` na `model Categoria`:

```python
...
    def __str__(self):
        return self.descricao
```

Volte ao [`Admin`](http://localhost:8000) verifique o que mudou na apresentação dos objetos da model `Categoria`.

**3.11 Criação do modelo de dados Editora**

-   Vamos criar o modelo de dados `Editora`, no arquivo `models.py`:

```python
...

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
```

**Observação:** O atributo `null=True` indica que o campo pode ser nulo. O atributo `blank=True` indica que o campo pode ser deixado em branco. Na prática, usamos esses atributos quando queremos que um campo seja **opcional**.

Não esqueça de que a cada criação de novas `models`, é necessário:

-   Registrar a model no arquivo `admin.py`;
-   Fazer as migrações (`makemigrations`);
-   Efetivar as migrações (`migrate`);

Seu arquivo `admin.py` ficará assim:

```python
from django.contrib import admin

from livraria.models import Categoria, Editora

admin.site.register(Categoria)
admin.site.register(Editora)
```

Após fazer isso tudo, inclua algumas editoras na tabela e veja como ficou o seu banco de dados.

# 4. Colocando o projeto no GitHub

**4.1 Um aviso importante**

Antes de mais nada, seguem **3 regras** a serem consideradas ao seguir as instruções:

-   **Antes de clicar ou responder, leia atentamente as instruções.**
-   **Leia atentamente as instruções antes de clicar ou responder.**
-   **Nunca clique ou responda sem antes ler atentamente as instruções.**

As 3 regras falam a mesma coisa? Sim, você entendeu o recado. ;-)

**4.2 Configurando o projeto git**

-   Se o computador estiver configurado com contas individuais, você precisará fazer isso apenas uma vez. Ainda assim, é bom verificar se está tudo certo.
-   Verifique se já não existe uma conta conectada ao **GitHub** no **VS Code**, clicando no ícone **Contas** na barra lateral esquerda. Deve ser o penúltimo ícone da baixo pra cima. Se houver, **desconecte primeiro**.
-   Inicialize o repositório **git**. Clique no ícone do **git** no painel lateral esquerdo. Deve ser o segundo ícone, de cima pra baixo. Opcionalmente, tecle (`Control+Shift+G`). Depois, clique no botão `Initialize repository`.
-   Se aparecer uma bolinha azul no ícone do git com um número, o repositório foi ativado. Esse número indica o número de arquivos que foram criados ou alterados.
-   Se aparecem muitos arquivos alterados (10 mil, por exemplo), é provável que exista um repositório **git** criado na pasta raiz do usuário. Apague esse repositório assim:

```shell
rm -Rf ~/.git
```

-   Recarregue a janela do **VS Code**:

```shell
Control + Shift + P + "Recarregar a Janela"
```

-   Verifique se o número mudou para algo mais razoável (em torno de 100 arquivos).

**4.3 Configurando as variáveis do git**

-   Informe seu nome e email no git. Para isso, abra o terminal do VS Code e digite:

```shell
git config --global user.name "Seu Nome"
git config --global user.email "seuEmailNoGitHub@gmail.com"
```

-   Para verificar se as variáveis foram configuradas corretamente, digite:

```shell
git config -l
```

-   Se aparecer outro nome de usuário ou outras informações estranhas, remova o arquivo com as configurações globais do git:

```shell
rm ~/.gitconfig
```

Repita o processo de configuração de nome e email.

**4.4 Criando o arquivo `.gitignore`**

Vamos criar um arquivo chamado `.gitignore` na raiz do projeto. Esse arquivo serve para indicar quais arquivos não devem ser versionados (monitorados pelo **git**).

-   Vá no site [gitignore.io](https://gitignore.io/)
-   Escolha as opções `Python` e `Django`.
-   Clique em `Criar`.
-   Selecione todo o texto (`Control + A`) e copie (`Control + C`).
-   Crie um arquivo novo na raiz do projeto e dê o nome de `.gitignore`:

```shell
touch .gitignore
```

-   Cole o conteúdo copiado (`Control + V`).
-   Encontre as linhas que se referem a "`db.sqlite3`" e comente-as (`Control + /`).

**4.5 Publicando o projeto**

-   Escreva uma descrição para o commit (`"commit Inicial"`, por exemplo.).
-   Tecle `Control+ENTER` para fazer o envio para o servidor do **GitHub**.
-   Leia atentamente as instruções relacionadas a autenticação no **GitHub** e criação do projeto.
-   Ao final, seu projeto será incluído no **GitHub** e você poderá visulizá-lo lá.

**4.6 Fazendo alterações no projeto e enviando novamente**

Vamos agora realizar algumas mudanças no projeto e enviá-lo novamente para o **GitHub**.

-   Abra o arquivo `models.py`:

```shell
Control + P + models.py
```

-   Selecione todo o texto (`Control + A`) e mande formatar o código:

```shell
Control + Shift + I
```

ou

```shell
Control + Shift + P + "Formatar o Documento"
```

-   Deve aparecer uma mensagem pedindo para instalar um **formatador de código** (`black`). Concorde com a instalação.
-   Após a instalação, execute o comando para formatar novamente. O arquivo deve ser formatado.
-   Faça a mesma coisa com o arquivo `admin.py`.
-   Altere outros arquivos. Por exemplo: apague os comentários iniciais dos arquivos `settings.py` e `urls.py`.
-   Nesse ponto, você já deve ter vários arquivos modificados.
-   Vá para a aba do **GitHub** no **VS Code** e coloque o nome do **commit** como sendo `Formatação dos arquivos do projeto`.
-   Confirme o **commit** teclando `Control+ENTER`.
-   Faça o envio (`push`), clicando no ícone de envio.
-   Vá no seu projeto no **GitHub**, atualize a página e verifique as modificações.

**IMPORTANTE: Escrevendo uma boa mensagem de commit**

-   Escreva uma mensagem de commit que descreva o que foi feito.
-   Dessa forma fica mais fácil identificar as mudanças sem precisar ver o código.
-   Não escreva mensagens como `Alteração 1`, `Alteração 2`, `Alteração 3`, etc.
-   Escreva mensagens como:
    -   Modificação do arquivo `models.py`
    -   Inclusão da Categoria de Veículos
    -   Alteração do Marca do Veículo

**4.7 Baixando novamente o projeto**

Agora que seu projeto está no **GitHub**, você pode baixá-lo onde quiser, seja na aula, em casa ou no trabalho, por exemplo. Vamos testar isso.

**A partir desse ponto, vamos repetir uma série de passos que já fizemos nas aulas anteriores. Em caso de dúvidas, volte nessas aulas para mais detalhes.**

-   Feche o projeto no **VS Code**.
-   Abra o terminal na pasta superior à pasta do projeto:

```shell
Control + Alt + T
```

-   Apague todo o projeto do seu computador (_isso mesmo, coragem_):

```shell
rm -rf livraria
# rmdir livraria /s /q # no Windows
```

-   Vá no projeto no **GitHub**, clique no botão **Code** e copie a URL dele. Deve ser algo no seguinte formato: `https://github.com/marrcandre/garagem.git`
-   Clone o projeto para a pasta atual:

```shell
git clone https://github.com/marrcandre/livraria.git #troque essa URL pela sua
```

-   Vá para a pasta do projeto:

```shell
cd livraria
```

-   Abra o projeto no **VS Code**:

```shell
code .
```

-   Instale as dependências do projeto e ative o ambiente virtual:

```shell
pdm install
```

-   Rode o servidor:

```shell
pdm run python manage.py runserver
```

-   Acesse o projeto no navegador:

    http://localhost:8000/

Pronto! Seu projeto está de volta no computador e rodando.

# 5. Criando um segundo projeto

Nessa aula, vamos criar um segundo projeto, o projeto Garagem, com uma aplicação e alguns modelos.

**5.1 [Exercício](): Crie o projeto Garagem**


# 6. Criando os outros modelos de dados

Vamos criar os outros modelos de dados do projeto **Livraria**.

**6.1 Criando o modelo de dados Autor**

-   Vamos criar o modelo de dados `Autor`, no arquivo `models.py`:

```python
...

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
```

**Uso da classe `Meta`**

-   Utilizamos o `verbose_name_plural` para alterar o nome do modelo no plural, que por padrão é o nome do modelo acrescido de `s`. Sem ele, o nome do modelo no plural seria `Autors`.

-   Utilizamos também o `verbose_name` para alterar o nome do modelo no singular. Nesse caso não é necessário, pois o nome do modelo no singular é o mesmo do plural, mas vamos deixar para fins de exemplo.
    Isso é útil quando:
    -   o nome do modelo é muito grande e não cabe no menu do admin. Exemplo: `Categoria de Veículos`.
    -   o nome do modelo é muito pequeno e não é claro. Exemplo: `Cat`.
    -   queremos que o nome apareça com acentos. Exemplo: `Acessório`.

**6.2 Criando o modelo de dados Livro**

-   Vamos criar o modelo de dados `Livro`, no arquivo `models.py`:

```python

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"
```

Antes de efetivarmos as alterações no banco de dados, vamos incluir duas chaves estrangeiras no modelo `Livro`.

**6.3 Incluindo chaves estrangeiras no modelo**

Nosso livro terá uma **categoria** e uma **editora**. Para isso, vamos incluir campos que serão chaves estrageiras, referenciando os modelos `Categoria` e `Editora`.

**6.3.1 Campo `categoria` no `Livro`**

-   Inclua a linha a seguir no modelo `Livro`, logo após o atributo `preco`:

```python
...
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
...
```

-   Vamos entender cada parte:
    -   `models.ForeignKey`: define o campo como sendo uma chave estrangeira.
    -   `Categoria`: o model que será associado a esse campo.
    -   `on_delete=models.PROTECT`: impede de apagar uma _categoria_ que possua _livros_ associados.
    -   `related_name="livros"`: cria um atributo `livros` na classe `Categoria`, permitindo acessar todos os livros de uma categoria.

**6.3.2 Campo `editora` no `Livro`**

-   De forma semelhante, vamos associar o livro a uma editora, incluindo logo em seguida à categoria, a seguinte linha:

```python
editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")
```

**6.4 Inclusão dos modelos no `Admin`**

-   Inclua os modelos criados no arquivo `admin.py`:

```python
from django.contrib import admin

from livraria.models import Autor, Categoria, Editora, Livro

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
```

**6.5 Efetivando as alterações no banco de dados**

-   Prepare as migrações:

```shell
pdm run python manage.py makemigrations
```

-   Efetive as migrações:

```shell
pdm run python manage.py migrate
```

**6.6 Testando o atributo `on_delete`**

Feito isso, verifique se tudo funcionou.

No `Admin`:

-   Cadastre algumas categorias, editoras, autores e livros.
-   Note como os livros acessam as categorias e editoras já cadastradas.
-   Tente apagar uma editora ou categoria **com** livros associados.
    -   O que aconteceu?
    -   Por que isso aconteceu?
-   Tente apagar uma editora ou categoria **sem** livros associados.
    -   O que aconteceu?
    -   Por que isso aconteceu?

**6.7 Testando o atributo related_name no Django Shell**

No `Django Shell` (que iremos estudar em mais detalhes em uma aula mais adiante), é possível testar o acesso a **todos os livros de uma categoria** usando algo parecido com isso:

-   Abra o Django shell:

```shell
pdm run python manage.py shell
```

-   Acesse os livros da categoria com `id` 1:

```python
>>> from livraria.models import Categoria
>>> Categoria.objects.get(id=1).livros.all()
```

**6.8 [Exercício](#aula-6-crie-os-demais-modelos-de-dados-no-projeto-garagem): Crie os demais modelos de dados no projeto Garagem**


# 7. Criando uma API REST

Nessa aula, vamos criar uma API REST para o projeto `livraria`. Ao final, teremos uma API que permite criar, listar, atualizar e deletar categorias, editoras, autores e livros.



**7.1 Instalação do DRF**

-   Instale o `djangorestframework`:

```shell
pdm add djangorestframework
```

-   Adicione o `rest_framework` no arquivo `settings.py`:

```python
INSTALLED_APPS = [
...
    "rest_framework",
    "livraria",
]
```

**7.2 Criação do serializer**

Um _serializer_ é um objeto que transforma um objeto do banco de dados em um objeto JSON.

-   Crie o arquivo `serializers.py` no diretório `livraria`:

```shell
touch livraria/serializers.py
```

-   Adicione o seguinte código no arquivo `serializers.py`:

```python
from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
```

**7.2.1 Explicando o código**

-   `model = Categoria`: define o model que será serializado.
-   `fields = "__all__"`: define que todos os campos serão serializados.

**7.3 Criação da view**

Uma _view_ é um objeto que recebe uma requisição HTTP e retorna uma resposta HTTP.

-   Crie a view `CategoriaViewSet` no arquivo `views.py`:

```python
from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
```

**7.3.1 Explicando o código**

-   `queryset = Categoria.objects.all()`: define o conjunto de objetos que será retornado pela view.
-   `serializer_class = CategoriaSerializer`: define o serializer que será utilizado para serializar os objetos.

**7.4 Criação das rotas (urls)**

As rotas são responsáveis por mapear as URLs para as views.

-   Para criar as rotas da `Categoria`, edite o arquivo `urls.py` na pasta `config`. Substitua o seu conteúdo por esse:

```python
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
```

**IMPORTANTE**: as nomes das rotas serão sempre nomes **únicos**, no **plural** e em **minúsculas**.

**7.5 Testando a API**

-   Para acessar a interface gerada pelo DRF, acesse:

    http://localhost:8000

Se tudo correu bem, você deve ver a interface do DRF.

-   Você pode acessar diretamente a rota da `Categoria`:
    http://localhost:8000/categorias/

Isso deve trazer todas as categorias do banco, no formato **JSON**.

-   Para acessar um único registro, use o seguinte formato:
    http://localhost:8000/categorias/1/

Nesse caso, `1` é o `id` do registro no banco de dados.

**7.6 Opções de manipulação do banco de dados**

As opções disponíveis para manipulação dos dados são:

-   **GET** para **listar** **todos** os registros: http://localhost:8000/categorias/
-   **GET** para **listar** **apenas 1** registro: http://localhost:8000/categorias/1/
-   **POST** (para **criar** um **novo** registro): http://localhost:8000/categorias/
-   **PUT** (para **alterar** um registro existente): http://localhost:8000/categorias/1/
-   **PATCH** (para **alterar parcialmente** um registro): http://localhost:8000/categorias/1/
-   **DELETE** (para **remover** um registro): http://localhost:8000/categorias/1/

**7.7 Outras ferramentas para testar a API**

A interface do DRF é funcional, porém simples e limitada. Algumas opções de ferramentas para o teste da API são:

-   [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) (extensão do **VS Code**)
-   [RapidAPI](https://marketplace.visualstudio.com/items?itemName=RapidAPI.vscode-rapidapi-client) (extensão do **VS Code**)
-   [Insomnia](https://docs.insomnia.rest/insomnia/install) (externo)
-   [Postman](https://www.postman.com/downloads/) (externo)

**7.8 Testando a API e as ferramentas**

Instale uma ou mais das ferramentas sugeridas.

-   Experimente as seguintes tarefas:
    -   Criar uma ou mais categorias;
    -   Listar todas as categorias;
    -   Alterar uma ou mais categorias, utilizando PUT e PATCH;
    -   Listar a categoria alterada;
    -   Remover uma categoria;
    -   Incluir outra categoria;
    -   Listar todas as categorias.

**7.9 [Exercício](#aula-7-crie-a-api-rest-no-projeto-garagem): Crie a API REST no projeto Garagem**



# 8. Continuando a criação da API REST

Vamos continuar a criação da API REST para o projeto `livraria`.

**8.1 Criação da API para a classe Editora**

Crie a API para a classe `Editora` seguindo os passos anteriores.

-   Os passos são:

    -   Criar o serializador em `serializers.py`
    -   Criar a viewset em `views.py`.
    -   Incluir a nova rota em `urls.py`

-   Os arquivos ficarão assim:

**`serializers.py`**

```python
from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora

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

from livraria.models import Categoria, Editora
from livraria.serializers import CategoriaSerializer, EditoraSerializer

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
from livraria.views import CategoriaViewSet, EditoraViewSet
...
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
...
```

**8.2 Teste da API da Editora**

-   Teste todas as operações da `Editora`.
-   Verifique se é possível incluir novas editoras sem incluir todos os campos.
-   Tente utilizar o PUT e o PATCH sem informar todos os campos.
-   Tente remover uma editora com livros associados a ela.

**8.3 Criação da API para Autor e Livro**

**8.3.1 Criação da API para Autor**

-   Crie a API para a classe `Autor` seguindo os passos anteriores.
-   Teste o funcionamento.
-   Faça o commit.

**8.3.2 Criação da API para Livro**

-   Crie a API para a classe `Livro` seguindo os passos anteriores.
-   Teste o funcionamento.
-   **Observou que no `Livro`, aparecem apenas os campos `id` da categoria e da editora, e não o nome?**

**8.4 Criação de múltiplos serializadores**

**8.4.1 Apresentação das informações de categoria e editora no livro**

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
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
```

**8.4.2 Criação de um serializador para a listagem de livros**

-   Crie um serializador para a listagem de livros, que mostre apenas o id, o título e o preço.

```python
class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "titulo", "preco"]
```

-   Altere a viewset para utilizar esse serializador na listagem:

```python
    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
```

-   Teste a API. Observe que a listagem de vários livros está diferente da recuperação de um único livro.

-   Teste a API.

**8.5 [Exercício](#aula-8-crie-a-api-rest-no-projeto-garagem-para-as-demais-classes): Crie a API REST no projeto Garagem para as demais classes**



# 9. Aplicação frontend Vuejs e Django CORS Headers

**9.1 Executando uma aplicação _frontend_ de exemplo**

Faça um `fork` do repositório [https://github.com/marrcandre/livraria-vue-3](https://github.com/marrcandre/livraria-vue3.git) e execute os seguintes comandos:

```shell
npm install
```

```shell
npm run dev
```

> Para maiores detalhes sobre a instalação do npm, acesse o tutorial de [Instalação da versão LTS do NodeJS](https://eduardo-da-silva.github.io/aula-desenvolvimento-web/ambiente) do [Prof. Eduardo da Silva](https://eduardo-da-silva.github.io/aula-desenvolvimento-web/ambiente).

**9.1.1 Diferenças no JSON de retorno com e sem paginação**

Quando a paginação não está ativada, o JSON de retorno é um objeto com a lista de objetos. Quando a paginação está ativada, o JSON de retorno é um objeto com a lista de objetos, mas a lista de objetos está dentro de um objeto `results`.

**Exemplo de `categorias` com a paginação desativada**

```json
[
    {
        "id": 1,
        "descricao": "Ficção"
    },
    {
        "id": 2,
        "descricao": "Terror"
    },
    {
        "id": 3,
        "descricao": "Romance"
    }
]
```

**Exemplo de `categorias` com a paginação ativada**

```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "descricao": "Ficção"
        },
        {
            "id": 2,
            "descricao": "Terror"
        },
        {
            "id": 3,
            "descricao": "Romance"
        }
    ]
}
```
Sendo assim, é importante que a aplicação _frontend_ esteja preparada para lidar com essas diferenças. Essa alterações deverão ser feitas nos arquivos da pasta `src/api` do projeto _frontend_.

Um exemplo é o arquivo `categorias.js`:

```javascript
import axios from "axios";
export default class CategoriasApi {
  async buscarTodasAsCategorias() {
    const { data } = await axios.get("/categorias/");
    return data.results;
  }
  async adicionarCategoria(categoria) {
    const { data } = await axios.post("/categorias/", categoria);
    return data.results;
  }
  async atualizarCategoria(categoria) {
    const { data } = await axios.put(`/categorias/${categoria.id}/`, categoria);
    return data.results;
  }
  async excluirCategoria(id) {
    const { data } = await axios.delete(`/categorias/${id}/`);
    return data.results;
  }
}
```

-----

Se tudo correu bem, execute a aplicação:

http://localhost:3000


> **ATENÇÃO:** Se os dados não aparecerem, entre na opção **Inspecionar** do seu navegador (`Control`+`Shift`+I ou **botão direto - Inspecionar**.)
> Na opção `Console`, verifique se aparece um erro de **CORS**. Se isso ocorrer, siga o tutorial a seguir.

**9.2 Inclusão do Django CORS headers no projeto**

Adicionar o Django CORS headers permite que seu projeto seja acessado de outros domínios. Isso é necessário, por exemplo, para acessar a API através de uma aplicação de _frontend_ feita em _vuejs_.

**No projeto `livraria` (backend), faça o seguinte:**

-   Instale o pacote `django-cors-headers`:

```shell
pdm add django-cors-headers
```

-   Adicione o pacote `corsheaders` em `INSTALLED_APPS` em `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    "corsheaders",
    "rest_framework",
    "livraria",
    ...,
]
```

> Não esqueça da vírgula no final de cada linha e procure manter nessa mesma ordem.

-   Adicione o Middleware `corsheaders.middleware.CorsMiddleware` em `MIDDLEWARE` em `settings.py`:

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```

> **IMPORTANTE**: a ordem aqui precisa ser essa.

Por fim, adicione a seguinte linha ao final do arquivo `settings.py`:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

Feito isso, reinicie o servidor e tudo deve funcionar.


**9.1 Exercício: Crie uma aplicação FrontEnd com Vuejs para a Livraria**

-   Modifique a aplicação frontend com Vuejs para consumir a API REST das demais classes do projeto `Livraria`.

**9.1.2 [Exercício](#aula-9-crie-uma-aplicação-frontend-com-vuejs-para-a-garagem): Crie uma aplicação FrontEnd com Vuejs para a Garagem**


# 10. Relacionamento n para n

**Model com ManyToManyField - Livros com vários autores**

Um livro pode ter vários autores, por isso criaremos agora um relacionamento n para n entre `Livro` e `Autor`. Para isso utilizaremos um campo do tipo `ManyToManyField`.

-   Inclua o campo `autores` no modelo `Livro`:

```python
...
autores = models.ManyToManyField(Autor, related_name="livros")
...
```

-   Crie as migrações:

```shell
pdm run python manage.py makemigrations
```

-   Execute as migrações:

```shell
pdm run python manage.py migrate
```

Feito isso, observe no banco de dados que esse campo não foi criado na tabela de livros. Ao invés disso, uma **tabela associativa** foi criada, com o nome `livraria_livro_autores`, contendo os campos `livro_id` e `autor_id`. É assim que é feito um relacionamento n para n no Django.

**10.1 Exercícios**

**10.1.1 No projeto Livraria**

**10.1.1.1 No Admin**:

-   Entre no **Admin**;
-   Cadastre alguns autores;
-   Cadastre alguns livros com mais do que um autor.

**10.1.1.2 Na API**:

-   Teste a API REST de livros e autores.

**10.2 [Exercício](#aula-10-crie-um-relacionamento-n-para-n-entre-veiculo-e-acessorio-no-projeto-garagem): Crie um relacionamento n para n entre `Veiculo` e `Acessorio` no projeto Garagem**



# 11. Autenticação e autorização

11.1 Introdução

Vamos trabalhar agora os conceitos de segurança relacionados a **autenticação** (_login_) e **autorização** (_permissão_). Utilizaremos aquilo que o Django já oferece, em termos de usuários e grupos.

Uma estratégia muito utilizada para a definição de permissões de acesso é:

-   Criar **grupos** para perfis de usuários específicos.
-   Definir as **permissões** que esse grupo de usuários terá.
-   Criar um **usuário** para cada pessoa que utilizará a aplicação.
-   **Incluir** os usuários nos grupos, dando assim as permissões.
-   No caso de mudanças nas permissões, elas são sempre feitas nos **grupos**, refletindo nos usuários.
-   Se um usuário possui mais do que um perfil de permissões, ele deve ser incluído em **vários** grupos.
-   Quando um usuário sai de uma função ou deve perder seus privilégios, ele é **removido** do grupo específico.

> **Resumindo:** toda a estratégia de permissões parte da criação de grupos e inclusão ou remoção de usuários desses grupos.

> Observe no **Admin**, para cada usuário em **Usuários (Users)**, as opções de **Permissões do usuário**.

**Relação entre nomes das ações**

| Ação      | HTTP        | CRUD   | Admin  |
| --------- | ----------- | ------ | ------ |
| Criar     | POST        | Create | add    |
| Ler       | GET         | Read   | view   |
| Atualizar | PUT (PATCH) | Update | change |
| Deletar   | DELETE      | Delete | delete |

**11.2 Criando grupos e dando permissões**

Vamos começar criando 2 grupos e dando a eles permissões distintas:

-   Crie um grupo chamado `compradores`, com as seguintes permissões:
    -   Visualizar: `autor`, `categoria` e `editora`.
    -   Adicionar, editar e visualizar: `livro`.
-   Crie um grupo chamado `administradores`, com as seguintes as permissões:
    -   Adicionar, editar, visualizar e remover: `autor`, `categoria`, `editora` e `livro`.

**11.3 Criando usuários e adicionando aos grupos**

-   Crie um usuário `admin1` e o inclua no grupo `administradores`.
-   Crie um usuário `comprador1` e o inclua no grupo `compradores`.

# 12. Usando as permissões do DRF

**12.1 Autenticação e permissão**

_A **autenticação** ou **identificação** por si só geralmente não é suficiente para obter acesso à informação ou código. Para isso, a entidade que solicita o acesso deve ter **autorização**._ [(Permissões no DRF)](https://www.django-rest-framework.org/api-guide/permissions/)

**Autenticação** significa que um usuário foi **identificado** em um sistema, portanto ele é **conhecido**. Isso se dá, normamente por um sistema de **_login_**.

**Permissão (autorização)** se dá por um esquema de **conceder privilégios**, seja a usuários ou grupos.

Por padrão, qualquer usuário, mesmo sem autenticação, tem acesso irrestrito e permissão de fazer qualquer coisa em uma aplicação.

As permissões podem ser definidas a nível de objeto (nas _views_ ou _viewsets_, por exemplo) ou de forma global, no arquivo `settings.py`.

**12.2 Exemplo de uso de permisssão na viewset**

Como ilustração, modifique o arquivo `views.py`, da seguinte forma.

-   Importe a seguinte função:

```python
from rest_framework.permissions import IsAuthenticated
```

-   Inclua também a seguinte linha na `CategoriaViewSet`:

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

**12.3 Exemplo de uso de permisssão no `settings.py`**

> IMPORTANTE: Outra forma de gerenciamento de permissões é feita no arquivo `settings.py`. Para utilizá-la, comente as últimas alterações feitas no arquivo `views.py`.

Uma forma de conseguir o mesmo resultado de forma padrão para todo o projeto, isto é, permitir acesso aos _endpoints_ apenas para usuários autenticados, é configurar desse modo o arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}
```

> Inclua o código acima e teste novamente o acesso aos _endpoints_ do DRF (categorias, editoras, etc.) com e sem uma sessão autenticada.

**12.4 Permissões com o `DjangoModelPermissions`**

Apesar de ser possível definir a autorização das formas que vimos anteriormente, adotaremos uma outra forma. Essa forma que iremos adotar para o gerenciamento de permissões será com o uso do [DjangoModelPermissions](https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions).

Esta classe de permissão está ligada às permissões do modelo `django.contrib.auth` padrão do Django. Essa permissão deve ser aplicada apenas a visualizações que tenham uma propriedade `.queryset` ou método `get_queryset()` (exatamente o que temos).

A autorização só será concedida se o usuário estiver autenticado e tiver as permissões de modelo relevantes atribuídas, da seguinte forma:

-   As solicitações `POST` exigem que o usuário tenha a permissão de adição (`add`) no modelo.
-   As solicitações `PUT` e `PATCH` exigem que o usuário tenha a permissão de alteração (`change`) no modelo.
-   As solicitações `DELETE` exigem que o usuário tenha a permissão de exclusão (`remove`) no modelo.

Para isso, teremos que alterar a classe de autenticação, substituindo o que colocamos anteriormente:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissions",
    ],
    ...
}
```

> **Resumindo**, utilizaremos a estrutura de usuários, grupos e permissões que o próprio Django já nos fornece. Para isso, utilizaremos o `DjangoModelPermissions` para gerenciar as permissões.

Para utilizar essa estrutura de permissões corretamente, precisaremos de um sistema de autenticação (`login`) no nosso projeto, de forma a enviar essas informações via a `URL`. Para isso, utilizaremos o **SimpleJWT**.

# 13. Autenticação com o SimpleJWT

**Um resumo sobre autenticação e autorização**

Relembrando o que estudamos até aqui em termos de autenticação e autorização:

-   Como criar grupos e usuários e inserir os usuários nesses grupos
-   Como dar permissões nas models (via **Admin**) para visualização (`view`), adição (`add`), alteração (`change`) e exclusão (`remove`).
-   Como utilizar diversas formas de gerenciamento de permissões no Django, incluindo as permissões em cada `view` ou as permissões padrão no `settings.py`.
-   Como utilizar o `DjangoModelPermissions` para fazer uso do gerenciamento de permissões já incluído no **Django Admin**.

Agora, vamos utilizar o **SimpleJWT** para a autenticação no **Django REST Framework**.

> **Resumindo**, utilizaremos o **SimpleJWT** para _autenticação_ e a _estrutura de permissões do Django_ para **autorização**.

**O SimpleJWT**

O [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) é um plug-in de autenticação JSON Web Token para o Django REST Framework.

**Instalação e configuração**

-   Para instalar o SimpleJWT, execute o seguinte comando:

```shell
pdm add djangorestframework-simplejwt
```

-   Adicione o `SimpleJWT` no arquivo `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "rest_framework_simplejwt",
    ...
]
```

-   Adicione o `SimpleJWT` no arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    ...
}
```

-   Adicione o `SimpleJWT` no arquivo `urls.py`:

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ...
]
```

-   Feitas essa aterações, coloque o servidor do Django novamente em execução.

**Exercícios: Testando as permissões com o SimpleJWT**

Para testar se tudo deu certo, utilizaremos um cliente HTTP, como o **Thunder Client**.

**Colocando as informações do token na requisição**

**Dica:** se sua ferramenta permitir, crie várias requisições separadas e dê nomes, como _login_, _consulta_, _inclusão_, etc.

-   Ao tentar acessar um _endpoint_ com `GET`, como esse:

[GET] http://localhost:8000/categorias/

-   Você deverá receber uma resposta parecida com essa:

```json
{
    "detail": "As credenciais de autenticação não foram fornecidas."
}
```

-   Para fazer a autenticação, precisamos enviar as informações de `usuário` e `senha`. Faremos isso enviando uma requisição do tipo `POST`, com as seguintes informações, no `Body` em `JSON`:

```json
{
    "username": "comprador1",
    "password": "senha.123"
}
```

-   O endereço para envio da requisição é o seguinte:

    [POST] http://localhost:8000/token/

> **IMPORTANTE:** Não esqueça da barra (`/`) final no endereço e lembre-se que essa é uma requisição do tipo `POST`.

Você deve receber uma resposta semelhante a essa:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTcyNDUxMCwiaWF0IjoxNjYxNjM4MTEwLCJqdGkiOiJiN2RhNWZkMjEwYTI0NjliOWE0MjgxZjQxZDcwNjZhMCIsInVzZXJfaWQiOjN9.lATd6io76oVa6nW5zuBEtsa8htvsL6wVhp-KzXMK-rk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNjM4NDEwLCJpYXQiOjE2NjE2MzgxMTAsImp0aSI6ImRhYTBmNDcyZDI3YTQ5ZTM4M2I4ZjJhOTcwYjhlMWNmIiwidXNlcl9pZCI6M30.HY2j0L6eQBaPxAoHrPz_KFK_sWyb9lHmR7dQ1sOPTNY"
}
```

> Para verificar as informações do token, acesse os sites [jwt.io](https://jwt.io/) ou [token.dev](https://token.dev/), cole o valor do token no campo `Encoded` e clique no botão `Decode`.

Todas as chamadas ao sistema que precisarem de autenticação deverão ser feitas com o campo `access` token. Para isso, copie o valor do campo `access` e cole no campo `Auth`, opção `Bearer` do Thunder Client.

Para testar, acesse com `GET` o seguinte endereço:

```
[GET] ​http://localhost:8000/categorias/
```

Você deverá conseguir visualizar todas as categorias cadastradas.

**_Token_ expirado**

Quando o token expira, você receberá uma resposta semelhante a essa:

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

Para renovar o token, faça novamente a requisição de autenticação, enviando as informações de usuário e senha.

**Tentando alterar uma informação**

```
[PUT] ​http://localhost:8000/categorias/10/
```

```json
{
    "descricao": "Cobol"
}
```

```json
{
    "detail": "Método \"PUT\" não é permitido."
}
```

Você não pode alterar uma informação com esse usuário. Para isso, você precisa de um usuário com permissão de escrita.

**Testando com outro usuário**

Repita o processo de autenticação e consulta com o usuário `admin1` que criamos anteriormente.

Resumindo, você vai precisar:

-   Criar uma requisição de autenticação, do tipo `POST`, para a URL `token`, enviando as informações de usuário e senha.
-   Copiar a chave do tipo `access` e colocá-la no cabeçalho `Auth`, opção `Bearer` da requisição do tipo `GET` que você fará.

Com isso, fizemos um sistema básico de **autenticação** (_login_) e **autorização** (_permissões_) usando o próprio sistema já fornecido pelo Django.

# 14. Reestruturação em pastas de _models_, _views_ e _serializers_

Por padrão, as _models_, as _views_ e os _serializers_ são criados todos em um único arquivo, chamados respectivamente de `models.py`, `views.py` e `serializers.py`. Na medida em que o projeto vai crescendo e vão aumento o número de entidades, percebemos que é importante organizar essas entidades em arquivos separados. Obtemos com isso as seguintes vantagens:

-   Os arquivos ficam menores e mais fácil de encontrar o ponto correto de modificação.
-   Os conflitos no **GitHub** são evitados, pois normalmente as pessoas da equipe trabalham em entidades diferentes ao mesmo tempo.

Sendo assim, vamos fazer a separação dessas entidades em arquivos distintos, organizados dentro de uma pasta.

> **IMPORTANTE:** essa mudança não afeta a forma de uso desses componentes, nem desempenho da aplicação e nem o banco de dados. É uma simples refatoração de código.

**Colocando os modelos em arquivos separados**

Siga os passos:

-   Crie uma pasta `models` dentro da pasta da aplicação (`livraria`):

```shell
mkdir livraria/models
```

-   Crie um arquivo `__init__.py` dentro da pasta `models` recém criada:

```shell
touch livraria/models/__init__.py
```

> O arquivo `__init__.py` é necessário para que o Python reconheça a pasta como um módulo.

> Quando o Python importa um módulo, ele executa o código do arquivo `__init__.py` antes de importar os outros arquivos.

-   Crie um arquivo `autor.py` (será nossa primeira entidade) dentro da pasta `models`:

```shell
touch livraria/models/autor.py
```

-   Copie o conteúdo referente à entidade `Autor` do arquivo `models.py` para o arquivo `models/autor.py`.

```python
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"
```

-   Remova o conteúdo copiado no arquivo `models.py`. Não remova a linha do `import`, pois ela será utilizada por todas as entidades.
-   Inclua a importação da entidade `Autor` no arquivo `__init__.py`:

```python
from .autor import Autor
```

-   Repita os mesmos passos para as demais entidades (Categoria, Editora, Livro, etc.)
-   Observe que a entidade livro referencia as demais entidades, portanto elas precisam ser importadas em `livro.py`:

```python
from django.db import models

from livraria.models import Autor, Categoria, Editora


class Livro(models.Model):
...
```

> Ao final desse processo o arquivo `model.py` deverá estar vazio e poderá ser removido. A aplicação deve continuar rodando perfeitamente.

**Separando _views_ e _serializers_ em arquivos**

Para separar as _views_ e os _serializers_ em arquivos, repita o mesmo processo feito para as _models_:

-   Crie a pasta correspondente (`views` e `serializers`).
-   Crie o arquivo `__init__.py` dentro de cada pasta.
-   Crie um arquivo para cada entidade dentro da pasta.
-   Copie o conteúdo do arquivo para o arquivo correspondente dentro da pasta.
-   Adicione a importação no arquivo `__init__.py`.
-   Remova o conteúdo do arquivo.

> Opcionalmente, você pode criar a estrutura de pastas e arquivos via linha de comando, usando o comando `mkdir` e `touch`.

- Para criar a pasta `views`, execute os seguintes comandos:

```shell
mkdir livraria/views && cd livraria/views && touch __init__.py autor.py categoria.py editora.py livro.py && cd ../..
```

- Você pode fazer o mesmo para a pasta `serializers`:

```shell
mkdir livraria/serializers && cd livraria/serializers && touch __init__.py autor.py categoria.py editora.py livro.py && cd ../..
```

Ao final , você terá uma estrutura parecida com essa:

```
livraria
├── __init__.py
├── admin.py
├── apps.py
├── migrations
├── models
│   ├── __init__.py
│   ├── autor.py
│   ├── categoria.py
│   ├── editora.py
│   └── livro.py
├── serializers
│   ├── __init__.py
│   ├── autor.py
│   ├── categoria.py
│   ├── editora.py
│   └── livro.py
├── tests.py
└── views
    ├── __init__.py
    ├── autor.py
    ├── categoria.py
    ├── editora.py
    └── livro.py
```

> A partir dessa organização, cada nova entidade criada terá seus arquivos correspondentes. Nada impede, no entanto, de agrupar entidades relacionadas em, um único conjunto de arquivos. Por exemplo, as entidades `Compra` e `ItensCompra` poderiam ficar em arquivos `compra.py`.

# 15. Modificando o usuário padrão do Django

Utilizaremos uma estratégia simples para a inclusão de campos ao usuário padrão do Django. Essa estratégia terá as seguintes características:

-   **Substituiremos** a classe `User` padrão do Django pela nossa própria classe `Usuario`.
-   **Não removeremos** os campos padrão do usuário.
-   **Incluiremos** os campos que precisamos no nosso usuário.
-   **Removeremos** o banco de dados e criaremos um novo, perdendo todos os dados.
-   Faremos a **migração** do banco de dados.
-   Modificaremos o **Admin** para que ele utilize a nossa classe `Usuario` e não a classe `User` padrão.
-   Em nosso exemplo, incluiremos os campos `cpf`, `telefone` e `data_nascimento` ao usuário.
-   Posteriormente, incluiremos a foto do usuário.


**Instalando o setuptools**

-   Instale o pacote `setuptools`:

```shell
pdm add setuptools
```

**Instalando a app `usuario`**

-   Baixe e descompacte o arquivo com a app pronta para ser utilizada:

- No Linux:

```shell
wget https://github.com/marrcandre/django-drf-tutorial/raw/main/apps/usuario.zip -O usuario.zip && unzip usuario.zip && rm usuario.zip
```

- No `Windows`:

```shell
Invoke-WebRequest -Uri https://github.com/marrcandre/django-drf-tutorial/raw/main/apps/usuario.zip -OutFile usuario.zip
Expand-Archive -Path usuario.zip -DestinationPath .
Remove-Item -Force usuario.zip
```

A pasta ficará assim:

```
usuario
├── admin.py
├── apps.py
├── forms.py
├── __init__.py
├── managers.py
├── migrations
│   └── __init__.py
├── models.py
├── router.py
├── serializers.py
└── views.py
```

**Adicionando a app `usuario` ao projeto**

-   Edite o arquivo `settings.py` e inclua a app `usuario` na lista de apps instaladas:

```python
INSTALLED_APPS = [
    ...
    "usuario", # inclua essa linha
    "livraria",
]
```

-   Edite o arquivo `settings.py` e inclua a configuração abaixo:

```python
AUTH_USER_MODEL = "usuario.Usuario"
```

> Essa configuração indica ao Django que a classe `Usuario` da app `usuario` será utilizada como classe de usuário padrão.

-   Edite o arquivo `urls.py` e inclua as rotas da app `usuario`:

```python
...
from usuario.router import router as usuario_router
...

urlpatterns = [
    ...
    path("api/", include(usuario_router.urls)),
]
```

> Ela será acessada através da rota `/api/usuario/`.

**Removendo arquivos temporários, migrations e o banco de dados**

- No Linux:

```shell
find . -name "__pycache__" -type d -exec rm -r {} +
find . -path "*/migrations/*.pyc" -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
rm -rf __pypackages__ pdm.lock
rm db.sqlite3
```

- No Windows:

```shell
Get-ChildItem -Path . -Recurse -Directory -Filter "_pycache_" | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Recurse -File -Filter ".pyc" -Path "\migrations\" | Remove-Item -Force
Get-ChildItem -Path . -Recurse -File -Filter ".py" -Path "\migrations\" | Where-Object { $.Name -ne "init_.py" } | Remove-Item -Force
Remove-Item -Path "_pypackages_" -Recurse -Force
Remove-Item -Path "pdm.lock" -Force
Remove-Item -Path "db.sqlite3" -Force
```

**Reinstalando as dependências**

```shell
pdm install
```

**Criando o banco de dados e executando as migrações**

-   Crie novamente o banco de dados e execute as migrações:

```shell
pdm run python manage.py makemigrations
pdm run python manage.py migrate
```

**Criando um novo usuário**

-   Crie um novo superusuário:

```shell
pdm run python manage.py createsuperuser
```

> Ao criar um novo usuário, observe que o `email` é agora o campo principal, no lugar do `username`.

-   Entre no `Admin` e crie um novo usuário.

> Observe que os campos `cpf`, `telefone` e `data_nascimento` foram incluídos.

Para testar o login, utilize o **Thunder Client**:

-   Faça uma requisição do tipo `POST` para a URL `http://localhost:8000/api/token/`, enviando as informações de usuário e senha no `Body` em `JSON`:

```json
{
    "email": "comprador@a.com",
    "password": "senha.123"
}
```

-   Copie o valor do campo `access` e coloque no cabeçalho `Auth`, opção `Bearer` da requisição do tipo `GET` que você fará.


# 16. Upload e associação de imagens

Vamos instalar uma aplicação para gerenciar o upload de imagens e sua associação ao nosso modelos.

**Configuração**
Baixe e descompacte o arquivo com a app pronta para ser utilizada:

```shell
wget https://github.com/marrcandre/django-drf-tutorial/raw/main/apps/uploader.zip -O uploader.zip && unzip uploader.zip && rm uploader.zip
```

No `Windows`, execute os seguintes comandos no `PowerShell`:

```shell
Invoke-WebRequest -Uri https://github.com/marrcandre/django-drf-tutorial/raw/main/apps/uploader.zip -OutFile uploader.zip
```

```shell
Expand-Archive -Path uploader.zip -DestinationPath .
```

```shell
Remove-Item -Force uploader.zip
```

O projeto ficará com uma estrutura parecida com essa:

```
.
├── livraria
├── config
├── uploader
│   ├── models
│   │   ├── document.py
│   │   ├── image.py
│   │   └── __init__.py
│   ├── router.py
│   ├── serializers
│   │   ├── document.py
│   │   ├── image.py
│   │   └── __init__.py
├── static
└── utils
    └── files.py
```

**Instalando as dependências**

-   Instale os pacotes `Pillow e python-magic`:

```shell
pdm add Pillow
pdm add "python-magic; sys_platform=='linux'"
pdm add "python-magic-bin; sys_platform=='win32, darwin'"
```

> O pacote `python-magic` é utilizado para identificar o tipo de arquivo, enquanto o `Pillow` é utilizado para manipulação de imagens.

> O pacote `python-magic-bin` é utilizado no Windows e MacOS, enquanto o `python-magic` é utilizado no Linux.

**Registro da app**

-   Adicione o pacote `uploader` na lista de `INSTALLED_APPS`, no `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "uploader",
    "livraria",
    ...
]
```

**Configuração no `settings.py`**

-   Ainda no `settings.py` faça as seguintes configurações:

```python
# App Uploader settings
MEDIA_URL = "http://localhost:8000/media/"
MEDIA_ENDPOINT = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
FILE_UPLOAD_PERMISSIONS = 0o640
```

- Você vai precisar incluir o módulo `os` no início do arquivo `settings.py`:

```python
import os
```

**Configuração no `urls.py`**

-   Inclua o seguinte conteúdo no arquivo `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static
...
from uploader.router import router as uploader_router
...
path("api/media/", include(uploader_router.urls)),
...
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
...
```

**Migração do banco de dados**

-   Faça a migração do banco de dados:

```shell
pdm run python manage.py makemigrations uploader
pdm run python manage.py migrate
```

**Uso em modelos**

-   Edite o arquivo `models/livro.py` da aplicação `livraria` e inclua o seguinte conteúdo:

```python
...
from uploader.models import Image


class Livro(models.Model):
...
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
```

-   Faça novamente a migração do banco de dados:

```shell
pdm run python manage.py makemigrations livraria
pdm run python manage.py migrate
```

**Uso no serializer**

-   Edite o arquivo `serializers/livro.py` da aplicação `livraria` e inclua o seguinte conteúdo:

```python
...
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer
...
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

...
class LivroDetailSerializer(ModelSerializer):
...
    capa = ImageSerializer(required=False)
```

**Teste de upload e associação com o livro**

-   Acesse a API de media:

    http://localhost:8000/api/media/images/

-   Faça o upload de uma imagem.
-   Observe que o campo `capa_attachment_key` foi preenchido com o valor `attachment_key` da imagem.
-   Guarde o valor do campo `capa_attachment_key`.
-   Crie um novo livro, preenchendo o campo `capa_attachment_key` com o valor guardado anteriormente.
-   Acesse o endpoint `http://localhost:8000/api/media/images/` e observe que a imagem foi associada ao livro.

# 17. Habilitando o Swagger e Redoc usando DRF Spectacular

Vamos instalar uma aplicação para gerar a documentação da API usando o Swagger e o Redoc.

**Instalação e Configuração**

-   Instale o pacote `drf-spectacular`:

```shell
pdm add drf-spectacular
```

-   Adicione o pacote `drf_spectacular` na lista de `INSTALLED_APPS`, no `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "drf_spectacular",
    ...
]
```

-   Registre o pacote no `settings.py`:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
```

-   Faça ainda algumas configurações no `settings.py`:

```python
SPECTACULAR_SETTINGS = {
    "TITLE": "Livraria API",
    "DESCRIPTION": "API para gerenciamento de livraria, incluindo endpoints e documentação.",
    "VERSION": "1.0.0",
}
```

-   Inclua o seguinte conteúdo no arquivo `urls.py`, **organizando-o adequadamente**:

```python
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
...
urlpatterns = [
    ...
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
```

**Teste**

-   Acesse o Swagger:

    http://localhost:8000/api/swagger/

**Alteração da URL da API**

-   Edite o arquivo `urls.py` altere a URL da API para `http://localhost:8000/api/`:

```python
urlpatterns = [
    ...
    path("api/", include(router.urls)),
    ...
]
```

# 18. Dump e Load de dados

Vamos aprender a fazer o _dump_ e _load_ de dados. O _dump_ é a exportação dos dados do banco de dados para um arquivo, enquanto o _load_ é a importação dos dados de um arquivo para o banco de dados. Isso é útil para fazer cópias de segurança, migração de dados entre ambientes e carga inicial de dados.

<!-- **Carga inicial de dados**

- Acesse o seguinte link:

  - Link: `http://191.52.55.156:19005/admin`
  - Usuário: `a@a.com`
  - Senha: `senha.123`

- Cadastre pelos menos 10 livros, com autor e editora
- Verifique se o livro, autor ou editora já estão cadastrados.
- **NÃO USE CAIXA ALTA!!!**
- Use o formato de nomes de livros, como no exemplo: `O Senhor dos Anéis - A Sociedade do Anel` -->



**Cópia de segurança dos dados**

-   Execute o comando `dumpdata`:

```shell
pdm run python manage.py dumpdata --indent 2 > livraria_bkp.json
```

-   Observe que o arquivo `livraria_bkp.json` foi criado:

```shell
code livraria_bkp.json
```

**Carga dos dados**

Baixe o arquivo `livraria.json`.

- No Linux:

```shell
wget https://github.com/marrcandre/django-drf-tutorial/raw/versao-2023/scripts/livraria.json
```

- No Windows:

```shell
Invoke-WebRequest -Uri "https://github.com/marrcandre/django-drf-tutorial/raw/versao-2023/scripts/livraria.json" -OutFile livraria.json
```

**Carga dos dados**

-   Execute o comando `loaddata`:

```shell
pdm run python manage.py loaddata livraria.json
```

-   Observe que os dados foram carregados:

```shell
pdm run python manage.py shell
>>> from livraria.models import Livro
>>> Livro.objects.all()
```

Você também pode acessar o Django Admin ou o Swagger e verificar que os dados foram carregados.

# 19. Uso do Django Shell

O Django Shell é uma ferramenta para interagir com o banco de dados.

-   Acesse o shell:

```shell
pdm run python manage.py shell
```

-   Importe os modelos de `livraria.models`:

```python
>>> from livraria.models import Autor, Categoria, Editora, Livro
```

-   Crie um objeto:

```python
>>> categoria = Categoria.objects.create(descricao="Desenvolvimento Web")
```

-   Observe que o objeto foi criado:

```python
>>> categoria
<Categoria: Desenvolvimento Web>
```

-   Liste os objetos:

```python
>>> Categoria.objects.all()
<QuerySet [<Categoria: Desenvolvimento Web>]>
```

-   Obtenha o objeto:

```python
>>> categoria = Categoria.objects.get(descricao="Desenvolvimento Web")
```

-   Observe que o objeto foi obtido:

```python
>>> categoria
<Categoria: Desenvolvimento Web>
```

-   Atualize o objeto:

```python
>>> categoria.descricao = "Desenvolvimento Web com Django"
>>> categoria.save()
```

-   Observe que o objeto foi atualizado:

```python
>>> categoria
<Categoria: Desenvolvimento Web com Django>
```

-   Remova o objeto:

```python
>>> categoria.delete()
(1, {'livraria.Categoria': 1})
```

-   Observe que o objeto foi removido:

```python
>>> Categoria.objects.all()
<QuerySet []>
```

-   Acesso a todos os livros de um autor:

```python
Autor.objects.get(id=1).livros.all()
```

-   Acesso a todos os livros de uma categoria:

```python
Categoria.objects.get(id=1).livros.all()
```

-   Acesso a todos os livros de uma editora:

```python
Editora.objects.get(id=1).livros.all()
```

-   Encerre o shell:

```python
>>> exit()
```

# 20. Customização do Admin

O Admin é uma ferramenta para gerenciar os dados do banco de dados. Ele pode ser customizado para melhorar a experiência do usuário.

**Customização do Admin**

-   Edite o arquivo `livraria/admin.py`:

```python
...
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'categoria')
    search_fields = ('titulo', 'editora__nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('titulo', 'editora', 'categoria')
    list_per_page = 25
```

-   Acesse o Admin:

    http://localhost:8000/admin/


# 21. Configurando diferentes ambientes

Vamos configurar diferentes ambientes para desenvolvimento, migração e produção. Para isso, vamos criar um arquivo `.env` na raiz do projeto. Nesse arquivo, vamos definir as variáveis de ambiente que queremos que tenham valores diferentes para cada ambiente.

**Instalação do pacote `python-dotenv`**

-   Instale o pacote `python-dotenv`:

```shell
pdm add python-dotenv
```

**Instalação do `python3-dev` e do `netifaces`**

-   Instale o pacote `python3-dev`:

```shell
sudo apt install python3-dev
```

-   Instale o pacote `netifaces`:

```shell
pdm add netifaces
```

> O pacote `netifaces` é necessário para que possamos obter o IP da máquina. Ele depende do pacote `python3-dev`.

**Baixe o script de configuração do IP**

-   Baixe o arquivo `set_my_ip.py`:

```shell
mkdir -p scripts && curl https://raw.githubusercontent.com/marrcandre/django-drf-tutorial/main/scripts/set_my_ip.py -o ./scripts/set_my_ip.py
```
> Esse comando baixa o arquivo `set_my_ip.py` e o coloca na pasta `scripts`, criando a pasta caso ela não exista.

> Esse script pega o IP da máquina e o coloca no arquivo `.env`, na variável `MY_IP`.

**Configure os scripts de execução do projeto**

-   Edite o arquivo `pyproject.toml ` e inclua o seguinte conteúdo:

```shell
[tool.pdm.scripts]
pre_dev = "python ./scripts/set_my_ip.py"
dev = "python manage.py runserver 0.0.0.0:19003"
```

> O script `pre_dev` será executado antes do script `dev`.

> O script `pre_dev` executa o script `set_my_ip.py`, que pega o IP da máquina e o coloca no arquivo `.env`, na variável `MY_IP`.

> O script `dev` executa o comando `runserver` do Django, que roda o servidor de desenvolvimento na porta `19003`.


**Rodando o projeto**

- Execute o seguinte comando:

```shell
pdm run dev
```

- O projeto ficará disponivel no endereço: `http://localhost:19003/`.


**Configuração do ambiente de desenvolvimento**

-   Edite o arquivo `.env`, incluindo as seguintes variáveis:

```shell
# Django
SECRET_KEY=django_insecure_#-
DEBUG=True
ALLOWED_HOSTS=['*']

MODE=DEVELOPMENT # DEVELOPMENT, PRODUCTION, MIGRATE
```

-   Edite o arquivo `settings.py`, incluindo o seguinte código:

```python
import os
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv("MODE")

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False")
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://localhost:8000", "https://*.fl0.io/"]
...

if MODE in ["PRODUCTION", "MIGRATE"]:
    MEDIA_URL = '/media/'
else:
    MY_IP = os.getenv("MY_IP", "127.0.0.1")
    MEDIA_URL = f"http://{MY_IP}:19003/media/"
```

> **ATENÇÃO: as referências anteriores a essas variáveis no arquivo `settings.py` devem ser removidas.**

> O comando load_dotenv() carrega as variáveis de ambiente definidas no arquivo `.env` ou no sistema operacional.

> Na variável `CSRF_TRUSTED_ORIGINS` foram incluídos os endereços dos ambientes de desenvolvimento e produção. Isso é necessário para que o Django aceite requisições de outros domínios. Você deve incluir os endereços dos seus ambientes de desenvolvimento e produção.

> A variável `MODE` é definida no arquivo `.env`. Ela será utilizada para definir o modo de execução do projeto. No caso, o modo de execução é o `DEVELOPMENT`.

> Isso tudo pode ser facilmente alterado, de acordo com a necessidade, apenas modificando o arquivo `.env`.

> Na máquina local, a variável `MEDIA_URL` é definida com o IP da máquina, na porta `19003`. Isso é necessário para que o Django possa servir os arquivos de mídia.


**Testando a configuração**

-   Execute o comando `pdm run python manage.py runserver` para testar a configuração.

> Tudo deve funcionar como antes, uma vez que as variáveis de ambiente definidas no arquivo `.env` são as mesmas que estavam definidas no arquivo `settings.py`.

> Posteriormente, vamos alterar o modo para `PRODUCTION` e a base de dados será algum outro banco de dados remoto.

- Faça o commit das alterações.


**Criando um arquivo .env_exemplo**

O arquivo `.env` não deve ser versionado. Para isso, vamos criar um arquivo `.env_exemplo` com as variáveis de ambiente que devem ser definidas.

- Crie um arquivo `.env_exemplo` na raiz do projeto, copiando o conteúdo do arquivo `.env`. Não inclua nesse arquivo nenhuma informação sensível, como senhas, tokens, etc.

- No arquivo `.gitignore`, inclua a linha `.env` para que o arquivo `.env` não seja versionado.

Um exemplo de arquivo `.env_exemplo`:

```shell
# Django
SECRET_KEY=django_insecure_#-
DEBUG=True
ALLOWED_HOSTS=['*']

MODE=DEVELOPMENT # DEVELOPMENT, PRODUCTION, MIGRATE
```

**Recriando o arquivo .env**

Sempre que você clonar o projeto, precisará recriar o arquivo `.env` com as informações sensíveis, uma vez que o arquivo `.env` não é versionado.

-   Para recriar o arquivo `.env`, basta copiar o arquivo `.env_exemplo` para `.env` e incluir as informações sensíveis.

> Nos servidores de produção, as variáveis de ambiente são definidas no próprio servidor, não sendo necessário criar o arquivo `.env`.

# 22. Implantação (Deploy) do projeto

Esta parte foi modificada. Não utilizaremos mais o **Fl0** para a implantação do projeto. Em vez disso, utilizaremos o **Supabase** para o banco de dados e o **Render** para a implantação do projeto.

Acesse [aqui](#a99-implantação-deploy-do-projeto).

# 23. Inclusão da foto de perfil no usuário

Vamos incluir a foto de perfil no usuário.

**Criação do campo de foto de perfil**

-   No arquivo `models/usuario.py`, inclua o campo `foto`:

```python
...
from uploader.models import Image
...
class Usuario(AbstractUser):
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
```

-   Faça as migrações:

```shell
pdm run python manage.py makemigrations livraria
pdm run python manage.py migrate
```

-   No arquivo `admin.py`, inclua o campo `foto`:

```python
...
class UsuarioAdmin(UserAdmin):
    ...
    "fields": ("first_name","last_name","foto",...),
    ...
```

-   Crie um serializador para o usuário:

```python
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from livraria.models import Usuario
from uploader.models import Image
from uploader.serializers import ImageSerializer


class UsuarioSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Usuario
        fields = "__all__"
```

-   Inclua o novo serializador no arquivo
    `__init__.py` dos serializadores:

```python
from .usuario import UsuarioSerializer
```

-   Crie uma nova view para o usuário:

```python
from rest_framework.viewsets import ModelViewSet

from livraria.models import Usuario
from livraria.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
```

-   Inclua a nova view no arquivo `__init__.py` das views:

```python
from .usuario import UsuarioViewSet
```

-   Inclua a nova view no arquivo `urls.py`:

```python
from livraria.views import UsuarioViewSet
...
router.register(r"usuarios", UsuarioViewSet)
```

**Testando**

-   Inclua uma foto de perfil em um usuário.

# 24. Criação da entidade `Compra` integrada ao usuário do projeto

Nessa aula, vamos criar um model de compras integrada à model do usuário do projeto.

**Criando o model de compras**

-   Crie um novo arquivo `compra.py` dentro da pasta `models` do app `livraria`:

```shell
touch livraria/models/compra.py
```

-   Inclua o seguinte conteúdo no arquivo `compra.py`:

```python
from django.db import models

from usuario.models import Usuario

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)
```

> Note que estamos utilizando o `Usuario` do app `usuario` como `ForeignKey` para o model `Compra`.

> `StatusCompra` é do tipo `IntegerChoices`, que é uma forma de criar um campo `choices` com valores inteiros.

> `status` é um campo `IntegerField` que utiliza o `choices` `StatusCompra.choices` e tem o valor padrão `StatusCompra.CARRINHO`.

- Inclua a nova model no arquivo `__init__.py` dos models:

```python
from .compra import Compra
```

-   Adicione o model `Compra` ao `admin.py` do app `livraria`:

```python
...
from livraria.models import Compra

admin.site.register(Compra)
```

-   Execute as migrações:

```shell
pdm run python manage.py makemigrations
pdm run python manage.py migrate
```

-   Teste o model `Compra` no admin do Django.

# 25. Criando os itens da compra

No caso dos itens da compra, não vamos utilizar um campo `livro` do tipo `ManyToManyField` no model `Compra`, pois queremos ter a possibilidade de adicionar mais informações ao item da compra, como a `quantidade`, por exemplo.

-   Vamos adicionar um novo model `ItensCompra` ao arquivo `compra.py`:

```python
class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
```

> No atributo `compra`, utilizamos `models.CASCADE`, pois queremos que, ao deletar uma compra, todos os itens da compra sejam deletados também.

> No atributo `livro`, utilizamos `models.PROTECT`, pois queremos impedir que um livro seja deletado se ele estiver associado a um item de compra.

> Ainda no `livro`, utilizamos `related_name="+"`, pois não queremos que o `ItensCompra` tenha um atributo `livro`.

- Inclua o novo model no arquivo `__init__.py` dos models:

```python
from .compra import Compra, ItensCompra
```

-   Execute as migrações (você já sabe como fazer, certo?)
-   Verifique que a tabela `livraria_itenscompra` foi criada no banco de dados.
-   Inclua o model `ItensCompra` no `Admin` do Django.

# 26. Uso de `TabularInline` no `Admin` para Itens da Compra

Vamos mostrar os itens da compra no admin do Django, utilizando o `TabularInline`. Desta forma, podemos adicionar os itens da compra diretamente na tela de edição da compra.

-   No arquivo `admin.py` do app `livraria`, adicione o seguinte código:

```python
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]
```

> Desta forma, quando você editar uma compra no admin do Django, você verá os itens da compra logo abaixo do formulário de edição da compra.

-   Teste no admin do Django.

# 27. Endpoint para listagem básica de Compras

Vamos criar um endpoint para listagem básica de compras.

**Serializer de Compra**

-   Crie um novo arquivo `compra.py` dentro da pasta `serializers` do app `livraria`:

```shell
touch livraria/serializers/compra.py
```

-   Inclua o seguinte conteúdo no arquivo `compra.py`:

```python
from rest_framework.serializers import ModelSerializer, CharField

from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
```

-   Inclua o novo `CompraSerializer` no arquivo `__init__.py` dos serializers:

```python
from .compra import CompraSerializer
```

**Viewset de Compra**

-   Crie um novo arquivo `compra.py` dentro da pasta `views` do app `livraria`:

```shell
touch livraria/views/compra.py
```

-   Inclua o seguinte conteúdo no arquivo `compra.py`:

```python
from rest_framework.viewsets import ModelViewSet

from livraria.models import Compra
from livraria.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
```

-   Inclua o novo `CompraViewSet` no arquivo `__init__.py` das views:

```python
from .compra import CompraViewSet
```

**URL para listagem de compras**

-   Inclua o endpoint no arquivo `urls.py` do app `livraria`:

```python
...
from livraria.views import AutorViewSet, CategoriaViewSet, CompraViewSet, EditoraViewSet, LivroViewSet
...
router.register(r"compras", CompraViewSet)
...
```

-  Teste o endpoint no navegador.
-  Faça o _commit_ e _push_ das alterações.

**Inclusão do email do usuário na listagem da compra**

-   Vamos incluir o email do usuário na listagem da compra.
-   No serializer de `Compra`, inclua o seguinte código:

```python
...
...
class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
...
```

> O parâmetro `source` indica qual campo do model `Compra` será utilizado para preencher o campo `usuario` do serializer.

> O parâmetro `read_only` indica que o campo `usuario` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ e _push_ das alterações.

**Inclusão do status da compra na listagem da compra**

-   Vamos incluir o status da compra na listagem da compra.
-   No serializer de `Compra`, inclua o seguinte código:

```python
...
class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True)
...
```

> O parâmetro `source` indica qual método do model `Compra` será utilizado para preencher o campo `status` do serializer. Sempre que utilizamos um campo do tipo `IntegerChoices`, podemos utilizar o método `get_<nome_do_campo>_display` para obter a descrição do campo.

> O parâmetro `read_only` indica que o campo `status` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ e _push_ das alterações.

# 28. Visualização dos itens da compra no endpoint de listagem de compras

Vamos incluir os itens da compra na listagem de compras.

-   Crie um serializer para `ItensCompra`:

```python
...
from livraria.models import Compra, ItensCompra
...

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
```

No `ComprasSerializer`, inclua o seguinte código:

```python
...
itens = ItensCompraSerializer(many=True, read_only=True)
...
```

> O parâmetro `many=True` indica que o campo `itens` é uma lista de itens.

> O parâmetro `read_only=True` indica que o campo `itens` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ e _push_ das alterações.

**Mostrando os detalhes dos itens da compra na listagem de compras**

-   No serializer de `ItensCompra`, modifique o código:

```python
class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1
```

> O parâmetro `depth=1` indica que o serializer deve mostrar os detalhes do model `ItensCompra`. O valor `1` indica que o serializer deve mostrar os detalhes do model `ItensCompra` e dos models relacionados a ele. Se o valor fosse `2`, o serializer mostraria os detalhes do model `ItensCompra`, dos models relacionados a ele e dos models relacionados aos models relacionados a ele.

**Mostrando apenas os campos necessários dos itens da compra na listagem de compras**

Você deve ter percebido que o serializer de `ItensCompra` está mostrando todos os seus campos, incluindo o campo `compra`. Vamos modificar o serializer para mostrar apenas os campos necessários. Nesse exemplo, vamos mostrar apenas os campos`livro` e `quantidade`.

-   No `ItensCompraSerializer`, modifique a linha `fields`:

```python
fields = ["livro", "quantidade"]
```

> O parâmetro `fields` indica quais campos do model `ItensCompra` serão mostrados no serializer. Se o valor for `__all__`, todos os campos serão mostrados. Se o valor for uma lista de campos, apenas os campos da lista serão mostrados.

-   Teste o endpoint no navegador.

**Mostrando mais detalhes do livro na listagem de compras**

Utilizando depth = 2, podemos mostrar mais detalhes do livro na listagem de compras.

-   No `ItensCompraSerializer`, modifique a linha `depth`:

```python
depth = 2
```

> Nesse caso, vamos ver os detalhes dos livros, como editora, autor e categoria.

-  Teste o endpoint no navegador.
-  Faça o _commit_ e _push_ das alterações.

**Mostrando o total do item na listagem de compras**

O total do item é calculado pelo preço do livro multiplicado pela quantidade. Esse é um campo calculado, que não existe no model `ItensCompra`. Vamos incluir esse campo na listagem de compras.

-   No `ItensCompraSerializer`, inclua o seguinte código:

```python
...
total = SerializerMethodField()
...
def get_total(self, instance):
    return instance.quantidade * instance.livro.preco
...
```

> O parâmetro `SerializerMethodField` indica que o campo `total` não existe no model `ItensCompra`. Ele será calculado pelo método `get_total`.

> O método `get_total` recebe como parâmetro o objeto `instance`, que representa o item da compra. A partir dele, podemos acessar os campos do item da compra, como `quantidade` e `livro.preco`.

> O método `get_total` retorna o valor do campo `total`, que é calculado pelo preço do livro multiplicado pela quantidade.

> O método `get_<nome_do_campo>` é um método especial do serializer que é chamado para calcular o valor do campo `<nome_do_campo>`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ e _push_ das alterações.

# 29. Totalização dos itens de compra na `model` e `serializer` de compra

Vamos incluir o total da compra na listagem de compras. O total da compra é calculado pela soma dos totais dos itens da compra. Esse é um campo calculado, que não existe no model `Compra`. Vamos incluir esse campo na listagem de compras.

- Ao final da `model` `Compra`, inclua o seguinte código:

```python
...
    @property
    def total(self):
        # total = 0
        # for item in self.itens.all():
        #     total += item.livro.preco * item.quantidade
        # return total
        return sum(item.livro.preco * item.quantidade for item in self.itens.all())
```
> No código acima, temos duas formas de calcular o total da compra. A primeira forma está comentada. A segunda forma está descomentada. A segunda forma é mais simples e mais eficiente, e utiliza uma _list comprehension_.

> O método `property` indica que o campo `total` não existe no model `Compra`. Ele será calculado pelo método `total`.

> O método `total` retorna o valor do campo `total`, que é calculado pela soma dos totais dos itens da compra, que é calculado pelo preço do livro multiplicado pela quantidade do item da compra.

- Precisamos incluir o campo `total` no serializer de `Compra`. No `ComprasSerializer`, inclua o seguinte código:

```python
...
        fields = ("id", "usuario", "status", "total", "itens")
...
```

> O parâmetro `fields` indica quais campos do model `Compra` serão mostrados no serializer. Se o valor for `__all__`, todos os campos serão mostrados. Se o valor for uma lista de campos, apenas os campos da lista serão mostrados, na ordem da lista.

- Teste o endpoint no navegador.
- Faça o _commit_ e _push_ das alterações.

# 30. Criação de um endpoint para criar novas compras

Vamos primeiro definir o que é necessário para criar uma nova compra. Para criar uma nova compra, precisamos informar o **usuário** e os **itens da compra**. Os itens da compra são compostos pelo **livro** e pela **quantidade**. Essas são as informações necessárias para criar uma nova compra.

O formato dos dados para criar uma nova compra é o seguinte:

```json
{
    "usuario": 1,
    "itens": [
        {
            "livro": 1,
            "quantidade": 1
        },
        {
            "livro": 2,
            "quantidade": 2
        }
    ]
}
```

Tendo definido o formato dos dados, vamos criar um novo `serializer`, que será usado para criar uma nova compra ou editar uma compra já existente.

- No arquivo `serializer/compra.py` , inclua o seguinte código:

```python
...
class CriarEditarCompraSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("usuario", "itens")
...

```

> O parâmetro `many=True` indica que o campo `itens` é uma lista de itens de compra.

Vamos alterar o `viewset` de `Compra` para usar o novo `serializer`.

- No arquivo `views/compra.py` altere o `viewset` de `Compra` para usar o novo `serializer`:

```python
...
class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer
...
```

- Tente criar uma nova compra no endpoint `compras/` no `ThunderClient`, utilizando o método `POST`:

```json
{
    "usuario": 1,
    "itens": [
        {
            "livro": 1,
            "quantidade": 1
        }
    ]
}
```

Você receberá o seguinte erro:

```
AssertionError at /api/compras/
The `.create()` method does not support writable nested fields by default.
Write an explicit `.create()` method for serializer `livraria.serializers.compra.CriarEditarCompraSerializer`, or set `read_only=True` on nested serializer fields.
```

Traduzindo, chegamos no seguinte:

```
Erro de afirmação em /api/compras/
O método `.create()` não suporta campos aninhados graváveis por padrão.
Escreva um método `.create()` explícito para o serializer `livraria.serializers.compra.CriarEditarCompraSerializer`, ou defina `read_only=True` nos campos do serializer aninhado.
```

O erro ocorre por que os itens da compra vêm de outra tabela, a tabela `ItemCompra`, através de uma chave estangeira. O serializer de `Compra` não sabe como criar os itens da compra. Precisamos alterar o método `create` do `serializer` de `Compra` para criar os itens da compra.

- No arqiuvo `serializers/compra.py` , altere o `serializer` de `Compra` para suportar campos aninhados:

```python
...

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True) # Aqui mudou

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra

```

> O método `create` é chamado quando uma nova compra é criada. Ele recebe os dados validados e cria a compra e os itens da compra.

- Precisamos criar também um novo `serializer` para os itens da compra. No `serializers/compra.py`, inclua o seguinte código:

```python
...
class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")
...
```

> O `serializer` de `ItensCompra` é bem simples, pois ele apenas recebe o livro e a quantidade.


- Teste o endpoint no `ThunderClient.
- Faça o _commit_ e _push_ das alterações.

# 31. Criação de um endpoint para atualizar compras

- Vamos tentar alterar uma compra existente no endpoint `compras/1/` (ou aquela que você preferir) no `ThunderClient`, utilizando o método `PUT`:

```json
{
    "usuario": 2,
    "itens": [
        {
            "livro": 2,
            "quantidade": 2
        }
    ]
}
```

Você receberá o seguinte erro:

```
AssertionError at /api/compras/1/
The `.update()` method does not support writable nested fields by default.
Write an explicit `.update()` method for serializer `livraria.serializers.compra.CriarEditarCompraSerializer`, or set `read_only=True` on nested serializer fields.
```

Traduzindo, chegamos no seguinte:

```
Erro de afirmação em /api/compras/1/
O método `.update()` não suporta campos aninhados graváveis por padrão.
Escreva um método `.update()` explícito para o serializer `livraria.serializers.compra.CriarEditarCompraSerializer`, ou defina `read_only=True` nos campos do serializer aninhado.
```

> O erro ocorre por que os itens da compra vêm de outra tabela, a tabela `ItensCompra`, através de uma chave estangeira. O serializer de `Compra` não sabe como atualizar os itens da compra. Precisamos alterar o método `update` do `serializer` de `Compra` para atualizar os itens da compra.

- No arquivo `serializers/compra.py`, altere o `serializer` de `Compra` para suportar campos aninhados:

```python
...
    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance
...
```

> O método `update` é chamado quando uma compra é atualizada. Ele recebe os dados validados e atualiza a compra e os itens da compra.

> O método `update` recebe dois parâmetros: `instance` e `validated_data`. O `instance` é a compra que está sendo atualizada. O `validated_data` são os dados validados que estão sendo atualizados.

> O método `update` remove todos os itens da compra (se houverem) e cria novos itens com os dados validados.

> O método `update` salvamos a compra e retornamos a instância.

- Teste o endpoint no `ThunderClient`:
  - use o método `PUT`, para atualizar a compra de forma completa;
  - use o método `PATCH`, para atualizar a compra de forma parcial.
    - Experimente mudar apenas o usuário;
    - Experimente mudar apenas a quantidade de um item da compra;
    - Experimente mudar o livro de um item da compra;
- Faça o _commit_ e _push_ das alterações.

# 32. Criação de uma compra a partir do usuário autenticado

Ao invés de passar o usuário no corpo da requisição, podemos pegar o usuário autenticado e criar a compra a partir dele. O `Django Rest Framework` nos dá uma forma de fazer isso.

- Primeiro, vamos importar todos os `serializers` de `rest_framework` em `serializers/compra.py`:

```python
from rest_framework import serializers
```

- Agora, vamos definir o usuário como um campo oculto, cujo valor padrão é o usuário autenticado:

```python
class ComprasSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")
```

> O campo `usuario` é um campo oculto, pois foi definido como `serializers.HiddenField`. Ele não é exibido no `serializer`.

> O valor padrão do campo é o usuário autenticado.

> O `CurrentUserDefault` é um campo padrão que retorna o usuário autenticado.

Para testar, vamos criar uma nova compra no endpoint `compras/` no `ThunderClient`, utilizando o método `POST`:

```json
{
    "itens": [
        {
            "livro": 2,
            "quantidade": 2
        }
    ]
}
```

> Observe que não precisamos mais passar o usuário no corpo da requisição, pois ele pega o usuário autenticado.

- Faça o _commit_ e _push_ das alterações.

# 33. Filtrando apenas as compras do usuário autenticado

Nesse momento, qualquer usuário pode ver todas as compras. Vamos filtrar apenas as compras do usuário autenticado.

- No `views.py`, vamos alterar o `viewset` de `Compra` para filtrar apenas as compras do usuário autenticado:

```python
...
class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
...
```

> O método `get_queryset` é chamado quando uma compra é listada. Ele retorna apenas as compras do usuário autenticado.
> O `request` é o objeto que representa a requisição. O `request.user` é o usuário autenticado.
> Se o usuário for superusuário ou for membro do grupo "*Administradores*", retorna todas as compras.

- Para testar, autentique-se com um usuário normal e depois com um que seja administrador. Você verá que o administrador consegue ver todas as compras, enquanto o usuário normal só consegue ver as suas compras.

# 34. Validando a quantidade de itens em estoque

Nesse momento, é possível criar uma compra com uma quantidade de itens maior do que a quantidade em estoque. Vamos validar isso.

- No `serializers/compra.py`, vamos alterar o `serializer` `CriarEditarItensCompraSerializer` para validar a quantidade de itens em estoque:

```python
...
    def validate(self, data):
        if data["quantidade"] > data["livro"].quantidade:
            raise serializers.ValidationError(
                {"quantidade": "Quantidade solicitada não disponível em estoque."}
            )
        return data
...
```

- Para testar, tente criar uma compra com uma quantidade de itens maior do que a quantidade em estoque. Você verá que a compra não é criada e é exibida uma mensagem de erro.
- Faça o _commit_ e _push_ das alterações.

# 35. Gravando o preço do livro no item da compra

Nesse momento, o preço do livro não é gravado no item da compra. Vamos gravar o preço do livro no item da compra, uma vez que o preço do livro pode mudar e queremos manter o registro do preço do livro no momento da compra.

- Primeiro, precisamos incluir o campo `preco_item` no model `ItensCompra`:

```python
...
class ItensCompra(models.Model):
...
    preco_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
...
```

- Execute as migrações.

- No `serializers/compra.py`, vamos alterar a função `create` do `serializer` `CriarEditarCompraSerializer` para gravar o preço do livro no item da compra:

```python
...
    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item["preco_item"] = item["livro"].preco # Coloca o preço do livro no item de compra
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
...
```

> O método `create` é chamado quando uma nova compra é criada. Ele recebe os dados validados e cria a compra e os itens da compra.

- Para finalizar, precisamos alterar o campo total da compra para considerar o preço do item da compra:

```python
...
    @property
    def total(self):
        return sum(item.preco_item * item.quantidade for item in self.itens.all())
...
```

> Estamos utilizando o campo `preco_item` para calcular o total da compra, ao invés do campo `livro.preco`.

- Para testar, crie uma nova compra e verifique que o preço do livro foi gravado no item da compra.
- Faça o _commit_ e _push_ das alterações.

Da mesma forma, podemos alterar o método `update` do `serializer` `CriarEditarCompraSerializer` para gravar o preço do livro no item da compra:

```python
...
    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                item["preco_item"] = item["livro"].preco # Coloca o preço do livro no item de compra
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return instance
...
```

- Para testar, altere uma compra e verifique que o preço do livro foi gravado no item da compra.
- Faça o _commit_ e _push_ das alterações.


# 36. Filtrando os livros


Nesse momento, é possível apenas listar todos os livros. Vamos ver como podemos filtrar os livros por seus atributos, como `categoria`, `editora` e `autores`.

## Filtrando os livros por categoria

Vamos começar filtrando os livros por categoria. Para isso, utilizaremos o pacote [`django-filter`](https://django-filter.readthedocs.io/en/stable/):

- Instale o pacote `django-filter`:

```shell
pdm add django-filter
```

- No `settings.py`, inclua o `django-filter` no `INSTALLED_APPS`:

```python
...
INSTALLED_APPS = [
    ...
    "django_filters",
    ...
]
...
```

- No `views/livro.py`, vamos alterar o `viewset` de `Livro` para filtrar os livros por categoria:

```python
...
from django_filters.rest_framework import DjangoFilterBackend
...
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria__descricao"]
...
```

> O `DjangoFilterBackend` é o filtro do `django-filter`.
> O `filterset_fields` indica quais campos serão filtrados. Nesse caso, estamos filtrando apenas pelo campo `categoria`.

- Para testar no `Swagger`, clique no endpoint `livros/` e depois em `Try it out`. Você verá que apareceu um campo `categoria` para filtrar os livros por categoria. Informe a `descrição` da categoria e clique em `Execute`. Você verá que apenas os livros da categoria informada foram listados.
- Para testar no ThunderClient, utilize a url com o seguinte formato: `http://127.0.0.1:8000/api/livros/?categoria=Python`. Você verá que apenas os livros da categoria informada foram listados.
- Faça o _commit_ e _push_ das alterações.

## Acrescentando outros filtros na listagem de livros

Vamos acrescentar outros filtros na listagem de livros.

- No `views/livro.py`, vamos alterar o atributo `filterset_fields`, na `viewset` de `Livro` para filtrar os livros por `categoria` e `editora`:

```python
...
    filterset_fields = ["categoria__descricao", "editora__nome"]
...
```

- Para filtrar por categoria e editora:
  - http://127.0.0.1:8000/api/livros/?categoria__descricao=Python&editora__nome=Novatec
  - http://127.0.0.1:8000/api/livros/?autores=3&categoria=4&editora=1
- Para filtrar apenas por editora:
  - http://127.0.0.1:8000/api/livros/?editora__nome=Novatec

**Exercício**

- Acrescente filtros nas *models* `Autor`, `Categoria`, `Editora` e `Compra`.

# 37. Busca textual nos livros

A busca textual serve para adicionar a funcionalidade de realizar buscas dentro de determinados valores de texto armazenados na base de dados.

Contudo a busca só funciona para campos de texto, como `CharField` e `TextField`.

- Para utilizar a busca textual nos livros, devemos promover duas alterações em nossa `ViewSet`:
- Novamente alterar o atributo `filter_backends`, adicionando o *Backend* `SearchFilter` que irá processar a busca; e
- Adicionar o atributo `search_fields`, contendo os campos que permitirão a busca.

- A `LivroViewSet` ficará assim:

```python
...
from rest_framework.filters import SearchFilter
...

class LivroViewSet(viewsets.ModelViewSet):
...
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["categoria__descricao", "editora__nome"]
    search_fields = ["titulo"]
...
```

- Para pesquisar por um livro, basta adicionar o parâmetro `search` na URL, com o valor a ser pesquisado. Por exemplo, para pesquisar por livros que contenham a palavra `python` no título, a URL ficaria assim:
  - http://127.0.0.1:8000/api/livros/?search=python

- Faça o _commit_ e _push_ das alterações.

**Exercício**

- Acrescente a busca textual nas *models* `Autor`, `Categoria`, `Editora` e `Compra`.

# 38. Ordenação dos livros

A ordenação serve para adicionar a funcionalidade de ordenar os resultados de uma consulta.

- Para utilizar a ordenação nos livros, devemos promover três alterações em nossa `ViewSet`:
- Novamente alterar o atributo `filter_backends`, adicionando o *Backend* `OrderingFilter` que irá processar a ordenação; e
- Adicionar o atributo `ordering_fields`, contendo os campos que permitirão a ordenação.
- Adicionar o atributo `ordering` com o campo que será utilizado como padrão para ordenação.
- A `LivroViewSet` ficará assim:

```python
...
from rest_framework.filters import SearchFilter, OrderingFilter
...

class LivroViewSet(viewsets.ModelViewSet):
...
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["categoria__descricao", "editora__nome"]
    search_fields = ["titulo"]
    ordering_fields = ["titulo", "preco"]
    ordering = ["titulo"]
...
```

- Para ordenar os livros, basta adicionar o parâmetro `ordering` na URL, com o valor do campo a ser ordenado. Por exemplo, para ordenar os livros pelo título, a URL ficaria assim:
  - http://127.0.0.1:8000/api/livros/?ordering=titulo
- Pode-se ainda juntar a ordenação com a busca textual. Por exemplo, para ordenar os livros pelo título e que contenham a palavra `python` no título, a URL ficaria assim:
  - http://127.0.0.1:8000/api/livros/?ordering=titulo&search=python
- Para utilizar os filtros e a ordenação, basta adicionar os parâmetros na URL, com os valores desejados. Por exemplo, para ordenar os livros pelo título de uma determinada categoria e editora, a URL ficaria assim:
  - http://127.0.0.1:8000/api/livros/?categoria=1&editora=1&ordering=titulo
  - É possível utilizar todos os recursos ao mesmo tempo: múltiplos filtros, busca textual e ordenação.
    - http://127.0.0.1:8000/api/livros/?categoria=20&editora=18&ordering=titulo&search=python

- Faça o _commit_ e _push_ das alterações.

**Exercício**

- Acrescente a ordenação nas *models* `Autor`, `Categoria`, `Editora` e `Compra`.


# 39. Acrescentando a data da compra

Nesse momento, não temos a data da compra. Vamos incluir a data da compra, utilizando a data e hora atual no momento da criação da compra.

- No `models.py`, vamos incluir o campo `data` no model `Compra`:

```python
...
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.ABERTA)
    data = models.DateTimeField(auto_now_add=True)
...
```

> O campo `data` é um campo do tipo `DateTimeField`, que armazena a data e a hora da compra. O parâmetro `auto_now_add=True` indica que o campo será preenchido automaticamente com a data e hora atual, quando a compra for criada.

- Execute as migrações.
- Para testar, crie uma nova compra e verifique que a data da compra foi gravada.
- Faça o _commit_ e _push_ das alterações.

**Modificando o serializer de compra para mostrar a data da compra**

- No `serializers/compra.py`, vamos incluir o campo `data` no `serializer` de `Compra`:

```python
...
class ComprasSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    data = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "data", "itens")
...
```

**Acrescentando filtro e ordenação por data**

- No `views/compra.py`, vamos alterar o atributo `filterset_fields`, na `viewset` de `Compra` para filtrar as compras por `data`.
- Vamos também alterar o atributo `ordering_fields`, na `viewset` de `Compra` para ordenar as compras por `data`.

```python
...
    filterset_fields = ["usuario", "status", "data"]
    ordering_fields = ["usuario", "status", "data"]
...
```

- Para ordenar por data, em ordem descrente:
  - http://127.0.0.1:8000/api/compras/?ordering=-data

# 40. Adicionando paginação à API

Nesse momento, a API retorna todos os registros de uma vez. Vamos adicionar paginação à API.

- No objeto `REST_FRAMEWORK`, no `settings.py`, vamos incluir os seguintes parâmetros:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    ...
}
```

> Feito isso, o resultado da API será paginado, com 10 registros por página.

> O formato do resultado da API será o seguinte:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "usuario": 1,
            "status": 1,
            "total": "100.00",
            "data": "2021-08-22T21:00:00Z",
            "itens": [
                {
                    "id": 1,
                    "livro": 1,
                    "quantidade": 1,
                    "preco_item": "100.00",
                    "total": "100.00"
                }
            ]
        },
        {
            "id": 2,
            "usuario": 1,
            "status": 1,
            "total": "100.00",
            "data": "2021-08-22T21:00:00Z",
            "itens": [
                {
                    "id": 2,
                    "livro": 1,
                    "quantidade": 1,
                    "preco_item": "100.00",
                    "total": "100.00"
                }
            ]
        }
    ]
}
```

> O campo `count` indica a quantidade de registros retornados.

> O campo `next` indica a url da próxima página.

> O campo `previous` indica a url da página anterior.

> O campo `results` indica os registros retornados.


# 41. Adicionando tipo de pagamento à model de Compra

Vamos adicionar o tipo de pagamento à compra. O tipo de pagamento pode ser `cartão de crédito`, `cartão de débito`, `pix`, `boleto` ou `outros`.

- No `models\compra.py`, vamos incluir o campo `tipo_pagamento` no model `Compra`:

```python
...
class Compra(models.Model):
    class TipoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, "Cartão de Crédito"
        CARTAO_DEBITO = 2, "Cartão de Débito"
        PIX = 3, "PIX"
        BOLETO = 4, "Boleto"
        TRANSFERENCIA_BANCARIA = 5, "Transferência Bancária"
        DINHEIRO = 6, "Dinheiro"
        OUTRO = 7, "Outro"
...
    tipo_pagamento = models.IntegerField(choices=TipoPagamento.choices, default=TipoPagamento.CARTAO_CREDITO)
...
```

> O campo `tipo_pagamento` é um campo do tipo `IntegerField`, que armazena o tipo de pagamento da compra. O parâmetro `choices` indica as opções de pagamento. O parâmetro `default` indica o tipo de pagamento padrão.

- Execute as migrações.
- Para testar, crie uma nova compra e verifique que o tipo de pagamento foi gravado.
- Faça o _commit_ e _push_ das alterações.

# 42. Adicionando o tipo de usuário à model de Usuário

Uma forma de diferenciar os usuários é através do tipo de usuário. Vamos adicionar o tipo de usuário à model de usuário.
Outra abordagem possível é utilizar o `Group` do Django.

- No `models\usuario.py`, vamos incluir o campo `tipo_usuario` no model `Usuario`:

```python
...
class Usuario(AbstractUser):
    class TipoUsuario(models.IntegerChoices):
        CLIENTE = 1, "Cliente"
        VENDEDOR = 2, "Vendedor"
        GERENTE = 3, "Gerente"
...
    tipo_usuario = models.IntegerField(_("User Type"), choices=TipoUsuario.choices, default=TipoUsuario.CLIENTE)
...
```

> O campo `tipo_usuario` é um campo do tipo `IntegerField`, que armazena o tipo de usuário. O parâmetro `choices` indica as opções de usuário. O parâmetro `default` indica o tipo de usuário padrão.

- Execute as migrações.
- Para testar, crie um novo usuário e verifique que o tipo de usuário foi gravado.

Uma forma de utilizar o tipo de usuário é verificando se o usuário é `GERENTE` e então permitir que ele tenha acesso a todas as compras. Vamos ver como fazer isso.

- No `views/compra.py`, vamos alterar o método `get_queryset` para permitir que o usuário `GERENTE` tenha acesso a todas as compras:

```python
...
class CompraViewSet(ModelViewSet):
...
    def get_queryset(self):
        usuario = self.request.user
...
        if usuario.tipo == Usuario.Tipos.GERENTE:
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
...
```

> O método `get_queryset` é chamado quando uma compra é listada. Ele retorna apenas as compras do usuário autenticado, exceto se o usuário for `GERENTE`, que retorna todas as compras.

- Para testar, autentique-se com um usuário normal e depois com um que seja `GERENTE`. Você verá que o `GERENTE` consegue ver todas as compras, enquanto o usuário normal só consegue ver as suas compras.
- Faça o _commit_ e _push_ das alterações.

---

# Exercícios

## Garagem

O projeto Garagem é um projeto de uma garagem de carros. O objetivo é praticar aquilo que foi visto nesse tutorial, no projeto Livraria.

No final, nosso projeto ficará assim:

![Modelo Garagem](diagramas/garagem_mer.png "Modelo Garagem")

### [Aula 5](#5-criando-um-segundo-projeto): Crie o projeto Garagem

Seguindo aquilo que você já aprendeu na criação do projeto da `Livraria`, crie um **novo projeto**:

-   Crie uma pasta para o projeto.
-   Crie um ambiente virtual para o projeto (pdm).
-   Instale o Django.
-   Crie o projeto Django, e a aplicação:
    -   Nome do projeto: **config**.
    -   Nome da aplicação: **garagem**.
    -   Registre a aplicação no `settings.py`.
-   Suba o projeto pro **GitHub**:
    -   Não esqueça de criar o arquivo `.gitignore` e de retirar o `db.sqlite3` dele.
    -   Nomeie o commit como sendo `Criação do projeto`.
-   Crie os modelos conforme a definição abaixo:
    -   Crie o modelo `Marca`, com as seguintes definições:
        -   `nome` (string, máximo 50 caracteres).
        -   `nacionalidade` (string, máximo 50 caracteres, opcional).
        -   `__str__` (retorna o nome da marca em caixa alta).
    -   Registre a model `Marca` no `Admin`.
    -   Faça um commit com a mensagem _"Criação do modelo Marca"_.
    -   Crie o modelo `Categoria`, com as seguintes definições:
        -   `descricao` (string, máximo 100 caracteres).
        -   `__str__` (retorna a descrição da categoria).
    -   Registre a model `Categoria` no `Admin`.
    -   Faça um commit com a mensagem _"Criação do modelo Categoria"_.
    -   Inclua alguns registros no banco de dados.


### [Aula 6](#6-criando-os-outros-modelos-de-dados): Crie os demais modelos de dados no projeto Garagem

Crie os modelos de dados `Acessório` e `Cor`, com os seguintes atributos:

-   `Acessório`:

    -   `descricao` (string, máximo 100 caracteres).
    -   `__str__` (retorna a descrição do acessório).

-   `Cor`:
    -   `descricao` (string, máximo 100 caracteres).
    -   `__str__` (retorna a descrição da cor).

Crie o modelo `Veículo`, com os seguintes atributos:

-   `Veículo`:
    -   `marca` (chave estrangeira para `Marca`).
    -   `categoria` (chave estrangeira para `Categoria`).
    -   `cor` (chave estrangeira para `Cor`).
    -   `ano` (inteiro, permite nulo, default 0).
    -   `preco` (decimal, máximo 10, dígitos, 2 casas decimais, permite nulo, default 0).
    -   `__str__` (retorna a marca, modelo, ano e cor do carro).


### [Aula 7](#7-criando-uma-api-rest): Crie a API REST no projeto Garagem

-   Instale o `djangorestframework`.
-   Crie o serializador para a classe `Marca`.
-   Teste a API com a ferramenta de sua preferência.

### [Aula 8](#8-continuando-a-criação-da-api-rest): Crie a API REST no projeto Garagem para as demais classes

-   Crie a API para as classes `Categoria`, `Cor`, `Acessorio`, e `Veiculo`.
    -   Faça um commit para cada _endpoint_ criado.
-   Crie **3 serializadores** diferentes para a classe `Veículo`:
    -   Um para a listagem, que mostre apenas o id, o modelo e o ano.
    -   Outro para a recuperação de um único veículo, que mostre todos os campos, com profundidade 1.
    -   Outro para a criação e alteração, que mostre todos os campos, sem profundidade.
-   Teste a API com a ferramenta de sua preferência.

### [Aula 9](#9-aplicação-frontend-vuejs-e-django-cors-headers): Crie uma aplicação FrontEnd com Vuejs para a Garagem

-   Criação de uma aplicação frontend com Vuejs para consumir a API REST do projeto `Garagem`.

### [Aula 10](#10-relacionamento-n-para-n): Crie um relacionamento n para n entre `Veiculo` e `Acessorio` no projeto Garagem



-   Crie um relacionamento n para n entre `Veiculo` e `Acessorio`, utilizando um campo do tipo `ManyToManyField`.
-   Inclua alguns acessórios em alguns veículos pelo Admin.
-   Teste a API REST de veículos e acessórios.


### Primeira avaliação do segundo trimestre

- Modifique o projeto Garagem para refletir o seguinte modelo:

![Modelo Garagem](diagramas/garagem_mer.png "Modelo Garagem")

- Crie (ou modifique) as `views`, `urls` e `serializers` necessários para implementar a API REST para o modelo acima.
- Reestruture o projeto em pastas, para `models`, `views` e `serializers` ficarem em pastas separadas.
- Modifique o usuário padrão do Django para usar o `email` como `username`.
- Permita que um carro possa ter várias fotos.
- Habilite  o Swagger no projeto.
- Faça o cadastro completo, com fotos, de pelo menos 3 carros.
- Instale o `django-extensions` e [gere o diagrama](#a4-gerando-um-diagrama-de-banco-de-dados-a-partir-das-models) de banco de dados do projeto.
- Veja se o diagrama gerado está correto, de acordo com o modelo proposto acima.

---

# Apêndices

# A0. Instalação do VS Code

**1.1.2 Atualização do VS Code**

Para **instalar** ou **atualizar** o **VS Code**, siga as seguintes instruções:

**No Ubuntu/Mint e derivados:**

```shell
sudo apt install code
```

**No Manjaro:**

```shell
yay -Syu visual-studio-code-bin
```

**No Windows:**

-   Clique no ícone de engrenagem no canto inferior esquerdo da tela do VS Code e clique em `Check for Updates`.

# A0. Instalação e sincronização de extensões do VS Code

## Instalação de extensões no VS Code

Instale as extensoẽs do **VS Code** de sua preferência. Você pode instalar as extensões clicando no ícone de extensões no canto esquerdo da tela do **VS Code** e pesquisando pelo nome da extensão.

Eu recomendo as seguintes:

-   [Black Formatter(Formatação de código)](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
-   [ESLint (JavaScript)](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
-   [Even Better TOML (Melhorias na edição de arquivos TOML)](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)
-   [Intellicode (Desenvolvimento Inteligente)](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
-   [isort (Organização de imports)](https://marketplace.visualstudio.com/items?itemName=Tyriar.sort-lines)
-   [Markdown All in One (Edição de arquivos Markdown)](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
-   [Material Icon Theme (Temas de ícones)](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
-   [Peacock (Personalização de cores)](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock)
-   [Portuguese (Brazil) Language Pack for Visual Studio Code (Tradução para Português da interface do VS Code)](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-pt-br)
-   [Prettier (Formatação de código)](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
-   [Python (Uhuuuu!)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [SqLite Viewer (Visualização de bancos de dados SQLite)](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
-   [Thunder Client (Teste de APIs)](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
-   [TODO Highlight (Realce de TODOs)](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
-   [TypeScript Vue Plugin (Desenvolvimento de aplicações Vue.js)](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.vue)
-   [Vue Language Features (Desenvolvimento de aplicações Vue.js)](https://marketplace.visualstudio.com/items?itemName=octref.vetur)


**Extensão Vue.js devtools no Google Chrome**

-   [Vue.js devtools](https://chrome.google.com/webstore/detail/nhdogjmejiglipccpnnnanhbledajbpd)

## Sinconização de extensões no VS Code

Você pode configurar a sincronização das extensões entre os computadores. Para isso:

-   Faça login com a conta do **GitHub** ou da **Microsoft** no VS Code.
-   Clique no ícone de engrenagem no canto inferior esquerdo da tela do VS Code e clique em `Ativar a Sincronização de Configurações`.

# A0. Instalação e configuração do PDM

**1.2 Instalação do PDM**

**1.2.1 Instalação do PDM no Linux**

As instruções a seguir são para o **Linux Manjaro e Ubuntu**. Se você estiver usando outra distribuição ou quiser mais informações, consulte a documentação do [PDM](https://pdm.fming.dev/latest/).

-   Abra um terminal:

    `Ctrl + Alt + T`

-   Verifique se o **PDM** está instalado:

```shell
pdm -V
```

-   Se a versão for inferior a 2, instale a versão mais recente:

```shell
curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
```

**Configuração do PDM no `bash` (Ubuntu e derivados)**

-   Execute o seguinte comando:

```shell
curl -sSL https://github.com/marrcandre/django-drf-tutorial/raw/main/scripts/pdm_config_bash.sh | bash
```

**Configuração do PDM no `zsh` com o `Oh! My Zsh` (Manjaro e derivados)**

-   Execute o seguinte comando:

```shell
curl -sSL https://github.com/marrcandre/django-drf-tutorial/raw/main/scripts/pdm_config_ohmyzsh.sh | zsh
```

**Após executar os comandos acima, reinicie o terminal, e verifique se o PDM está instalado.**

**1.2.2 Instalação do PDM no Windows**
Execute o comando abaixo no **PowerShell** (pode ser no Terminal do `VS Code`):

```shell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py -UseBasicParsing).Content | python -
```

Verifique se o **PDM** está configurado para não usar virtualenv:

```shell
pdm config
```

**Observação:**

Se você não fizer essa configuração, o **PDM** irá criar uma pasta `.venv` no diretório do projeto. Para resolver isso, você deve apagar a pasta `.venv` e executar o comando `pdm config python.use_venv false` e então executar o comando `pdm install`.


# A1. Criação de _scripts_ PDM

Como o `npm run`, com o `PDM`, você pode executar _scripts_ ou comandos arbitrários com pacotes locais carregados.

Aqui estão alguns exemplos de scripts que você pode adicionar ao seu `pyproject.toml`:

-   Edite o arquivo `pyproject.toml` na raiz do projeto:

```python
[tool.pdm.scripts]
dev = "python manage.py runserver"
runserver = "python manage.py runserver"
createsuperuser = "python manage.py createsuperuser"
migrate = "python manage.py migrate"
makemigrations = "python manage.py makemigrations"
shell = "python manage.py shell"
test = "python manage.py test"
startapp = "python manage.py startapp {args}"
loaddata = "python manage.py loaddata {args}"
dumpdata = "python manage.py dumpdata {args}"
```

-   Agora, você pode executar os comandos do Django com o `pdm run`, por exemplo:

```shell
pdm run dev
```

# A2. Formatação de código com isort e black

As ferramentas de formatação de código `isort` e `black` são muito úteis para manter o código Python organizado e legível. Enquanto o `isort` organiza as importações, o `black` formata o código, seguindo as convenções do PEP8.

-   Instale as ferramentas de desenvolvimento `isort` e `black`:

```shell
pdm add --dev isort black
```

-   Crie um arquivo `.isort.cfg` na raiz do projeto:

```shell
touch .isort.cfg
```

-   Abra o arquivo `.isort.cfg` e coloque o seguinte conteúdo:

```python
[isort]
default_section = THIRDPARTY
known_first_party = config  # change it for the name of your django project
known_django = django
sections = FUTURE,STDLIB,DJANGO,THIRDPARTY,FIRSTPARTY,LOCALFOLDER

[settings]
profile=black
skip=.git, __init__.py, __pypackages__/
```

-  Abra o arquivo `pyproject.toml` e inclua o seguinte conteúdo:

```python
[tool.black]
line-length = 120
```

**Usando o isort e o black**

Execute os seguintes comandos:

```shell
pdm run isort .
pdm run black .
```

Opcionalmente, você pode utilizador o formatador de código em um arquivo, selecionando o código (`Ctrl` + `A`) e pressionando `Ctrl + Shift + I`.

# A3. Gerando o arquivo requirements.txt automaticamente

O arquivo `requirements.txt` é utilizado para instalar as dependências do projeto em um ambiente virtual. Ele será utilizado pelo Heroku, Render, PythonAnywhere e outros servidores de hospedagem para instalar as dependências do projeto.

-   Instale o plugin `pdm-autoexport` do `pdm`:

```shell
pdm plugin add pdm-autoexport
```

-   Execute o seguinte comando:

-   Configure o `autoexport` para gerar o arquivo `requirements.txt` automaticamente, incluindo as seguintes linhas no arquivo `pyproject.toml`:

```toml
[[tool.pdm.autoexport]]
filename = "requirements.txt"
without-hashes = "true"
```

Para gerar o arquivo `requirements.txt` automaticamente, instale qualquer pacote com o `pdm`:

```shell
pdm add django
```

> A partir de agora, sempre que você instalar um pacote com o `pdm`, o arquivo `requirements.txt` será atualizado automaticamente.

# A4. Gerando um diagrama de banco de dados a partir das models

- Instale o `GraphViz`:

```shell
sudo apt install graphviz
```

-   Instale o `django-extensions` e o `pydotplus`:

```shell
pdm add django-extensions pydotplus
```

-   Adicione o `django-extensions` ao `INSTALLED_APPS` do arquivo `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "django_extensions",
]
```

-   Gere o diagrama de banco de dados:

```shell
pdm run python manage.py graph_models -g -o livraria.png livraria
```
# A5. Usando curl para testar a API via linha de comando

-   Liste todas as categorias:

```shell
curl -X GET http://localhost:8000/categorias/
```

-   Liste uma categoria específica:

```shell
curl -X GET http://localhost:8000/categorias/1/
```

-   Crie uma nova categoria:

```shell
curl -X POST http://localhost:8000/categorias/ -d "descricao=Teste"
```

-   Atualize uma categoria:

```shell
curl -X PUT http://localhost:8000/categorias/1/ -d "descricao=Teste 2"
```

-   Delete uma categoria:

```shell
curl -X DELETE http://localhost:8000/categorias/1/
```

# A6. Resolução de erros

**Instalação do plugin pdm-vscode**

Se seu projeto não estiver reconhecendo os arquivos do Python ou do Django, você pode instalar o plugin `pdm-vscode`, que permite a integração do **PDM** com o **VS Code**:


- Instale o plugin `pdm-vscode`, que permite a integração do **PDM** com o **VS Code**:

```shell
pdm plugin add pdm-vscode
```

Na criação do projeto, será criada uma pasta `.vscode` com um arquivo `settings.json` que contém as configurações do **PDM** para o **VS Code**:

```json
{
    "python.analysis.extraPaths": [
        "${workspaceFolder}/__pypackages__/3.10/lib"
    ],
    "python.autoComplete.extraPaths": [
        "${workspaceFolder}/__pypackages__/3.10/lib"
    ]
}
```

> Se esse arquivo não for criado, você pode criá-lo manualmente.

> Se esse arquivo existir, mas não tiver o conteúdo acima, você pode incluir o conteúdo acima manualmente.


## Liberando uma porta em uso

-   Ao tentar executar o comando:

```python
pdm run python manage.py runserver
```

-   Se você receber o seguinte erro:

```shell
Error: That port is already in use.
```

-   Execute o seguinte comando:

```shell
fuser -k 8000/tcp
```

> Este comando vai matar o processo que está rodando na porta 8000. Mude o número da porta conforme necessário.

## Descobrindo o IP da máquina

-   Execute o seguinte comando:

```shell
nmcli device show | grep IP4.ADDRESS | head -1 | awk '{print $2}' | rev | cut -c 4- | rev
```

## Rodando o Django no IP da máquina

-   Execute o seguinte comando:

```shell
pdm run python manage.py runserver <ip_da_maquina>:<porta>
```

Exemplo:

```shell
pdm run python manage.py runserver 191.52.62.13:19005
```

> Essa é uma forma de rodar o Django em um IP e porta específicos, por exemplo, para testar a API em um dispositivo móvel.

## Descobrindo o IP da máquina e rodando o Django no IP da máquina

-   Execute o seguinte comando:

```shell
pdm run python manage.py runserver $(nmcli device show | grep IP4.ADDRESS | head -1 | awk '{print $2}' | rev | cut -c 4- | rev):19005
```

## Removendo temporários, migrations e o banco de dados

```shell
find . -name "__pycache__" -type d -exec rm -r {} +
find . -path "*/migrations/*.pyc" -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
rm -rf __pypackages__ pdm.lock
rm db.sqlite3
```


## Pasta `.venv` criada no projeto

-   Se seu projeto tiver a pasta `.venv`, e não a pasta `__pypackages__`, remova a pasta `.venv`:

```shell
rm -rf .venv
```

- Depois, execute novamente o script de configuração do pdm, da aula 1.
- Opcionalmente, rode o seguinte comando, para configurar o projeto para não usar ambiente virtual:

```shell
pdm config python.use_venv false
```

- Feito isso, execute o `pdm install` novamente.
- Por fim, execute o `pdm run python manage.py runserver` novamente.


## Geração da SECRET_KEY

A SECRET_KEY é uma chave secreta usada pelo Django para criptografar dados sensíveis. Ela é usada, por exemplo, para criptografar as senhas dos usuários. Em sistemas em produção ela deve ser mantida em segredo.

-   Para gerar uma nova SECRET_KEY (chave secreta), a ser colocada no arquivo `.env`, execute o comando:

```shell
python -c "import secrets; print(secrets.token_urlsafe())"
```
- No Django, o comando é:

```shell
pdm run python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

-   Você também pode gerar uma nova chave secreta em https://djecrety.ir/

> Para saber mais sobre a chave secreta, acesse a [documentação](https://docs.djangoproject.com/en/4.1/ref/settings/#secret-key) do Django.

> Não esqueça de substituir a chave secreta pelo valor gerado.

## Abrindo um arquivo sqlite3 na web

- Acesse o site https://sqliteviewer.app/ e abra o arquivo `db.sqlite3` do projeto.

# A7. Aumentando o tempo de vida do token de autenticação JWT

-   Adicione as seguintes linhas ao arquivo `settings.py`:

```shell
from datetime import timedelta
...
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=180),
    "REFRESH_TOKEN_LIFETIME":timedelta(days=1),
}
```
# A99. Implantação (Deploy) do projeto

# A99a. Criação do Banco de Dados no Supabase

Para evitar a perda dos dados a cada nova publicação do projeto, vamos criar um banco de dados externamente no **Supabase**. O banco de dados **SQLite** local será utilizado apenas para desenvolvimento.

**Criando um projeto no Supabase**

Para criar o banco de dados no **Supabase**, siga as instruções a seguir:

-   Acesse o site do [Supabase](https://supabase.com/).
-   Crie uma conta ou conecte-se no **Supabase**.
-   Clique na opção [Start your project](https://supabase.com/dashboard/projects).
- Dẽ um nome ao projeto.
- Selecione a opção `Create a new organization`.
- Dẽ um nome à organização.
- Dê um nome ao banco de dados.
- Escolha uma senha e **guarde-a** (você vai precisar dela).
- Selecione a região `South America (São Paulo)`.

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

**Instalando o pacote `dj_database_url`**

O pacote `dj_database_url` facilita a configuração do banco de dados no Django, pois ele converte a URL do banco de dados para o formato que o Django entende.

- Instale o pacote `dj_database_url`:

```shell
pdm add dj-database-url
```

- Adicione o pacote `dj_database_url` ao arquivo `settings.py`:

```python
import dj_database_url
```

- Substitua a configuração do banco de dados no arquivo `settings.py`:

```python
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        conn_health_checks=True,
    )
}
```

> Essa configuração permite que o Django use o banco de dados local em desenvolvimento e o banco de dados do **Supabase** em produção, definindo a variável de ambiente `DATABASE_URL`.

**Migrando o banco de dados**

- No arquivo `.env`:
  - Altere o valor da variável `MODE` para `MIGRATE`.
  - Descomente a linha `DATABASE_URL`.
- Faça a migracão do banco de dados:

```shell
pdm run python migrate
```

> Observe que o banco de dados foi migrado no `Supabase`.

> Para testar, crie alguns registros no banco de dados. Depois volte a configuração local e perceba que os dados são diferentes na base local e na base do **Supabase**.

- No site do `Supabase`, acesse o `Table Editor` e verifique que as tabelas foram criadas.
- Você também pode ver o esquema das tabelas, em `Database`, `Schema Visualizer`.

**Utilizando o banco de dados local**

- Para voltar a usar o banco de dados local, no arquivo `.env`:
  - Altere o valor da variável `MODE` para `DEVELOPMENT`.
  - Comente a linha `DATABASE_URL`.

**IMPORTANTE:** A cada nova alteração no banco de dados, você deve repetir esse processo de migração, tanto no banco de dados local quanto no banco de dados do **Supabase**.

# A99b. Publicação o projeto no `Render`

O **Render** é uma plataforma de hospedagem que permite publicar aplicações web, bancos de dados e outros serviços. No site existe um link para o tutorial oficial: [https://render.com/docs/deploy-django](https://render.com/docs/deploy-django)


**Criando um script de Build**

Precisamos executar uma série de comandos para construir nosso aplicativo. Podemos fazer isso com um script de construção (`build script`).

- Crie um arquivo chamado `build.sh` na raiz do projeto com o seguinte conteúdo:

```shell
#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Atualiza o pip
pip install --upgrade pip

# Instala as dependências
pip install -r requirements.txt

# Coleta os arquivos estáticos
python manage.py collectstatic --no-input

# Aplica as migrações
python manage.py migrate
```

- Torne o script executável:

```shell
chmod a+x build.sh
```

- Adicione os pacotes `Uvicorn` e `Gunicorn` ao projeto:

```shell
pdm add uvicorn gunicorn
```

**Testando a execução localmente**

- Execute a seguinte linha de comando para testar a execução localmente:

```shell
pdm run python -m gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker
```

- Acesse o endereço `http://localhost:8000` no navegador para verificar se a aplicação está funcionando.

> O que fizemos foi substituir o servidor de desenvolvimento do Django pelo servidor `Uvicorn` e `Gunicorn`.

**Configurando o Render**

- **Acesse** o site do [Render](https://render.com/)
- **Crie** uma conta ou **conecte-se** a uma conta existente.
- Crie um novo serviço (**Web Service**).
- Escolha a opção `Build and deploy from a Git repository` (Construir e implantar a partir de um repositório Git).
- Escolha o repositório do projeto.
- Preencha as informações necessárias:
  - Name: `nome-do-projeto`.
  - Region: `Ohio (US East)`.
  - Branch: `main`.
  - Runtime: `Python`.
  - Build command: `./build.sh`.
  - Start command: `python -m gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker`.
  - Instance Type: `Free`.

- Environment Variables: clique em `Add from .env` e adicione as informações do seu arquivo `.env`:

```ini
MODE=PRODUCTION
DEBUG=False
SECRET_KEY=[sua_secret_key]
WEB_CONCURRENCY=4
DATABASE_URL=[sua_database_url]
CLOUDINARY_URL=cloudinary://your_api_key:your_api_secret@your_cloud_name
```
> Crie uma `SECRET_KEY` nova. Veja como [aqui](#geração-da-secret_key). Coloque essa chave no lugar de `[sua_secret_key]`.

> Coloque a URL do banco de dados do **Supabase** no lugar de `[sua_database_url]`.

- Clique em `Create Web Service`.

> Se tudo estiver correto, o projeto será implantado no **Render**.

# A99c. Armazenando arquivos estáticos no Cloudinary

Vamos utilizar o Cloudinary para armazenar os arquivos estáticos, como as imagens dos livros. Detsa forma, os arquivos não serão perdidos a cada nova implantação.

**Criando uma conta no Cloudinary**

Acesse o site do [Cloudinary](https://cloudinary.com/) e crie uma conta.

**Instalação do pacote `django-cloudinary-storage`**

- Para instalar, digite:

```shell
pdm add django-cloudinary-storage
```

- Adicione os pacotes  `cloudinary_storage` e `cloudinary` ao `INSTALLED_APPS`, no `settings.py`, logo após o pacote `django.contrib.staticfiles`:

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    # ...
]
```

- Nas configurações de arquivos estáticos, inclua o seguinte conteúdo:

```python
STATIC_URL = "/static/"

if MODE in ["PRODUCTION", "MIGRATE"]:
    CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    MEDIA_URL = '/media/'
else:
    MY_IP = os.getenv("MY_IP", "127.0.0.1")
    MEDIA_URL = f"http://{MY_IP}:19003/media/"
```

**Configuração do Cloudinary**

-   Edite o arquivo `.env`, incluindo a seguinte variável:

```shell
# Cloudinary
CLOUDINARY_URL=cloudinary://your_api_key:your_api_secret@your_cloud_name
```

> Altere as informações de acordo com o seu projeto, acessando o [Cloudinary Console](https://cloudinary.com/console) na opção `Dashboard`.

- Inclua essa mesma variável no Fl0, na aba `Environment variables`.

**Testando**

- Coloque a variável `MODE` com o valor `MIGRATE` no arquivo `.env`.
-  Faça o upload de uma imagem pelo `Admin` do `Django` e verifique se ela foi salva no `Cloudinary`, na opção `Media Explorer`.
-  Se deu certo, faça o *commit* das alterações.
-  Sua aplicação deve estar funcionando normalmente, utilizando o `Cloudinary` para armazenar os arquivos estáticos.


# Contribua

**Para contriburi com esse projeto:**

-   Criar um _fork_ do projeto.
-   Clonar o _fork_
-   Criar um _branch_ para a sua contribuição.
-   Fazer as alterações no seu _branch_.
-   Enviar um _pull request_ para o projeto original.

---

Marco André Mendes \<marcoandre@gmail.com>
