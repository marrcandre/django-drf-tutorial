[Voltar ao README](README.md)

# Migração do projeto antigo para o novo template com SimpleJWT

## Tabela de conteúdo

- [Contexto](#contexto)
- [Estratégia da migração](#estratégia-da-migração)
- [O que copiar, adaptar e não copiar](#o-que-copiar-adaptar-e-não-copiar)
- [Pré-requisitos](#pré-requisitos)
- [Etapa 1: criar e validar o projeto novo](#etapa-1-criar-e-validar-o-projeto-novo)
- [Etapa 2: copiar apenas os arquivos de domínio](#etapa-2-copiar-apenas-os-arquivos-de-domínio)
- [Etapa 3: adaptar os arquivos de integração](#etapa-3-adaptar-os-arquivos-de-integração)
- [Etapa 4: revisar o que não deve ser reaproveitado](#etapa-4-revisar-o-que-não-deve-ser-reaproveitado)
- [Etapa 5: gerar migrations novas no projeto novo](#etapa-5-gerar-migrations-novas-no-projeto-novo)
- [Etapa 6: validar a aplicação](#etapa-6-validar-a-aplicação)
- [Erros mais comuns](#erros-mais-comuns)
- [Conclusão](#conclusão)

## Contexto

Se você começou o projeto com o template antigo, este material é para você.

Na versão antiga do template, o projeto usava Passage para autenticação e o modelo `User` possuía o campo `passage_id`.

O template novo mudou essa base:

- a autenticação agora usa `SimpleJWT`;
- o `User` não usa mais `passage_id`;
- o projeto já vem com endpoints de token prontos;
- a estrutura de usuário e autenticação do template novo já está consistente com o frontend atual.

Isso significa que você não deve copiar o projeto antigo inteiro por cima do novo.

O caminho correto é outro: criar um projeto novo a partir do template atual e trazer para ele apenas aquilo que você já construiu no domínio da livraria.

> IMPORTANTE: Esta migração deve ser tratada como uma reconstrução guiada do projeto, e não como uma cópia integral do repositório antigo.

## Estratégia da migração

Em resumo, você vai:

1. criar um projeto novo com o template atual;
2. validar que ele está funcionando com a autenticação nova;
3. copiar apenas os arquivos de domínio que você criou no projeto antigo;
4. adaptar os arquivos de integração do projeto novo;
5. gerar migrations novas apenas no projeto novo.

## O que copiar, adaptar e não copiar

### 1. Trazer do projeto antigo

- models de domínio, como `Autor`, `Categoria`, `Editora` e `Livro`;
- serializers dessas entidades;
- viewsets dessas entidades;
- regras de negócio que estejam nesses models, serializers e views;
- nomes e registros das entidades que precisarão voltar ao projeto;
- campos e comportamentos do domínio já implementados por você;
- nomes das rotas e das entidades que precisarão ser registradas no `app/urls.py` do projeto novo.

### 2. Adaptar no projeto novo

- `core/admin.py`;
- `app/urls.py`;
- `core/models/__init__.py`;
- `core/serializers/__init__.py`;
- `core/views/__init__.py`;
- trechos específicos do `SPECTACULAR_SETTINGS`, se necessário.

### 3. Não trazer do projeto antigo

- `core/authentication.py`;
- `core/models/user.py` antigo;
- `core/serializers/user.py` antigo;
- `core/views/user.py` antigo;
- `passage_id`;
- variáveis `PASSAGE_APP_ID` e `PASSAGE_API_KEY`;
- `pyproject.toml` antigo;
- `requirements.txt` antigo;
- migrations antigas do projeto baseado em Passage;
- `db.sqlite3` antigo;
- `dump.json` antigo.

## Pré-requisitos

Antes de começar, você precisa ter:

- o projeto antigo disponível para consulta;
- um projeto novo criado a partir do template atual;
- o projeto novo funcionando localmente;
- o VS Code aberto com os dois projetos disponíveis para comparação.

## Etapa 1: criar e validar o projeto novo

Crie um repositório novo usando o template atual em https://github.com/marrcandre/template_django_pdm e depois clone o projeto normalmente.

Para essa preparação inicial, você também pode se apoiar na aula [2.2 Criação de uma aplicação](secoes/02-fundacao-do-projeto/02-02-criacao-de-uma-aplicacao.md), principalmente na parte em que o tutorial mostra a estrutura da aplicação `core` e como validar migrations, banco e admin.

Em seguida, instale as dependências:

```shell
pdm install
```

Crie o arquivo `.env`:

```shell
cp .env.exemplo .env
```

Suba o servidor:

```shell
pdm run dev
```

Agora valide o projeto novo antes de copiar qualquer código do projeto antigo.

### O que conferir agora

- o admin abre normalmente;
- o schema da API está acessível;
- os endpoints de token existem;
- o endpoint de registro existe;
- os usuários que já vêm no banco do template continuam disponíveis.

### Teste mínimo antes de continuar

Abra o Swagger em `/api/doc` e verifique se estes endpoints existem:

- `/api/token/`
- `/api/token/refresh/`
- `/api/token/verify/`
- `/api/registro/`
- `/api/usuarios/me/`

> IMPORTANTE: Neste momento, não substitua `db.sqlite3`, não use o `dump.json` antigo e não copie as migrations do projeto anterior.

## Etapa 2: copiar apenas os arquivos de domínio

Agora você vai abrir o projeto antigo e localizar apenas os arquivos que pertencem ao domínio da livraria.

Faça isso arquivo por arquivo, sem copiar pastas inteiras.

No caso da turma, isso normalmente inclui:

- `core/models/autor.py`
- `core/models/categoria.py`
- `core/models/editora.py`
- `core/models/livro.py`
- `core/serializers/autor.py`
- `core/serializers/categoria.py`
- `core/serializers/editora.py`
- `core/serializers/livro.py`
- `core/views/autor.py`
- `core/views/categoria.py`
- `core/views/editora.py`
- `core/views/livro.py`

Copie esses arquivos para o projeto novo, preservando os nomes e a organização das pastas.

### O que observar ao copiar

- mantenha apenas código do domínio;
- não copie o `User` antigo;
- não copie arquivos de autenticação;
- não copie migrations antigas;
- não copie arquivos que existiam apenas para suportar Passage.

### Teste mínimo antes de continuar

Depois de copiar os arquivos, abra cada um deles no projeto novo e confira se os imports ainda fazem sentido.

Se algum arquivo importar algo que não existe no template novo, corrija isso antes de seguir.

## Etapa 3: adaptar os arquivos de integração

Depois de copiar os arquivos do domínio, você precisa reconectar esse código à estrutura do projeto novo.

Esta etapa exige edição manual. Não substitua esses arquivos por inteiro.

### 3.1 Atualizar `core/models/__init__.py`

Abra o arquivo do projeto novo e acrescente apenas os imports dos models que você trouxe.

Exemplo do que deve passar a existir:

```python
from .autor import Autor
from .categoria import Categoria
from .editora import Editora
from .livro import Livro
from .user import User
```

### 3.2 Atualizar `core/serializers/__init__.py`

Preserve os serializers de usuário do template novo e acrescente os serializers do domínio.

Exemplo:

```python
from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .livro import LivroSerializer
from .user import UserRegistrationSerializer, UserSerializer
```

### 3.3 Atualizar `core/views/__init__.py`

Preserve as views de usuário do template novo e acrescente os viewsets do domínio.

Exemplo:

```python
from .autor import AutorViewSet
from .categoria import CategoriaViewSet
from .editora import EditoraViewSet
from .livro import LivroViewSet
from .user import UserRegistrationView, UserViewSet
```

### 3.4 Atualizar `core/admin.py`

Mantenha o `UserAdmin` do template novo.

Depois, registre os models do domínio que você trouxe.

Se o seu `admin.py` antigo tinha registros de `Autor`, `Categoria`, `Editora` e `Livro`, reintroduza apenas esses registros.

Mantendo o registro do `User` do template novo, adicione ao final do arquivo linhas como estas:

```python
admin.site.register(models.Autor)
admin.site.register(models.Categoria)
admin.site.register(models.Editora)
admin.site.register(models.Livro)
```

> IMPORTANTE: Não recoloque `passage_id` no `UserAdmin`.

### 3.5 Atualizar `app/urls.py`

Aqui você precisa ter cuidado para não apagar a autenticação nova do template.

O arquivo `app/urls.py` do projeto novo já vem com a parte de autenticação e documentação pronta. Essa estrutura deve ser mantida.

Você deve preservar:

- schema;
- swagger ou doc;
- redoc;
- `/api/token/`;
- `/api/token/refresh/`;
- `/api/token/verify/`;
- `/api/registro/`;
- `/api/usuarios/`.

Depois disso, faça apenas duas alterações.

### Primeiro ajuste: importar os viewsets do domínio

Antes de registrar esses routers, você precisa importar os viewsets no bloco de imports vindo de `core.views`.

No template novo, esse import vem enxuto, trazendo apenas as views de usuário. Substitua esse trecho por um bloco como este:

```python
from core.views import (
    AutorViewSet,
    CategoriaViewSet,
    EditoraViewSet,
    LivroViewSet,
    UserRegistrationView,
    UserViewSet,
)
```

Esse bloco deve ficar na mesma região do arquivo onde o template novo já importa `UserRegistrationView` e `UserViewSet`.

### Segundo ajuste: registrar os routers das entidades do domínio

Depois dos imports, vá até a parte do arquivo onde aparece:

```python
router = DefaultRouter()
```

Logo abaixo dessa linha, adicione os registros das suas entidades. Exemplo:

```python
router.register(r'autores', AutorViewSet, basename='autores')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'editoras', EditoraViewSet, basename='editoras')
router.register(r'livros', LivroViewSet, basename='livros')
```

Essas linhas devem ficar antes de `urlpatterns`.

Se você preferir, pense no `app/urls.py` assim:

1. mantenha todas as rotas de autenticação e documentação que o template novo já trouxe;
2. aumente o bloco de imports de `core.views` para incluir seus viewsets;
3. registre apenas os routers das entidades da livraria.

### Teste mínimo antes de continuar

Antes de gerar migrations, confira se:

- os imports dos `__init__.py` estão corretos;
- os novos viewsets aparecem em `app/urls.py`;
- o projeto ainda preserva os endpoints JWT;
- o arquivo `core/admin.py` não voltou a depender de `passage_id`.

## Etapa 4: revisar o que não deve ser reaproveitado

Agora faça uma revisão final para garantir que os resíduos do template antigo não foram trazidos para o projeto novo.

Além disso, observe a barra inferior do VS Code e confira se o editor mostra que não há problemas no projeto, isto é, `0` erros e `0` avisos.

### Remova ou evite trazer

- `core/authentication.py`
- `core/models/user.py` antigo
- `core/serializers/user.py` antigo
- `core/views/user.py` antigo
- qualquer referência a `passage_id`
- variáveis `PASSAGE_APP_ID` e `PASSAGE_API_KEY`
- dependência `passage-identity`
- migrations antigas do projeto
- `db.sqlite3` antigo
- `dump.json` antigo

### O que deve permanecer do template novo

- `core/models/user.py`
- `core/serializers/user.py`
- `core/views/user.py`
- a configuração de JWT no `app/settings.py`
- os endpoints de token e registro no `app/urls.py`
- o banco inicial do template novo
- as migrations do template novo

## Etapa 5: gerar migrations novas no projeto novo

Depois que os arquivos do domínio estiverem no lugar e os arquivos estruturais estiverem adaptados, gere as migrations no projeto novo.

```shell
pdm run migrate
```

Como o script `migrate` do projeto já executa `makemigrations` antes, ele deve criar apenas as migrations novas referentes ao domínio que você trouxe.

### O que você deve observar

- o projeto não deve tentar recriar o `User` antigo;
- o projeto não deve tentar reintroduzir `passage_id`;
- as migrations novas devem corresponder às entidades do domínio trazidas para o projeto novo.

### Teste mínimo antes de continuar

Depois de rodar as migrations:

- abra o admin;
- verifique se os usuários do template novo continuam existindo;
- verifique se as novas tabelas do domínio foram criadas;
- abra o arquivo `core.png` e verifique se as entidades foram criadas corretamente. Se quiser, compare com a imagem do projeto antigo;
- abra o banco de dados em `db.sqlite3` e confira se as tabelas foram criadas corretamente.

## Etapa 6: validar a aplicação

Com a migração concluída, valide o funcionamento geral do projeto.

### Checklist de validação

- login via `/api/token/` funcionando;
- refresh de token funcionando;
- endpoint `/api/usuarios/me/` funcionando;
- CRUD de `Autor` funcionando;
- CRUD de `Categoria` funcionando;
- CRUD de `Editora` funcionando;
- CRUD de `Livro` funcionando;
- admin exibindo os modelos trazidos;
- documentação da API listando os endpoints esperados.

## Erros mais comuns

### 1. Copiar a pasta `core` inteira

Esse é o erro mais comum e mais perigoso.

Quando você faz isso, normalmente leva junto:

- o `User` antigo;
- a autenticação antiga;
- referências a `passage_id`;
- imports que já não fazem sentido no template novo.

### 2. Substituir `app/urls.py` por inteiro

Ao fazer isso, você pode perder os endpoints do JWT e do registro de usuário.

### 3. Substituir `app/settings.py` por inteiro

Ao fazer isso, você corre o risco de remover a configuração atual de autenticação e voltar a depender de variáveis do Passage.

### 4. Esquecer de atualizar os arquivos `__init__.py`

Nesse caso, os arquivos existem, mas o projeto não consegue enxergá-los corretamente.

### 5. Tentar reaproveitar o banco antigo

O objetivo desta aula é migrar a estrutura do código do domínio para um projeto novo.

Ela não foi pensada para reaproveitar o banco legado do template antigo.

## Conclusão

Agora você tem novamente o projeto da livraria com as entidades e APIs que já havia construído, mas usando a autenticação nova baseada em SimpleJWT.

Com isso, o backend fica alinhado com o template atual do curso e pronto para integração com o frontend.

Agora você já pode criar também um projeto frontend a partir do template Vue em https://github.com/marrcandre/template-vue3. A conexão da API ao frontend com Vue 3 é apresentada na aula 5 do tutorial em https://github.com/marrcandre/django-drf-tutorial?tab=readme-ov-file#5-conectando-a-api-ao-frontend-com-vue-3, e esse template deve se conectar corretamente ao backend que você acabou de migrar.

[Voltar ao README](README.md)