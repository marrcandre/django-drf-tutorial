**DJANGO COM DRF (2025)**

Tutorial para desenvolvimento de APIs REST usando o [Django](https://www.djangoproject.com/) com [DRF](https://www.django-rest-framework.org/) (Django Rest Framework). Esse tutorial foi construído a partir do curso em vídeo [Django com DRF](https://www.youtube.com/playlist?list=PL6u1VNwqZdJZT5lCMbBQA1UHVWy0FOYOl) do [Eduardo da Silva](https://github.com/eduardo-da-silva).

Existe uma versão completa e funcional do projeto da livraria, que pode ser acessada neste  [repositório do GitHub](https://github.com/marrcandre/livraria_marrcandre_2024) e está publicada no [render](https://livraria-marrcandre-2024.onrender.com/api/).

Este tutorial está em constante desenvolvimento. Envie sugestões e correções para meu [e-mail](mailto:marcoandre@gmail.com). Se preferir, faça uma [solicitação de contribuição ao projeto](#contribua).

---

**TABELA DE CONTEÚDO**

- [1. Preparação do ambiente](#1-preparação-do-ambiente)
- [2. Criação do projeto](#2-criação-do-projeto)
- [3. Criação de uma aplicação](#3-criação-de-uma-aplicação)
- [4. Criação de uma API REST](#4-criação-de-uma-api-rest)
- [5. Conectando a API ao frontend com Vue 3](#5-conectando-a-api-ao-frontend-com-vue-3)
- [6. Inclusão da Editora no projeto Livraria](#6-inclusão-da-editora-no-projeto-livraria)
- [7. Criação da API para Autor](#7-criação-da-api-para-autor)
- [8. Criação da API para Livro](#8-criação-da-api-para-livro)
- [9. Inclusão das chaves estrangeiras no modelo Livro](#9-inclusão-das-chaves-estrangeiras-no-modelo-livro)
- [10. Inclusão do relacionamento n para n no modelo do Livro](#10-inclusão-do-relacionamento-n-para-n-no-modelo-do-livro)
- [11. Modificação da API para Livro](#11-modificação-da-api-para-livro)
- [12. Upload e associação de imagens](#12-upload-e-associação-de-imagens)
- [13. Dump e Load de dados](#13-dump-e-load-de-dados)
- [14. Customização do Admin](#14-customização-do-admin)
- [15. Uso do Django Shell e do Django Shell Plus](#15-uso-do-django-shell-e-do-django-shell-plus)
- [16. Autenticação e autorização](#16-autenticação-e-autorização)
- [17. Utilização das permissões do DRF](#17-utilização-das-permissões-do-drf)
- [18. Autenticação com o SimpleJWT](#18-autenticação-com-o-simplejwt)
- [19. Inclusão da foto de perfil no usuário](#19-inclusão-da-foto-de-perfil-no-usuário)
- [20. Criação da entidade Compra integrada ao usuário do projeto](#20-criação-da-entidade-compra-integrada-ao-usuário-do-projeto)
- [21. Criação dos itens da compra](#21-criação-dos-itens-da-compra)
- [22. Uso de TabularInline no Admin para Itens da Compra](#22-uso-de-tabularinline-no-admin-para-itens-da-compra)
- [23. Endpoint para a listagem básica de compras](#23-endpoint-para-a-listagem-básica-de-compras)
- [24. Visualização dos itens da compra no endpoint da listagem de compras](#24-visualização-dos-itens-da-compra-no-endpoint-da-listagem-de-compras)
- [25. Exibição do total do item na listagem de compras](#25-exibição-do-total-do-item-na-listagem-de-compras)
- [26. Inclusão do total da compra na listagem de compras](#26-inclusão-do-total-da-compra-na-listagem-de-compras)
- [27. Criação de compras com itens aninhados via API](#27-criação-de-compras-com-itens-aninhados-via-api)
- [28. Atualização de compras e seus itens via API](#28-atualização-de-compras-e-seus-itens-via-api)
- [28b. Criação de um serializador específico para a listagem de compras](#28b-criação-de-um-serializador-específico-para-a-listagem-de-compras)
- [29. Criação de uma compra a partir do usuário autenticado](#29-criação-de-uma-compra-a-partir-do-usuário-autenticado)
- [30. Visualização de compras com base no perfil do usuário](#30-visualização-de-compras-com-base-no-perfil-do-usuário)
- [31. Validação dos campos no Serializer](#31-validação-dos-campos-no-serializer)
- [32. Gravação do preço do livro no item da compra](#32-gravação-do-preço-do-livro-no-item-da-compra)
- [33. Registro da data da compra](#33-registro-da-data-da-compra)
- [34. Inclusão do tipo de pagamento à entidade de Compra](#34-inclusão-do-tipo-de-pagamento-à-entidade-de-compra)
- [35a. Ações personalizadas: Introdução e alteração do preço de um livro](#35a-ações-personalizadas-introdução-e-alteração-do-preço-de-um-livro)
- [35b. Ações personalizadas em coleções e relatório de vendas do mês](#35b-ações-personalizadas-em-coleções-e-relatório-de-vendas-do-mês)
- [35c.  Ações personalizadas: finalizando a compra e atualizando o estoque](#35c--ações-personalizadas-finalizando-a-compra-e-atualizando-o-estoque)
- [35d.  Ações personalizadas: listando livros com mais de 10 cópias vendidas](#35d--ações-personalizadas-listando-livros-com-mais-de-10-cópias-vendidas)
- [35e. Ações personalizadas: ajustando o estoque de um livro](#35e-ações-personalizadas-ajustando-o-estoque-de-um-livro)
- [36. Utilização de filtros para listagem de recursos](#36-utilização-de-filtros-para-listagem-de-recursos)
- [37. Utilização de busca textual em campos de texto](#37-utilização-de-busca-textual-em-campos-de-texto)
- [38. Utilização de ordenação dos resultados](#38-utilização-de-ordenação-dos-resultados)
- [39. Inclusão do limite de um carrinho de compras por usuário](#39-inclusão-do-limite-de-um-carrinho-de-compras-por-usuário)
- [Exercícios Garagem](#exercícios-garagem)
- [Apêndices](#apêndices)
- [A1. Instalação e atualização do VS Code](#a1-instalação-e-atualização-do-vs-code)
- [A2. Instalação e sincronização de extensões do VS Code](#a2-instalação-e-sincronização-de-extensões-do-vs-code)
- [A3. Instalação e configuração do PDM](#a3-instalação-e-configuração-do-pdm)
- [A4. Publicação do banco de dados no Supabase](#a4-publicação-do-banco-de-dados-no-supabase)
- [A5. Publicação do projeto no Render](#a5-publicação-do-projeto-no-render)
- [A6. Publicação: armazenamento de arquivos estáticos no Cloudinary](#a6-publicação-armazenamento-de-arquivos-estáticos-no-cloudinary)
- [A7. Resolução de erros](#a7-resolução-de-erros)
- [A8. Configuração do git](#a8-configuração-do-git)
- [A9. Uso do curl para testar a API via linha de comando](#a9-uso-do-curl-para-testar-a-api-via-linha-de-comando)
- [A10. Django Shell - Comandos úteis](#a10-django-shell---comandos-úteis)
- [A11. DBShell - Comandos úteis](#a11-dbshell---comandos-úteis)
- [A12 - Aplicando os 12 Fatores de uma Aplicação ao Nosso Projeto Django + Vue.js](#a12---aplicando-os-12-fatores-de-uma-aplicação-ao-nosso-projeto-django--vuejs)
- [A13 - Rodando o Django com HTTPS no ambiente de desenvolvimento](#a13---rodando-o-django-com-https-no-ambiente-de-desenvolvimento)
- [Contribua](#contribua)


---

**Trilha do Curso**

Esse curso é parte de uma trilha de aprendizado. Siga os links abaixo para acessar os outros cursos da trilha:

- [**Programação I**](https://github.com/ldmfabio/Programacao) ([Prof. Fábio Longo de Moura](https://github.com/ldmfabio)): Lógica de Programação com JavaScript.
- [**Desenvolvimento Web II**](https://eduardo-da-silva.github.io/aula-desenvolvimento-web/) ([Prof. Eduardo da Silva](https://github.com/eduardo-da-silva)): Desenvolvimento front-end com VueJS.
- [**Desenvolvimento Dispositivos Móveis III**](https://eduardo-da-silva.github.io/aula-desenvolvimento-mobile/) ([Prof. Eduardo da Silva](https://github.com/eduardo-da-silva)): Desenvolvimento para dispositivos móveis com Vue + Vite + PWA.
- [**Desenvolvimento Web III - Atual**](https://github.com/marrcandre/django-drf-tutorial) ([Prof. Marco André Lopes Mendes](https://github.com/marrcandre/)): Desenvolvimento back-end com Django e DRF, utilizando o [modelo de projeto](https://github.com/marrcandre/template_django_pdm).
- [**Desenvolvimento Web III (2023)**](https://github.com/marrcandre/django-drf-tutorial) ([Prof. Marco André Lopes Mendes](https://github.com/marrcandre/)): Desenvolvimento back-end com Django e DRF, do zero, sem utilizar o template.

Bons estudos!

---

# 1. Preparação do ambiente

A preparação do ambiente será feita apenas uma vez em cada computador. Ela consiste em instalar e configurar o **VS Code**, o **PDM** e o **Python**.

- [Instale ou atualize o VS Code](#a1-instalação-e-atualização-do-vs-code)
- [Instale e sincronize as extensões do VS Code.](#a2-instalação-e-sincronização-de-extensões-do-vs-code)
- [Instale e configure o PDM](#a3-instalação-e-configuração-do-pdm)

---

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

**Usando o VS Code**
    - Abra o **VS Code**.
    - Clique no ícone de **Source Control** na barra lateral esquerda.
        - Clique no botão `Clone Repository`.
        - Você também pode teclar `Control+Shift+P` e digitar `Clone Repository`.
    - Digite a URL do repositório do projeto (ou procure na lista de repositórios disponíveis).
    - Escolha a pasta onde o projeto será clonado.
    - Clique no botão `Clone`.

**Usando o terminal**
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

        http://127.0.0.1:8000/admin

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

---

# 3. Criação de uma aplicação

**3.1 Compreendendo uma aplicação**

Uma aplicação no **Django** é um conjunto de arquivos e pastas que contém o código de uma funcionalidade específica do seu site.

Uma aplicação pode ser criada dentro de um projeto ou importada de outro projeto.

Em nosso projeto, temos uma aplicação criada, chamada `core`, conforme a imagem abaixo:

![App core](imagens/core_app.png)

> Todas as aplicações precisam ser adicionadas ao arquivo `settings.py` do projeto, na seção `INSTALLED_APPS`.

Dentro da pasta `core` temos alguns arquivos e pastas, mas os mais importantes são:

-   `migrations`: é a pasta de migrações de banco de dados da aplicação.
-   `models`: é a pasta onde ficam as `models` (modelos de banco de dados, ou tabelas) da aplicação.
-   `serializers`: é a pasta onde ficam os serializadores (serializadores) da aplicação.
-   `views`: é a pasta onde ficam as views (visões) da aplicação.
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

A tabela ainda não apareceu, certo? Isso acontece porque ainda não incluímos a `model` no `Admin`.

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
-   Você perceberá que a descrição das informações que você inclui está meio estranha, algo como `Categoria object (1)` e assim por diante.
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
-  Faça um _commit_ com a mensagem:

```
feat: criação da model de Categoria
```

**IMPORTANTE: Escrevendo uma boa mensagem de _commit_**

-   Escreva uma mensagem de _commit_ que descreva o que foi feito.
-   Dessa forma fica mais fácil identificar as mudanças sem precisar ver o código.
-   Não escreva mensagens como `Alteração 1`, `Alteração 2`, `Alteração 3`, etc.
- Utilize **prefixos**:
    - feat: Para novas funcionalidades.
    - fix: Para correções de bugs.
    - chore: Para tarefas de manutenção ou mudanças que não afetam o código de produção.
    - docs: Para alterações na documentação.
    - style: Para mudanças de formatação ou estilo de código (sem alterar lógica).
    - refactor: Para refatoração de código sem adicionar funcionalidades ou corrigir bugs.
    - test: Para adição ou modificação de testes.
- Exempos de _commits_:
    - feat: Criação da model de Categoria
    - fix: Correção do método __str__ da model Categoria
    - chore: Atualização do README.md
    - docs: Adição de comentários no código
    - style: Alteração de formatação do código
    - refactor: Refatoração do código da model Categoria
    - test: Adição de testes para a model Categoria

---

# 4. Criação de uma API REST

No ano passado, vocês consumiram uma API (como a do TMDB) usando `GET` com `axios` no JavaScript e no Vue.

Agora vamos fazer o contrário.

Em vez de consumir uma API, vamos **criar a nossa própria API** para o projeto `livraria`.

Ao final desta aula, você terá uma API completa para `Categoria`, capaz de:

- Criar registros
- Listar todos
- Buscar um específico
- Atualizar
- Deletar

Ou seja: você estará construindo o backend que antes apenas utilizava.

---

**Antes de começar: o que é uma API REST?**

Uma **API** é uma forma de comunicação entre sistemas.

Por exemplo:
- Um front-end em Vue
- Um aplicativo mobile
- Outro sistema qualquer

Todos eles podem conversar com o nosso backend através de requisições HTTP.

**E o que significa REST?**

REST é um jeito organizado de construir APIs:

- Cada tipo de dado é um **recurso**
- Cada recurso tem uma **URL**
- Usamos métodos HTTP como `GET`, `POST`, `PUT`, `PATCH` e `DELETE`

No nosso caso:

- `Categoria` é um recurso
- `/categorias/` será a URL que representa esse recurso

---

**Como uma API funciona no Django Rest Framework?**

A estrutura básica é esta:

```
Model → Serializer → ViewSet → Router → URL
```

- O **Model** representa os dados no banco.
- O **Serializer** transforma dados em JSON (e JSON em dados).
- O **ViewSet** implementa as ações da API.
- O **Router** cria as rotas automaticamente.
- A **URL** é o endereço que acessamos no navegador.

Vamos montar isso passo a passo.

---

**4.1 DRF já está instalado**

O Django Rest Framework (DRF) já está instalado no projeto:

- Está listado no `pyproject.toml`
- Está no `requirements.txt`
- Já está configurado no `INSTALLED_APPS`

Isso foi feito no template inicial do projeto.

Se fosse um projeto do zero, precisaríamos instalar e configurar manualmente.

---

**4.2 Criando o Serializer**

Lembra que quando você consumia a API do TMDB, recebia um JSON?

Alguém precisou transformar os dados do banco em JSON.

É exatamente isso que o **Serializer** faz.

Ele converte:

- Model → JSON
- JSON → Model

**Criando o arquivo**

Crie o arquivo:

```
core/serializers/categoria.py
```

E adicione:

```python
from rest_framework.serializers import ModelSerializer

from core.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
```

**O que está acontecendo aqui?**

- `model = Categoria` → estamos dizendo qual model será usado.
- `fields = '__all__'` → todos os campos serão enviados na API.

⚠️ Em projetos reais, muitas vezes escolhemos os campos manualmente, para ter mais controle.

**Não esqueça do __init__.py**

No arquivo:

```
core/serializers/__init__.py
```

Adicione:

```python
from .categoria import CategoriaSerializer
```

---

**4.3 Criando a View**

Agora precisamos dizer como a API vai se comportar.

Crie o arquivo:

```
core/views/categoria.py
```

E adicione:

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
```

**O que é ModelViewSet?**

Aqui está a parte interessante.

O `ModelViewSet` já cria automaticamente:

- `list()` → listar todos
- `retrieve()` → buscar um
- `create()` → criar
- `update()` → atualizar totalmente
- `partial_update()` → atualizar parcialmente
- `destroy()` → remover

Ou seja, não precisamos escrever essas funções manualmente.

Isso é o poder do DRF.

**Explicando as duas linhas principais**

- `queryset` → define quais objetos a view vai usar.
- `serializer_class` → define qual serializer será usado.

**Atualize o __init__.py**

No arquivo:

```
core/views/__init__.py
```

Adicione:

```python
from .categoria import CategoriaViewSet
```

---

**4.4 Criando as rotas (URLs)**

Agora precisamos criar os endereços da API.

No arquivo `urls.py` da pasta `app`, adicione:

```python
from core.views import CategoriaViewSet, UserViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'users', UserViewSet, basename='users')
```

O `router.register` cria automaticamente as rotas.

Ele vai gerar:

- `/api/categorias/`
- `/api/categorias/{id}/`

**Sobre o basename**

O `basename` é usado internamente pelo DRF para gerar os nomes das rotas.

Ele deve ser:

- Único
- Em minúsculo
- No plural

---

**4.5 Testando a API**

Inicie o servidor e acesse:

```
http://127.0.0.1:8000/api/
```

Se tudo estiver certo, você verá a interface automática do DRF.

**Listar todas as categorias**

```
http://127.0.0.1:8000/api/categorias/
```

**Busca uma categoria específica**

```
http://127.0.0.1:8000/api/categorias/1/
```

Se existir um registro com `id = 1`, você verá algo como:

```json
{
    "id": 1,
    "nome": "Romance"
}
```

Perceba: isso é exatamente o tipo de resposta que você já consumiu no front-end.

Só que agora você criou.

---

**4.6 Métodos HTTP**

A API usa métodos HTTP para manipular dados:

- **GET** → buscar dados
- **POST** → criar
- **PUT** → atualizar completamente
- **PATCH** → atualizar parcialmente
- **DELETE** → remover

**Qual a diferença entre PUT e PATCH?**

- **PUT** substitui o objeto inteiro.
- **PATCH** altera apenas os campos enviados.

---

**Códigos de status HTTP**

Quando você faz uma requisição, o servidor responde com um código:

- **200 OK** → deu certo
- **201 Created** → criado com sucesso
- **204 No Content** → removido com sucesso
- **400 Bad Request** → erro nos dados enviados
- **404 Not Found** → não encontrado

Você já deve ter visto alguns desses erros no navegador.

---

**4.7 Testando com outras ferramentas**

O navegador funciona bem para testes simples, mas existem ferramentas mais completas:

- Thunder Client (VS Code)
- RapidAPI (VS Code)
- Insomnia
- Postman

Essas ferramentas permitem enviar requisições com mais controle.

---

**4.8 Swagger**

O Swagger gera uma documentação interativa da API.

Acesse:

```
http://127.0.0.1:8000/api/swagger/
```

Você poderá testar os endpoints diretamente por lá.

---

**O que acontece quando fazemos um GET?**

Quando você acessa `/categorias/`:

1. A URL chama o Router.
2. O Router direciona para o ViewSet.
3. O ViewSet consulta o banco.
4. O Serializer transforma os dados em JSON.
5. O DRF retorna a resposta HTTP.

Tudo isso acontece automaticamente.

---

**4.9 Exercícios**

Agora é sua vez.

Utilizando o navegador ou uma ferramenta como Thunder Client:

- Crie algumas categorias.
- Liste todas.
- Atualize usando PUT.
- Atualize usando PATCH.
- Delete uma categoria.
- Crie outra.
- Liste novamente.

Teste tudo.

Quebre.

Experimente.

---

**4.10 Commit**

Faça um commit com a mensagem:

```
feat: criação da API para Categoria
```

Parabéns.

Agora você não é apenas alguém que consome API.

Você cria APIs.

---

# 5. Conectando a API ao frontend com Vue 3

Na aula anterior, você criou sua primeira API REST no backend.

Agora vamos fazer o outro lado da comunicação acontecer.

Até aqui:
- Criamos a API de `Categoria`
- Testamos com navegador, Swagger e ferramentas como Thunder Client

Mas agora vamos consumir essa API em uma aplicação real de frontend.

E mais importante: essa aplicação será o modelo base para o frontend completo da nossa **Livraria**.

---

**5.1 Objetivo da Aula**

Nesta aula você vai:

- Criar uma aplicação Vue 3 a partir de um template
- Executar o projeto localmente
- Conectar o frontend com a API da `Categoria`
- Confirmar que os dados estão vindo do backend

---

**5.2 Criando o Projeto a partir do Template**

Vamos usar um template já estruturado para acelerar o processo.

Acesse o repositório:

👉 https://github.com/marrcandre/template-vue3

**Passos:**

1. Clique no botão **"Use this template"**
2. Escolha **"Create a new repository"**
3. Dê um nome para o seu projeto (ex: `livraria-frontend`)
4. Clone o repositório para o seu computador

---

**5.3 Instalando as dependências**

Entre na pasta do projeto pelo terminal e execute:

```bash
npm install
```

Esse comando irá instalar todas as dependências necessárias definidas no `package.json`.

---

**5.4 Executando a aplicação**

Depois da instalação, execute:

```bash
npm run dev
```

Se tudo estiver correto, a aplicação será iniciada em:

```
http://localhost:3000
```

Abra no navegador.

---

**5.5 Conectando com a API da Categoria**

O template já possui uma estrutura básica para requisições.

Agora precisamos confirmar:

- O backend está rodando?
- A API está acessível?

Certifique-se de que sua API Django esteja rodando em:

```
http://127.0.0.1:8000
```

E que o endpoint funcione:

```
http://127.0.0.1:8000/api/categorias/
```

Se a aplicação Vue estiver configurada corretamente, ela deverá buscar os dados da API e exibir as categorias na tela.

---

**5.6 Se os dados não aparecerem**

Caso nada seja exibido:

1. Pressione **F12** no navegador.
2. Vá até a aba **Network**.
3. Verifique se a requisição foi feita.
4. Observe possíveis erros:
   - Erro de CORS
   - Erro 404
   - Erro 500
   - URL incorreta

Lembre-se:

Frontend e Backend estão em portas diferentes:
- Vue → 3000
- Django → 8000

---

**5.7 Entendendo o que está acontecendo**

Quando a página carrega:

1. O Vue faz uma requisição HTTP (GET)
2. A API responde com JSON
3. O Vue armazena os dados
4. O template renderiza na tela

Você acabou de conectar:

Frontend ↔ Backend

Essa é a base de qualquer aplicação moderna.

---

**5.8 Importante: NodeJS**

Se você tiver problemas com `npm`, verifique se está usando a versão LTS do NodeJS.

Consulte o tutorial:

👉 Instalação da versão LTS do NodeJS
https://eduardo-da-silva.github.io/aula-desenvolvimento-web/ambiente (Material do Prof. Eduardo da Silva).

---

**5.9 Exercícios**

1. Confirme se as categorias aparecem corretamente.
2. Adicione uma nova categoria pelo backend.
3. Atualize a página do frontend.
4. O novo dado aparece?
5. Tente desligar o backend e atualizar a página.
   - O que acontece?

Observe.
Teste.
Entenda o fluxo completo.

---

**Objetivo desta etapa**

Você não está apenas rodando um template.

Você está estabelecendo a arquitetura da aplicação:

Backend (API REST)
↓
Frontend (Vue.js)

E a partir daqui, tudo começa a se integrar.

---

# 6. Inclusão da Editora no projeto Livraria

Na aula anterior, criamos juntos a API de `Categoria`, passo a passo.

Agora o cenário muda.

Você já viu como funciona:
- Model
- Migração
- Admin
- Serializer
- ViewSet
- Router

Então agora é sua vez.

Nesta aula, você vai criar **sozinho** a API completa da `Editora`.

A ideia é:
1. Tentar fazer sem olhar o código pronto.
2. Usar a API de `Categoria` como referência, se necessário.
3. Depois comparar com a implementação final.

É assim que se constrói autonomia.

---

**6.1 Contexto**

Nossa aplicação é uma **livraria**.

Já temos:
- Categoria

Agora vamos criar:
- Editora
- (Depois criaremos Autor)
- (Por último, Livro)

A `Editora` representa a empresa responsável pela publicação dos livros.

Exemplos:
- Record
- Novatec
- Dark Side
- HarperCollins

Nossa Editora terá os seguintes campos:
- `nome`: string de no máximo 100 caracteres (obrigatório)
- `site`: URL do site da editora (opcional)

---
**6.2 O Desafio**

Crie a API completa da `Editora`, repetindo o mesmo padrão utilizado em `Categoria`.

**Você precisa:**

1. Criar a model `Editora`, no arquivo `core/models/editora.py`
2. Registrar no `models/__init__.py`
3. Criar e aplicar a migração (`pdm run migrate`)
4. Verificar se a tabela foi criada no banco de dados
5. Registrar no `admin.py`
6. Testar se a Editora aparece no painel administrativo.
7. Criar algumas editoras para testar a exibição
8. Criar o serializer no arquivo `core/serializers/editora.py`
9. Registrar no `serializers/__init__.py`
10. Criar a viewset no arquivo `core/views/editora.py`
11. Registrar no `views/__init__.py`
12. Adicionar a rota no `urls.py`
13. Testar a API

⚠️ Tente fazer antes de olhar a solução abaixo.

---

**6.3 Implementação esperada**

Após concluir, compare com os arquivos abaixo.

---

**📁 models/editora.py**

```python
from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome
```

**Reflita:**

- Por que `site` possui `blank=True` e `null=True`?
- Faz sentido obrigar que toda editora tenha site?

---

**📁 models/__init__.py**

```python
from .editora import Editora
```

---

**6.4 Migração**

Após criar a model:

```bash
pdm run migrate
```

Verifique se a tabela `core_editora` foi criada corretamente.

Se ocorrer erro:
- Você importou no `__init__.py`?
- Salvou todos os arquivos?
- Reiniciou o servidor?

---

**📁 admin.py**

```python
admin.site.register(models.Editora)
```

Acesse o painel administrativo e confirme se a Editora aparece.

---

**📁 serializers/editora.py**

```python
from rest_framework.serializers import ModelSerializer
from core.models import Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'
```

---

**📁 serializers/__init__.py**

```python
from .editora import EditoraSerializer
```

Pergunta importante:

O que acontece se você esquecer de importar o serializer no `__init__.py`?

---

**📁 views/editora.py**

```python
from rest_framework.viewsets import ModelViewSet
from core.models import Editora
from core.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
```

---

**📁 views/__init__.py**

```python
from .editora import EditoraViewSet
```

Pergunta:

Por que não precisamos implementar manualmente métodos como `create()` ou `list()`?

---

**📁 urls.py**

```python
from core.views import CategoriaViewSet, EditoraViewSet, UserViewSet

router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
```

Agora teste o endpoint:

```
http://127.0.0.1:8000/api/editoras/
```

---

**6.5 Testes obrigatórios**

Teste todos os métodos da API:

- GET
- POST
- PUT
- PATCH
- DELETE

---

**Exercícios de reflexão**

1. É possível criar uma Editora sem informar `site`?
2. O que acontece se você usar PUT sem enviar todos os campos?
3. O PATCH exige todos os campos?
4. Qual código HTTP é retornado ao criar com sucesso?
5. O que acontece ao buscar um ID inexistente?

Não apenas responda.
Teste.

---

**6.6 Commit**

Finalize com o commit:

```
feat: criação da API para Editora
```

---

**Objetivo desta aula**

Reforçar o padrão da arquitetura:

Model → Serializer → ViewSet → Router → URL

Repetição gera domínio.

Agora você já começa a construir APIs sem depender de passo a passo.

Na próxima aula, vamos criar a API de `Autor`. Até lá!

---

# 7. Criação da API para Autor

Vamos continuar a criação da API REST para o projeto `livraria`, criando a model `Autor` e a API para ela. Os passos são os mesmos que fizemos para as classes `Categoria` e `Editora`.

- Crie a API para a classe `Autor`.

O autor terá os seguintes atributos:

-   `nome`: `string` de no máximo 100 caracteres.
-   `email`: campo do tipo e-mail de no máximo 100 caracteres, que pode ser nulo.

- Teste a API.
- Faça o _commit_, com a mensagem:

```
feat: criação da API para Autor
```

**Exercícios:**

- Crie no Vuejs a tela para listar, incluir, alterar e excluir autores.

---


# 8. Criação da API para Livro

Vamos continuar a criação da API REST para o projeto `livraria`, criando a model `Livro` e a API para ela. Os passos iniciais são os mesmos que fizemos para as classes `Categoria`, `Editora` e `Autor`.

**8.1 Criação automática dos arquivos necessários**

Para facilitar a criação dos arquivos necessários para a model `Livro`, utilizar um script que cria automaticamente os arquivos necessários. Além disso, ele abre todos os arquivos necessários para criar a API, na ordem correta.

- Antes de executar o script, feche todas as abas do **VS Code** com o atalho `Ctrl+K W`.

- Execute o seguinte comando no terminal:

```shell
pdm cria_api livro
```

> O comando `pdm cria_api livro` é um comando que executa um script Python que cria automaticamente os arquivos necessários para a model `Livro`. Ele também abre todos os arquivos necessários para criar a API, na ordem correta.

**8.2 Criando o modelo de dados `Livro`**

-   Vamos criar o modelo de dados `Livro`, no arquivo `models/livro.py`:

```python

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f'({self.id}) {self.titulo} ({self.quantidade})'
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
- Faça um _commit_ com a mensagem:

```
feat: criação da entidade para Livro
```

---


# 9. Inclusão das chaves estrangeiras no modelo Livro

Nosso livro terá uma **categoria** e uma **editora**. Para isso, vamos incluir campos que serão **chaves estrangeiras**, referenciando os modelos `Categoria` e `Editora`. Esse relacionamento é do tipo **n para 1**. Posteriormente, vamos incluir um relacionamento **n para n** entre `Livro` e `Autor`.

**9.1 Campo `categoria` no `Livro`**

-   Inclua a linha a seguir no modelo `Livro`, logo após o atributo `preco`:

```python
from .categoria import Categoria
...
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='livros', null=True, blank=True
    )
...
```

-   Vamos entender cada parte:
    - `models.ForeignKey`: define o campo como sendo uma chave estrangeira.
    - `Categoria`: o `model` que será associado a este campo.
    - `on_delete=models.PROTECT`: impede de apagar uma _categoria_ que possua _livros_ associados. É conhecido **integridade referencial**. Outras formas de definir o comportamento são:
        - `models.PROTECT`: impede a exclusão de um objeto que possui referências em outros objetos.
        - `models.CASCADE`: exclui todos os objetos associados ao objeto que está sendo excluído.
        - `models.SET_NULL`: define o campo como nulo quando o objeto associado é excluído.
        - `models.SET_DEFAULT`: define o campo como o valor padrão quando o objeto associado é excluído.
    - `related_name='livros'`: é chamado de **relacionamento reverso**. Cria um atributo na classe `Categoria` que permite acessar todos os livros de uma categoria. Ou seja, quando você acessar uma categoria, poderá acessar todos os livros associados a ela.
    - `null=True, blank=True`:
        - `null=True`: permite que o campo seja nulo no banco de dados.
        - `blank=True`: permite que o campo seja nulo no formulário do Django Admin.
        - Na prática, juntos eles permitem que o campo seja **não obrigatório**.
        - Isso é útil para evitar problemas na migração.

**9.2 Campo `editora` no `Livro`**

-   De forma semelhante, vamos associar o **livro** a uma **editora**, incluindo logo em seguida à **categoria**, a seguinte linha:

```python
from .editora import Editora
...
editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros', null=True, blank=True)
```

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

No `Django Shell` (que iremos estudar em mais detalhes em uma [aula mais adiante](#14-uso-do-django-shell-e-do-django-shell-plus)), é possível testar o acesso a **todos os livros de uma categoria** usando algo parecido com isso:

-   Abra o Django shell:

```shell
pdm run shellp
```

-   Acesse os livros da categoria com `id` 1:

```python
>>> Categoria.objects.get(id=1).livros.all()
```

> O comando `pdm run shellp` é utilizado para abrir o Django Shell Plus com o ambiente virtual do projeto.

-  Faça um _commit_ com a mensagem:

```
feat: inclusão do relacionamento de Livro com Categoria e Editora
```

---


# 10. Inclusão do relacionamento n para n no modelo do Livro

**10.1 Model com ManyToManyField - Livros com vários autores**

Um livro pode ter vários autores, e um autor pode escrever vários livros. Sendo assim, criaremos agora um relacionamento **n para n** entre `Livro` e `Autor`. Para isso, utilizaremos um campo do tipo `ManyToManyField`.

> Uma outra forma de fazer isso seria criar uma **tabela associativa** (o que faremos posteriormente). Isso seria útil se quiséssemos armazenar informações adicionais sobre o relacionamento, como o papel do autor no livro (autor principal, coautor, etc.).

-   Inclua o campo `autores` no modelo `Livro`:

```python
from .autor import Autor
...
autores = models.ManyToManyField(Autor, related_name='livros', blank=True)
...
```

- Execute as migrações.

> Observe que o campo `autores` não foi criado na tabela `core_livro`. Ao invés disso, uma **tabela associativa** foi criada, com o nome `core_livro_autores`, contendo os campos `livro_id` e `autor_id`. É assim que é feito um relacionamento **n para n** no Django.

> Nesse caso, não é necessário usar o atributo `null=True` e `blank=True`, pois um campo do tipo `ManyToManyField` cria uma tabela associativa.

- A model `Livro` ficará assim:

![Projeto com a model Livro](diagramas/core_categoria_editora_autor_livro3.png)

> Note que na ligação entre `Livro` e `Autor` existem uma "bolinha" em cada lado, indicando que o relacionamento é **n para n**.

> Já no caso de `Livro` com `Categoria` e `Editora`, existe uma "bolinha" em `Livro` e um "pino" em `Categoria` e `Editora`, indicando que o relacionamento é **n para 1**.

> Observe as alterações no **banco de dados**, no **Admin** e na **API**.

- Faça um _commit_ com a mensagem:

```
feat: inclusão do relacionamento n para n entre Livro e Autor
```

**10.2 Exercícios**

- Teste a API REST de livros com modificações feitas.
- Faça o [Exercício da Garagem (E1)](#e1-crie-o-projeto-garagem) para praticar o que foi aprendido até aqui.

---


# 11. Modificação da API para Livro

- Acesse a API do Livro e veja como está a apresentação dos autores:

    http://127.0.0.1:8000/api/livros/

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
        fields = '__all__'
        depth = 1
```

Teste e você verá que isso resolve a listagem (GET), mas gera problema na criação e alteração (POST, PUT e PATCH).

- Para resolver isso, vamos criar dois (ou mais) serializadores, sendo um para a listagem e outro para a recuperação de um único livro:

```python
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class LivroListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1
```

- Inclua o serializador `LivroListRetrieveSerializer` no arquivo `serializers/__init__.py`:

```python
from .livro import LivroListRetrieveSerializer, LivroSerializer
```

> Observe que no `LivroListRetrieveSerializer` foi incluído o atributo `depth = 1`, que permite a apresentação dos dados relacionados.

- Na viewset, escolhemos o serializador conforme a operação:

```python
...
from core.serializers import LivroListRetrieveSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in {'list', 'retrieve'}:
            return LivroListRetrieveSerializer
        return LivroSerializer
```

> Nesse caso, o serializador `LivroListRetrieveSerializer` é utilizado para a listagem e recuperação de um único livro, enquanto o `LivroSerializer` é utilizado para as demais operações, ou seja, criação e alteração.

- Teste a API.
- Faça um _commit_ com a mensagem:

```
feat: criação de dois serializadores para Livro
```

**Criação de um serializador para a listagem de livros**

Podemos criar um serializador para a listagem de livros, que mostre apenas o `id`, o `título` e o `preço`. Isso pode ser útil, pois traz menos informações, o que pode tornar a listagem mais rápida.

-   Inclua um serializador `LivroListSerializer` para a listagem de livros, que mostre apenas o `id`, o `título` e o `preço` e renomeie o serializador `LivroListRetrieveSerializer` para `LivroRetrieveSerializer`:

```python
from core.serializers import (
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
...
class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ('id', 'titulo', 'preco')

class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1
```

-   Altere a viewset para utilizar este serializador na listagem:

```python
    def get_serializer_class(self):
        if self.action == 'list':
            return LivroListSerializer
        elif self.action == 'retrieve':
            return LivroRetrieveSerializer
        return LivroSerializer
```

> Observe que o serializador `LivroListSerializer` é utilizado apenas na listagem, enquanto o `LivroRetrieveSerializer` é utilizado na recuperação de um único livro e o `LivroSerializer` é utilizado nas demais operações.

- Não eaqueça de atualizar o arquivo `serializers/__init__.py`:

```python
from .livro import LivroListSerializer, LivroRetrieveSerializer, LivroSerializer
```

-   Teste a API. Observe que a listagem de vários livros está diferente da recuperação de um único livro.
-  Faça um _commit_ com a mensagem:

```
feat: criação de múltiplos serializadores para Livro
```

---


# 12. Upload e associação de imagens

Vamos instalar uma aplicação para gerenciar o upload de imagens e sua associação ao nosso modelo. Com isso poderemos associar imagens aos livros, ao perfil do usuário, etc.

Essa aplicação não será instalada através do comando `pdm add <pacote>`, pois é uma aplicação que não está disponível no `PyPI`. Ela será instalada manualmente, baixando e descompactando um arquivo compactado.

**Baixando o pacote**

Baixe e descompacte o arquivo com a `app` pronta para ser utilizada.

- No `Linux`, execute o seguinte comando no terminal:

```shell
wget https://github.com/marrcandre/django-drf-tutorial/raw/main/apps/uploader.zip -O uploader.zip && unzip uploader.zip && rm -v uploader.zip
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

- Remova a pasta `__pypackages__`  e o arquivo `pdm.lock`:

```shell
rm -rf __pypackages__ pdm.lock
```

- Recrie o arquivo `pdm.lock`:

```shell
pdm lock
```

- Instale as dependências:

```shell
pdm install
```

**Registro da app**

-   Adicione o pacote `uploader` na lista de `INSTALLED_APPS`, no `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'uploader', # nova linha
    'core',
    ...
]
```

**IMPORTANTE:** Não esqueça da vírgula no final da linha.

**Configuração no `urls.py`**

-   Inclua o seguinte conteúdo no arquivo `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static
...
from uploader.router import router as uploader_router
...
urlpatterns = [
    ...
    path('api/media/', include(uploader_router.urls)),  # nova linha
    ...
]
...
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
...
```

- Modifique a linha `post_migrate` no arquivo `pyproject.toml` para incluir a geração do diagrama da app `uploader`:

```shell
post_migrate = "python manage.py graph_models --disable-sort-fields -S -g -o core.png core uploader"
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
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
```

> O campo `capa` é uma chave estrangeira para a tabela `uploader_image`.

> O atributo `related_name='+'` indica que não será criado um atributo inverso na tabela `uploader_image`.

> O atributo `on_delete=models.SET_NULL` indica que, ao apagar a imagem, o campo `capa` será setado como `NULL`.

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
class LivroRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1
...
class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Livro
        fields = '__all__'
```

> Alteramos dois serializadores: um para a gravação e outro para a recuperação de um único livro.

> O campo `capa_attachment_key` é utilizado para a gravação da imagem, enquanto o campo `capa` é utilizado para a recuperação da imagem.


**Teste de upload e associação com o livro**

-   Acesse a API de media:

    http://127.0.0.1:8000/api/media/images/

-   Faça o upload de uma imagem.
-   Observe que o campo `capa_attachment_key` foi preenchido com o valor `attachment_key` da imagem.
-   Guarde o valor do campo `capa_attachment_key`.
-   Crie um novo livro, preenchendo o campo `capa_attachment_key` com o valor guardado anteriormente.
-   Acesse o endpoint `http://127.0.0.1:8000/api/media/images/` e observe que a imagem foi associada ao livro.

- Faça um _commit_ com a mensagem:

```
feat: inclusão da app de upload e associação de imagens
```

---


# 13. Dump e Load de dados

O **dump** dos dados permite que você salve os dados do banco de dados em um arquivo. O **load** dos dados permite que você carregue os dados de um arquivo para o banco de dados. Isso é útil para fazer cópias de segurança, para transferir dados entre bancos de dados, para carregar dados iniciais, etc.

**Carga inicial de dados**

- Acesse o seguinte link:

  - Link: [`http://191.52.55.236:8000/admin/`](http://191.52.55.236:8000/admin/) (ou peça ao professor)
  - Usuário: `a@a.com`
  - Senha: `teste.123`

- Cadastre pelos menos 10 livros, com autor e editora
- Verifique se o livro, categoria, autor ou editora já estão cadastrados, para **evitar duplicidade**.
- **NÃO USE CAIXA ALTA!!!**
- Use o formato de nomes de livros, como no exemplo: `O Senhor dos Anéis - A Sociedade do Anel`

**Cópia de segurança dos dados**

-   Execute o comando `dumpdata`:

```shell
pdm run dumpdata > core.json
```

-   Observe que o arquivo `core_bkp.json` foi criado:

```shell
code core.json
```

**IMPORTANTE:** Se o arquivo tiver algumas linhas semelhantes a essas no seu início, apague-as:

```ini
MODE = 'DEVELOPMENT'
MEDIA_URL = 'http://191.52.55.44:8000/media/'
DATABASES = {'default': {'NAME': 'db.sqlite3', 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '', 'CONN_MAX_AGE': 600, 'CONN_HEALTH_CHECKS': True, 'DISABLE_SERVER_SIDE_CURSORS': False, 'ENGINE': 'django.db.backends.sqlite3'}}
```

**Arquivo exemplo:**

-   Baixe o arquivo `core.json`:

**No Linux:**

```shell
wget https://raw.githubusercontent.com/marrcandre/django-drf-tutorial/refs/heads/main/scripts/core.json
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

> O comando espera um arquivo `core.json` na pasta raiz do projeto.

**Criando os campos email e cidade para Editora**

Você deve receber uma mensagem de erro ao tentar fazer o "load" dos dados, pois os campos `email` e `cidade` não existem na model `Editora`. Para resolver isso, você deve criar esses campos na model `Editora`.


-   Edite o arquivo `models/editora.py` e adicione os campos `email` e `cidade`:

```python
class Editora(models.Model):
...
    email = models.EmailField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

```
-   Faça a migração dos dados e tente fazer o "load" novamente:

**Verificando se a carga dos dados funcionou**

-  Utilizando o Django Shell Plus, observe que os dados foram carregados:

```shell
pdm run shellp
```
E dentro dele, execute:

```python
>>> Livro.objects.all()
```

Você também pode acessar o Django Admin ou o Swagger e verificar que os dados foram carregados.

---


# 14. Customização do Admin

O **Admin** é uma ferramenta para gerenciar os dados do banco de dados. Ele pode ser customizado para melhorar a experiência do usuário.

-   Edite o arquivo `core/admin.py`:

**Importação das models**

Vamos importar as models de forma explícita:

```python
from core.models import Autor, Categoria, Editora, Livro, User
```

**Registro das models através do decorator `@admin.register`**

Vamos registrar as models através do decorator `@admin.register`, ao invés de utilizar a função `admin.site.register()`. Por exemplo, para a model `User`:

```python
@admin.register(User)
class UserAdmin(BaseUserAdmin):
...
```

- A linha `admin.site.register(User, BaseUserAdmin)` deve ser removida.

**Customização do Admin**

Vamos customizar o Admin para as models `Autor`, `Categoria`, `Editora` e `Livro`:

```python
...
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')
    list_per_page = 10

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 10

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade')
    search_fields = ('nome', 'email', 'cidade')
    list_filter = ('nome', 'email', 'cidade')
    ordering = ('nome', 'email', 'cidade')
    list_per_page = 10

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

-   Acesse o `Admin` e veja as modificações:

    http://127.0.0.1:8000/api/admin/

-  Faça um _commit_ com a mensagem:

```
feat: customização do Admin
```

---


# 15. Uso do Django Shell e do Django Shell Plus

O **Django Shell** é uma ferramenta para interagir com o banco de dados. O **Django Shell Plus** é uma extensão do Django Shell que inclui alguns recursos adicionais, como a inclusão automática dos modelos.

-   Acesse o shell:

```shell
pdm run shellp
```

-   Crie um objeto:

```python
>>> categoria = Categoria.objects.create(descricao='Desenvolvimento Web')
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
>>> categoria = Categoria.objects.get(descricao='Desenvolvimento Web')
```

-   Observe que o objeto foi obtido:

```python
>>> categoria
<Categoria: Desenvolvimento Web>
```

-   Atualize o objeto:

```python
>>> categoria.descricao = 'Desenvolvimento Web com Django'
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

**Usando o atributo `related_name`**

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
Para mais exemplos de uso do Django Shell Plus, acesse este [anexo](#a10-django-shell---comandos-úteis).

---


# 16. Autenticação e autorização

**Introdução**

Vamos trabalhar agora os conceitos de segurança relacionados a **autenticação** (_login_) e **autorização** (_permissão_). Utilizaremos aquilo que o Django já oferece, em termos de usuários e grupos.

Uma estratégia muito utilizada para a definição de permissões de acesso é:

-   Criar **grupos** para perfis de usuários específicos.
-   Definir as **permissões** que este grupo de usuários terá.
-   Criar um **usuário** para cada pessoa que utilizará a aplicação.
-   **Incluir** os usuários nos grupos, dando assim as permissões.
-   No caso de mudanças nas permissões, elas são sempre feitas nos **grupos**, refletindo nos usuários.
-   Se um usuário possui mais do que um perfil de permissões, ele deve ser incluído em **vários** grupos.
-   Quando um usuário sai de uma função ou deve perder seus privilégios, ele é **removido** do grupo específico.

> **Resumindo:** toda a estratégia de permissões parte da criação de grupos e inclusão ou remoção de usuários desses grupos.

> Observe no **Admin**, para cada usuário em **Usuários (Users)**, as opções de **Permissões do usuário**.

**Relação entre nomes das ações**

Podemos perceber uma relação entre as ações que compõem o **CRUD**, os termos utilizados no **Admin**, os verbos **HTTP** e as **actions** dos **serializadores** do **Django REST Framework**.:

| Ação      | CRUD   | Admin  | Verbos HTTP        | Ações do DRF |
| --------- | ------ | ------ | ----------- | ------------------ |
| Criar     | **C**reate | `add`    | `POST`        | `create`           |
| Ler       | **R**ead   | `view`   | `GET`         | `retrieve`, `list` |
| Atualizar | **U**pdate | `change` | `PUT (PATCH)` | `update`, `partial_update` |
| Deletar   | **D**elete | `delete` | `DELETE`      | `destroy`          |

**Exercícios**

No `Admin`, crie os seguintes usuários e grupos e dê as permissões necessárias:

**a. Criando grupos e dando permissões**

Vamos começar criando 2 grupos e dando a eles permissões distintas:

-   Crie um grupo chamado `administradores`, com as seguintes as permissões:
    -   Adicionar, editar, visualizar e remover: `autor`, `categoria` e`editora`.
    -   Adicionar, editar e visualizar: `livro`.
-   Crie um grupo chamado `compradores`, com as seguintes permissões:
    -   Visualizar: `autor`, `categoria` e `editora`.
    -   Adicionar, editar e visualizar: `livro`.

As permissões para `compradores` devem ficar assim:

![Permissões do grupo Compradores](imagens/permissoes_compradores.png)

**b. Criando usuários e adicionando aos grupos**

-   Crie um usuário `admin1@a.com` e o inclua no grupo `Administradores`.
-   Crie um usuário `comprador1@a.com` e o inclua no grupo `Compradores`.

**c. Testando as permissões**

-   Acesse o `Admin` com o usuário `admin1@a.com` e verifique se ele tem acesso a todas as permissões do grupo `Administradores`.
    - Ele deve conseguir adicionar, editar, visualizar e remover `autor`, `categoria`, `editora`.
    - Deve também conseguir adicionar, editar e visualizar `livro` (mas não deve conseguir remover `livro`).
-   Acesse o `Admin` com o usuário `comprador1@a.com` e verifique se ele tem acesso apenas às permissões do grupo `Compradores`.
    - Ele deve conseguir apenas visualizar `autor`, `categoria` e `editora`, sem alterar ou excluir esses objetos.
    - Ele deve também conseguir adicionar, editar e visualizar `livro`, mas não deve conseguir excluir livros.

---


# 17. Utilização das permissões do DRF

**Autenticação e permissão**

_A **autenticação** ou **identificação** por si só geralmente não é suficiente para obter acesso à informação ou código. Para isso, a entidade que solicita o acesso deve ter **autorização**._ [(Permissões no DRF)](https://www.django-rest-framework.org/api-guide/permissions/)

**Autenticação** significa que um usuário foi **identificado** em um sistema, portanto ele é **conhecido**. Isso se dá, normalmente por um sistema de **_login_**.

**Permissão (autorização)** se dá por um esquema de **conceder privilégios**, seja a usuários ou grupos.

Por padrão, qualquer usuário, mesmo sem autenticação, tem acesso irrestrito e permissão de fazer qualquer coisa em uma aplicação.

As permissões podem ser definidas:

1. a nível de objeto (nas `views` ou `viewsets`, por exemplo);
1. de forma global, no arquivo `settings.py`;
1. com o uso de classes de permissão do `Django REST Framework`.

Vamos analisar cada uma dessas formas.

**a. Exemplo de uso de permissão na `viewset`**

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

**b. Exemplo de uso de permissão no `settings.py`**

Outra forma de gerenciamento de permissões é feita no arquivo `settings.py`.

> **IMPORTANTE:** Para utilizá-la, comente as últimas alterações feitas no arquivo `views/categoria.py`.

Uma forma de conseguir o mesmo resultado de forma padrão para todo o projeto, isto é, permitir acesso aos _endpoints_ **apenas para usuários autenticados**, é configurar desse modo o arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

Para testar:

- Inclua o código acima e teste novamente o acesso aos _endpoints_ do DRF (categorias, editoras, etc.) com e sem uma sessão autenticada.

> **Resumindo**, utilizamos a classe `IsAuthenticated` no `settings.py` para permitir acesso apenas a usuários autenticados.

**c. Permissões com o `DjangoModelPermissionsOrAnonReadOnly`**

Apesar de ser possível definir a autorização das formas que vimos anteriormente, adotaremos uma outra forma. Essa forma que iremos adotar para o gerenciamento de permissões será com o uso do [DjangoModelPermissions](https://www.django-rest-framework.org/api-guide/permissions/).

Esta classe de permissão está ligada às permissões do modelo `django.contrib.auth` padrão do Django. Essa permissão deve ser aplicada apenas a visualizações que tenham uma propriedade `.queryset` ou método `get_queryset()` (exatamente o que temos).

A autorização só será concedida se o usuário estiver autenticado e tiver as permissões de modelo relevantes atribuídas, da seguinte forma:

-   As solicitações `POST` exigem que o usuário tenha a permissão de adição (`add`) no modelo.
-   As solicitações `PUT` e `PATCH` exigem que o usuário tenha a permissão de alteração (`change`) no modelo.
-   As solicitações `DELETE` exigem que o usuário tenha a permissão de exclusão (`remove`) no modelo.
-   **Se o usuário não estiver autenticado, ele terá acesso somente leitura à API.**

Para isso, teremos que alterar a classe de autenticação, substituindo o que colocamos anteriormente:

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly', ),  # autorização de acesso
    ...
}
```

> **Resumindo**, utilizaremos a estrutura de usuários, grupos e permissões que o próprio Django já nos fornece. Para isso, utilizaremos o [DjangoModelPermissionsOrAnonReadOnly](https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissionsoranonreadonly) para gerenciar as permissões.

Para utilizar essa estrutura de permissões corretamente, precisaremos de um sistema de autenticação (`login`) no nosso projeto, de forma a enviar essas informações via a `URL`. Para isso, utilizaremos o **SimpleJWT**.

---


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

**Ativando o SimpleJWT**

-   Adicione (ou descomente) o `SimpleJWT` no arquivo `settings.py`:

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",),
    ...
}
```

-   Observe que já existem as entradas referentes ao `SimpleJWT` no arquivo `urls.py`:

    - `/api/token/` — obtenção do token (login)
    - `/api/token/refresh/` — renovação do token
    - `/api/token/verify/` — verificação do token
    - `/api/registro/` — registro de novos usuários

-   Feitas essas alterações, coloque o servidor do Django novamente em execução.

**Exercícios: Testando a autenticação com o SimpleJWT**

Para testar se tudo deu certo, utilizaremos um cliente HTTP, como o **Thunder Client**.

**Dica:** se sua ferramenta permitir, crie várias requisições separadas e dê nomes, como _login_, _consulta_, _inclusão_, etc.

-   Ao tentar acessar um _endpoint_ com `GET`, como esse:

```
[GET] http://0.0.0.0:19003/api/categorias/
```

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
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

> Para verificar as informações do token, acesse os sites [jwt.io](https://jwt.io/) ou [token.dev](https://token.dev/), cole o valor do token no campo `Encoded` e clique no botão `Decode`.

Todas as chamadas ao sistema que precisarem de autenticação deverão ser feitas com o campo `access` token. Para isso, copie o valor do campo `access` e cole no campo `Auth`, opção `Bearer` do Thunder Client.

Para testar, acesse com `GET` o seguinte endereço:

```
[GET] http://0.0.0.0:19003/api/categorias/
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

Para renovar o token, você pode:

1. Fazer novamente a requisição de autenticação (`/api/token/`), enviando as informações de usuário e senha.
2. Usar o _refresh token_ para obter um novo _access token_, enviando uma requisição `POST` para `/api/token/refresh/` com o campo `refresh`:

```json
{
    "refresh": "seu_refresh_token_aqui"
}
```

**Tentando alterar uma informação**

```
[PUT] http://0.0.0.0:19003/api/categorias/10/
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

-   Criar uma requisição de autenticação, do tipo `POST`, para a URL `/api/token/`, enviando as informações de usuário e senha.
-   Copiar a chave do tipo `access` e colocá-la no cabeçalho `Auth`, opção `Bearer` da requisição do tipo `GET` que você fará.

Com isso, fizemos um sistema básico de **autenticação** (_login_) e **autorização** (_permissões_) usando o próprio sistema já fornecido pelo Django.

**Finalizando**

- Faça um _commit_ com a mensagem `Autenticação com o SimpleJWT`.

**Extra**

Fazendo login pela linha de comando, utilizando o `curl`:

```shell
curl -X POST http://127.0.0.1:19003/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"email": "comprador1@a.com", "password": "teste.123"}'
```

---


# 19. Inclusão da foto de perfil no usuário

Vamos aproveitar a aplicação `uploader` para incluir a foto de perfil no usuário.

**Criação do campo de foto de perfil**

-   No arquivo `models/user.py`, inclua o campo `foto`:

```python
...
from uploader.models import Image
...
class User(AbstractBaseUser, PermissionsMixin):
    foto = models.ForeignKey(
        Image,
        related_name='user_foto',
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

> Observe a ligação entre a model `User` e a model `Image`, através da chave estrangeira `foto`.

**Inclusão da foto no `Admin`**

-   No arquivo `admin.py`, inclua o campo `foto`:

```python
...
class UserAdmin(BaseUserAdmin):
    ...
        (_('Personal Info'), {'fields': ('name', 'foto')}),# inclua a foto aqui
    ...
```

- Teste a inclusão da foto de um usuário pelo `Admin`.

**Inclusão da foto no serializer**

-   Substitua o serializador para o usuário, em `serializers/user.py`, por este:

```python
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import User
from uploader.models import Image
from uploader.serializers import ImageSerializer


class UserSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source='foto',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(
        required=False,
        read_only=True
    )

    class Meta:
        model = User
        fields = '__all__'
```

> O atributo `write_only=True` indica que o campo `foto_attachment_key` é apenas para escrita. Isso significa que ele não será exibido na resposta da API.

> O atributo `read_only=True` indica que o campo `foto` é apenas para leitura. Isso significa que ele não será aceito na requisição da API.

**Testando**

-   Inclua uma foto de perfil em um usuário, através da API.

**Finalizando**

- Faça as alterações no sistema publicado.
- Faça um _commit_ com a mensagem:

```
feat: inclusão da foto de perfil no usuário
```

---


# 20. Criação da entidade Compra integrada ao usuário do projeto

A partir dessa aula, vamos implementar o processo de compra de livros, na nossa aplicação. Nessa aula, vamos criar um entidade de compras integrada à entidade do usuário do projeto.

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
        CARRINHO = 1, 'Carrinho'
        FINALIZADO = 2, 'Finalizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)
```

> Note que estamos utilizando a model `User` como `ForeignKey` para a model `Compra`.

> `StatusCompra` é do tipo `IntegerChoices`, que é uma forma de criar um campo `choices` com valores inteiros.

> `status` é um campo `IntegerField` que utiliza o `choices` `StatusCompra.choices` e tem o valor padrão `StatusCompra.CARRINHO`, que no caso é `1`.

> Opcionalmente, poderíamos ter criado uma entidade `StatusCompra` e utilizado um campo `ForeignKey` para ela. No entanto, como temos um número pequeno de status, optamos por utilizar o `IntegerField` com `choices`.

- Inclua a nova model no arquivo `core/models/__init__.py`:

```python
from .compra import Compra
```

**Adicionando a model `Compra` ao `Admin`**

-   Adicione a model `Compra` ao `admin.py` do app `core`:

```python
...
from core.models import Compra
...
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status')
    ordering = ('usuario', 'status')
    list_per_page = 10
```

**Executando as migrações**

-   Execute as migrações.

O seu projeto deve ficar assim:

![Projeto com a model Compra](diagramas/core_compra1.png)

**Testando a model `Compra`**

-   Teste a model `Compra` no `Admin` do Django.

**Finalizando**

- Faça um _commit_ com a mensagem:

```
feat: criação da entidade Compra integrada ao usuário do projeto
```

---


# 21. Criação dos itens da compra

No caso dos itens da compra, não vamos utilizar um campo `livro` do tipo `ManyToManyField` no model `Compra`, pois queremos ter a possibilidade de adicionar mais informações ao item da compra, como a `quantidade`, por exemplo. Desta forma, vamos criar "manualmente" a **entidade associativa**, que será chamada de `ItensCompra`.

-   Vamos adicionar uma nova entidade `ItensCompra` ao arquivo `core/models/compra.py`:

```python
...
from .livro import Livro
...
class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField(default=1)
```

> No atributo `compra`, utilizamos `models.CASCADE`, pois queremos que, ao deletar uma compra, todos os itens da compra sejam deletados também.

> No atributo `livro`, utilizamos `models.PROTECT`, pois queremos impedir que um livro seja deletado se ele estiver associado a um item de compra.

> Ainda no `livro`, utilizamos `related_name='+'`, pois não queremos que o `ItensCompra` tenha um atributo `livro`.

- Inclua o novo model no arquivo `__init__.py` dos models:

```python
from .compra import Compra, ItensCompra
```

-   Execute as migrações (você já sabe como fazer, certo?)

O seu projeto deve ficar assim:

![Projeto com a model Compra](diagramas/core_compra_com_itens.png)

-   Verifique que a tabela `core_itenscompra` foi criada no banco de dados.
-   Inclua o model `ItensCompra` no `Admin` do Django.
-   Faça um _commit_ com a mensagem:

```
feat: criação dos itens da compra
```

---


# 22. Uso de TabularInline no Admin para Itens da Compra

Da forma que configuramos o `Admin` para a model `ItensCompra`, não é possível adicionar itens da compra diretamente na tela de edição da compra. Isso é pouco natural, pois há uma relação direta entre a compra e seus itens.

Sendo assim, vamos mostrar os itens da compra no `Admin` do Django, utilizando o `TabularInline`. Desta forma, podemos adicionar os itens da compra diretamente na tela de edição da compra.

-   No arquivo `admin.py` do app `core`, modifique o código das models `Compra` e `ItensCompra` da seguinte forma:

```python
class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    extra = 1  # Quantidade de itens adicionais


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status')
    search_fields = ('usuario', 'status')
    list_filter = ('usuario', 'status')
    ordering = ('usuario', 'status')
    list_per_page = 10
    inlines = [ItensCompraInline]
```

> Desta forma, quando você editar uma compra no `Admin` do Django, você verá os itens da compra logo abaixo do formulário de edição da compra.

> Opcionalmente, você pode utilizar o `StackedInline` ao invés do `TabularInline`. Experimente e veja a diferença.

-   Teste no `Admin` do Django.
-   Faça um _commit_ com a mensagem:

```
feat: uso de TabularInline e StackedInline no Admin para Itens da Compra
```

---


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
        fields = '__all__'
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
from core.views import (
    AutorViewSet,
    CategoriaViewSet,
    CompraViewSet, # inclua essa linha
    EditoraViewSet,
    LivroViewSet,
    UserViewSet,
)
...
router.register(r'compras', CompraViewSet)
...
```

-  Teste o endpoint no navegador.
-  Faça o _commit_ com a mensagem:

```
feat: criação do endpoint para a listagem básica de compras
```

**Inclusão do e-mail do usuário na listagem da compra**

Nesse momento, a listagem de compras mostra apenas o `id` do usuário. Vamos substituir o `id` pelo `email` do usuário.

-   No serializer de `Compra`, inclua o seguinte código:

```python
...
from rest_framework.serializers import CharField, ModelSerializer
...
class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True) # inclua essa linha
...
```

> O parâmetro `source` indica qual campo do model `Compra` será utilizado para preencher o campo `usuario` do serializer.

> O parâmetro `read_only` indica que o campo `usuario` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem:

```
feat: inclusão do e-mail do usuário na listagem da compra
```

**Inclusão do status da compra na listagem da compra**

De forma semelhante ao e-mail do usuário, vamos incluir o status da compra na listagem da compra.

-   No serializer de `Compra`, inclua o seguinte código:

```python
...
class CompraSerializer(ModelSerializer):
    status = CharField(source='get_status_display', read_only=True) # inclua essa linha
...
```

> O parâmetro `source` indica qual método do model `Compra` será utilizado para preencher o campo `status` do serializer. Sempre que utilizamos um campo do tipo `IntegerChoices`, podemos utilizar o método `get_<nome_do_campo>_display` para obter a descrição do campo.

> O parâmetro `read_only` indica que o campo `status` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem:

```
feat: inclusão do status da compra na listagem da compra
```

> Estes são apenas dois exemplos de como podemos modificar a listagem de compras. Você pode incluir outros campos, como o total da compra, por exemplo.

---



# 24. Visualização dos itens da compra no endpoint da listagem de compras

De forma semelhante ao que fizemos no `Admin`, vamos incluir os itens da compra na listagem de compras.

-   Crie um serializer para `ItensCompra`, no arquivo `serializers/compra.py`:

```python
...
from core.models import Compra, ItensCompra
...

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = '__all__'
```

No `CompraSerializer`, inclua o seguinte código:

```python
...
itens = ItensCompraSerializer(many=True, read_only=True)
...
```

> O parâmetro `many=True` indica que o campo `itens` é uma lista de itens.

> O parâmetro `read_only=True` indica que o campo `itens` não será utilizado para atualizar o model `Compra`.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem:

```
feat: visualização dos itens da compra na listagem da compra
```

**Mostrando os detalhes dos itens da compra na listagem de compras**

-   No serializer de `ItensCompra`, modifique o código:

```python
class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = '__all__'
        depth = 1
```

> O parâmetro `depth=1` indica que o serializer deve mostrar os detalhes do model `ItensCompra`. O valor `1` indica que o serializer deve mostrar os detalhes do model `ItensCompra` e dos models relacionados a ele (nesse caso, o `livro`). Se o valor fosse `2`, o serializer mostraria os detalhes do model `ItensCompra`, dos models relacionados a ele e dos models relacionados aos models relacionados a ele (nesse caso, a `categoria`, a `editora` e o `autor`).

- Experimente alterar o valor de `depth` e veja o resultado no navegador.

**Mostrando apenas os campos necessários dos itens da compra na listagem de compras**

Você deve ter percebido que o serializer de `ItensCompra` está mostrando todos os seus campos, incluindo o campo `compra`. Vamos modificar o serializer para mostrar apenas os campos necessários. Nesse exemplo, vamos mostrar apenas os campos`livro` e `quantidade`.

-   No `ItensCompraSerializer`, modifique a linha `fields`:

```python
fields = ('livro', 'quantidade')
```

> O parâmetro `fields` indica quais campos do model `ItensCompra` serão mostrados no serializer. Se o valor for `__all__`, todos os campos serão mostrados. Se o valor for uma sequência de campos, apenas esses campos serão mostrados.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem:

```
feat: limitando os campos dos itens da compra na listagem de compras
```

---


# 25. Exibição do total do item na listagem de compras

O total do item é calculado pelo preço do livro multiplicado pela quantidade. Esse é um campo calculado, que não existe no model `ItensCompra`. Vamos incluir este campo na listagem de compras.

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
        fields = ('livro', 'quantidade', 'total')
        depth = 1
```

> O parâmetro `SerializerMethodField` indica que o campo `total` não existe no model `ItensCompra`. Ele será calculado pelo método `get_total`.

> O método `get_total` recebe como parâmetro o objeto `instance`, que representa o item da compra. A partir dele, podemos acessar os campos do item da compra, como `quantidade` e `livro.preco`.

> O método `get_total` retorna o valor do campo `total`, que é calculado pelo preço do livro multiplicado pela quantidade.

> O método `get_<nome_do_campo>` é um método especial do serializer que é chamado para calcular o valor do campo `<nome_do_campo>`.

> Incluimos o campo `total` no atributo `fields` do serializer.

-   Teste o endpoint no navegador.
-   Faça o _commit_ com a mensagem:

```
feat: mostrando o total do item na listagem de compras
```

---


# 26. Inclusão do total da compra na listagem de compras

Vamos incluir o total da compra na listagem de compras. O total da compra é calculado pela soma dos totais dos itens da compra. Esse é um campo calculado, que não existe no model `Compra`. Vamos incluir este campo na listagem de compras.

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

- Precisamos incluir o campo `total` no serializer de `Compra`. No `CompraSerializer`, inclua o seguinte código:

```python
...
        fields = ('id', 'usuario', 'status', 'total', 'itens')
...
```

> O parâmetro `fields` indica quais campos do model `Compra` serão mostrados no serializer. Se o valor for `__all__`, todos os campos serão mostrados. Se o valor for uma lista de campos, apenas os campos da lista serão mostrados, na ordem da lista.

- Teste o endpoint no navegador.
- Faça o _commit_ com a mensagem:

```
feat: inclusão do total da compra na listagem de compras
```

**Inclusão do total da compra no Admin**

Para finalizar, vamos incluir o total da compra no `Admin` do Django.

-   No arquivo `admin.py` do app `core`, modifique o código da model `Compra`:

```python
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status', 'total_formatado')  # mostra na listagem
    ordering = ('usuario', 'status')
    list_per_page = 10
    inlines = [ItensCompraInline]
    readonly_fields = ("total_formatado",)  # mostra dentro do formulário

    @admin.display(description="Total")
    def total_formatado(self, obj):
        """Exibe R$ 123,45 em vez de 123.45."""
        return f"R$ {obj.total:.2f}"
```

> O método `total_formatado` é um método especial do `admin` que é chamado para formatar o valor do campo `total`. Ele recebe como parâmetro o objeto `obj`, que representa a compra. A partir dele, podemos acessar os campos da compra, como `total`.

> O método `total_formatado` retorna o valor do campo `total` formatado como uma string, com duas casas decimais e o símbolo de real (R$).

> O parâmetro `readonly_fields` indica que o campo `total_formatado` é apenas para leitura. Isso significa que ele não será editável no formulário de edição da compra.

> O parâmetro `@admin.display(description="Total")` indica que o campo `total_formatado` será exibido com o título "Total" na listagem do `Admin`.

> O parâmetro `list_display` indica quais campos serão exibidos na listagem do `Admin`. O campo `total_formatado` será exibido na listagem, com o título "Total".

-   Teste o `Admin` do Django e verifique se o total da compra está sendo exibido corretamente.
-   Faça um _commit_ com a mensagem:

```
feat: inclusão do total da compra no Admin
```

---


# 27. Criação de compras com itens aninhados via API

Vamos primeiro definir o que é necessário para criar uma nova compra. Para isso, precisamos informar o usuário e os itens da compra. Os itens da compra são compostos pelo livro e pela quantidade.

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

**Criando serializers para criação de compras**

Como estamos lidando com dados aninhados (compra com vários itens), precisamos criar serializers específicos para entrada de dados.

**1. `ItensCompraCreateUpdateSerializer`**

Esse serializer será usado para criar os itens de uma compra. Ele é simples, pois requer apenas o `livro` e a `quantidade`.

No início do arquivo `serializers/compra.py`, adicione:

```python
class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')
```

**2. CompraCreateUpdateSerializer**

Agora vamos criar o serializer da `Compra`, utilizando o serializer acima no campo `itens`.

Ainda no `serializers/compra.py`, inclua o seguinte código:

```python
class CompraCreateUpdateSerializer(ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('usuario', 'itens')
```

> O parâmetro `many=True` indica que o campo `itens` é uma lista de itens de compra.

- Inclua também o serializer no arquivo `__init__.py` dos `serializers`:

```python
from .compra import (
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraSerializer,
)
```

**Atualizando a `view` para usar o serializer de criação**

Vamos alterar o `viewset` de `Compra` para usar o novo serializer, nas operações de criação e alteração.

- No arquivo `views/compra.py` altere o `viewset` de `Compra` para usar o novo serializer:

```python
...
from core.serializers import CompraCreateUpdateSerializer, CompraSerializer
...
class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return CompraCreateUpdateSerializer
        return CompraSerializer
```

**Testando a criação de compra**

- Tente criar uma nova compra usando o método `POST` no endpoint `/compras/`, por exemplo no ThunderClient:

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

AssertionError at `/api/compras/`
The `.create()` method does not support writable nested fields by default.
Write an explicit `.create()` method for serializer `core.serializers.compra.CompraCreateUpdateSerializer`, or set `read_only=True` on nested serializer fields.

Traduzindo, chegamos no seguinte:

Erro de afirmação em `/api/compras/`
O método `.create()` não suporta campos aninhados graváveis por padrão.
Escreva um método `.create()` explícito para o serializer `core.serializers.compra.CompraCreateUpdateSerializer`, ou defina `read_only=True` nos campos do serializer aninhado.

**Entendendo o erro**

Esse erro acontece porque o DRF, por padrão, n**ão sabe como salvar campos aninhados** (como os itens da compra). Precisamos sobrescrever o método **create** no serializer da **Compra**.

**Implementando o método create**

Atualize o `CompraCreateUpdateSerializer` no `serializers/compra`.py para incluir o método:

```python
...

class CompraCreateUpdateSerializer(ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('usuario', 'itens')

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra

```

**Explicação**

> O método `create` é chamado quando uma nova compra é criada. Ele recebe os dados validados e cria a compra e os itens da compra.

> O método `create` recebe um parâmetro `validated_data`, que são os dados validados que estão sendo criados.

> `validade_data.pop('itens')` remove os itens da compra dos dados validados. Isso é necessário, pois os itens da compra são criados separadamente.

> O comando `Compra.objects.create(**validated_data)` cria a compra com os dados validados, exceto os itens da compra.

> O comando `ItensCompra.objects.create(compra=compra, **item_data)` cria novos itens com os dados validados. Ele liga os itens da compra à compra recém criada, através do parâmetro `compra=compra`.

**Conclusão**

- Teste o endpoint no `ThunderClient.
- Faça o _commit_ com a mensagem:

```
feat: criação de um endpoint para criar novas compras
```

---


# 28. Atualização de compras e seus itens via API

**Entendendo o problema**


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

AssertionError at `/api/compras/1/`
The `.update()` method does not support writable nested fields by default.
Write an explicit `.update()` method for serializer `core.serializers.compra.CompraCreateUpdateSerializer`, or set `read_only=True` on nested serializer fields.

Traduzindo:

Erro de afirmação em `/api/compras/1/`
O método `.update()` não suporta campos aninhados graváveis por padrão.
Escreva um método `.update()` explícito para o serializer `core.serializers.compra.CompraCreateUpdateSerializer`, ou defina `read_only=True` nos campos do serializer aninhado.

> Esse erro acontece porque os itens da compra vêm de uma tabela relacionada (`ItensCompra`) e o DRF, por padrão, **não sabe como atualizar campos aninhados**. Precisamos, portanto, sobrescrever o método update() do serializer.

**Sobrescrevendo o método `update`**

- No arquivo `serializers/compra.py`, altere o `CompraCreateUpdateSerializer` adicionando o seguinte:

```python
    def update(self, compra, validated_data):
        itens_data = validated_data.pop('itens', [])
        if itens_data:
            compra.itens.all().delete()
            for item_data in itens_data:
                ItensCompra.objects.create(compra=compra, **item_data)
        return super().update(compra, validated_data)
```

**Explicando o método `update`**

- `validated_data.pop('itens', [])`: remove os dados dos itens para tratar separadamente;
- `compra.itens.all().delete()`: remove todos os itens antigos da compra;
- `ItensCompra.objects.create(...)`: recria cada item com os novos dados;
- `super().update(...)`: atualiza os demais campos da compra.

**Testando o endpoint no `ThunderClient`**

  - use o método `PUT`, para atualizar a compra de forma completa;
  - use o método `PATCH`, para atualizar a compra de forma parcial.
    - Experimente mudar apenas o usuário;
    - Experimente mudar apenas a quantidade de um item da compra;
    - Experimente mudar o livro de um item da compra;

**Finalize com um commit**

```
feat: criação de um endpoint para atualizar compras
```

---


# 28b. Criação de um serializador específico para a listagem de compras

Como fizemos com o `Livro`, vamos criar um serializador específico para a listagem de compras, que vai mostrar apenas os campos necessários. Com isso, a listagem de compras ficará mais enxuta.

- No arquivo `serializers/compra.py`, crie um novo serializador chamado `CompraListSerializer`:

```python
...
class CompraListSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    itens = ItensCompraListSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')
...
```

> O serializer `CompraListSerializer` é um serializer específico para a listagem de compras. Ele mostra apenas os campos necessários.

Vamos criar também um serializador específico para os itens da compra:

```python
...
class ItensCompraListSerializer(ModelSerializer):
    livro = CharField(source='livro.titulo', read_only=True)

    class Meta:
        model = ItensCompra
        fields = ('quantidade', 'livro')
        depth = 1
...
```

Temos que incluir o novo serializer no arquivo `__init__.py` dos `serializers`:

```python
...
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, # novo
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, # novo
    ItensCompraSerializer,
)
...
```

- No `viewset` de `Compra`, vamos alterar o `serializer_class` para usar o novo serializer:

```python
...
from .serializers import CompraCreateUpdateSerializer, CompraListSerializer, CompraSerializer
...
class CompraViewSet(ModelViewSet):
...
    def get_serializer_class(self):
        if self.action == 'list':
            return CompraListSerializer
        if self.action in ('create', 'update', 'partial_update'):
            return CompraCreateUpdateSerializer
        return CompraSerializer
...
```

- Teste o endpoint no navegador.
- Faça o _commit_ com a mensagem:

```
feat: criação de um serializador específico para a listagem de compras
```

---


# 29. Criação de uma compra a partir do usuário autenticado

Nesta aula, vamos aprimorar a criação de uma *compra* na nossa API. Em vez de enviar o campo `usuario` no corpo da requisição, vamos configurar o *serializer* para usar automaticamente o usuário que está autenticado no sistema. Isso torna a API mais segura e prática para o consumidor.

**Ajustes no serializer**

Abra o arquivo `serializers/compra.py` e adicione as seguintes importações:

```python
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,  # novo
    HiddenField,         # novo
    ModelSerializer,
    SerializerMethodField,
)
```

Agora, no `CompraCreateUpdateSerializer`, substitua o campo usuario para que ele seja preenchido automaticamente com o usuário autenticado:

```python
class CompraCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')
```

> O campo `usuario` agora é um `HiddenField`, ou seja, não aparece nem na requisição nem na resposta.

> Com `CurrentUserDefault()`, o DRF preenche automaticamente com o usuário logado no momento da requisição.

**Teste no Thunder Client**

Faça um teste enviando uma requisição `POST` para o endpoint `/compras/`, com o seguinte corpo:

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

> Observe que **não precisamos mais informar o usuário**, pois ele será automaticamente associado à compra com base no token de autenticação.

> Esse comportamento só funciona corretamente se a requisição estiver autenticada (via token ou sessão).

**Commit**

- Faça o _commit_ com a mensagem:

```
feat: criação de uma compra a partir do usuário autenticado
```

---


# 30. Visualização de compras com base no perfil do usuário

Atualmente, qualquer usuário pode visualizar todas as compras cadastradas na API, o que não é o comportamento desejado. Vamos ajustar isso para que:

- Usuários normais vejam apenas as suas próprias compras.
- Administradores (superusuários ou membros do grupo *administradores*) vejam todas as compras.

**Atualizando o ViewSet**

Abra o arquivo `views/compra.py` e localize o `CompraViewSet`. Vamos sobrescrever o método `get_queryset`:

```python
from rest_framework.viewsets import ModelViewSet
from core.models import Compra
from core.serializers.compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer,
    CompraSerializer,
)

class CompraViewSet(ModelViewSet):
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name='administradores'):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
...
```

**Explicação do código**

- O método `get_queryset` é chamado sempre que o DRF precisa buscar objetos no banco de dados.
- Usamos `self.request.user` para acessar o usuário autenticado.
- Se o usuário for um superusuário ou pertencer ao grupo `administradores`, ele verá todas as compras.
- Caso contrário, retornamos apenas as compras associadas ao próprio usuário.

> Com isso, garantimos uma separação adequada de permissões entre usuários comuns e administradores.

**Testando a funcionalidade**

1. Faça login com um usuário normal.
2. Acesse o endpoint `/compras/` e confirme que apenas as compras feitas por esse usuário estão visíveis.
3. Agora autentique-se com um administrador (superusuário ou membro do grupo `administradores`).
4. Verifique se todas as compras aparecem.

**Commit**

- Faça o _commit_ com a mensagem:

```
feat: filtrando apenas as compras do usuário autenticado
```

---


# 31. Validação dos campos no Serializer

**Objetivo da aula**
- Entender a importância da validação de dados no backend.
- Aprender a impedir que dados inválidos (como itens com quantidade zero) sejam salvos no banco.

---

**Revisão rápida**
- **Serializer:** Ferramenta do Django REST Framework que transforma objetos Python em JSON e vice-versa.
- **Validação:** Processo de garantir que os dados recebidos pelo serializer atendam às regras do negócio antes de salvar no banco.

---

**Fluxo de Validação no DRF**

- Cliente envia dados (POST/PUT).
- Serializer recebe os dados (`data=request.data`).
- Chamado `is_valid()` → começa a validação.
   - Verificação de tipos (int, string, email, date, etc.).
   - Execução dos validadores (`validators=[]`).
   - Métodos `validate_<campo>` (ex.: `validate_quantidade`).
   - Método `validate(self, attrs)` para regras entre campos.
- Se inválido → retorna **400 Bad Request** com erros em JSON.
- Se válido → `serializer.save()` grava no banco.

---

**Não permitindo itens com quantidade zero**

Nesse momento, é possível criar uma compra com um item com quantidade zero. Vamos validar isso.

- No `serializers/compra.py`, vamos alterar o serializer `ItensCompraCreateUpdateSerializer` para validar a quantidade do item da compra:

```python
...
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError, # novo
)

class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')

    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError('A quantidade deve ser maior do que zero.')
        return quantidade
...
```

> A função `validate_<nome_do_campo>` é chamada quando um campo é validado. Nesse caso, ela está verificando se a quantidade do item da compra (`quantidade`) é maior do que zero.

> Se a quantidade for menor ou igual a zero, é lançada uma exceção `ValidationError`.

**Não permitindo quantidade de itens maior do que a quantidade em estoque**

Nesse momento, é possível criar uma compra com uma quantidade de itens maior do que a quantidade em estoque. Vamos validar isso.

- No `serializers/compra.py`, vamos alterar o serializer `ItensCompraCreateUpdateSerializer` para validar a quantidade de itens em estoque, de forma a não permitir que a quantidade de itens solicitada seja maior do que a quantidade em estoque:

```python
...
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError, # novo
)
...
    def validate(self, item):
        if item['quantidade'] > item['livro'].quantidade:
            raise ValidationError('Quantidade de itens maior do que a quantidade em estoque.')
        return item
...
```
> A função `validate` permite adicionar validações de campo que dependem de múltiplos valores ao mesmo tempo. Nesse caso, ela está verificando se a quantidade solicitada do item (`item['quantidade']`) não excede a quantidade disponível em estoque (`item['livro'].quantidade`).

- Para testar, tente criar uma compra com um item com a quantidade maior do que a quantidade em estoque daquele item. Você verá que a compra não é criada e é exibida uma mensagem de erro.
- Faça o _commit_ com a mensagem:

```
feat: validando a quantidade de itens na compra
```

**Formatando dados antes de salvar**

Podemos usar as funções de validação para formatar os dados antes de salvar. Por exemplo, podemos gravar o e-mail da Editora em minúsculas.

- No `serializers/editora.py`, vamos alterar o serializer `EditoraSerializer` para formatar o e-mail da Editora em minúsculas:

```python
...
    def validate_email(self, email):
        return email.lower()
...
```

> A função `validate_<nome_do_campo>` é chamada quando um campo é validado. Nesse caso, ela está formatando o e-mail da Editora em minúsculas.


- Para testar, altere o e-mail de uma Editora para maiúsculas e veja que o e-mail foi gravado em minúsculas.
- Faça o _commit_ com a mensagem:
```
feat: validando e formatando dados antes de salvar
```

---


# 32. Gravação do preço do livro no item da compra

Até agora, o preço do item da compra era calculado dinamicamente a partir do livro associado. Isso gera um problema: se o preço do livro mudar, o histórico das compras anteriores também mudaria, o que não é desejado.

**Objetivo desta aula:** manter registrado no banco o preço do livro **no momento da compra**, garantindo que o histórico seja preservado.

**Incluindo o campo `preco` em `ItensCompra`**

- No arquivo `models/compra.py`, adicione o campo `preco`:

```python
...
class ItensCompra(models.Model):
...
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
```

- Execute as migrações.
- Se você já estiver utilizando um banco publicado (por exemplo, no Render), **não esqueça de rodar as migrações lá também**.

**Gravando o preço do livro na criação da compra**

- No `serializers/compra.py`, altere o método `create` do `CompraCreateUpdateSerializer` para registrar o preço do livro:

```python
...
    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            item['preco'] = item['livro'].preco # preço do livro no momento da compra
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra
...
```

> O método `create` é chamado quando uma nova compra é criada. Ele recebe os dados validados e cria a compra e os itens da compra.

**Calculando o total do item de compra baseado no preço do livro**

- No `ItensCompraSerializer`, atualize a função `get_total` para usar o preço gravado no item, e não mais o preço atual do livro:

```python
    def get_total(self, instance):
        return instance.quantidade * instance.preco
```

**Calculando o total da compra com base no preço do item**

- No arquivo `models/compra.py`, altere a propriedade `total` da model `Compra`:

```python
...
    @property
    def total(self):
        return sum(item.preco * item.quantidade for item in self.itens.all())
...
```

Agora o **total da compra** considera o preço registrado no item, e não o preço atual do livro.

**Inclua o `preco` nos campos `fields` dos serializers**

```python
class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'preco')  # mudou
```

```python
class ItensCompraListSerializer(ModelSerializer):
    livro = CharField(source='livro.titulo', read_only=True)

    class Meta:
        model = ItensCompra
        fields = ('quantidade', 'preco', 'livro')  # mudou
        depth = 1
```

```python
class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'preco', 'total')  # mudou
...
```

**Testando**

- Para testar, crie uma nova compra e verifique que o preço do livro foi gravado no item da compra.

**Gravando o preço do livro na atualização do item da compra**

No mesmo serializer (`CompraCreateUpdateSerializer`), ajuste o método `update`:

```python
...
    def update(self, compra, validated_data):
        itens = validated_data.pop('itens')
        if itens:
            compra.itens.all().delete()
            for item in itens:
                item['preco'] = item['livro'].preco  # grava o preço histórico
                ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return super().update(compra, validated_data)
...
```

**Testando**

- Crie uma nova compra via API (POST `/compras/`).
- Confira no banco (ou no endpoint de listagem) que o preço foi gravado em `ItensCompra`.
- Atualize o preço de um livro.
- Consulte a compra anterior: o preço gravado não muda.

---

**Commit**

```
feat: Gravação do preço do livro no item da compra
```

---

# 33. Registro da data da compra

Atualmente, não existe nenhum registro da data da compra. Vamos incluir esse campo para que a data seja definida automaticamente no momento da criação da compra.

No arquivo `models/compra.py`, adicione o campo `data` na entidade **Compra**:

```python
...
class Compra(models.Model):
    ...
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    data = models.DateTimeField(auto_now_add=True)  # campo novo
```

> O campo data é do tipo `DateTimeField`, que armazena tanto a data quanto a hora da compra.

> O parâmetro `auto_now_add=True` faz com que o campo seja preenchido automaticamente com a data e hora atuais no momento em que a compra é criada.

**Migração**

Agora, execute as migrações.

Durante a criação da migration, será exibido um erro informando que o campo data não pode ser nulo.

Escolha a **opção 1**, que preenche automaticamente o campo com a data atual (`timezone.now`).

Depois, aplique as migrações também no banco publicado, caso você esteja utilizando.

**Modificando o serializer de compra para mostrar a data da compra**

Para que a data apareça no endpoint, vamos incluir esse campo no serializer de Compra.

No arquivo `serializers/compra.py`, modifique o código da seguinte forma:

```python
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    DateTimeField, # novo
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)
...
class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    data = DateTimeField(read_only=True) # novo campo
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'data', 'itens') # modificado
...
```

**Testando**

- Crie uma nova compra.
- Verifique se a data foi gravada corretamente no banco de dados.
- Confira se o campo aparece na resposta do endpoint.

**Incluindo a data no Admin do Django**

No arquivo `admin.py` do app `core`, modifique o código da model `Compra`:

```python
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    @admin.display(description="Total")
    def total_formatado(self, obj):
        """Exibe R$ 123,45 em vez de 123.45."""
        return f"R$ {obj.total:.2f}"

    list_display = ('usuario', 'status', 'total_formatado', 'data')  # mostra na listagem
    ordering = ('usuario', 'status', 'data')  # ordena por esses campos
    search_fields = ('usuario__email', 'status')  # campos pesquisáveis
    list_filter = ('status', 'data')  # filtros laterais
    list_per_page = 10
    inlines = [ItensCompraInline]
    readonly_fields = ('data', 'total_formatado',)  # campos somente leitura
...
```

**Exercício**

- Inclua um campo `data_atualizacao`, que armazena a data da última atualização da compra.
  - Dicas:
    - use o parâmetro `auto_now=True`.
    - inclua o campo no serializer de `Compra`.
    - inclua o campo no `list_display` e `readonly_fields` do Admin.
    - modifique o nome do campo `data` para `data_criacao`.

**Commit**

- Faça o _commit_ com a mensagem:
```
feat: registrando a data da compra
```

---

# 34. Inclusão do tipo de pagamento à entidade de Compra

**Contexto**

Em qualquer sistema de e-commerce ou livraria online, é essencial registrar **como cada compra foi paga**.
Além de organizar a operação (financeiro, emissão de notas, devoluções), também permite gerar **estatísticas úteis**:

- Quantas compras foram feitas via cartão de crédito?
- Quantos clientes preferem PIX ou boleto?
- Qual é a forma de pagamento mais usada?

**Implementação no Model**

No arquivo `models/compra.py`, adicione o campo `tipo_pagamento`:

```python
...
class Compra(models.Model):
    class TipoPagamento(models.IntegerChoices):
        CARTAO_CREDITO = 1, 'Cartão de Crédito'
        CARTAO_DEBITO = 2, 'Cartão de Débito'
        PIX = 3, 'PIX'
        BOLETO = 4, 'Boleto'
        TRANSFERENCIA_BANCARIA = 5, 'Transferência Bancária'
        DINHEIRO = 6, 'Dinheiro'
        OUTRO = 7, 'Outro'
...
    tipo_pagamento = models.IntegerField(
        choices=TipoPagamento.choices,
        default=TipoPagamento.CARTAO_CREDITO
    )
...
```

**O que está acontecendo aqui?**

- `IntegerChoices` cria uma lista de opções amigáveis para o campo.
- O banco armazena apenas o **número**, mas a aplicação mostra o valor legível.
- Definimos o **padrão** como cartão de crédito.

Execute as migrações.

**Exibição no Serializer**

No arquivo `serializers/compra.py`, inclua o novo campo:

```python
...
class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    data = DateTimeField(read_only=True)
    tipo_pagamento = CharField(source='get_tipo_pagamento_display', read_only=True) # novo campo
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'data', 'tipo_pagamento', 'itens') # modificado
...
```

> O campo `tipo_pagamento` é um campo do tipo `CharField`, que mostra o tipo de pagamento da compra. O parâmetro `source` indica o método que retorna o tipo de pagamento.

> O método `get_tipo_pagamento_display` é um método especial do model que retorna o valor legível do campo `tipo_pagamento`.

> O campo `tipo_pagamento` foi incluído no atributo `fields` do serializer.

**Testando**

- Crie uma nova compra e verifique que o **tipo de pagamento padrão** foi gravado.
- No **Django Shell**, rode:

```python
compra = Compra.objects.first()
print(compra.tipo_pagamento)              # mostra o valor interno (ex: 1)
print(compra.get_tipo_pagamento_display()) # mostra o valor legível (ex: 'Cartão de Crédito')
```

**Atividade Prática**

- **Adicione um novo tipo de pagamento** chamado “Cheque” (por exemplo).
- Faça as migrações.
- Crie uma compra no Django Admin usando “Cheque”.
- Acesse o endpoint da API e confirme que o campo aparece corretamente.

**Commit**

- Faça o _commit_ com a mensagem:
```
feat: adicionando tipo de pagamento à entidade de Compra
```

---


# 35a. Ações personalizadas: Introdução e alteração do preço de um livro

**Objetivo**

Entender o conceito de **ações personalizadas (actions)** no Django REST Framework e aprender a criar uma na prática.

---

**O que são ações personalizadas?**

No DRF, os ViewSets já oferecem automaticamente as ações padrão:

- `list`: listar objetos
- `retrieve`: buscar objeto específico
- `create`: criar novo objeto
- `update` / `partial_update`: atualizar objeto
- `destroy`: excluir objeto

Essas ações cobrem o básico do CRUD.
Mas muitas vezes precisamos de **funcionalidades extras**, que não se encaixam nesses métodos.
É aí que entram as **ações personalizadas**: endpoints adicionais que podemos criar em um `ViewSet`, usando o decorador `@action`.

Exemplos práticos:

- Alterar o preço de um livro.
- Marcar uma compra como "paga".
- Gerar um relatório.

---

**Alterando o preço de um livro**

Nosso primeiro exemplo será uma ação para alterar o **preço de um livro específico**, passando o novo preço no corpo da requisição e o ID do livro na URL.

**Criando um serializer específico para a ação**

É uma boa prática usar um serializer específico na `action` `ajustar_preco`. Isso traria várias vantagens, como validação mais robusta dos dados de entrada e organização do código. Ao usar um serializer dedicado, você garante que a lógica de validação e conversão dos dados está separada da view, seguindo o princípio de responsabilidade única e tornando o código mais limpo e reutilizável.

Vamos incluir um novo serializer chamado `AjustarPrecoSerializer` no arquivo `serializers/livro.py`:

```python
from rest_framework.serializers import (
    DecimalField,
    ModelSerializer,
    Serializer,
    SlugRelatedField,
    ValidationError,
)
...
class LivroAlterarPrecoSerializer(Serializer):
    preco = DecimalField(max_digits=7, decimal_places=2)

    def validate_preco(self, preco):
        '''Valida se o preço é um valor positivo.'''
        if preco <= 0:
            raise ValidationError('O preço deve ser um valor positivo.')
        return preco
...
```

- Inclua o novo serializer no arquivo `__init__.py` dos `serializers`:

```python
...
from .livro import (
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
...
```

---

**Criando uma ação personalizada para alterar o preço de um livro**

Vamos agora criar uma ação personalizada para alterar o preço de um livro. Essa ação será aplicada a um **recurso específico**, ou seja, a um livro específico.

- No `views/livro.py`, vamos criar um método `alterar_preco` na view `LivroViewSet`:

```python
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import (
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
...
    @action(detail=True, methods=['patch'])
    def alterar_preco(self, request, pk=None):
        livro = self.get_object()

        serializer = LivroAlterarPrecoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        livro.preco = serializer.validated_data['preco']
        livro.save()

        return Response(
            {'detail': f'Preço do livro "{livro.titulo}" atualizado para {livro.preco}.'}, status=status.HTTP_200_OK
        )
```

> O decorador `@action` cria um endpoint para a ação `alterar_preco`, no formato `api/livros/{id}/alterar_preco`.

> O método `alterar_preco` é um método de ação que altera o preço de um livro. Ele recebe o livro que está sendo alterado.

> O método `get_object()` é um método que recupera um objeto com base no `pk` fornecido.

> O método `LivroAlterarPrecoSerializer` é um serializer específico para a ação `alterar_preco`. Ele valida o preço fornecido.

> O método `is_valid(raise_exception=True)` é um método que valida os dados fornecidos. Se os dados não forem válidos, ele lança uma exceção.

> O método `validated_data` é um atributo que contém os dados validados.

> O método `Response` retorna uma resposta HTTP.

> O status `HTTP_200_OK` indica que a requisição foi bem sucedida.

---

**Testando a action**

- No Swagger, localize o endpoint:
**POST /livros/{id}/alterar_preco/**
- Envie o corpo da requisição:

```json
{
  "preco": 59.90
}
```

- Verifique se o livro teve seu preço alterado corretamente.

---

**Documentando a action no Swagger**

- No `views/livro.py`, adicione a documentação para o Swagger:

```python
from drf_spectacular.utils import extend_schema
...
    @extend_schema(
        request=LivroAlterarPrecoSerializer,
        responses={200: None},
        description="Altera o preço de um livro específico.",
        summary="Alterar preço do livro",
    )
    @action(detail=True, methods=['patch'])
    def alterar_preco(self, request, pk=None):
        ...
```

> O decorador `@extend_schema` é usado para documentar a action no Swagger.

- Teste novamente no Swagger e veja que a documentação foi atualizada.
**Commit**

- Faça o _commit_ com a mensagem:

```
feat: alterando o preço de um livro
```

---
# 35b. Ações personalizadas em coleções e relatório de vendas do mês

**Objetivo**

Aprender a criar ações personalizadas que atuam sobre o conjunto inteiro de objetos, e não apenas em um item específico.

---

**Quando usar** `detail=False`?

- `detail=True` cria endpoints para um **item específico**, como:
    ```
    /api/livros/{id}/alterar_preco/
    ```
- `detail=False` cria endpoints para o **conjunto de registros**, como:
    ```
    /api/livros/mais_vendidos/
    /api/compras/relatorio_vendas_mes/
    ```

Essas ações são ideais para consultas, estatísticas e relatórios.

---

**Exemplo: Relatório de vendas do mês**

No arquivo `views/compra.py`, dentro da `CompraViewSet`, crie o relatório:

```python
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class CompraViewSet(ModelViewSet):
...

    @action(detail=False, methods=['get'])
    def relatorio_vendas_mes(self, request):
        agora = timezone.now()
        inicio_mes = agora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        compras = Compra.objects.filter(
                status=Compra.StatusCompra.FINALIZADO,
                data__gte=inicio_mes
        )

        total_vendas = sum(compra.total for compra in compras)
        quantidade_vendas = compras.count()

        return Response(
            {
                'status': 'Relatório de vendas deste mês',
                'total_vendas': total_vendas,
                'quantidade_vendas': quantidade_vendas,
            },
            status=status.HTTP_200_OK,
        )
```

---

**Explicação**

- `@action(detail=False, methods=['get'])`: cria o endpoint `/api/compras/relatorio_vendas_mes/`.
- `timezone.now()`: captura a data e hora atuais.
- `inicio_mes`: marca o primeiro dia do mês(para filtrar compras do mês atual).
- `Compra.objects.filter(...)`: filtra compras finalizadas no mês atual.
- `sum(compra.total for compra in compras)`: soma os valores totais.

---

**Testando**

No Swagger, acesse:
```
GET /compras/relatorio_vendas_mes/
```
A resposta será algo como:

```json
{
    "status": "Relatório de vendas deste mês",
    "total_vendas": 1249.80,
    "quantidade_vendas": 8
}
```
**Documentando a action no Swagger**

- No `views/compra.py`, adicione a documentação para o Swagger:

```python
from drf_spectacular.utils import extend_schema
...
    @extend_schema(
        request=None,
        responses={200: None},
        description="Gera um relatório de vendas do mês atual.",
        summary="Relatório de vendas do mês",
    )
    @action(detail=False, methods=['get'])
    def relatorio_vendas_mes(self, request):
        ...
```

---

**Commit**

```shell
feat: adicionando relatório de vendas mensal em compras
```

---


# 35c.  Ações personalizadas: finalizando a compra e atualizando o estoque

**Objetivo**

Aprender a criar uma ação personalizada que realiza ajustes em vários registros (compra e itens de estoque), garantindo integridade transacional e validação efetiva durante o processo de finalização de compra.

---

**Contexto do problema**

Quando o usuário faz uma compra, ela inicia no status `CARRINHO` e ainda não impacta o estoque dos livros. Ao finalizar a compra, o status passa para `FINALIZADO` e o sistema precisa:

- **Diminuir o estoque dos livros** conforme a quantidade comprada.
- Garantir que não seja possível finalizar se o **estoque for insuficiente**.
- Validar o status da compra para **evitar duplicidade**.

---

**Implementação do endpoint de finalização**

No arquivo `views/compra.py`, crie a ação personalizada `finalizar` dentro do `CompraViewSet`:

```python
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class CompraViewSet(ModelViewSet):
    ...
    @extend_schema(
        request=None,
        responses={200: None, 400: None},
        description="Finaliza a compra, atualizando o estoque dos livros.",
        summary="Finalizar compra",
    )
    @action(detail=True, methods=["post"])
    def finalizar(self, request, pk=None):
        compra = self.get_object()

        # Verifica se a compra já foi finalizada
        if compra.status == Compra.StatusCompra.FINALIZADO:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'status': 'Compra já finalizada'}
            )

        # Garante integridade transacional durante a finalização
        with transaction.atomic():
            for item in compra.itens.all():

                # Valida se o estoque é suficiente para cada livro
                if item.quantidade > item.livro.quantidade:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={
                            'status': 'Quantidade insuficiente',
                            'livro': item.livro.titulo,
                            'quantidade_disponivel': item.livro.quantidade,
                        }
                    )

                # Atualiza o estoque dos livros
                item.livro.quantidade -= item.quantidade
                item.livro.save()

            # Finaliza a compra: atualiza status
            compra.status = Compra.StatusCompra.FINALIZADO
            compra.save()

        return Response(status=status.HTTP_200_OK, data={'status': 'Compra finalizada'})
```

- O decorador `@action` gera o endpoint `api/compras/{id}/finalizar` para esse recurso.
- O bloco `with transaction.atomic()` garante que toda operação será executada com consistência: se algo falhar, nada será salvo.
- O método verifica o status, valida o estoque e realiza a atualização do status e estoque dos livros.

---
- Para testar:
  - Tente finalizar uma compra que não foi finalizada.
  - Tente finalizar uma compra que já foi finalizada.
  - Tente finalizar uma compra com quantidade de itens maior do que a quantidade em estoque.
  - Tente finalizar uma compra com quantidade de itens menor ou igual à quantidade em estoque.
---

**Commit**

```shell
feat: finalizando a compra e atualizando a quantidade de itens em estoque
```

---


# 35d.  Ações personalizadas: listando livros com mais de 10 cópias vendidas

Vamos criar uma ação personalizada na API para listar os livros que venderam mais de 10 unidades. Essa funcionalidade será implementada como um endpoint de coleção, aplicável a todos os livros cadastrados.

**Ajustando a Model**

Primeiro, inclua o parâmetro `related_name` no campo `livro` da entidade `ItensCompra` em `models/compra.py`. Isso facilitará consultas reversas e deixará o código mais expressivo.

```python
class ItensCompra(models.Model):
    ...
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='itens_compra')
    ...
```

Após o ajuste, execute as migrações:

```
pdm migrate
```

**Criando o Serializer**

Para garantir padronização e flexibilidade de retorno, utilize um serializer específico na resposta:

```python
class LivroMaisVendidoSerializer(ModelSerializer):
    total_vendidos = IntegerField()

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'total_vendidos']
```

**Implementando a Ação Personalizada**

No arquivo `views/livro.py`, inclua o método `mais_vendidos` na view `LivroViewSet`:

```python
from django.db.models import Q, Sum
...
from core.serializers import LivroMaisVendidoSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer  # Seu serializer padrão

    @action(detail=False, methods=['get'])
    def mais_vendidos(self, request):
        livros = Livro.objects.annotate(
            total_vendidos=Sum(
                'itens_compra__quantidade',
                filter=Q(itens_compra__compra__status=Compra.StatusCompra.FINALIZADO)
            )
        ).filter(total_vendidos__gt=10).order_by('-total_vendidos')

        serializer = LivroMaisVendidoSerializer(livros, many=True)

        if not serializer.data:
            return Response(
                {"detail": "Nenhum livro excedeu 10 vendas."},
                status=status.HTTP_200_OK
            )

        return Response(serializer.data, status=status.HTTP_200_OK)
```

> O decorador `@action(detail=False)` define um endpoint de coleção no formato `/api/livros/mais_vendidos/`.

> O método `annotate` soma o total vendido para cada livro por meio do relacionamento reverso (`itens_compra__quantidade`).

> O `filter` dentro do `Sum` assegura que apenas itens de compras finalizadas sejam considerados.

> O `filter(total_vendidos__gt=10)` retorna apenas livros com mais de 10 unidades vendidas.

> O método Q permite aplicar filtros complexos, garantindo que apenas itens de compras finalizadas sejam considerados.

> Os resultados são filtrados para retornar apenas livros que tenham mais de 10 unidades vendidas e já vêm ordenados do maior para o menor total.

> O serializer facilita a manutenção e a extensão da resposta.

**Documentação Swagger/OpenAPI com drf-spectacular**

Se estiver utilizando `drf-spectacular`, acrescente a documentação da action com o decorador @extend_schema:

```python
class LivroViewSet(ModelViewSet):
    ...

    @extend_schema(
        summary="Lista os livros mais vendidos",
        description="Retorna os livros que venderam mais de 10 unidades.",
        responses={
            200: LivroMaisVendidoSerializer(many=True)
        },
    )
    @action(detail=False, methods=['get'])
    def mais_vendidos(self, request):
        ...
```

Assim, o endpoint `/api/livros/mais_vendidos/` será exibido automaticamente na documentação Swagger com os campos `id`, `título` e `total_vendidos`, e poderá ser testado por qualquer consumidor da API.

**Exemplo de resposta**

Ao realizar uma requisição GET para `/api/livros/mais_vendidos/`, o retorno será deste formato:

```json
[
  {
    "id": 1,
    "titulo": "O Código Limpo",
    "total_vendidos": 33
  },
  {
    "id": 2,
    "titulo": "O Codificador Limpo",
    "total_vendidos": 25
  }
]
```

Se nenhum livro exceder 10 vendas, o resultado será:

```json
{
  "detail": "Nenhum livro excedeu 10 vendas."
}
```

**Commit**

Faça o commit com a mensagem:

```
feat: listando livros com mais de 10 cópias vendidas
```

---


# 35e. Ações personalizadas: ajustando o estoque de um livro

**Objetivo:** criar uma action personalizada que permita ajustar (aumentar ou diminuir) o estoque de um livro de forma segura, impedindo que o valor fique negativo.

**Serializer específico**

Adicione em `serializers/livro.py`:

```python
class LivroAjustarEstoqueSerializer(Serializer):
    quantidade = serializers.IntegerField()

    def validate_quantidade(self, value):
        livro = self.context.get('livro')
        if livro:
            nova_quantidade = livro.quantidade + value
            if nova_quantidade < 0:
                raise ValidationError('A quantidade em estoque não pode ser negativa.')
        return value
```

Atualize `serializers/__init__.py`:

```python
from .livro import (
    LivroAjustarEstoqueSerializer,
...
)
```

**Action na ViewSet**

Em `views/livro.py`, adicione a action ao `LivroViewSet`:

```python
...
from drf_spectacular.utils import OpenApiResponse, extend_schema
from .serializers import LivroAjustarEstoqueSerializer

class LivroViewSet(ModelViewSet):
    ...
    @extend_schema(
        summary="Ajusta o estoque de um livro",
        description="Aumenta ou diminui o estoque; impede resultado negativo.",
        request=LivroAjustarEstoqueSerializer,
        responses={
            200: OpenApiResponse(
                response=None,
                description="Estoque ajustado com sucesso.",
                examples=[
                    {
                        "status": "Quantidade ajustada com sucesso",
                        "novo_estoque": 30
                    }
                ]
            ),
            400: OpenApiResponse(
                description="Erro de validação",
                examples=[
                    {"quantidade": "A quantidade em estoque não pode ser negativa."}
                ]
            ),
        },
        )
    @action(detail=True, methods=['post'])
    def ajustar_estoque(self, request, pk=None):
        livro = self.get_object()

        serializer = LivroAjustarEstoqueSerializer(data=request.data, context={'livro': livro})
        serializer.is_valid(raise_exception=True)

        quantidade_ajuste = serializer.validated_data['quantidade']
        livro.quantidade += quantidade_ajuste
        livro.save()

        return Response(
            {'status': 'Quantidade ajustada com sucesso', 'novo_estoque': livro.quantidade},
            status=status.HTTP_200_OK
        )
```

**Testando o Endpoint**

Para ajustar o estoque, envie uma requisição POST para `/api/livros/{id}/ajustar_estoque/` com um JSON contendo o campo `quantidade`.

Exemplo de entrada:

```json
{"quantidade": 5}
```

Exemplo de resposta bem-sucedida:

```json
{
  "status": "Quantidade ajustada com sucesso",
  "novo_estoque": 30
}
```

Exemplo de resposta de erro:

```json
{
  "quantidade": [
    "A quantidade em estoque não pode ser negativa."
  ]
}
```

**Teste e Validação**

- Tente ajustar o estoque com valores positivos e negativos para diferentes livros.
- Teste sem fornecer o campo quantidade para validar a mensagem de erro.
- Verifique que o endpoint e as respostas aparecem documentados automaticamente no Swagger/Redoc da sua API.

**Commit**

Faça o commit com a mensagem:

```
feat: ajustando o estoque de um livro
```

---


# 36. Utilização de filtros para listagem de recursos

Até agora, nossa API lista todos os livros, sem possibilidade de filtragem. Nesta aula, vamos implementar filtros para facilitar consultas específicas, como por categoria, editora e autores.

**Preparando o Filter Backend no ViewSet**

O pacote `django-filter` já está instalado no projeto, o que permite criar filtros dinâmicos e declarativos.

No arquivo `views/livro.py`, vamos configurar o `LivroViewSet` para usar filtros:

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria__descricao', 'editora__nome']  # Campos para filtragem
```

> `filter_backends` define o backend que aplica os filtros na query.

> `filterset_fields` indica quais campos do model (ou relacionamentos) estarão disponíveis para filtro.

> Usamos a notação de dupla underscore (`__`) para acessar campos de modelos relacionados.

**Testando a Filtragem**

Com essa configuração, o endpoint GET `/api/livros/` aceita parâmetros de consulta, como:

- Filtrar por categoria:
    - `GET /api/livros/?categoria__descricao=Python`

- Filtrar por editora:
    - `GET /api/livros/?editora__nome=Novatec`

- Combinado:
    - `GET /api/livros/?categoria__descricao=Python&editora__nome=Novatec`

No **Swagger**, acessando o endpoint `livros/`, clique em **Try it out** e verá campos para filtrar por `categoria__descricao` e `editora__nome`.

Também pode testar via chamadas HTTP diretas com ferramentas como **ThunderClient** ou **curl**.

**Acrescentando Filtros em Outros Models**

De modo semelhante, acrescente filtros nos viewsets dos models Autor, Categoria, Editora e Compra.


**Commit**

Faça o _commit_ com a mensagem:

```
feat: adicionando filtros para listagem de recursos
```

---

# 37. Utilização de busca textual em campos de texto

A busca textual permite pesquisar dentro dos valores de texto dos campos de um banco de dados, facilitando encontrar registros que contenham determinado texto. Essa funcionalidade é aplicável a campos como `CharField` e `TextField`.

**Configurando a Busca Textual no LivroViewSet**

No arquivo `views/livro.py`, vamos alterar o `LivroViewSet` para incluir o backend `SearchFilter` e definir quais campos permitirão a busca textual:

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
...

class LivroViewSet(viewsets.ModelViewSet):
...
    filter_backends = [DjangoFilterBackend, SearchFilter]  # Adicionando SearchFilter
    filterset_fields = ['categoria__descricao', 'editora__nome']  # Campos para filtro
    search_fields = ['titulo']  # Campos para busca textual
```

> `filter_backends` inclui agora tanto `DjangoFilterBackend` para filtros específicos por campos, quanto `SearchFilter` para busca textual.

> `search_fields` define os campos que terão busca textual ativada, neste caso, o campo `titulo` do livro.

**Utilizando a Busca Textual**

Com esta configuração, para buscar livros que contenham uma palavra no título, basta fazer uma requisição `GET` para o endpoint com o parâmetro `search`.

Exemplo para buscar livros com a palavra "python" no título:

```text
GET /api/livros/?search=python
```

- No Swagger, o campo `search` aparecerá automaticamente para preenchimento ao testar o endpoint de listagem de livros.

- Combine filtros específicos (com `filterset_fields`) e busca textual para refinar resultados.

**Commit**

Faça commit com a mensagem padrão para recursos novos:

```
feat: adicionando busca textual
```

---

# 38. Utilização de ordenação dos resultados

Toda `viewset` possui um atributo chamado `ordering_fields`, que é uma lista de campos que podem ser utilizados para ordenar os resultados. Além disso, o atributo `ordering` é utilizado para definir o campo padrão de ordenação. Se você ainda quiser permitir a ordenação reversa, basta adicionar um sinal de menos (-) na frente do campo.

Independentemente dessa ordenação padrão, o usuário pode ordenar os resultados de acordo com o campo desejado, passando o nome do campo como parâmetro na URL.

A ordenação serve para adicionar a funcionalidade de ordenar os resultados de uma consulta.

- Para utilizar a ordenação nos livros, devemos promover três alterações em nossa `ViewSet`:
- Novamente alterar o atributo `filter_backends`, adicionando o *Backend* `OrderingFilter` que irá processar a ordenação; e
- Adicionar o atributo `ordering_fields`, contendo os campos que permitirão a ordenação.
- Adicionar o atributo `ordering` com o campo que será utilizado como padrão para ordenação.
- A `LivroViewSet` em `views/livro.py` ficará assim:

```python
...
from rest_framework.filters import SearchFilter, OrderingFilter
...

class LivroViewSet(viewsets.ModelViewSet):
...
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categoria__descricao', 'editora__nome']
    search_fields = ['titulo']
    ordering_fields = ['titulo', 'preco']
    ordering = ['titulo']
...
```

- Para ordenar os livros, basta adicionar o parâmetro `ordering` na URL, com o valor do campo a ser ordenado.
- Se você não coloca o parâmetro `ordering`, a ordenação será feita pelo campo definido no atributo `ordering`, nesse caso, `titulo`:
  - http://127.0.0.1:8000/api/livros/
- Compare com este exemplo, e perceba que a saída é a mesma:
  - http://127.0.0.1:8000/api/livros/?ordering=titulo
- Para mostrar na ordem reversa, basta adicionar um sinal de menos (-) na frente do campo:
  - http://127.0.0.1:8000/api/livros/?ordering=-titulo
- Ou mostrar os livros ordenando pelo preço:
  - http://127.0.0.1:8000/api/livros/?ordering=preco
- Pode-se ainda juntar a ordenação com a busca textual. Por exemplo, para ordenar os livros pelo título e que contenham a palavra `python` no título, a URL ficaria assim:
  - http://127.0.0.1:8000/api/livros/?ordering=titulo&search=python
- Para utilizar os filtros e a ordenação, basta adicionar os parâmetros na URL, com os valores desejados. Por exemplo, para ordenar os livros pelo título de uma determinada categoria e editora, a URL ficaria assim:
  - http://127.0.0.1:8000/api/livros/?categoria__descricao=Python&editora_nome=Novatec&ordering=titulo
- É possível utilizar todos os recursos ao mesmo tempo: múltiplos filtros, busca textual e ordenação.
    - http://127.0.0.1:8000/api/livros/?categoria_descricao=Python&editora_nome=Novatec&ordering=titulo&search=python

Esses são apenas alguns exemplos de como utilizar os filtros, a pesquisa textual e a ordenação. Você pode combinar esses recursos da forma que desejar.

**Acrescentando filtro e ordenação por data**

Vamos ver ainda um último exemplo de como adicionar filtro e ordenação.

- No `views/compra.py`, vamos alterar o atributo `filterset_fields`, na `viewset` de `Compra` para filtrar as compras por `data`.
- Vamos também alterar o atributo `ordering_fields`, na `viewset` de `Compra` para ordenar as compras por `data`.

```python
...
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['usuario__email', 'status', 'data']
    search_fields = ['usuario__email']
    ordering_fields = ['usuario__email', 'status', 'data']
    ordering = ['-data']
...
```

- Para ordenar por data, em ordem descrente:
  - http://127.0.0.1:8000/api/compras/?ordering=-data

**Exercício**

- Acrescente a ordenação nas *models* `Autor`, `Categoria`, `Editora` e `Compra`.
- Faça o _commit_ com a mensagem:
```
feat: adicionando ordenação
```

---

# 39. Inclusão do limite de um carrinho de compras por usuário

Nesse momento, um usuário pode ter vários carrinhos de compras. Vamos limitar a um carrinho de compras por usuário. Faremos isso verificando se o usuário já possui um carrinho de compras. Se ele já tiver, retornaremos o carrinho existente. Caso contrário, criaremos um novo carrinho. Vamos aproveitar e verificar se um livro já foi adicionado ao carrinho. Se ele já foi adicionado, vamos incrementar a quantidade.

Uma vantagem dessa abordagem é que podemos incluir um livro no carrinho simplesmente enviando o `id` do livro e a quantidade. Se o livro já estiver no carrinho, a quantidade será incrementada. Se o livro não estiver no carrinho, ele será adicionado.

- No `serializers/compra.py`, vamos alterar o serializer chamado `CompraCreateUpdateSerializer`:

```python
class CompraCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('usuario', 'itens')

    def create(self, validated_data):
        itens = validated_data.pop('itens')
        usuario = validated_data['usuario']

        compra, criada = Compra.objects.get_or_create(
            usuario=usuario, status=Compra.StatusCompra.CARRINHO, defaults=validated_data
        )

        for item in itens:
            item_existente = compra.itens.filter(livro=item['livro']).first()

            if item_existente:
                item_existente.quantidade += item['quantidade']
                item_existente.preco = item['livro'].preco
                item_existente.save()
            else:
                item['preco'] = item['livro'].preco
                ItensCompra.objects.create(compra=compra, **item)

        return compra

    def update(self, compra, validated_data):
        itens = validated_data.pop('itens', [])
        if itens:
            compra.itens.all().delete()
            for item in itens:
                item['preco'] = item['livro'].preco
                ItensCompra.objects.create(compra=compra, **item)

        return super().update(compra, validated_data)

```

> O método `get_or_create` retorna um objeto `Compra` existente ou cria um novo objeto `Compra` se ele não existir.

> O método `filter` retorna um objeto `ItensCompra` que atenda aos critérios de pesquisa.

> O método `first` retorna o primeiro objeto `ItensCompra` que atenda aos critérios de pesquisa ou `None` se não houver objetos.

---

**40. Inclusão do total da compra no modelo**

Nesta etapa, vamos adicionar um campo *total* ao modelo `Compra`, responsável por armazenar o valor total de cada compra.
Isso traz ganhos de **performance** e **facilidade** nas consultas, permitindo ordenar e filtrar diretamente pelo total no banco de dados.

---

**1. Adicionando o campo total**

No arquivo `models/compra.py`, inclua o campo abaixo:

```python
class Compra(models.Model):
    ...
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ...
```

**2. Calculando o total automaticamente**

Vamos sobrescrever o método `save` para calcular o total antes de salvar a compra:

```python
class Compra(models.Model):
    ...
    def save(self, *args, **kwargs):
        if self.pk:
            self.total = sum(item.preco * item.quantidade for item in self.itens.all())
        super().save(*args, **kwargs)
```

**Explicando o método:**

> `save` é chamado sempre que um objeto é salvo no banco.

> `super().save(*args, **kwargs)` chama o método original da classe pai.

> `self.itens.all()` retorna todos os itens associados à compra.

> `sum(...)` soma o total de cada item (preço × quantidade).

> O `if self.pk` garante que o cálculo só ocorra depois da criação inicial da compra.

**3. Removendo a property antiga**

Como o total agora está armazenado no banco, podemos remover o cálculo dinâmico da `property total`:

```python
class Compra(models.Model):
    ...
    # Remover o trecho abaixo, se existir:
    # @property
    # def total(self):
    #     return sum(item.preco * item.quantidade for item in self.itens.all())
    ...
```

**4. Salvando o total no serializer**

No serializer `CompraCreateUpdateSerializer`, garanta que o método `create` salve a compra após a criação dos itens, para atualizar o campo total:

```python
class CompraCreateUpdateSerializer(ModelSerializer):
    ...
    def create(self, validated_data):
        ...
        compra.save()  # Linha adicionada para atualizar o campo total
        return compra
    ...
```

**5. Executando migraçõe**s

Após essas alterações, execute as migrações para atualizar o banco de dados:

```shell
pdm migrate
```

**6. Atualizando compras existentes**

Para atualizar o campo total das compras já existentes, utilize o shell do Django:

```python
for compra in Compra.objects.all():
    compra.save()
```

Isso recalcula e salva o total de todas as compras já registradas.

**7. Testando o funcionamento**

- Crie uma nova compra.
- Adicione um ou mais livros ao carrinho.
- Altere a quantidade de um dos livros.
- Verifique se o total é atualizado corretamente.

**8. Ordenações e consultas**

Com o campo total armazenado, podemos realizar consultas otimizadas:

**Ordenar pelo total (decrescente):**

```python
compras = Compra.objects.all().order_by('-total')
```

**Filtrar compras com valor mínimo:**

```python
compras = Compra.objects.filter(total__gte=100)
```

**9. Commit**

Por fim, registre a alteração no controle de versão:

```shell
 feat: adicionando o total da compra
```


**Resumo da aula**

Adicionamos o campo `total` ao modelo `Compra`.
O valor total é calculado automaticamente no `save()`.
A property antiga foi removida.
O serializer foi atualizado para garantir o salvamento.
Atualizamos os registros existentes e testamos consultas com base no total.

---


# Exercícios Garagem

O projeto **Garagem** é um projeto de uma garagem de carros. O objetivo é praticar aquilo que foi visto nesse tutorial, no projeto da **Livraria**.

## E1. Crie o projeto Garagem

Seguindo aquilo que você já aprendeu na criação do projeto da `Livraria`, crie um **novo projeto**, a partir do [template](https://github.com/marrcandre/template_django_pdm).

1. Pode chamar o repositório de `garagem`.
2. Nomeie o _commit_ como sendo:

    `feat: Criação do projeto`.

3. Siga [esses passos](#6-inclusão-da-editora-no-projeto-livraria) para criar a API.
   - Você pode utilizar o script de criação da API também, conforme explicado [aqui](#8-criação-da-api-para-livro).
4. Crie as seguintes APIs, **fazendo um _commit_ para cada etapa**:
    -   `Acessorio`:
        -   `descricao` (string, máximo 100 caracteres).
        -   `__str__` (retorna o id e a a descrição).
        -   Exemplos: `Ar condicionado`, `Direção hidráulica`, `Vidros elétricos`, `Travas elétricas`, `Alarme`, `Airbag`, `Freios ABS`.
    -   `Cor`:
        -   `nome` (string, máximo 40 caracteres).
        -   `__str__` (retorna o nome e o id).
        -   Exemplo: `Preto`, `Branco`, `Prata`, `Vermelho`,  `Cinza`, `Grafite`.
    -   `Modelo`:
        -   `nome` (string, máximo 80 caracteres).
        -   `marca`(string, máximo 80 caracteres, não obrigatório).
        -   `categoria` (string, máximo 80 caracteres, não obrigatório).
        -   `__str__` (retorna id, marca (maiúsculas) e nome do modelo (maiúsculas).
        -   Exemplo: `KA`, `FIESTA`, `ECOSPORT`, `RANGER`, `ONIX`, `PRISMA`, `TRACKER`, `S10`, `GOL`, `POLO`, `TAOS`, `AMAROK`, `ARGO`, `TORO`, `UNO`, `CRONOS`, `COMPASS`, `CIVIC`, `HR-V`, `FIT`, `CITY`, `HB20`, `CRETA`, `TUCSON`, `KICKS`, `FRONTIER`, `208`, `3008`, `C3`, `C4`.
5. Crie a API para o `Veiculo` no projeto `Garagem`.
   - Crie o modelo `Veiculo`, com os seguintes atributos:
     -   `ano` (inteiro, permite nulo, default 0).
     -   `preco` (decimal, máximo 7 dígitos, 2 casas decimais, permite nulo, default 0).
     -   `modelo` (chave estrangeira para `Modelo`).
     -   `cor` (chave estrangeira para `Cor`).
     -   `acessorios` (chave estrangeira para `Acessorio`, muitos para muitos).
     -   `__str__` (retorna o id, modelo, cor e ano do carro).
   -  Crie a API REST para o modelo `Veiculo`.

Ao final, o diagrama no arquivo `core.png`, **que é obrigatório**, deve ficar assim:

![Diagrama do projeto Garagem](./diagramas/garagem_1.png)


<!-- ## E2. Crie o modelo Categoria
Vamos incluir o modelo `Categoria` no projeto `Garagem`.
- Crie o modelo `Categoria`, com os seguintes atributos:
    -   `Categoria`:
        -   `descricao` (string, máximo 100 caracteres).
        -   `__str__` (retorna a descrição e o id.
        -   Exemplos: `Sedan`, `Hatch`, `SUV`, `Picape`, `Caminhonete`, `Conversível`, `Esportivo`, `Utilitário`.


-   Crie a API REST para o modelo `Modelo`.
-   Crie a aplicação frontend com Vuejs para consumir a API REST do modelo `Modelo`.
-   Faça um _commit_ para cada etapa.


    -   `Marca`:
        -   `nome` (string, máximo 50 caracteres).
        -   `nacionalidade` (string, máximo 50 caracteres, permite nulo).
        -   `__str__` (retorna o nome **em caixa alta** e o id).
        -   Exemplo: `FORD`, `CHEVROLET`, `VOLKSWAGEN`, `FIAT`, `RENAULT`, `TOYOTA`, `HONDA`, `HYUNDAI`, `KIA`, `NISSAN`, `PEUGEOT`, `CITROEN`, `JEEP`, `MITSUBISHI`, `MERCEDES-BENZ`, `BMW`, `AUDI`, `VOLVO`.

## E3. Crie o modelo Veiculo


-  Faça um _commit_ para cada etapa. -->

---

# Apêndices

---


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

---


# A2. Instalação e sincronização de extensões do VS Code

**Instalação de extensões no VS Code**

Instale as extensoẽs do **VS Code** de sua preferência. Você pode instalar as extensões clicando no ícone de extensões no canto esquerdo da tela do **VS Code** e pesquisando pelo nome da extensão.

Eu recomendo as seguintes:

-   [DotENV (Suporte a arquivos `.env`) ](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv)
-   [ESLint (JavaScript)](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
-   [Even Better TOML (Melhorias na edição de arquivos TOML)](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)
-   [Intellicode (Desenvolvimento Inteligente)](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
-   [Markdown All in One (Edição de arquivos Markdown)](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
-   [Peacock (Personalização de cores)](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock)
-   [Portuguese (Brazil) Language Pack for Visual Studio Code (Tradução para Português da interface do VS Code)](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-pt-br)
-   [Prettier (Formatação de código)](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
-   [Python (Uhuuuu!)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
-   [Ruff (Linter e formatador de código)](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
-   [SqLite Viewer (Visualização de bancos de dados SQLite)](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)
-   [Thunder Client (Teste de APIs)](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
-   [TODO Highlight (Realce de TODOs)](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
-   [vscode-icons (Ícones para o VS Code)](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)
-   [Vue - Official (Desenvolvimento de aplicações Vue.js)](https://marketplace.visualstudio.com/items?itemName=octref.vetur)
-   [Vue 3 Support - All in One (Suporte ao Vue 3)](https://marketplace.visualstudio.com/items?itemName=znck.vue3)

**Extensão Vue.js devtools no Google Chrome**

-   [Vue.js devtools](https://chrome.google.com/webstore/detail/nhdogjmejiglipccpnnnanhbledajbpd)


**Tema de cores**

Utilizo o tema de cores `Escuro +` do **VS Code**. Dẽ preferência, utilize este tema, pois facilita na visualização do erros no seu código.

Para alterar o tema de cores, useo atalho `Ctrl + K` e depois `Ctrl + T`.

**Sincronização de extensões no VS Code**

Você pode configurar a sincronização das extensões entre os computadores. Para isso:

-   Faça login com a conta do **GitHub** ou da **Microsoft** no VS Code.
-   Clique no ícone de engrenagem no canto inferior esquerdo da tela do VS Code e clique em `Ativar a Sincronização de Configurações`.

---


# A3. Instalação e configuração do PDM

**Instalação do PDM no Linux**

As instruções a seguir são para o **Linux Manjaro e Ubuntu**. Se você estiver usando outra distribuição ou quiser mais informações, consulte a documentação do [PDM](https://pdm.fming.dev/latest/).

-   Abra um terminal:

    `Ctrl + Alt + T`

-   Verifique se o **PDM** está instalado:

```shell
pdm -V
```

-   **Se não estiver instalado**, instale a versão mais recente:

```shell
curl -sSL https://pdm-project.org/install.sh | bash
```

- Após a instalação, **feche o terminal** (`Ctrl + D`) e **abra um novo terminal** (`Ctrl + Alt + T`).

**IMPORTANTE: Configuração do PDM**

-   Execute os seguintes comandos:

```shell
pdm --pep582 >> ~/.bashrc
pdm config python.use_venv false
pdm plugin add pdm-vscode pdm-autoexport pdm-django
```
> O comando `pdm --pep582 >> ~/.bashrc` adiciona a configuração necessária para que o PDM funcione corretamente no terminal.

> O comando `pdm config python.use_venv false` configura o PDM para não usar virtualenv, evitando a criação de uma pasta `.venv` no diretório do projeto. Ao invés disso, ele criará uma pasta `__pypackages__` para armazenar as dependências do projeto.

> Os comandos `pdm plugin add` adicionam plugins úteis para o desenvolvimento com Django e integração com o VS Code.

**Verificação da configuração do PDM**

Verifique se o **PDM** está configurado para não usar virtualenv:

```shell
pdm config
```

A saída deve conter a linha:

```
python.use_venv: False
```

**Instalação do PDM no Windows**

Execute o comando abaixo no **PowerShell** (pode ser no Terminal do `VS Code`):

```shell
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install.ps1 | iex"
```

Após instalar, no **PowerShell**, siga os passos de configuração do PDM, conforme explicado para o **Linux**.


[Voltar para a preparação do ambiente](#1-preparação-do-ambiente)

---


# A4. Publicação do banco de dados no Supabase

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
- Escolha uma senha uma clique ana oção de gerar uma senha e **guarde-a** (você vai precisar dela).
- Selecione a região `South America (São Paulo)`.

**Configurando o banco de dados no projeto**

- Entre no [Dashboard](https://supabase.com/dashboard/projects) do projeto, e escolha o projeto criado.
- Clique na opção `Connect` (Conectar), ao lado do nome do projeto.
- Copia a linha de conexão do banco de dados da opção `Session Pooler`.
  - Ela deve ser parecida com isso: `postgresql://postgres.kfjxquvsjldesrrjqgzo:[YOUR-PASSWORD]@aws-0-sa-east-1.pooler.supabase.com:5432/postgres`
- Coloque a senha que você gerou no campo `[YOUR-PASSWORD]`.
- Copie a linha de conexão e cole no arquivo `.env` do projeto, como no exemplo:

```shell
# Supabase
DATABASE_URL=postgresql://postgres.kfjxquvsjldesrrjqgzo:senha123@aws-0-sa-east-1.pooler.supabase.com:5432/postgres
```

**Migrando o banco de dados**

- No arquivo `.env`:
  - Descomente a linha `DATABASE_URL`.
- Faça a migracão do banco de dados:

```shell
pdm run migrate
```

> Observe que o banco de dados foi migrado no `Supabase`.

> Para testar, crie alguns registros no banco de dados. Depois volte a configuração local e perceba que os dados são diferentes na base local e na base do **Supabase**.

- No site do `Supabase`, acesse o `Table Editor` e verifique que as tabelas foram criadas.
- Você também pode ver o esquema das tabelas, em `Database`, `Schema Visualizer`.

**Carregando os dados iniciais**

- Para carregar os dados iniciais no banco de dados do **Supabase**, acesse a [aula sobre dump e load de dados](#13-dump-e-load-de-dados).

**Utilizando o banco de dados local**

Após fazer as alterações no banco de dados remoto, volte a configuração para utilizar o banco de dados local:

- Para voltar a usar o banco de dados local, no arquivo `.env`:
  - Comente a linha `DATABASE_URL`.

**IMPORTANTE:** A cada nova alteração no banco de dados, você deve repetir este processo de **migração**, tanto no banco de dados local quanto no banco de dados do **Supabase**.

---


# A5. Publicação do projeto no Render

O **Render** é uma plataforma de hospedagem que permite publicar aplicações web, bancos de dados e outros serviços. No site existe um link para o tutorial oficial: [https://render.com/docs/deploy-django](https://render.com/docs/deploy-django)


**Criando um script de Build**

Precisamos executar uma série de comandos para construir nosso aplicativo. Podemos fazer isso com um script de construção (`build script`).

- Verifique se seu projeto já possui o arquivo `build.sh` na raiz do projeto.

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

---


# A6. Publicação: armazenamento de arquivos estáticos no Cloudinary

Vamos utilizar o Cloudinary para armazenar os arquivos estáticos, como as imagens dos livros. Desta forma, os arquivos não serão perdidos a cada nova implantação.

**Criando uma conta no Cloudinary**

- Acesse o site do [Cloudinary](https://cloudinary.com/) e crie uma conta.

**Configurando o Cloudinary**

-   Edite o arquivo `.env`, incluindo a seguinte variável:

```shell
# Cloudinary
CLOUDINARY_URL=cloudinary://your_api_key:your_api_secret@your_cloud_name
```

> Altere as informações de acordo com o seu projeto, acessando o [Cloudinary Console](https://cloudin**IMPORTANTE:**ary.com/console) na opção `Dashboard`.

- Inclua essa mesma variável no `Render` (ou no serviço de hospedagem que você estiver utilizando), na opção `Environment variables`.

**Testando**

- Coloque a variável `MODE` com o valor `MIGRATE` no arquivo `.env`.
-  Faça o upload de uma imagem pelo `Admin` do `Django` e verifique se ela foi salva no `Cloudinary`, na opção `Media Explorer`.
-  Se deu certo, sua aplicação deve estar funcionando normalmente, utilizando o `Cloudinary` para armazenar os arquivos estáticos.
- Faça o _commit_ com a mensagem:

```
feat: adicionando Cloudinary
```

---


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

## Pasta .venv criada no projeto

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
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

# A8. Configuração do git

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
-   Se aparecem muitos arquivos alterados (10 mil, por exemplo), é provável que exista um repositório **git** criado na pasta raiz do usuário. Apague este repositório assim:

```shell
rm -Rf ~/.git
```

-   Recarregue a janela do **VS Code**:

```shell
Control + Shift + P + "Recarregar a Janela"
```

-   Verifique se o número mudou para algo mais razoável (em torno de 100 arquivos).

**Configurando as variáveis do git**

-   Informe seu nome e e-mail no git. Para isso, abra o terminal do VS Code e digite:

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

Repita o processo de configuração de nome e e-mail.


---


# A9. Uso do curl para testar a API via linha de comando

-   Liste todas as categorias:

```shell
curl -X GET http://127.0.0.1:8000/api/categorias/
```

-   Liste uma categoria específica:

```shell
curl -X GET http://127.0.0.1:8000/api/categorias/1/
```

-   Crie uma nova categoria:

```shell
curl -X POST http://127.0.0.1:8000/api/categorias/ -d "descricao=Teste"
```

-   Atualize uma categoria:

```shell
curl -X PUT http://127.0.0.1:8000/api/categorias/1/ -d "descricao=Teste 2"
```

-   Delete uma categoria:

```shell
curl -X DELETE http://127.0.0.1:8000/api/categorias/1/
```

---


# A10. Django Shell - Comandos úteis

Seguem abaixo alguns comandos úteis para serem executados no **Django Shell**:

**Criar um objeto:**

```python
from core.models import Categoria
c = Categoria(descricao='Teste')
c.save()
```

**Listar todos os objetos:**

```python
Categoria.objects.all()
```

**Listar um objeto específico:**

```python
Categoria.objects.get(id=1)
```

**Atualizar um objeto:**

```python
c = Categoria.objects.get(id=1)
c.descricao = 'Teste 2'
c.save()
```

**Deletar um objeto:**

```python
c = Categoria.objects.get(id=1)
c.delete()
```

**Listar todos os livros com preço igual a zero:**

```python
from core.models import Livro
Livro.objects.filter(preco=10)
```

**Mostrar a quantidade de livros com preço igual a zero:**

```python
Livro.objects.filter(preco=0).count()
```

ou

```python
len(Livro.objects.filter(preco=0))
```

**Alterar o preço de todos os livros com preço igual a zero:**

```python
Livro.objects.filter(preco=0).update(preco=10)
```

**Listar todos os livros com preço nulo:**

```python
Livro.objects.filter(preco__isnull=True)
```

**Alterar a editora de todos os livros de um editora específica:**

```python
for livro in Editora.objects.get(id=167).livros.all():
    livro.editora_id = 11
    livro.save()
```

**Listar todos os livros de uma categoria específica (usando o atributo `related_name`):**

```python
Categoria.objects.get(descricao='Comédia').livros.all()
```

**Listar todos os livros de uma categoria específica (usando o atributo `categoria`):**

```python
Livro.objects.filter(categoria__descricao='Comédia')
```

**Remover todas as categorias que não possuem livros:**

```python
for categoria in Categoria.objects.all():
    if len(categoria.livros.all()) == 0:
        print(categoria)
        categoria.delete()
```

**Ajustar o preço do item de compra com base no preco do livro se o preço do item de compra estiver zerado.**

```python
from compras.models import ItensCompra

for item in ItensCompra.objects.filter(preco=0):
    item.preco = item.livro.preco
    item.save()
```

---

# A11. DBShell - Comandos úteis

Antes de utilizar o **DBShell**, é necessário instalar o pacote `sqlite3`.

Ubuntu/Mint e derivados:

```shell
sudo apt install sqlite3
```

Manjaro:

```shell
sudo pacman -S sqlite3
```

Seguem abaixo alguns comandos úteis para serem executados no **DBShell**:

- Remover todos os registros de uma tabela:

```shell
DELETE FROM core_categoria;
```

- Remover todos os usuários, com exceção do primeiro usuário cadastrado:

```shell
DELETE FROM core_user WHERE id > 1;
```

- Atualizar o preço de todos os livros com preço nulo para 10:

```shell
UPDATE core_livro SET preco = 10 WHERE preco IS NULL;
```

- Atualizar o preço de todos os livros com preço igual a zero para 10:

```shell
UPDATE core_livro SET preco = 10 WHERE preco = 0;
```

- Listar todos os livros com preço igual a zero:

```shell
SELECT * FROM core_livro WHERE preco = 0;
```

- Listar todos os livros com preço nulo:

```shell
SELECT * FROM core_livro WHERE preco IS NULL;
```

- Listar todos os livros de uma categoria específica:

```shell
SELECT * FROM core_livro WHERE categoria_id = 1;
```

---


# A12 - Aplicando os 12 Fatores de uma Aplicação ao Nosso Projeto Django + Vue.js

Os *12 Fatores* são princípios criados pela equipe da Heroku para o desenvolvimento de aplicações modernas, escaláveis e prontas para a nuvem. Eles ajudam a manter o código limpo, a implantação simples e a aplicação resiliente. Abaixo, explicamos cada um deles, aplicando diretamente ao nosso projeto.

Para maiores informações, assista ao vídeo [A Forma Ideal de Projetos Web | Os 12 Fatores](https://www.youtube.com/watch?v=gpJgtED36U4) de [Fábio Akita](https://www.youtube.com/@Akitando) ou acesse o site [12factors.net](https://12factor.net/). A documentação em português pode ser encontrada [aqui](https://12factor.net/pt_br/).

---

**1. Código-base – Uma base de código por aplicação**
Uma aplicação deve ter uma única base de código, versionada em um sistema de controle de versão (ex: Git). O código deve ser separado do ambiente de execução.

*Nosso projeto backend Django/DRF está em um repositório GitHub, separado do frontend Vue.js, também versionado no Git. Ambos seguem o princípio de um repositório por código-base, facilitando controle, versionamento e CI/CD.*

---

**2. Dependências – Declare e isole as dependências**
As dependências devem ser declaradas explicitamente e isoladas do sistema. Isso garante que a aplicação funcione em qualquer ambiente.

*No backend, usamos o PDM com o `pyproject.toml` para declarar pacotes como Django, DRF, djangorestframework-simplejwt, etc. No frontend, usamos `package.json` com Pinia, Axios e Vue. Assim, qualquer ambiente pode reproduzir o mesmo setup com `pdm install` ou `npm install`.*

---

**3. Configurações – Armazene as configurações no ambiente**

As configurações devem ser armazenadas como variáveis de ambiente, separadas do código. Isso permite que a aplicação funcione em diferentes ambientes (dev, test, stage, prod) sem alterações no código.

*As configurações são armazenadas em um arquivo `.env`, que não é versionado. O Django usa `django-environ` para carregar variáveis do `.env`, como `DATABASE_URL`, `SECRET_KEY`, `DEBUG`, etc. O Vue.js utiliza o plugin `dotenv` para carregar variáveis prefixadas com `VITE_`. Assim, as configurações são mantidas fora do código-fonte e podem ser alteradas facilmente.*

---

**4. Serviços de Apoio – Trate serviços de apoio como recursos anexos**

Serviços externos como banco de dados ou armazenamento devem ser tratados como recursos externos e facilmente substituíveis.
*O projeto usa PostgreSQL no Supabase e Cloudinary para armazenamento de imagens. O Vue.js consome a API do Django, que se conecta ao banco de dados. O SimpleJWT é usado para autenticação. Todos esses serviços são configurados via variáveis de ambiente, permitindo fácil troca entre ambientes. Nosso app pode usar SQLite localmente e PostgreSQL na produção, sem alterar o código.*

---

**5. Build, Release, Run – Separe os estágios de build e execução**

A aplicação deve ter um processo claro de *build*, *release* e *run*. O build prepara o código, o release configura o ambiente e o run executa a aplicação.

*No Django, fazemos `pdm install` (build), configuramos variáveis (release) e rodamos `pdm run dev` ou Gunicorn (run). O frontend Vue é empacotado com `npm run build` e serve arquivos estáticos via Render.*

---

**6. Processos – Execute a aplicação como um ou mais processos stateless**

A aplicação deve ser executada como um ou mais processos independentes, sem estado. Isso permite escalar horizontalmente e reiniciar processos sem perda de dados.

*O Django é executado com Gunicorn, que inicia múltiplos workers. O Vue.js é uma SPA, servida como arquivos estáticos. Ambos não mantêm estado entre requisições. O estado é gerenciado no frontend (Vuex) ou via tokens JWT. Isso permite escalar horizontalmente e reiniciar processos sem perda de dados.*

---

**7. Vínculo com Portas – Exporte serviços via binding de porta**

A aplicação deve se comunicar através de portas bem definidas, permitindo que serviços externos acessem a aplicação.

*O backend Django é exposto via porta definida por `PORT`, compatível com o Render. O frontend Vue se comunica com o backend via Axios, apontando para a URL da API configurada em tempo de build.*

---

**8. Concorrência – Escale por processo**

Aplicações devem ser escaláveis através da execução de múltiplos processos idênticos.

*Podemos escalar horizontalmente a API com múltiplos workers Gunicorn. O frontend Vue pode ser replicado em várias instâncias no Render, atendendo a múltiplos usuários simultaneamente.*

---

**9. Descartabilidade – Maximize a robustez com inicialização e desligamento rápidos**
Processos devem ser iniciados e parados rapidamente, permitindo fácil escalabilidade e recuperação de falhas.

*Nosso app inicia com `pdm run dev` em segundos, e pode ser reiniciado sem perda de dados. O frontend Vue também é estático, com build e deploy rápidos.*

---

**10. Paridade entre Ambientes – Mantenha desenvolvimento, staging e produção o mais similares possível**

Ambientes de desenvolvimento, staging e produção devem ser o mais semelhantes possível para evitar problemas de compatibilidade.

*A diferença principal entre dev e produção é o banco (SQLite vs PostgreSQL), mas toda a configuração é mantida via `.env`. Com isso, conseguimos boa paridade entre ambientes.*

---

**11. Logs – Trate logs como fluxo de eventos**

Os logs devem ser emitidos para `stdout`/`stderr` e tratados como fluxo contínuo

*Os logs do Django são enviados para o console, permitindo fácil monitoramento. No Render, os logs são capturados automaticamente. O Vue.js registra mensagens importantes no console para debug, facilitando a identificação de problemas.*

---

**12. Processos Administrativos – Execute tarefas admin como processos pontuais**

Tarefas como migrações ou comandos de manutenção devem ser executadas como processos avulsos.

*Usamos comandos como `pdm run migrate`, `createsuperuser` ou `shell_plus` para tarefas administrativas. No Vue.js, comandos de build e lint também são pontuais.*

---

**Conclusão**
Nosso projeto Django + Vue.js segue os 12 fatores de forma consistente, o que nos permite ter uma aplicação modular, escalável, fácil de manter e com deploy contínuo. Essas boas práticas são fundamentais para garantir qualidade e estabilidade tanto em desenvolvimento quanto em produção.

---


# A13 - Rodando o Django com HTTPS no ambiente de desenvolvimento

O `django-extensions` traz o comando `runserver_plus`, que permite iniciar o servidor de desenvolvimento do Django com **SSL (HTTPS)**. Isso é útil quando você precisa testar recursos que exigem HTTPS, como autenticação via OAuth2, cookies `Secure` ou APIs que só aceitam conexões seguras (como Spotify, por exemplo).

---

**1. Instalar dependências**

Primeiro, instale os pacotes necessários:

```bash
pdm add django-extensions werkzeug pyOpenSSL
```

- **django-extensions** → adiciona o comando `runserver_plus`.
- **werkzeug** → servidor de desenvolvimento avançado.
- **pyOpenSSL** → suporte a SSL.

---

**2. Executar com HTTPS**

Você pode rodar o servidor com um certificado autoassinado de forma bem simples:

```bash
pdm run python manage.py runserver_plus --cert-file cert.pem
```

Se o arquivo `cert.pem` **não existir**, o Django Extensions irá gerar automaticamente um certificado e uma chave, armazenando tudo em `cert.pem`.

---

**3. Automatizando com script no `pyproject.toml`**

Para não ter que digitar o comando completo toda vez, adicione um script no seu `pyproject.toml`:

```toml
[tool.pdm.scripts]
devssl = "python manage.py runserver_plus --cert-file cert.pem"
```

Agora você pode rodar com:

```bash
pdm devssl
```

---

**4. Observações importantes**

- O certificado gerado é **autoassinado**, então o navegador exibirá um aviso de “conexão não segura”. Isso é normal em ambiente de desenvolvimento.
- Caso você queira certificados que não mostrem aviso no navegador, pode usar ferramentas como [mkcert](https://github.com/FiloSottile/mkcert).

---

Pronto! Agora seu projeto Django pode ser testado com HTTPS de maneira simples durante o desenvolvimento.


# Contribua

**Para contribuir com este projeto:**

-   Criar um _fork_ do projeto.
-   Clonar o _fork_
-   Criar um _branch_ para a sua contribuição.
-   Fazer as alterações no seu _branch_.
-   Enviar um _pull request_ para o projeto original.

---

Marco André Mendes \<marcoandre@gmail.com>
