# Django com DRF (2024)

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

- [Instale ou atualize o VS Code](#a1-instalação-e-atualização-do-vs-code)
- [Instale e sincronize as extensões do VS Code.](#a2-instalação-e-sincronização-de-extensões-do-vs-code)
- [Instale e configure o PDM](#a3-instalação-e-configuração-do-pdm)


# 2. Criação do projeto

**2.1 O projeto Livraria**

Este projeto consiste em uma API REST para uma livraria. Ele terá as seguintes classes:

-   `Categoria`: representa a categoria de um livro.
-   `Editora`: representa a editora de um livro.
-   `Autor`: representa o autor de um livro.
-   `Livro`: representa um livro.
-   `User`: representa um usuário do sistema.
-   `Compra`: representa uma compra de livros.
-   `ItemCompra`: representa um item de uma compra.

**Modelo Entidade Relacionamento**

O modelo entidade relacionamento (MER) do projeto é o seguinte:

![Modelo ER](diagramas/livraria_MER.png "Modelo ER")

**Diagrama de Classes**

O diagrama de classes do projeto é o seguinte:

![Diagrama de Classes](diagramas/livraria_classes.png "Diagrama de Classes")

**Modelo de Dados do Django**

O modelo de dados do **Django** é o seguinte:

![Modelo de Dados do Django](diagramas/livraria_final.png "Modelo de Dados do Django")


**2.2 Criação do projeto a partir de um template**

> **IMPORTANTE**: Vamos criar o projeto `livraria` a partir de um repositório de _template_. Se você quiser criar aprender a criar um projeto do zero, acesse o tutorial de [2023](https://github.com/marrcandre/django-drf-tutorial/tree/versao-2023).

- Acesse o _template_ em https://github.com/marrcandre/template_django_pdm.
- Clique no botão `Use this template` em `Create a new repository`.
- Preencha as informações solicitadas:
  - `Owner`: <seu usuário no GitHub>
  - `Repository name`: `livraria`
- Click no botão `Create repository`.

> Feito isso, o repositório `livraria` será criado no seu GitHub.

**2.3 Clonando o projeto**

Você pode clonar o projeto de duas formas:

**2.3.1 Usando o VS Code**
  - Abra o **VS Code**.
  - Clique no ícone de **Source Control** na barra lateral esquerda.
    - Clique no botão `Clone Repository`.
    - Vocẽ também pode teclar `Control+Shift+P` e digitar `Clone Repository`.
  - Digite a URL do repositório do projeto (ou procure na lista de repositórios disponíveis).
  - Escolha a pasta onde o projeto será clonado.
  - Clique no botão `Clone`.

**2.3.2 Usando o terminal**
  - Abra o terminal.
  - Vá para a pasta onde o projeto será clonado.
  - Digite o comando:

```shell
git clone <URL do repositório>
```
- Abra o projeto no **VS Code**, digitando:

```shell
code .
```

O projeto criado ficará assim:

![Projeto inicial](imagens/template_arquivos_iniciais.png)

**2.4 Instalando as dependências**

-   Abra o terminal no **VS Code** (Ctrl+Shift+´).
-   Instale as dependências do projeto:

```shell
pdm install
```

**2.5 Criando o arquivo `.env`**

-   Crie o arquivo `.env`, a partir do arquivo `.env.exemplo`:
  - Abra o arquivo `.env.exemplo`.
  - Escolha a opção `Salvar como...` (Ctrl+Shift+S).
  - Salve o arquivo como `.env`.

> Opcionalmente, você pode criar o arquivo `.env` a partir do terminal, digitando:

```shell
cp .env.exemplo .env
```

**2.4 Rodando o servidor de desenvolvimento**

-   Para executar o projeto, digite no terminal:

```shell
pdm run dev
```

**2.5 Acessando o projeto**

-   Acesse o projeto no navegador:

    http://0.0.0.0:19003/admin

- Os dados de acesso são:
  - **Usuário**: `a@a.com`
  - **Senha**: `teste.123`
- Após acessar, você pode o nome do usuário e a senha.

> **IMPORTANTE**: O servidor de desenvolvimento deve estar sempre rodando para que o projeto funcione.

**É isso! Seu projeto está inicializado e rodando!!!**

**2.6 Exercício**

-   Apague o projeto e crie novamente, seguindo as instruções acima.
-   Verifique se o projeto está rodando e se o `Admin` está em execução.
-   Observe que configurações precisam ser feitas novamente e quais não foram mais necessárias.

# 3. Criação de uma aplicação

**3.1 Compreendendo uma aplicação**

Uma aplicação no **Django** é um conjunto de arquivos e pastas que contém o código de uma funcionalidade específica do seu site.

Uma aplicação pode ser criada dentro de um projeto ou importada de outro projeto.

Em nosso projeto, temos uma aplicação criada, chamada `core`, conforme a imagem abaixo:

![App core](imagens/core_app.png)

> Todas as aplicações precisam ser adicionadas ao arquivo `settings.py` do projeto, na seção `INSTALLED_APPS`.

Dentro da pasta `core` temos alguns arquivos e pastas, mas os mais importantes são:

-   `migrations`: é a pasta de migrações de banco de dados da aplicação.
-   `models`: é a pasta onde ficam as `models` (tabelas) da aplicação.
-   `serializers`: é a pasta onde ficam os serializadores da aplicação.
-   `views`: é a pasta onde ficam as views da aplicação.
-   `admin.py`: é o arquivo de configuração do `Admin`, uma ferramenta que permite que você gerencie os dados do seu site.

> O arquivo `__init__.py` é um arquivo que indica que a pasta é um pacote Python. Ele vai aparecer em todas as pastas que contêm código Python. Muitas vezes, ele é um arquivo vazio.

Posteriormente, iremos modificar esses arquivos, bem como incluir alguns arquivos novos.

**3.2 Model User**

Um modelo (`model`) no **Django** é uma classe que representa uma tabela no banco de dados. Cada atributo (variável) dessa classe representa um campo da tabela.

Para maiores informações consulte a [documentação](https://docs.djangoproject.com/en/4.0/topics/db/models/) do **Django** sobre `models`.

> Você pode observar que a pasta `models` já contém um modelo de dados, dentro do arquivo `user.py`, chamado `User`. Esse modelo modifica o usuário padrão fornecido pelo **Django** e representa um usuário do sistema.

**3.3 Criação da model de Categoria**

-   Vamos começar criando o modelo de dados `Categoria`, que representa uma categoria de livro, como por exemplo: `Ficção`, `Terror`, `Romance`, etc.

-   Dentro da pasta `models` da aplicação `core` crie um arquivo chamado `categoria.py`.
-   Adicione o seguinte código no arquivo `categoria.py`:

```python
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
```

Nesse código, você:

-   Importou o pacote necessário para criar a `model`;
-   Criou a classe `Categoria`;
-   Incluiu o campo `descricao`, que é uma `string` de no máximo 100 caracteres. Esse campo é obrigatório.

-  **IMPORTANTE**:
   -  O nome da classe deve ser sempre no singular e com a primeira letra maiúscula.
   -  O nome dos campos deve ser sempre no singular e com a primeira letra minúscula.

**3.4 Inclusão da `model` no arquivo `__init__.py`**

- Precisamos ainda incluir a `model` no arquivo `__init__.py` da pasta `models`:

```python
from .categoria import Categoria
```

**3.5 Efetivando a criação da tabela**

Precisamos ainda efetivar a criação da tabela no banco de dados.

-   Abra um novo terminal, deixando o terminal antigo executando o servidor do projeto.

-   Crie as migrações:

```shell
pdm run migrate
```

> Esse comando executará 3 comandos em sequência:
> - `makemigrations`: cria as migrações de banco de dados.
> - `migrate`: efetiva as migrações no banco de dados.
> - `graph_models`: cria/atualiza um diagrama de classes do modelo de dados.

-   Acesse o arquivo do banco de dados (`db.sqlite3`) e verifique se a tabela `core_categoria` foi criada.
-   Para ver o diagrama de classes atualizado, acesse o arquivo `core.png` na pasta raiz do projeto.
-   Acesse o `Admin` do projeto e verifique se a nova tabela aparece lá.

**3.6 Inclusão no Admin**

A tabela ainda não apareceu, certo? Isso acontece poque ainda não incluímos a `model` no `Admin`.

-   Vamos incluir a `model` no `Admin`. Abra o arquivo `admin.py` da aplicação `core` e adicione o seguinte código no final do arquivo:

```python
admin.site.register(models.Categoria)
```

**3.7 Exercício**

- Acesse novamente o `Admin` e inclua algumas categorias no banco de dados.

**3.8 O campo `id`**

O campo `id` é criado automaticamente pelo **Django**. Ele é o identificador único de cada registro da tabela.

**3.9 Mudando a forma de exibição dos registros criados**

-   Inclua algumas categorias no banco de dados.
-   Você perceberá que a descrição dos informações que você inclui está meio estranha, algo como `Categoria object (1)` e assim por diante.
-   Para resolver, isso, vamos fazer uma pequena modificação na `model` Categoria.

**3.10 O método `__str__`**

O método `__str__` é um método especial que é chamado quando você tenta imprimir um objeto. Ele é utilizado no `Admin` e em outros locais para definir como o objeto será exibido.

-   Vamos incluir o método `__str__` na `model` Categoria:

```python
...
    def __str__(self):
        return self.descricao
```

> Isso fará com que a descrição da categoria seja exibida no lugar de `Categoria object (1)`.
> O método `__str__` é um método especial do Python e deve sempre retornar uma `string`.

Volte ao `Admin` verifique o que mudou na apresentação dos objetos da model `Categoria`.

**3.11 Hora de fazer um _commit_**

- Verifique antes se seu computador está configurado corretamente para o **git** com as suas credenciais. Veja como fazer isso [aqui](#4-1-um-aviso-importante).
-  Faça um _commit_ com a mensagem `Criação da model de Categoria`.

**IMPORTANTE: Escrevendo uma boa mensagem de _commit_**

-   Escreva uma mensagem de _commit_ que descreva o que foi feito.
-   Dessa forma fica mais fácil identificar as mudanças sem precisar ver o código.
-   Não escreva mensagens como `Alteração 1`, `Alteração 2`, `Alteração 3`, etc.
-   Escreva mensagens como:
    -   Modificação do arquivo `models.py`
    -   Inclusão da Categoria de Veículos
    -   Alteração do Marca do Veículo


<!-- **3.11 Criação do modelo de dados Editora**

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

from core.models import Categoria, Editora

admin.site.register(Categoria)
admin.site.register(Editora)
```

Após fazer isso tudo, inclua algumas editoras na tabela e veja como ficou o seu banco de dados.



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

from core.models import Autor, Categoria, Editora, Livro

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
>>> from core.models import Categoria
>>> Categoria.objects.get(id=1).livros.all()
```

**6.8 [Exercício](#aula-6-crie-os-demais-modelos-de-dados-no-projeto-garagem): Crie os demais modelos de dados no projeto Garagem** -->


# 4. Criando uma API REST

Nesta aula, vamos criar uma API REST para o projeto `livraria`. Ao final, teremos uma API completa, que permite criar, listar, atualizar e deletar categorias.

**4.1 Instalação e configuração do Django Rest Framework (DRF)**

- Observe que o `DRF` já está instalado no projeto, conforme os arquivos `pyproject.toml` e `requirements.txt`.
- Além disso, o `DRF` já está configurado no arquivo `settings.py`, na seção `INSTALLED_APPS`.

> Essas configurações já foram feitas no template que utilizamos para criar o projeto. Se você estiver criando um projeto do zero, terá que fazer essas configurações manualmente.

**4.2 Criação do serializer**

Um _serializer_ é um objeto que transforma um objeto do banco de dados em um objeto JSON.

-   Crie o arquivo `categoria.py` na pasta `serializers` da aplicação `core`, e adicione o seguinte código, para criar a `CategoriaSerializer`:

```python
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
```

**4.2.1 Explicando o código**

-   `model = Categoria`: define o model que será serializado.
-   `fields = "__all__"`: define que todos os campos serão serializados.

**4.2.2 Inclusão do serializer no __init__.py**

-   Inclua o serializer no arquivo `__init__.py` da pasta `serializers`:

```python
from .categoria import CategoriaSerializer
```

**4.3 Criação da view**

Uma _view_ é um objeto que recebe uma requisição HTTP e retorna uma resposta HTTP.

-   Crie a view `CategoriaViewSet` na pasta `views` da aplicação `core`, no arquivo `categoria.py`:

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
```

**4.3.1 Explicando o código**

-   `queryset = Categoria.objects.all()`: define o conjunto de objetos que será retornado pela view.
-   `serializer_class = CategoriaSerializer`: define o `serializer` que será utilizado para serializar os objetos.

**4.3.2 Inclusão da view no __init__.py**

-   Inclua a view no arquivo `__init__.py` da pasta `views`:

```python
from .categoria import CategoriaViewSet
```

**4.4 Criação das rotas (urls)**

As rotas são responsáveis por mapear as `URLs` para as `views`.

-   Para criar as rotas da `Categoria`, edite o arquivo `urls.py` na pasta `app` e adicione as linhas indicadas:

```python
...
from core.views import UserViewSet
from core.views import CategoriaViewSet # nova linha

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet) # nova linha
router.register(r"users", UserViewSet, basename="users")
...
```

**IMPORTANTE**: as nomes das rotas serão sempre nomes **únicos**, no **plural** e em **minúsculas**. Na maiorias das vezes, os colocamos em **ordem alfabética**.

**4.5 Testando a API**

-   Para acessar a interface gerada pelo DRF, acesse:

    http://0.0.0.0:19003/api/

Se tudo correu bem, você deve ver a interface do DRF.

-   Você pode acessar diretamente a rota da `Categoria`:
    http://0.0.0.0:19003/api/categorias/

Isso deve trazer todas as categorias do banco, no formato **JSON**.

-   Para acessar um único registro, use o seguinte formato:
    http://0.0.0.0:19003/api/categorias/1/

Nesse caso, `1` é o `id` do registro no banco de dados.

**4.6 Opções de manipulação do banco de dados**

As opções disponíveis para manipulação dos dados são:

-   **GET** para **listar** **todos** os registros: http://0.0.0.0:19003/api/categorias/
-   **GET** para **listar** **apenas 1** registro: http://0.0.0.0:19003/api/categorias/1/
-   **POST** (para **criar** um **novo** registro): http://0.0.0.0:19003/api/categorias/
-   **PUT** (para **alterar** um registro existente): http://0.0.0.0:19003/api/categorias/1/
-   **PATCH** (para **alterar parcialmente** um registro): http://0.0.0.0:19003/api/categorias/1/
-   **DELETE** (para **remover** um registro): http://0.0.0.0:19003/api/categorias/1/

**4.7 Outras ferramentas para testar a API**

A interface do DRF é funcional, porém simples e limitada. Algumas opções de ferramentas para o teste da API são:

-   [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) (extensão do **VS Code**)
-   [RapidAPI](https://marketplace.visualstudio.com/items?itemName=RapidAPI.vscode-rapidapi-client) (extensão do **VS Code**)
-   [Insomnia](https://docs.insomnia.rest/insomnia/install) (externo)
-   [Postman](https://www.postman.com/downloads/) (externo)

**4.8 Utilizando o Swagger**

O **Swagger** é uma ferramenta que permite a documentação e teste de APIs.

- Para acessar o **Swagger**, acesse:

    http://0.0.0.0:19003/api/swagger/


**4.9 Exercícios: testando a API e as ferramentas**

Instale uma ou mais das ferramentas sugeridas.

-   Experimente as seguintes tarefas:
    -   Criar uma ou mais categorias;
    -   Listar todas as categorias;
    -   Alterar uma ou mais categorias, utilizando PUT e PATCH;
    -   Listar a categoria alterada;
    -   Remover uma categoria;
    -   Incluir outra categoria;
    -   Listar todas as categorias.

**4.10 Fazendo um _commit_**

-   Faça um _commit_ com a mensagem `Criação da API para Categoria`.

# 5. Aplicação frontend Vuejs

Agora que temos uma API REST completa, vamos criar uma aplicação frontend em `Vuejs` para consumir essa API da Categoria.

- Entre no repositório do template: https://github.com/marrcandre/livraria-vue3.
-  Clique no botão `Use this template` em `Create a new repository`.
-  Clone o projeto para o seu computador.
- Execute os seguintes comandos:

```shell
    npm install
```

```shell
    npm run dev
```
Se tudo correu bem, execute a aplicação:

- http://localhost:3000

> Se os dados não aparecerem, entre na opção Inspecionar do seu navegador (F12)

> Para maiores detalhes sobre a instalação do npm, acesse o tutorial de [Instalação da versão LTS do NodeJS](https://eduardo-da-silva.github.io/aula-desenvolvimento-web/ambiente) do [Prof. Eduardo da Silva](https://eduardo-da-silva.github.io/aula-desenvolvimento-web/ambiente).


# 6. Incluindo a Editora no projeto Livraria

Vamos continuar a criação da API REST para o projeto `livraria`, criando a model `Editora` e a API para ela.

**6.1 Criação da API para a classe Editora**

- Os passos para a criação da API para a classe `Editora` são os mesmos que fizemos para a classe `Categoria`:
  1. Criar a `model` Editora na pasta `models`.
  1. Incluir a `model` no `__init__.py` da pasta `models`.
  1. Incluir a `model` no `Admin`.
  1. Fazer a migração e efetivar a migração.
  1. Criar o serializador na pasta `serializers`.
  1. Incuir o serializador no `__init__.py` da pasta `serializers`.
  1. Criar a `viewset` na pasta `views`.
  1. Incluir a `viewset` no `__init__.py` da pasta `views`.
  1. Incluir a nova rota em `urls.py`.

**6.2 Criação e modificação dos arquivos**

-   Os arquivos ficarão assim:

**`models/editora.py`**

```python
from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome
```

**models/__init__.py**

```python
...
from .editora import Editora
```

**`admin.py`**

```python
...
admin.site.register(models.Editora)
```


**`serializers/editora.py`**

```python
from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora
...
class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
```

**`serializers/__init__.py`**

```python
...
from .editora import EditoraSerializer
```

**`views/editora.py`**

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora
from core.serializers import CategoriaSerializer, EditoraSerializer

...
class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
```

**`views/__init__.py`**

```python
...
from .editora import EditoraViewSet
```

**`urls.py`**

```python
...
from core.views import UserViewSet, CategoriaViewSet, EditoraViewSet
...
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
...
```

**6.3 Fazendo a migração e efetivando a migração**

-   Faça a migração e efetive a migração:

```shell
pdm run migrate
```

- Verifique se a tabela `core_editora` foi criada no banco de dados.

**6.4 Exercícios: testando da API da Editora**

-   Teste todas as operações da `Editora`.
-   Verifique se é possível incluir novas editoras sem incluir todos os campos.
-   Tente utilizar o PUT e o PATCH sem informar todos os campos.

**6.5 Fazendo um _commit_**

-   Faça um _commit_ com a mensagem `Criação da API para Editora`.

# 7. Criação da API para Autor

Vamos continuar a criação da API REST para o projeto `livraria`, criando a model `Autor` e a API para ela. Os passos são os mesmos que fizemos para as classes `Categoria` e `Editora`.

- Crie a API para a classe `Autor`.

O autor terá os seguintes atributos:

-   `nome`: `string` de no máximo 100 caracteres.
-   `email`: campo do tipo email de no máximo 100 caracteres, que pode ser nulo.

- Teste a API.
- Faça o _commit_, com a mensagem `Criação da API para Autor`.

Exercícios:

- Crie no Vuejs a tela para listar, incluir, alterar e excluir autores.

# 8. Criação da API para Livro

Vamos continuar a criação da API REST para o projeto `livraria`, criando a model `Livro` e a API para ela. Os passos iniciais são os mesmos que fizemos para as classes `Categoria`, `Editora` e `Autor`.

**8.1 Criação dos arquivos necessários**

Utilizando um comando no terminal, é possível criar todos os arquivos necessários para a criação da API para a classe `Livro`.

```shell
touch core/models/livro.py core/serializers/livro.py core/views/livro.py
```

É possivel também abrir todos os arquivos de uma vez, utilizando o comando:

```shell
code core/models/livro.py core/models/__init__.py core/serializers/livro.py core/serializers/__init__.py core/views/livro.py core/views/__init__.py app/urls.py core/admin.py
```

> Se você preferir, pode criar os arquivos utilizando o **VS Code**, como já fizemos anteriormente.

Você deve estar se perguntando: posso criar um comando para fazer isso automaticamente? Sim, pergunte-me como. :)

**8.2 Criando o modelo de dados `Livro`**

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

Inclua o modelo no arquivo `__init__.py` da pasta `models`:

```python
from .livro import Livro
```

- Faça as migrações e veja o resultado no banco de dados.

Seu projeto deve ficar assim:

![Projeto com a model Livro](diagramas/core_categoria_editora_autor_livro1.png)

**8.3 Criando a API para a classe Livro**

Da mesma forma que fizemos para as classes `Categoria`, `Editora` e `Autor`, vamos criar a API para a classe `Livro`.

[Siga os passos conforme já definimos.](#6-incluindo-a-editora-no-projeto-livraria)

- Após a criação da API, teste todas as operações de CRUD para a classe `Livro`.
- Faça um _commit_ com a mensagem `Criação da API para Livro`.

# 9. Incluindo chaves estrangeiras no modelo Livro

Nosso livro terá uma **categoria** e uma **editora**. Para isso, vamos incluir campos que serão chaves estrageiras, referenciando os modelos `Categoria` e `Editora`. Esse relacionamento é do tipo **n para 1**. Posteriormente, vamos incluir um relacionamento **n para n** entre `Livro` e `Autor`.

**9.1 Campo `categoria` no `Livro`**

-   Inclua a linha a seguir no modelo `Livro`, logo após o atributo `preco`:

```python
from .categoria import Categoria
...
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros", null=True, blank=True
    )
...
```

-   Vamos entender cada parte:
    -   `models.ForeignKey`: define o campo como sendo uma chave estrangeira.
    -   `Categoria`: o `model` que será associado a esse campo.
    -   `on_delete=models.PROTECT`: impede de apagar uma _categoria_ que possua _livros_ associados.
    -   `related_name="livros"`: cria um atributo `livros` na classe `Categoria`, permitindo acessar todos os livros de uma categoria.
    -   `null=True, blank=True`: permite que o campo seja nulo e em branco. Isso é útil para evitar problemas na migração.

**9.2 Campo `editora` no `Livro`**

-   De forma semelhante, vamos associar o livro a uma editora, incluindo logo em seguida à categoria, a seguinte linha:

```python
from .editora import Editora
...
editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
```
> Observe que os atributos `null=True` e `blank=True` não foram utilizados, pois os campos `categoria` e `editora` são obrigatórios.

- Faça a migração dos dados.

> Observe que os campos `categoria_id` e `editora_id` foram criados no banco de dados, na tabela `core_livro`. Eles são os campos que fazem referência às tabelas `core_categoria` e `core_editora`.

A model `Livro` ficará assim:

![Projeto com a model Livro](diagramas/core_categoria_editora_autor_livro2.png)

**9.3 Testando o atributo `on_delete`**

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

**9.4 Testando o atributo related_name no Django Shell**

No `Django Shell` (que iremos estudar em mais detalhes em uma aula mais adiante), é possível testar o acesso a **todos os livros de uma categoria** usando algo parecido com isso:

-   Abra o Django shell:

```shell
pdm run shellp
```

-   Acesse os livros da categoria com `id` 1:

```python
>>> Categoria.objects.get(id=1).livros.all()
```

> O comando `pdm run shellp` é utilizado para abrir o Django Shell Plus com o ambiente virtual do projeto.

-  Faça um _commit_ com a mensagem `Adiciona relacionamento de Livro com Categoria e Editora`.

# 10. Relacionamento n para n

**10.1 Model com ManyToManyField - Livros com vários autores**

Um livro pode ter vários autores, por isso criaremos agora um relacionamento **n para n** entre `Livro` e `Autor`. Para isso utilizaremos um campo do tipo `ManyToManyField`.

-   Inclua o campo `autores` no modelo `Livro`:

```python
from .autor import Autor
...
autores = models.ManyToManyField(Autor, related_name="livros")
...
```

- Execute as migrações.

> Observe que o campo `autores` não foi criado na tabela `core_livro`. Ao invés disso, uma **tabela associativa** foi criada, com o nome `core_livro_autores`, contendo os campos `livro_id` e `autor_id`. É assim que é feito um relacionamento **n para n** no Django.

> Nesse caso, não é necessário usar o atributo `null=True` e `blank=True`, pois um campo do tipo `ManyToManyField` cria uma tabela associativa.

- A model `Livro` ficará assim:

![Projeto com a model Livro](diagramas/core_categoria_editora_autor_livro3.png)

> Note que na ligação entre `Livro` e `Autor` existem uma "bolinha" em cada lado, indicando que o relacionamento é **n para n**.

> Observe as alterações no banco de dados, no Admin e na API.

**10.2 Exercícios**

-   Teste a API REST de livros e autores.

# 11. Modificação da API para Livro

- Acesse a API do Livro e veja como está a apresentação dos autores:

    http://0.0.0.0:19003/api/livros/

> **Observou que no `Livro`, aparecem apenas os campos `id` da categoria, da editora e dos autores e não as descrições?**

- Vamos resolver isso.

**Criação de múltiplos serializadores**

Podemos criar múltiplos serializadores para um mesmo modelo, de forma a apresentar as informações de diferentes formas, dependendo da operação.

**Apresentação das informações detalhadas no Livro**

Uma forma de mostrar essas informações é essa, em `serializers.py`:

```python
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
```

Teste e você verá que isso resolve a listagem (GET), mas gera problema no criação e alteração (POST, PUT e PATCH).

- Para resolver isso, vamos criar dois (ou mais) serializadores, sendo um para a listagem e outro para a recuperação de um único livro:

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

- Inclua o serializador `LivroDetailSerializer` no arquivo `serializers/__init__.py`:

```python
from .livro import LivroDetailSerializer, LivroSerializer
```

> Observe que no `LivroDetailSerializer` foi incluído o atributo `depth = 1`, que permite a apresentação dos dados relacionados.

- Na viewset, escolhemos o serializador conforme a operação:

```python
...
from core.serializers import LivroDetailSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
```

> Nesse caso, o serializador `LivroDetailSerializer` é utilizado para a listagem e recuperação de um único livro, enquanto o `LivroSerializer` é utilizado para as demais operações, ou seja, criação e alteração.

- Teste a API.
- Faça um _commit_ com a mensagem `Dois serializadores para Livro`.


**Criação de um serializador para a listagem de livros**

Podemos criar um serializador para a listagem de livros, que mostre apenas o `id`, o `título` e o `preço`. Isso pode ser útil, pois traz menos informações, o que pode tornar a listagem mais rápida.

-   Inclua um serializador para a listagem de livros, que mostre apenas o `id`, o `título` e o `preço`:

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

> Observe que o serializador `LivroListSerializer` é utilizado apenas na listagem, enquanto o `LivroDetailSerializer` é utilizado na recuperação de um único livro e o `LivroSerializer` é utilizado nas demais operações.

-   Teste a API. Observe que a listagem de vários livros está diferente da recuperação de um único livro.
-  Faça um _commit_ com a mensagem `Múltiplos serializadores para Livro`.

# 12. Upload e associação de imagens

Vamos instalar uma aplicação para gerenciar o upload de imagens e sua associação ao nosso modelos. Com isso poderemos associar imagens aos livros, ao perfil do usuário, etc.

Essa aplicação não será instalada através do comando `pdm add <pacote>`, pois é uma aplicação que não está disponível no `PyPI`. Ela será instalada manualmente, baixando e descopactando um arquivo compactado.

**Baixando o pacote**

Baixe e descompacte o arquivo com a `app` pronta para ser utilizada.

- No `Linux`, execute o seguinte comando no terminal:

```shell
wget https://github.com/marrcandre/django-drf-tutorial/raw/main/apps/uploader.zip -O uploader.zip && unzip uploader.zip && rm uploader.zip
```

- No `Windows`, execute os seguintes comandos no `PowerShell`:

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

![App Uploader](imagens/uploader_app.png)

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
    "uploader", # nova linha
    "core",
    ...
]
```

**IMPORTANTE:** Não esqueça da vírgula no final da linha.

**Configuração no `settings.py`**

-   Ainda no `settings.py` faça as seguintes configurações, logo após a configuração do `STATIC_URL`:

```python
# App Uploader settings
MEDIA_ENDPOINT = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
FILE_UPLOAD_PERMISSIONS = 0o640
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
pdm run migrate
```

- Se o seu projeto já foi publicado, não esqueça de fazer a migração também no servidor.

**Uso em modelos**

Agora que a aplicação `uploader` está configurada, vamos utilizá-la para associar imagens aos livros.

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

> O campo `capa` é uma chave estrangeira para a tabela `uploader_image`.

-   Faça novamente a migração do banco de dados:

```shell
pdm run migrate
```

O modelo `Livro` ficará assim:

![Projeto com a model Livro com capa](diagramas/core_categoria_editora_autor_livro_com_capa.png)

> Observe que o campo `capa_id` foi criado na tabela `core_livro`, fazendo referência à tabela `uploader_image`.

**Uso no serializer**

-   Edite o arquivo `serializers/livro.py` da aplicação `core` e inclua o seguinte conteúdo:

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

> Alteramos dois serializadores: um para a gravação e outro para a recuperação de um único livro.

**Teste de upload e associação com o livro**

-   Acesse a API de media:

    http://0.0.0.0:19003/api/media/images/

-   Faça o upload de uma imagem.
-   Observe que o campo `capa_attachment_key` foi preenchido com o valor `attachment_key` da imagem.
-   Guarde o valor do campo `capa_attachment_key`.
-   Crie um novo livro, preenchendo o campo `capa_attachment_key` com o valor guardado anteriormente.
-   Acesse o endpoint `http://0.0.0.0:19003/api/media/images/` e observe que a imagem foi associada ao livro.

# 13. Dump e Load de dados

O **dump** dos dados permite que você salve os dados do banco de dados em um arquivo. O **load** dos dados permite que você carregue os dados de um arquivo para o banco de dados. Isso é útil para fazer cópias de segurança, para transferir dados entre bancos de dados, para carregar dados iniciais, etc.

**Carga inicial de dados**

- Acesse o seguinte link:

  - Link: `http://191.52.55.156:19005/admin`
  - Usuário: `a@a.com`
  - Senha: `teste.123`

- Cadastre pelos menos 10 livros, com autor e editora
- Verifique se o livro, autor ou editora já estão cadastrados, para evitar duplicidade.
- **NÃO USE CAIXA ALTA!!!**
- Use o formato de nomes de livros, como no exemplo: `O Senhor dos Anéis - A Sociedade do Anel`

**Cópia de segurança dos dados**

-   Execute o comando `dumpdata`:

```shell
pdm run dumpdata > core_bkp.json
```

-   Observe que o arquivo `core_bkp.json` foi criado:

```shell
code core_bkp.json
```

**Arquivo exemplo**

-   Baixe o arquivo `core.json`:

**No Linux:**

```shell
wget https://github.com/marrcandre/django-drf-tutorial/raw/main/scripts/core.json
```

**No Windows:**

```shell
Invoke-WebRequest -Uri "https://github.com/marrcandre/django-drf-tutorial/raw/main/scripts/core.json" -OutFile core.json
```

**Carga dos dados**

-   Execute o comando `loaddata`:

```shell
pdm run loaddata
```

-  Utilizando o Django Shell Plus, observe que os dados foram carregados:

```shell
pdm run shellp
```
E dentro dele, execute:

```python
>>> Livro.objects.all()
```

Você também pode acessar o Django Admin ou o Swagger e verificar que os dados foram carregados.

# 14. Uso do Django Shell e do Django Shell Plus

O Django Shell é uma ferramenta para interagir com o banco de dados. O Django Shell Plus é uma extensão do Django Shell que inclui alguns recursos adicionais, como a inclusão automática dos modelos.

-   Acesse o shell:

```shell
pdm run shellp
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
(1, {'core.Categoria': 1})
```

-   Observe que o objeto foi removido:

```python
>>> Categoria.objects.all()
<QuerySet []>
```

**Useando o atributo `related_name`**

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

# 15. Customização do Admin

O Admin é uma ferramenta para gerenciar os dados do banco de dados. Ele pode ser customizado para melhorar a experiência do usuário.

-   Edite o arquivo `core/admin.py`:

**Importação das models**

Vamos importar as models de forma explícita:

```python
from core.models import Autor, Categoria, Editora, Livro, User
```

**Registro das models através do decorator `@admin.register`**

Vamos registrar as models através do decorator `@admin.register`:

```python
@admin.register(User)
class UserAdmin(UserAdmin):
...
```

**Customização do Admin**

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

- As linhas com `admin.site.register()` devem ser removidas.

> O atributo `list_display` é uma tupla que define os campos que serão exibidos na listagem.

> O atributo `search_fields` é uma tupla que define os campos que serão utilizados na busca.

> O atributo `list_filter` é uma tupla que define os campos que serão utilizados para filtrar os registros.

> O atributo `ordering` é uma tupla que define a ordem de exibição default dos registros.

-   Acesse o `Admin` e veja as midificações:

    http://0.0.0.0:19003/api/admin/

-  Faça um _commit_ com a mensagem `Customização do Admin`.

# 16. Autenticação e autorização

**Introdução**

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

Podemos perceber uma relação as ações que compôem o CRUD, os termos utilizados no Admin e os verbos HTTP:

Aqui está a tabela com a terceira coluna movida para o lugar da quarta:

| Ação      | CRUD   | Admin  | HTTP        |
| --------- | ------ | ------ | ----------- |
| Criar     | Create | add    | POST        |
| Ler       | Read   | view   | GET         |
| Atualizar | Update | change | PUT (PATCH) |
| Deletar   | Delete | delete | DELETE      |


**Exercício:**

No `Admin`, crie os seguintes usuários e grupos e dê as permissões necessárias:

**a. Criando grupos e dando permissões**

Vamos começar criando 2 grupos e dando a eles permissões distintas:

-   Crie um grupo chamado `Administradores`, com as seguintes as permissões:
    -   Adicionar, editar, visualizar e remover: `autor`, `categoria`, `editora` e `livro`.
-   Crie um grupo chamado `Compradores`, com as seguintes permissões:
    -   Visualizar: `autor`, `categoria` e `editora`.
    -   Adicionar, editar e visualizar: `livro`.

**b. Criando usuários e adicionando aos grupos**

-   Crie um usuário `admin1@a.com` e o inclua no grupo `Administradores`.
-   Crie um usuário `comprador1@a.com` e o inclua no grupo `Compradores`.

# 17. Usando as permissões do DRF

**Autenticação e permissão**

_A **autenticação** ou **identificação** por si só geralmente não é suficiente para obter acesso à informação ou código. Para isso, a entidade que solicita o acesso deve ter **autorização**._ [(Permissões no DRF)](https://www.django-rest-framework.org/api-guide/permissions/)

**Autenticação** significa que um usuário foi **identificado** em um sistema, portanto ele é **conhecido**. Isso se dá, normamente por um sistema de **_login_**.

**Permissão (autorização)** se dá por um esquema de **conceder privilégios**, seja a usuários ou grupos.

Por padrão, qualquer usuário, mesmo sem autenticação, tem acesso irrestrito e permissão de fazer qualquer coisa em uma aplicação.

As permissões podem ser definidas:

1. a nível de objeto (nas `views` ou `viewsets`, por exemplo);
1. de forma global, no arquivo `settings.py`;
1. com o uso de classes de permissão do `Django REST Framework`.

Vamos analisar cada uma dessas formas.

**a. Exemplo de uso de permisssão na `viewset`**

Vamos ver um exemplo de uso de permissão em uma `viewset`. No exemplo, vamos permitir acesso apenas a usuários autenticados na model `Categoria`.

Como ilustração, modifique o arquivo `views/categoria.py`, da seguinte forma.

-   Importe a seguinte função:

```python
from rest_framework.permissions import IsAuthenticated
```

-   Inclua também a seguinte linha na `CategoriaViewSet`:

```python
permission_classes = [IsAuthenticated]
```

Para testar:

-   Encerre a sessão do **Admin**.
-   Tente acessar as **categorias** pelo DRF.
-   Você deve receber o seguinte erro: `"As credenciais de autenticação não foram fornecidas."`
-   Agora entre novamente pelo **Admin**.
-   Tente acessar as **categorias** pelo DRF.
-   Você deve conseguir acessar novamente.

> **Resumindo**, utilizamos a classe `IsAuthenticated` para permitir acesso apenas a usuários autenticados.

**b. Exemplo de uso de permisssão no `settings.py`**

Outra forma de gerenciamento de permissões é feita no arquivo `settings.py`.

> **IMPORTANTE:** Para utilizá-la, comente as últimas alterações feitas no arquivo `views.py`.

Uma forma de conseguir o mesmo resultado de forma padrão para todo o projeto, isto é, permitir acesso aos _endpoints_ **apenas para usuários autenticados**, é configurar desse modo o arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}
```

Para testar:

- Inclua o código acima e teste novamente o acesso aos _endpoints_ do DRF (categorias, editoras, etc.) com e sem uma sessão autenticada.

> **Resumindo**, utilizamos a classe `IsAuthenticated` no `settings.py` para permitir acesso apenas a usuários autenticados.

**c. Permissões com o `DjangoModelPermissions`**

Apesar de ser possível definir a autorização das formas que vimos anteriormente, adotaremos uma outra forma. Essa forma que iremos adotar para o gerenciamento de permissões será com o uso do [DjangoModelPermissions](https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions).

Esta classe de permissão está ligada às permissões do modelo `django.contrib.auth` padrão do Django. Essa permissão deve ser aplicada apenas a `views` que tenham uma propriedade `.queryset` ou método `get_queryset()` (exatamente o que temos).

A autorização só será concedida se o usuário estiver autenticado e tiver as permissões de modelo relevantes atribuídas, da seguinte forma:

-   As solicitações `POST` exigem que o usuário tenha a permissão de adição (`add`) no modelo.
-   As solicitações `PUT` e `PATCH` exigem que o usuário tenha a permissão de alteração (`change`) no modelo.
-   As solicitações `DELETE` exigem que o usuário tenha a permissão de exclusão (`remove`) no modelo.

Para isso, teremos que alterar a classe de autenticação, substituindo o que colocamos anteriormente, por isso:

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

# 18. Autenticação com o SimpleJWT

**Um resumo sobre autenticação e autorização**

Relembrando o que estudamos até aqui em termos de autenticação e autorização:

-   Como criar grupos e usuários e inserir os usuários nesses grupos
-   Como dar permissões nas models (via **Admin**) para visualização (`view`), adição (`add`), alteração (`change`) e exclusão (`remove`).
-   Como utilizar diversas formas de gerenciamento de permissões no Django, incluindo as permissões em cada `view` ou as permissões padrão no `settings.py`.
-   Como utilizar o `DjangoModelPermissions` para fazer uso do gerenciamento de permissões já incluído no **Django Admin**.

Agora, vamos utilizar o **SimpleJWT** para a autenticação no **Django REST Framework**.

> **Resumindo**, utilizaremos o `SimpleJWT` para **autenticação** e a _estrutura de permissões do Django_ para **autorização**.

**O SimpleJWT**

O [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) é um plug-in de autenticação JSON Web Token para o Django REST Framework.

**Ativando o SIMPLEJWT**

-   Adicione (ou descomente) o `SimpleJWT` no arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",), # essa linha!
    ...
}
```

-   Observe que já existem duas entradas referentes ao `SimpleJWT` no arquivo `urls.py`:

    - http://0.0.0.0:19003/token/
    - http://0.0.0.0:19003/token/refresh/


-   Feitas essa aterações, coloque o servidor do Django novamente em execução.

**Exercícios: Testando as permissões com o SimpleJWT**

Para testar se tudo deu certo, utilizaremos um cliente HTTP, como o **Thunder Client**.

**Colocando as informações do token na requisição**

**Dica:** se sua ferramenta permitir, crie várias requisições separadas e dê nomes, como _login_, _consulta_, _inclusão_, etc.

-   Ao tentar acessar um _endpoint_ com `GET`, como esse:

[GET] http://0.0.0.0:19003/api/categorias/

-   Você deverá receber uma resposta parecida com essa:

```json
{
    "detail": "As credenciais de autenticação não foram fornecidas."
}
```

Para fazer a autenticação, precisamos enviar as informações de `usuário` e `senha`.

-  Faremos isso enviando uma requisição do tipo `POST`, com as seguintes informações, no `Body` em `JSON`:

```json
{
    "email": "comprador1@a.com",
    "password": "teste.123"
}
```

-   O endereço para envio da requisição é o seguinte:

    [POST] http://0.0.0.0:19003/api/token/

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
[GET] ​http://0.0.0.0:19003/api/categorias/
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
[PUT] ​http://0.0.0.0:19003/api/categorias/10/
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

**Finalizando**

- Faça um _commit_ com a mensagem `Autenticação com o SimpleJWT`.

# 19. Inclusão da foto de perfil no usuário

Vamos aproveitar a aplicação `uploader` para incluir a foto de perfil no usuário.

**Criação do campo de foto de perfil**

-   No arquivo `models/user.py`, inclua o campo `foto`:

```python
...
from uploader.models import Image
...
class User(AbstractUser):
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
```

> O campo `foto` é uma chave estrangeira para a tabela `uploader_image`.

> A foto será opcional, por isso utilizamos `null=True` e `blank=True`.

> O campo `foto` será `null` por padrão, por isso utilizamos `default=None`.

> Se a foto for deletada, o campo `foto` será `null`, por isso utilizamos `on_delete=models.SET_NULL`.

-   Faça as migrações:

Seu projeto deve ficar assim:

![Projeto com a model Livro](diagramas/core_categoria_editora_autor_livro_com_capa_usuario_com_foto.png)

> Observe a ligação entre a model `Usuario` e a model `Image`, através da chave estrangeira `foto`.

**Inclusão da foto no `Admin`**

-   No arquivo `admin.py`, inclua o campo `foto`:

```python
...
class UserAdmin(UserAdmin):
    ...
        (_("Personal Info"), {"fields": ("name","foto")}), # inclua a foto aqui

    ...
```

- Teste a inclusão da foto de um usuário pelo `Admin`.

**Inclusão da foto no `Serializer`**

-   Modifique o serializador para o usuário, em `serializers/user.py`:

```python
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Usuario
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

> O atributo `write_only=True` indica que o campo `foto_attachment_key` é apenas para escrita. Isso significa que ele não será exibido na resposta da API.

> O atributo `read_only=True` indica que o campo `foto` é apenas para leitura. Isso significa que ele não será aceito na requisição da API.

**Testando**

-   Inclua uma foto de perfil em um usuário, através da API.

**Finalizando**

- Faça as alterações no sistema publicado.
- Faça um _commit_ com a mensagem `Inclusão da foto de perfil no usuário`.

# 20. Criação da entidade `Compra` integrada ao usuário do projeto

Nessa aula, vamos criar um entidade de compras integrada à entidade do usuário do projeto.

**Criando o `model` de compras**

-   Crie um novo arquivo `compra.py` dentro da pasta `models` do app `core`, digitando no terminal:

```shell
touch core/models/compra.py
```

-   Inclua o seguinte conteúdo no arquivo `compra.py` recém criado:

```python
from django.db import models

from .user import User

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)
```

> Note que estamos utilizando a model `User` como `ForeignKey` para o model `Compra`.

> `StatusCompra` é do tipo `IntegerChoices`, que é uma forma de criar um campo `choices` com valores inteiros.

> `status` é um campo `IntegerField` que utiliza o `choices` `StatusCompra.choices` e tem o valor padrão `StatusCompra.CARRINHO`.

- Inclua a nova model no arquivo `core/models/__init__.py`:

```python
from .compra import Compra
```

**Adicionando a model `Compra` ao `Admin`**

-   Adicione o model `Compra` ao `admin.py` do app `core`:

```python
...
from core.models import Compra

admin.site.register(Compra)
```

**Executando as migrações**

-   Execute as migrações.

O seu projeto deve ficar assim:

![Projeto com a model Compra](diagramas/core_compra1.png)

**Testando a model `Compra`**

-   Teste o model `Compra` no admin do Django.

**Finalizando**

- Faça um _commit_ com a mensagem `Criação da entidade Compra integrada ao usuário do projeto`.


# 21. Criando os itens da compra

No caso dos itens da compra, não vamos utilizar um campo `livro` do tipo `ManyToManyField` no model `Compra`, pois queremos ter a possibilidade de adicionar mais informações ao item da compra, como a `quantidade`, por exemplo. Desta forna, vamos criar "manualmente" a **tabela associativa**, que será chamada de `ItensCompra`.

-   Vamos adicionar um nova entidade `ItensCompra` ao arquivo `core/models/compra.py`:

```python
...
from .livro import Livro
...
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

O seu projeto deve ficar assim:

![Projeto com a model Compra](diagramas/core_compra_com_itens.png)

-   Verifique que a tabela `core_itenscompra` foi criada no banco de dados.
-   Inclua o model `ItensCompra` no `Admin` do Django.
-   Faça um _commit_ com a mensagem `Criação dos itens da compra`.


# 22. Uso de `TabularInline` no `Admin` para Itens da Compra

Da forma que configuramos o `Admin` para a model `ItensCompra`, não é possível adicionar itens da compra diretamente na tela de edição da compra. Isso é pouco natural, pois há uma relação direta entre a compra e seus itens.

Vamos mostrar os itens da compra no admin do Django, utilizando o `TabularInline`. Desta forma, podemos adicionar os itens da compra diretamente na tela de edição da compra.

-   No arquivo `admin.py` do app `core`, modifique o código das models `Compra` e `ItensCompra` da seguinte forma:

```python
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    extra = 1 # Quantidade de itens adicionais


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("usuario", "status")
    search_fields = ("usuario", "status")
    list_filter = ("usuario", "status")
    ordering = ("usuario", "status")
    list_per_page = 25
    inlines = [ItensCompraInline]
```

> Desta forma, quando você editar uma compra no admin do Django, você verá os itens da compra logo abaixo do formulário de edição da compra.

-   Teste no admin do Django.
-   Faça um _commit_ com a mensagem `Uso de TabularInline no Admin para Itens da Compra`.

# 23. Endpoint para a listagem básica de compras

Vamos começar a criar os endpoints para a entidade `Compra`, começando pela listagem básica de compras. Posteriormente, vamos incluir os itens da compra e criar os endpoints para adicionar, editar e excluir compras.


**Criação do serializer de Compra**

-   Crie um novo arquivo `compra.py` dentro da pasta `serializers` do app `core`:

```shell
touch core/serializers/compra.py
```

-   Inclua o seguinte conteúdo no arquivo `compra.py` recém criado:

```python
from rest_framework.serializers import ModelSerializer

from core.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
```

-   Inclua o novo `CompraSerializer` no arquivo `__init__.py` dos serializers:

```python
from .compra import CompraSerializer
```

**Criação da Viewset de Compra**

-   Crie um novo arquivo `compra.py` dentro da pasta `views` do app `core`:

```shell
touch core/views/compra.py
```

-   Inclua o seguinte conteúdo no arquivo `compra.py` recém criado:

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
```

-   Inclua o novo `CompraViewSet` no arquivo `__init__.py` das views:

```python
from .compra import CompraViewSet
```

**URL para listagem de compras**

-   Inclua o endpoint no arquivo `urls.py` do app `core`:

```python
...
from core.views import AutorViewSet, CategoriaViewSet, CompraViewSet, EditoraViewSet, LivroViewSet
...
router.register(r"compras", CompraViewSet)
...
```

-  Teste o endpoint no navegador.
-  Faça o _commit_ com a mensagem `Endpoint para a listagem básica de compras`.

**Inclusão do email do usuário na listagem da compra**

Nesse momento, a listagem de compras mostra apenas o `id` do usuário. Vamos substituir o `id` pelo `email` do usuário.

-   No serializer de `Compra`, inclua o seguinte código:

```python
...
from rest_framework.serializers import CharField, ModelSerializer
...
class CompraSerializer(ModelSerializer):
    usuario = CharField(source="user.email", read_only=True) # inclua essa linha
...
```

> O parâmetro `source` indica qual campo do model `Compra` será utilizado para preencher o campo `usuario` do serializer.

> O parâmetro `read_only` indica que o campo `usuario` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem `Inclusão do email do usuário na listagem da compra`.

**Inclusão do status da compra na listagem da compra**

De forma semelhante ao email do usuário, vamos incluir o status da compra na listagem da compra.

-   No serializer de `Compra`, inclua o seguinte código:

```python
...
class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True) # inclua essa linha
...
```

> O parâmetro `source` indica qual método do model `Compra` será utilizado para preencher o campo `status` do serializer. Sempre que utilizamos um campo do tipo `IntegerChoices`, podemos utilizar o método `get_<nome_do_campo>_display` para obter a descrição do campo.

> O parâmetro `read_only` indica que o campo `status` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem `Inclusão do status da compra na listagem da compra`.

> Estes são apenas dois exemplos de como podemos modificar a listagem de compras. Você pode incluir outros campos, como o total da compra, por exemplo.


# 24. Visualização dos itens da compra no endpoint da listagem de compras

De forma semelhante ao que fizemos no `Admin`, vamos incluir os itens da compra na listagem de compras.

-   Crie um serializer para `ItensCompra`, no arquivo `serializers/compra.py`:

```shell

```python
...
from core.models import Compra, ItensCompra
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
-   Faça o _commit_ com a mensagem `Visualização dos itens da compra na listagem da compra`.

**Mostrando os detalhes dos itens da compra na listagem de compras**

-   No serializer de `ItensCompra`, modifique o código:

```python
class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1
```

> O parâmetro `depth=1` indica que o serializer deve mostrar os detalhes do model `ItensCompra`. O valor `1` indica que o serializer deve mostrar os detalhes do model `ItensCompra` e dos models relacionados a ele (nesse caso, o livro). Se o valor fosse `2`, o serializer mostraria os detalhes do model `ItensCompra`, dos models relacionados a ele e dos models relacionados aos models relacionados a ele (nesse caso, a categoria, a editora e o autor).

- Experimente alterar o valor de `depth` e veja o resultado no navegador.

**Mostrando apenas os campos necessários dos itens da compra na listagem de compras**

Você deve ter percebido que o serializer de `ItensCompra` está mostrando todos os seus campos, incluindo o campo `compra`. Vamos modificar o serializer para mostrar apenas os campos necessários. Nesse exemplo, vamos mostrar apenas os campos`livro` e `quantidade`.

-   No `ItensCompraSerializer`, modifique a linha `fields`:

```python
fields = ("livro", "quantidade")
```

> O parâmetro `fields` indica quais campos do model `ItensCompra` serão mostrados no serializer. Se o valor for `__all__`, todos os campos serão mostrados. Se o valor for uma sequência de campos, apenas esses campos serão mostrados.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem `Limitando os campos dos itens da compra na listagem de compras`.

**Mostrando o total do item na listagem de compras**

O total do item é calculado pelo preço do livro multiplicado pela quantidade. Esse é um campo calculado, que não existe no model `ItensCompra`. Vamos incluir esse campo na listagem de compras.

- Primeiro, importe o `SerializerMethodField` no arquivo `serializers/compra.py`:

```python
from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField
```

- Depois, modifique o `ItensCompraSerializer`, para que fique desse jeito:

```python
class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 1
```

> O parâmetro `SerializerMethodField` indica que o campo `total` não existe no model `ItensCompra`. Ele será calculado pelo método `get_total`.

> O método `get_total` recebe como parâmetro o objeto `instance`, que representa o item da compra. A partir dele, podemos acessar os campos do item da compra, como `quantidade` e `livro.preco`.

> O método `get_total` retorna o valor do campo `total`, que é calculado pelo preço do livro multiplicado pela quantidade.

> O método `get_<nome_do_campo>` é um método especial do serializer que é chamado para calcular o valor do campo `<nome_do_campo>`.

> Incluimos o campo `total` no `fields` do serializer.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem `Mostrando o total do item na listagem de compras`.

# 25. Inclusão do total da compra na listagem de compras

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
> No código acima, temos duas formas de calcular o total da compra. A primeira forma está comentada. A segunda forma está descomentada. A segunda forma é mais simples e mais eficiente, e utiliza uma compreensão de lista (_list comprehension_).

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
- Faça o _commit_ com a mensagem `Inclusão do total da compra na listagem de compras`.

# 26. Criação de um endpoint para criar novas compras

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

**Criando um serializer para os itens da compra**

Tendo definido o formato dos dados, vamos criar um novo `serializer`, que será usado para criar uma nova compra ou editar uma compra já existente.

- No arquivo `serializer/compra.py` , inclua o seguinte `serializer` no final do arquivo:

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

- Inclua também o `serializer` no arquivo `__init__.py` dos `serializers`:

```python
from .compra import CompraSerializer, CriarEditarCompraSerializer, ItensCompraSerializer
```

**Alterando o `viewset` de `Compra` para usar o novo `serializer`**

Vamos alterar o `viewset` de `Compra` para usar o novo `serializer`, nas operações de criação e edição.

- No arquivo `views/compra.py` altere o `viewset` de `Compra` para usar o novo `serializer`:

```python
...
from core.serializers import CompraSerializer, CriarEditarCompraSerializer
...
class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update"):
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
Write an explicit `.create()` method for serializer `core.serializers.compra.CriarEditarCompraSerializer`, or set `read_only=True` on nested serializer fields.
```

Traduzindo, chegamos no seguinte:

```
Erro de afirmação em /api/compras/
O método `.create()` não suporta campos aninhados graváveis por padrão.
Escreva um método `.create()` explícito para o serializer `core.serializers.compra.CriarEditarCompraSerializer`, ou defina `read_only=True` nos campos do serializer aninhado.
```

O erro ocorre por que os itens da compra vêm de outra tabela, a tabela `ItemCompra`, através de uma chave estangeira. O serializer de `Compra` não sabe como criar os itens da compra. Precisamos alterar o método `create` do `serializer` de `Compra` para criar os itens da compra.

**Alterando o método `create` do `serializer` de `Compra`**

- No arquivo `serializers/compra.py` , altere o `serializer` de `Compra` para suportar campos aninhados:

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

- Precisamos criar também o novo `serializer` `CriarEditarItensCompraSerializer` para os itens da compra. No `serializers/compra.py`, inclua o seguinte código, após o `ItensCompraSerializer`:

```python
...
class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")
...
```

> O `serializer` de `ItensCompra` é bem simples, pois ele recebe apenas o livro e a quantidade.

- Teste o endpoint no `ThunderClient.
- Faça o _commit_ com a mensagem `Criação de um endpoint para criar novas compras`.

# 27. Criação de um endpoint para atualizar compras

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
Write an explicit `.update()` method for serializer `core.serializers.compra.CriarEditarCompraSerializer`, or set `read_only=True` on nested serializer fields.
```

Traduzindo, chegamos no seguinte:

```
Erro de afirmação em /api/compras/1/
O método `.update()` não suporta campos aninhados graváveis por padrão.
Escreva um método `.update()` explícito para o serializer `core.serializers.compra.CriarEditarCompraSerializer`, ou defina `read_only=True` nos campos do serializer aninhado.
```

> O erro ocorre por que os itens da compra vêm de outra tabela, a tabela `ItensCompra`, através de uma chave estangeira. O serializer de `Compra` não sabe como atualizar os itens da compra. Precisamos alterar o método `update` do `serializer` de `Compra` para atualizar os itens da compra.

- No arquivo `serializers/compra.py`, redefina o método `update` do `serializer` de `CriarEditarCompraSerializer`:

```python
...
    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
        instance.save()
        return super().update(instance, validated_data)
...
```

> O método `update` é chamado quando uma compra é atualizada. Ele recebe os dados validados e atualiza a compra e os itens da compra.

> O método `update` recebe dois parâmetros: `instance` e `validated_data`. O `instance` é a compra que está sendo atualizada. O `validated_data` são os dados validados que estão sendo atualizados.

> O método `update` remove todos os itens da compra (se houverem) e cria novos itens com os dados validados.

> O método `update` salva a compra e retornamos a instância.

> O comando `super().update(instance, validated_data)` chama o método `update` da classe pai, que é o método padrão de atualização.

- Teste o endpoint no `ThunderClient`:
  - use o método `PUT`, para atualizar a compra de forma completa;
  - use o método `PATCH`, para atualizar a compra de forma parcial.
    - Experimente mudar apenas o usuário;
    - Experimente mudar apenas a quantidade de um item da compra;
    - Experimente mudar o livro de um item da compra;
- Faça o _commit_ com a mensagem `Criação de um endpoint para atualizar compras`.

# 28. Criação de uma compra a partir do usuário autenticado

Ao invés de passar o usuário no corpo da requisição, podemos pegar o usuário autenticado e criar a compra a partir dele. O `Django Rest Framework` nos dá uma forma de fazer isso.

- Primeiro, vamos importar todos os tipos de campos necessários no arquivo `serializers/compra.py`:

```python
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault, # novo
    HiddenField, # novo
    ModelSerializer,
    SerializerMethodField,
)
```

- Agora, vamos definir o usuário como um campo oculto, cujo valor padrão é o usuário autenticado, na criação ou edição de uma compra.

```python
class CriarEditarCompraSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
...
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

- Faça o _commit_ com a mensagem `Criação de uma compra a partir do usuário autenticado`.

# DAQUI PRA FRENTE O TUTORIAL NÃO ESTÁ REVISADO, PODENDO CONTER ERROS E INCONSISTÊNCIAS

# 29. Filtrando apenas as compras do usuário autenticado

Nesse momento, qualquer usuário pode ver todas as compras. Vamos filtrar da seguinte forma: se o usuário for um usuário normal, ele só pode ver as suas compras. Se o usuário for um administrador, ele pode ver todas as compras.

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

> O método `get_queryset` é chamado quando uma compra é listada.

> O `request` é o objeto que representa a requisição. O `request.user` é o usuário autenticado.

> Se o usuário for um superusuário ou for membro do grupo "*Administradores*", retorna todas as compras. Caso contrário, retorna apenas as compras do usuário autenticado.

- Para testar, autentique-se com um usuário normal e depois com um que seja administrador. Você verá que o administrador consegue ver todas as compras, enquanto o usuário normal só consegue ver as suas compras.
- Faça o _commit_ com a mensagem `Filtrando apenas as compras do usuário autenticado`.

# 30. Validando a quantidade de itens em estoque

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
- Faça o _commit_ com a mensagem `Validando a quantidade de itens em estoque`.



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

# 31. Finalizando a compra e atualizando a quantidade de itens em estoque

Nesse momento, a compra é criada com o status `CARRINHO`. Vamos criar um endpoint para finalizar a compra, alterando o status da compra para `REALIZADO`. No momento que a compra é finalizada, a quantidade de itens em estoque deve ser atualizada, isto é, a quantidade de itens em estoque deve ser reduzida pela quantidade de itens comprados.

- No `models/compra.py`, vamos criar um método `finalizar` na model `Compra`:

```python
from django.db import transaction

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
...
class Compra(models.Model):
...
    @action(detail=True, methods=["post"])
    def finalizar(self, request, pk=None):
        compra = self.get_object()
        if compra.status != Compra.StatusCompra.CARRINHO:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"status": "Compra já finalizada"},
            )
        with transaction.atomic():
            for item in compra.itens.all():
                if item.quantidade > item.livro.quantidade:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            "status": "Quantidade insuficiente",
                            "livro": item.livro.titulo,
                        },
                    )
                item.livro.quantidade -= item.quantidade
                item.livro.save()
            compra.status = Compra.StatusCompra.REALIZADO
            compra.save()
        return Response(status=status.HTTP_200_OK, data={"status": "Compra finalizada"})

```

> O decorador `@action` cria um endpoint para a ação `finalizar`, no formato `compras/api/<id>/finalizar/`.

> O método `finalizar` é um método de ação que finaliza a compra. Ele recebe a compra que está sendo finalizada.

> Se a compra já foi finalizada, retorna um erro.

> Se a quantidade de itens em estoque for menor do que a quantidade de itens comprados, retorna um erro.

> Se a quantidade de itens em estoque for maior ou igual à quantidade de itens comprados, atualiza a quantidade de itens em estoque e finaliza a compra.

> O comando `with transaction.atomic()` garante que todas as operações dentro do bloco `with` sejam executadas ou nenhuma seja executada.

> O método `save` é chamado para salvar a compra e o livro.

> O método `Response` retorna uma resposta HTTP.

> O status `HTTP_200_OK` indica que a requisição foi bem sucedida.

> O status `HTTP_400_BAD_REQUEST` indica que a requisição não foi bem sucedida.

- Para testar:
  - Tente finalizar uma compra que não foi finalizada.
  - Tente finalizar uma compra que já foi finalizada.
  - Tente finalizar uma compra com quantidade de itens maior do que a quantidade em estoque.
  - Tente finalizar uma compra com quantidade de itens menor ou igual à quantidade em estoque.

- Faça o _commit_ com a mensagem `Finalizando a compra e atualizando a quantidade de itens em estoque`.





---

# Exercícios Garagem

O projeto Garagem é um projeto de uma garagem de carros. O objetivo é praticar aquilo que foi visto nesse tutorial, no projeto core.

## E1. Crie o projeto Garagem

Seguindo aquilo que você já aprendeu na criação do projeto da `Livraria`, crie um **novo projeto**, a partir do template.

1. O projeto será chamado `Garagem`.
2. Nomeie o _commit_ como sendo `Criação do projeto`.
3. Crie as seguintes APIs, **fazendo um _commit_ para cada uma**:
    -   `Acessório`:
        -   `descricao` (string, máximo 100 caracteres).
        -   `__str__` (retorna a descrição e o id).
    -   `Categoria`:
        -   `descricao` (string, máximo 100 caracteres).
        -   `__str__` (retorna a descrição e o id.
    -   `Cor`:
        -   `nome` (string, máximo 100 caracteres).
        -   `__str__` (retorna o nome e o id).
    -   `Marca`:
        -   `nome` (string, máximo 50 caracteres).
        -   `nacionalidade` (string, máximo 50 caracteres, permite nulo).
        -   `__str__` (retorna o nome **em caixa alta** e o id).
4. Crie a aplicação frontend com Vuejs para consumir a API REST do projeto `Garagem`. Pode utilizar o template do projeto da `livraria-vue3` como base.

## E2. Crie o modelo `Modelo`

Vamos incluir o modelo `Modelo` no projeto `Garagem`.

- Crie o modelo `Modelo`, com os seguintes atributos:
  -   `nome` (string, máximo 100 caracteres).
  -   `marca` (chave estrangeira para `Marca`).
  -   `categoria` (chave estrangeira para `Categoria`).
  -   `__str__` (retorna o nome do modelo e a marca).
-   Crie a API REST para o modelo `Modelo`.
-   Crie a aplicação frontend com Vuejs para consumir a API REST do modelo `Modelo`.
-   Faça um _commit_ para cada etapa.

## E3. Crie o modelo `Veiculo`

Vamos incluir o modelo `Veiculo` no projeto `Garagem`.

- Crie o modelo `Veiculo`, com os seguintes atributos:
  -   `modelo` (chave estrangeira para `Modelo`).
  -   `cor` (chave estrangeira para `Cor`).
  -   `ano` (inteiro, permite nulo, default 0).
  -   `preco` (decimal, máximo 10 dígitos, 2 casas decimais, permite nulo, default 0).
  -   `acessorios` (chave estrangeira para `Acessorio`, muitos para muitos).
  -   `__str__` (retorna o modelo, ano e cor do carro).
-  Crie a API REST para o modelo `Veiculo`.
-  Crie a aplicação frontend com Vuejs para consumir a API REST do modelo `Veiculo`.
-  Faça um _commit_ para cada etapa.

---

# Apêndices

# A1. Instalação e atualização do VS Code

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

# A2. Instalação e sincronização de extensões do VS Code

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
-   [Vue Language Features (Desenvolvimento de aplicações Vue.js)](https://marketplace.visualstudio.com/items?itemName=octref.vetur)

**Extensão Vue.js devtools no Google Chrome**

-   [Vue.js devtools](https://chrome.google.com/webstore/detail/nhdogjmejiglipccpnnnanhbledajbpd)


## Sinconização de extensões no VS Code

Você pode configurar a sincronização das extensões entre os computadores. Para isso:

-   Faça login com a conta do **GitHub** ou da **Microsoft** no VS Code.
-   Clique no ícone de engrenagem no canto inferior esquerdo da tela do VS Code e clique em `Ativar a Sincronização de Configurações`.

# A3. Instalação e configuração do PDM

**Instalação do PDM no Linux**

As instruções a seguir são para o **Linux Manjaro e Ubuntu**. Se você estiver usando outra distribuição ou quiser mais informações, consulte a documentação do [PDM](https://pdm.fming.dev/latest/).

-   Abra um terminal:

    `Ctrl + Alt + T`

-   Verifique se o **PDM** está instalado:

```shell
pdm -V
```

-   Se não estiver instalado, instale a versão mais recente:

```shell
curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
```

- Após a instalação, feche o terminal (`Ctrl + D`) e abra um novo terminal (`Ctrl + Alt + T`).

> **IMPORTANTE**: Após a instalação do PDM, você precisa rodar o script de configuração, conforme descrito abaixo.

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

**Instalação do PDM no Windows**

Execute o comando abaixo no **PowerShell** (pode ser no Terminal do `VS Code`):

```shell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py -UseBasicParsing).Content | python -
```

Verifique se o **PDM** está configurado para não usar virtualenv:

```shell
pdm config
```

> **IMPORTANTE:** Se você não fizer essa configuração, o **PDM** irá criar uma pasta `.venv` no diretório do projeto. Para resolver isso, você deve apagar a pasta `.venv` e executar o comando `pdm config python.use_venv false` e então executar o comando `pdm install`.

**Se precisar instalar o Python:**

    sudo apt install python-is-python3 python3.10-venv

[Voltar para a preparação do ambiente](#1-preparação-do-ambiente)


# A4. Criação do Banco de Dados no Supabase

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
  - Ela deve ser parecida com isso: `postgres://postgres:[YOUR-PASSWORD]@site.supabase.co:5432/postgres`.
- Coloque as informações da sua conta.
- Copie a linha de conexão e cole no arquivo `.env` do projeto, como no exemplo:

```shell
# Supabase
DATABASE_URL=postgres://postgres:teste.123@!@db.vqcprcexhnwvyvewgrin.supabase.co:5432/postgres
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

# A5. Publicando o projeto no `Render`

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

# A6. Armazenando arquivos estáticos no Cloudinary

Vamos utilizar o Cloudinary para armazenar os arquivos estáticos, como as imagens dos livros. Detsa forma, os arquivos não serão perdidos a cada nova implantação.

**Criando uma conta no Cloudinary**

- Acesse o site do [Cloudinary](https://cloudinary.com/) e crie uma conta.

**Configurando o Cloudinary**

-   Edite o arquivo `.env`, incluindo a seguinte variável:

```shell
# Cloudinary
CLOUDINARY_URL=cloudinary://your_api_key:your_api_secret@your_cloud_name
```

> Altere as informações de acordo com o seu projeto, acessando o [Cloudinary Console](https://cloudinary.com/console) na opção `Dashboard`.

- Inclua essa mesma variável no `Render` (ou no serviço de hospedagem que você estiver utilizando), na opção `Environment variables`.

**Testando**

- Coloque a variável `MODE` com o valor `MIGRATE` no arquivo `.env`.
-  Faça o upload de uma imagem pelo `Admin` do `Django` e verifique se ela foi salva no `Cloudinary`, na opção `Media Explorer`.
-  Se deu certo, faça o *_commit_* das alterações.
-  Sua aplicação deve estar funcionando normalmente, utilizando o `Cloudinary` para armazenar os arquivos estáticos.


# A7. Resolução de erros

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
- Por fim, execute o `pdm run dev` novamente.


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

## Aumentando o tempo de vida do token de autenticação JWT

-   Adicione as seguintes linhas ao arquivo `settings.py`:

```shell
from datetime import timedelta
...
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=180),
    "REFRESH_TOKEN_LIFETIME":timedelta(days=1),
}
```

# A8. Configurando o git

**Um aviso importante**

Antes de mais nada, seguem **3 regras** a serem consideradas ao seguir as instruções:

-   **Antes de clicar ou responder, leia atentamente as instruções.**
-   **Leia atentamente as instruções antes de clicar ou responder.**
-   **Nunca clique ou responda sem antes ler atentamente as instruções.**

As 3 regras falam a mesma coisa? Sim, você entendeu o recado. ;-)

**Configurando o projeto git**

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

**Configurando as variáveis do git**

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


# A9. Usando curl para testar a API via linha de comando

-   Liste todas as categorias:

```shell
curl -X GET http://0.0.0.0:19003/api/categorias/
```

-   Liste uma categoria específica:

```shell
curl -X GET http://0.0.0.0:19003/api/categorias/1/
```

-   Crie uma nova categoria:

```shell
curl -X POST http://0.0.0.0:19003/api/categorias/ -d "descricao=Teste"
```

-   Atualize uma categoria:

```shell
curl -X PUT http://0.0.0.0:19003/api/categorias/1/ -d "descricao=Teste 2"
```

-   Delete uma categoria:

```shell
curl -X DELETE http://0.0.0.0:19003/api/categorias/1/
```
-----

# Contribua

**Para contriburi com esse projeto:**

-   Criar um _fork_ do projeto.
-   Clonar o _fork_
-   Criar um _branch_ para a sua contribuição.
-   Fazer as alterações no seu _branch_.
-   Enviar um _pull request_ para o projeto original.

---

Marco André Mendes \<marcoandre@gmail.com>

