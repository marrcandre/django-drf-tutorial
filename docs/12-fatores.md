# Os 12 Fatores de uma Aplicação Web Moderna

**Aplicados ao nosso projeto Django + DRF + Vue.js**

---

## Sumário

1. [Introdução](#introdução)
2. [Nosso Stack de Referência](#nosso-stack-de-referência)
3. [Os 12 Fatores](#os-12-fatores)
   - [I. Código-base](#i-código-base)
   - [II. Dependências](#ii-dependências)
   - [III. Configurações](#iii-configurações)
   - [IV. Serviços de Apoio](#iv-serviços-de-apoio)
   - [V. Build, Release, Run](#v-build-release-run)
   - [VI. Processos](#vi-processos)
   - [VII. Vínculo de Porta](#vii-vínculo-de-porta)
   - [VIII. Concorrência](#viii-concorrência)
   - [IX. Descartabilidade](#ix-descartabilidade)
   - [X. Dev/Prod Semelhantes](#x-devprod-semelhantes)
   - [XI. Logs](#xi-logs)
   - [XII. Processos Administrativos](#xii-processos-administrativos)
4. [Tabela Resumo](#tabela-resumo)
5. [Conclusão](#conclusão)
6. [Referências](#referências)

---

## Introdução

No início dos anos 2010, a equipe da Heroku — uma das primeiras plataformas de *cloud computing* como serviço —
acumulou a experiência de implantar e operar centenas de milhares de aplicações web. Com base nessa vivência,
Adam Wiggins sistematizou um conjunto de boas práticas que ficou conhecido como **A Metodologia dos Doze Fatores**
(do inglês, *The Twelve-Factor App*), publicado em [12factor.net](https://12factor.net/pt_br/).

A ideia central é simples: uma aplicação bem construída deve ser **fácil de implantar, fácil de escalar e
fácil de manter**, independentemente da linguagem ou do ambiente onde ela roda. Os 12 fatores não são
regras rígidas nem uma lista de verificação burocrática — são princípios que traduzem o que significa
construir software profissional na era da nuvem.

Esses princípios são especialmente relevantes para desenvolvedores que estão dando os primeiros passos com
projetos reais. Muitos problemas comuns — *"funciona na minha máquina"*, credenciais vazadas no GitHub,
deploys que quebram sem motivo aparente — têm solução direta em algum dos 12 fatores.

> **Para saber mais:** assista ao vídeo [A Forma Ideal de Projetos Web | Os 12 Fatores](https://www.youtube.com/watch?v=gpJgtED36U4)
> de [Fábio Akita](https://www.youtube.com/@Akitando) e leia a documentação completa em
> [12factor.net/pt_br](https://12factor.net/pt_br/).

---

## Nosso Stack de Referência

Ao longo deste documento, cada fator é explicado e então aplicado concretamente ao seguinte stack:

| Camada | Tecnologias |
|--------|-------------|
| **Backend** | Django 5+, Django REST Framework, SimpleJWT |
| **Gerenciador de pacotes (backend)** | PDM com `pyproject.toml` |
| **Frontend** | Vue.js 3, Vite, Pinia, Axios |
| **Gerenciador de pacotes (frontend)** | NPM com `packages.json` |
| **Controle de versão** | Git + GitHub (dois repositórios: backend e frontend) |
| **Deploy do frontend** | Vercel |
| **Deploy do backend** | Fabroku (implementação interna do Dokku na Fábrica de Software) |
| **Banco de dados (produção)** | PostgreSQL (provisionado no Fabroku) |
| **Banco de dados (desenvolvimento)** | SQLite (local) |
| **Arquivos de mídia** | Cloudinary |
| **Arquivos estáticos** | Whitenoise (servidos pelo próprio Django/Gunicorn) |

Esse stack representa um projeto realista de médio porte: desenvolvido localmente, versionado no GitHub,
implantado em plataformas de nuvem e capaz de crescer sem grandes refatorações.

---

## Os 12 Fatores

---

### I. Código-base

> *"Uma base de código com rastreamento utilizando controle de versão, muitos deploys."*

#### O princípio

Uma aplicação deve ter **exatamente uma base de código**, rastreada em um sistema de controle de versão como
o Git. A partir dessa única base, é possível ter múltiplos *deploys*: desenvolvimento local, ambiente de
homologação, produção, etc. Todos compartilham o mesmo código-fonte — o que os diferencia são as
configurações de ambiente.

O corolário importante: se você tem **dois serviços distintos** (ex: backend e frontend), eles devem ser
**dois repositórios separados**, pois são duas aplicações distintas. Isso evita confusão de responsabilidades
e permite que cada serviço seja implantado, versionado e escalado de forma independente.

Colocar múltiplas aplicações em um único repositório sem uma estratégia clara é uma das causas de
problemas em projetos que crescem: deploys amarrados, histórico de commits misturado e dificuldade em
reutilizar partes do código.

#### No nosso projeto

No nosso caso, seguimos exatamente essa separação:

```
github.com/seu-usuario/meu-projeto-backend   ← Django + DRF
github.com/seu-usuario/meu-projeto-frontend  ← Vue.js 3
```

O repositório do backend contém apenas o código Django: modelos, serializers, views, configurações,
migrações e scripts de administração. O repositório do frontend contém apenas o código Vue.js: componentes,
stores Pinia, chamadas de API via Axios e configurações do Vite.

A branch `main` em cada repositório é a versão que vai para produção. Branches de feature e de desenvolvimento
vivem em paralelo, mas o deploy acontece sempre a partir da `main`.

```
main      ← produção (Fabroku / Vercel)
develop   ← integração
feature/* ← desenvolvimento de funcionalidades
```

> **Dica prática:** nunca coloque o código do frontend dentro da pasta do backend Django (como em
> `backend/frontend/`). Além de violar este fator, isso complica o processo de build e cria acoplamento
> desnecessário entre os dois ciclos de vida da aplicação.

---

### II. Dependências

> *"Declare e isole explicitamente as dependências."*

#### O princípio

Uma aplicação doze-fatores **nunca assume** que uma biblioteca está instalada no sistema operacional onde
ela roda. Todas as dependências — e suas versões exatas — devem ser declaradas em um arquivo de manifesto
e instaladas de forma isolada, sem depender de pacotes globais do sistema.

Esse princípio garante duas coisas fundamentais: **reprodutibilidade** (qualquer pessoa pode clonar o
repositório e ter um ambiente idêntico) e **portabilidade** (a aplicação roda em qualquer servidor que
tenha apenas a linguagem instalada, sem configurações extras).

Dependências implícitas são uma das principais fontes do famoso problema *"funciona na minha máquina"*:
o desenvolvedor tem `libmagic` ou `ImageMagick` instalado globalmente e esquece de declarar, e então o
deploy falha em produção.

#### No nosso projeto

**Backend — PDM com `pyproject.toml`**

Usamos o [PDM](https://pdm-project.org/) como gerenciador de dependências e ambientes virtuais. Todas as
dependências são declaradas em `pyproject.toml`:

```toml
# pyproject.toml
[project]
dependencies = [
  "django>=5.1.3",
  "djangorestframework>=3.14.0",
  "djangorestframework-simplejwt>=5.5.1",
  "dj-database-url>=2.1.0",
  "python-dotenv>=1.0.0",
  "psycopg2-binary>=2.9.9",
  "gunicorn>=21.2.0",
  "cloudinary>=1.36.0",
  "django-cloudinary-storage>=0.3.0",
  "whitenoise[brotli]>=6.6.0",
  ...
]
```

No caso do Fabroku (e da maioria das plataformas de nuvem), o arquivo utilizado para instalar as dependências é o `requirements.txt`, que é gerado automaticamente a partir do `pyproject.toml`:

```bash
pdm export -f requirements > requirements.txt
```

Para instalar o ambiente em uma nova máquina, basta usar o pip do Python:

```bash
pip install -r requirements.txt
```

O PDM cria um ambiente virtual isolado em `__pypackages__/` e instala exatamente as versões declaradas.
Não há dependência de nada instalado globalmente no sistema.

**Frontend — NPM com `packages.json`**

No frontend, o NPM cumpre o mesmo papel:

```json
// packages.json
{
  "dependencies": {
    "axios": "^1.7.2",
    "pinia": "^2.1.7",
    "vue": "^3.4.33",
    "vue-router": "4.4.0"
  },
  "devDependencies": {
    "vite": "^7.3.1",
    "@vitejs/plugin-vue": "^6.0.5",
    "eslint": "^9.7.0"
  }
}
```

Para instalar:

```bash
npm install
```

O arquivo `package-lock.json` (gerado automaticamente) trava as versões exatas de cada pacote e suas
dependências transitivas, garantindo builds reproduzíveis.

> **Nunca commite** `__pypackages__/` nem `node_modules/`. Eles devem estar no `.gitignore` — o ambiente
> é sempre reconstruído a partir dos manifestos de dependência.

---

### III. Configurações

> *"Armazene as configurações no ambiente."*

#### O princípio

Configuração é tudo aquilo que **varia entre ambientes**: credenciais de banco de dados, chaves de API,
o flag `DEBUG`, a URL do serviço de e-mail, etc. A regra é clara: **configuração não vai no código**.

O teste definitivo é simples: você conseguiria publicar o código abertamente no GitHub agora, sem expor
nenhuma credencial? Se a resposta for não, há configuração vazando para o código.

A abordagem correta é usar **variáveis de ambiente**. Elas são:
- Independentes de linguagem e framework
- Fáceis de mudar entre deploys sem alterar uma linha de código
- Impossíveis de commitar por engano (se gerenciadas corretamente)
- Suportadas nativamente por todas as plataformas de cloud

#### No nosso projeto

**Backend — `python-dotenv` + `dj-database-url`**

Em desenvolvimento, as variáveis ficam em um arquivo `.env` na raiz do projeto:

```bash
# .env  (NÃO commitar — está no .gitignore)
MODE=DEVELOPMENT
SECRET_KEY=django-insecure-sua-chave-aqui
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

Em produção (Fabroku), as variáveis são configuradas diretamente no painel da plataforma, sem arquivo `.env`.

O `settings.py` carrega tudo via `python-dotenv` e `dj-database-url`:

```python
# app/settings.py
import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()  # carrega o .env em desenvolvimento

MODE = os.getenv('MODE')
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure')
DEBUG = os.getenv('DEBUG', 'False')

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
    )
}

# Cloudinary só é configurado fora do modo DEVELOPMENT
if MODE != 'DEVELOPMENT':
    CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')
```

Com `dj-database-url`, o mesmo código suporta SQLite localmente e PostgreSQL em produção, bastando
mudar a variável `DATABASE_URL`.

**Frontend — variáveis `VITE_`**

O Vite carrega automaticamente variáveis de um arquivo `.env` prefixadas com `VITE_`:

```bash
# .env  (NÃO commitar — está no .gitignore)
VITE_BASE_URL=http://localhost:8000/api
```

No código Vue, o acesso é feito via `import.meta.env`:

```javascript
// src/plugins/axios.js
axios.defaults.baseURL =
  import.meta.env.VITE_BASE_URL || 'http://localhost:8000/api'
```

Em produção (Vercel), a variável `VITE_BASE_URL` aponta para a URL real do backend no Fabroku.

> **Regra de ouro:** `.env` no `.gitignore`, sempre. Forneça um `.env.example` com as chaves necessárias
> (mas sem valores reais) para orientar novos desenvolvedores.

---

### IV. Serviços de Apoio

> *"Trate serviços de apoio como recursos anexados."*

#### O princípio

Um **serviço de apoio** é qualquer recurso externo que a aplicação consuma pela rede: banco de dados,
sistema de arquivos distribuído, serviço de e-mail, fila de mensagens, cache, etc. O princípio diz que
a aplicação **não deve distinguir** entre um serviço local e um de terceiros — ambos são recursos
anexados e devem ser configurados da mesma forma: por URL ou credencial em variável de ambiente.

A consequência prática é poderosa: trocar o banco de dados, o serviço de armazenamento ou qualquer outro
recurso externo deve ser uma questão de **mudar uma variável de ambiente**, não de alterar código.

Isso também reforça o baixo acoplamento: a aplicação não sabe (nem deveria saber) onde o banco está
fisicamente rodando.

#### No nosso projeto

O nosso projeto usa vários serviços de apoio, todos configurados exclusivamente por variáveis de ambiente:

| Serviço | Desenvolvimento | Produção | Variável de ambiente |
|---------|----------------|----------|---------------------|
| **Banco de dados** | SQLite (arquivo local) | PostgreSQL no Fabroku | `DATABASE_URL` |
| **Armazenamento de mídia** | Sistema de arquivos local (`/media/`) | Cloudinary | `CLOUDINARY_URL` |
| **Autenticação** | SimpleJWT (embutido no Django) | SimpleJWT (mesmo código) | `SECRET_KEY`, `ACCESS_TOKEN_LIFETIME` |

O `settings.py` implementa exatamente essa lógica:

```python
# Banco: SQLite em dev, PostgreSQL em produção — mesmo código, variável diferente
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Mídia: sistema de arquivos em dev, Cloudinary em produção
if MODE == 'DEVELOPMENT':
    MEDIA_URL = 'http://127.0.0.1:8000/media/'
else:
    CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')
    STORAGES = {
        'default': {
            'BACKEND': 'cloudinary_storage.storage.MediaCloudinaryStorage',
        },
        ...
    }
```

Note que **nenhuma URL está hardcoded no código**. Se amanhã precisarmos trocar o Cloudinary por
Amazon S3, a mudança é no `settings.py` (qual backend usar) e na variável de ambiente — o restante
da aplicação não sabe a diferença.

---

### V. Build, Release, Run

> *"Separe estritamente os estágios de construção e execução."*

#### O princípio

O ciclo de vida de um deploy tem três fases distintas e que não devem se misturar:

1. **Build (construção):** o código-fonte é compilado/preparado — dependências são instaladas, assets são
   empacotados, binários são gerados. O resultado é um artefato imutável.

2. **Release (lançamento):** o artefato do build é combinado com as configurações do ambiente específico
   (variáveis de ambiente). O resultado é o *release* — tudo pronto para execução.

3. **Run (execução):** o release é colocado em execução no ambiente de destino.

A separação é crucial porque **não se deve alterar código em tempo de execução**. Uma mudança no código
sempre deve gerar um novo build, um novo release e um novo deploy. Isso garante rastreabilidade e a
possibilidade de *rollback* para um release anterior.

#### No nosso projeto

**Backend (Fabroku)**

```
Build:   pdm install                     ← instala dependências
         python manage.py collectstatic  ← coleta arquivos estáticos
Release: python manage.py migrate        ← aplica migrações ao banco
Run:     gunicorn app.wsgi --log-file -  ← sobe o servidor (definido no Procfile)
```

O `Procfile` define o comando de execução:

```
# Procfile
web: gunicorn app.wsgi --log-file -
```

O Fabroku (assim como o Heroku) lê o `Procfile` automaticamente para saber como executar a aplicação.
O `release` command (migrações) pode ser definido também:

```
# Procfile
web: gunicorn app.wsgi --log-file -
release: python manage.py migrate
```

**Frontend (Vercel)**

```
Build:   npm install && npm run build  ← gera os arquivos estáticos em dist/
Release: (configuração de env vars no painel do Vercel)
Run:     Vercel serve os arquivos dist/ como CDN estático
```

Nos scripts do PDM, os estágios de release também estão organizados:

```toml
# pyproject.toml — [tool.pdm.scripts]
pre_migrate = "python manage.py makemigrations"  # gera os arquivos de migração
migrate     = "python manage.py migrate"          # aplica ao banco (release)
dev         = "python manage.py runserver ..."    # execução local (run)
```

> **Por que isso importa?** Um erro comum é rodar `makemigrations` em produção. A criação de arquivos
> de migração é parte do **build** (deve acontecer no desenvolvimento, com o arquivo versionado no Git).
> Em produção, só se executa `migrate` — o release.

---

### VI. Processos

> *"Execute a aplicação como um ou mais processos que não armazenam estado."*

#### O princípio

Processos de uma aplicação doze-fatores são **stateless** (sem estado) e **share-nothing** (não compartilham
nada entre si). Qualquer dado que precise persistir deve ser armazenado em um serviço de apoio externo —
tipicamente um banco de dados.

O processo **nunca deve assumir** que algo armazenado na memória ou no sistema de arquivos local estará
disponível na próxima requisição. Isso porque:
- Em ambientes com múltiplos workers, a próxima requisição pode ser atendida por um worker diferente.
- Um restart do processo apaga tudo que estava na memória.
- Em deploys em nuvem, o processo pode ser movido para outro servidor a qualquer momento.

Sessões de usuário armazenadas na memória do processo (`sticky sessions`) violam este fator. O estado
de sessão deve ir para um banco de dados ou cache externo (Redis, por exemplo).

#### No nosso projeto

**Backend — Gunicorn stateless**

O Django com DRF não mantém estado entre requisições. Cada chamada à API é independente — autenticação
é feita via **JWT (JSON Web Token)**, que carrega todas as informações necessárias no próprio token,
sem precisar de sessão server-side:

```python
# app/settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    ...
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

O token JWT é armazenado no **frontend** (localStorage no navegador), não no servidor. O servidor apenas
valida o token em cada requisição — sem tabelas de sessão, sem estado.

**Frontend — SPA estático**

O Vue.js é uma *Single Page Application* compilada para arquivos estáticos (`dist/`). Não há processo
server-side rodando — o Vercel simplesmente serve os arquivos HTML, CSS e JavaScript.

O estado da aplicação (lista de itens, usuário logado, etc.) vive na store Pinia, que existe **apenas
no navegador do usuário**, não no servidor.

> **Implicação prática:** se você precisar de cache de dados entre requisições, use Redis ou o banco de
> dados — nunca a memória de um worker Gunicorn ou uma variável global em Python.

---

### VII. Vínculo de Porta

> *"Exporte serviços por ligação de porta."*

#### O princípio

Uma aplicação doze-fatores é **autocontida**: ela expõe seus serviços através de uma porta de rede,
sem depender de um servidor externo como Apache ou Nginx para ser executada. Ela **é** o servidor.

Isso significa que o servidor web está embutido na própria aplicação (ex: Gunicorn no Python), não é
uma configuração separada. A porta em que a aplicação escuta é definida por uma variável de ambiente
(`PORT`), permitindo que a plataforma atribua a porta dinamicamente.

Esse princípio é o que permite que uma aplicação seja um **serviço de apoio para outra**: o backend
é simplesmente acessível por uma URL, e o frontend o consome como qualquer outro serviço HTTP.

#### No nosso projeto

**Backend — Gunicorn + PORT**

O Gunicorn é um servidor HTTP WSGI embutido na aplicação Django. Não precisamos de Nginx na frente para
rodar em produção na maioria dos casos:

```
# Procfile
web: gunicorn app.wsgi --log-file -
```

O Fabroku injeta automaticamente a variável `PORT` no ambiente, e o Gunicorn a lê para saber em qual
porta escutar. Não há configuração manual de porta no código.

Em desenvolvimento:

```toml
# pyproject.toml — [tool.pdm.scripts]
dev = "python manage.py runserver 127.0.0.1:8000"
```

**Frontend — `VITE_BASE_URL`**

O frontend se comunica com o backend exclusivamente por URL configurada em variável de ambiente:

```javascript
// src/plugins/axios.js
axios.defaults.baseURL =
  import.meta.env.VITE_BASE_URL || 'http://localhost:8000/api'
```

Em desenvolvimento, o Vite sobe em `http://localhost:5173`:

```bash
npm run dev   # → http://localhost:5173
```

Em produção, o Vercel atribui sua própria porta e domínio. A `VITE_BASE_URL` no painel do Vercel
aponta para o domínio do backend no Fabroku.

> **Resumo da comunicação:** Vercel (porta 443/HTTPS) → URL pública do Fabroku (porta 443/HTTPS) →
> Gunicorn (porta interna definida pelo Fabroku).

---

### VIII. Concorrência

> *"Dimensione por um modelo de processo."*

#### O princípio

Em uma aplicação doze-fatores, a escala horizontal é feita **adicionando processos**, não aumentando
os recursos de um único processo (escala vertical). Cada tipo de trabalho tem seu tipo de processo:
requisições web, tarefas em background, workers de fila, etc.

O modelo de processo é inspirado no conceito Unix de processos: cada processo faz uma coisa bem feita,
e a escala é horizontal — mais processos do mesmo tipo. Isso contrasta com o modelo de um único processo
gigante que tenta fazer tudo.

A aplicação não deve tentar gerenciar processos internamente (como um daemon que cria suas próprias
threads ou sub-processos). Isso é responsabilidade do sistema operacional ou do gerenciador de processos
da plataforma.

#### No nosso projeto

**Backend — workers Gunicorn**

O Gunicorn gerencia múltiplos *workers* que processam requisições em paralelo. No Fabroku, é possível
configurar o número de workers pela variável `WEB_CONCURRENCY`:

```bash
# No painel do Fabroku ou no Procfile
WEB_CONCURRENCY=4
```

Cada worker é um processo independente que atende requisições — stateless, conforme o fator VI. Se um
worker travar, os demais continuam atendendo normalmente.

Para tarefas demoradas (envio de e-mails em lote, processamento de imagens, relatórios), o padrão seria
adicionar um tipo de processo worker com uma fila (ex: Celery + Redis). Isso seria declarado no `Procfile`:

```
# Procfile (exemplo com worker assíncrono)
web:    gunicorn app.wsgi --log-file -
worker: celery -A app worker --loglevel=info
```

**Frontend — escala automática no Vercel**

O Vercel distribui os arquivos estáticos do Vue.js via CDN global. Não há processo a gerenciar —
o Vercel escala automaticamente conforme a demanda.

> **Dica:** para o contexto de um projeto acadêmico ou pequeno negócio, um único processo web com
> 2-4 workers já é suficiente. O importante é conhecer o modelo para quando precisar crescer.

---

### IX. Descartabilidade

> *"Maximize a robustez com inicialização e desligamento rápido."*

#### O princípio

Processos de uma aplicação doze-fatores devem ser **descartáveis**: podem ser iniciados ou parados a
qualquer momento, sem consequências inesperadas. Isso exige:

- **Inicialização rápida:** o processo deve estar pronto para atender requisições em poucos segundos.
- **Desligamento gracioso:** ao receber um sinal de término (`SIGTERM`), o processo finaliza as
  requisições em andamento e para de aceitar novas, sem perder dados.
- **Robustez a falhas:** o processo deve ser capaz de lidar com interrupções abruptas sem corromper
  dados (ex: usando transações atômicas no banco de dados).

Esse fator é o que permite *deploys sem downtime*, escalonamento rápido e recuperação automática de falhas.

#### No nosso projeto

**Backend — Gunicorn com desligamento gracioso**

O Gunicorn suporta desligamento gracioso nativamente. Ao receber `SIGTERM`, ele para de aceitar novas
requisições e aguarda as atuais terminarem antes de encerrar:

```
# Procfile
web: gunicorn app.wsgi --log-file - --timeout 30
```

O `--timeout 30` define 30 segundos para uma requisição responder antes de ser encerrada forçosamente.

O Fabroku envia `SIGTERM` antes de cada novo deploy, permitindo que o processo atual termine antes do
novo ser iniciado — isso é o **zero-downtime deploy**.

**Frontend — build imutável no Vercel**

O Vercel implementa a descartabilidade de forma ainda mais simples: cada deploy gera um novo artefato
imutável, e a troca entre versões é atômica. Um novo deploy nunca afeta um usuário que está usando a
versão anterior — ambas coexistem por um breve momento.

**Robustez com transações Django**

O Django usa transações atômicas no banco de dados para garantir que operações parcialmente completas
não deixem dados inconsistentes:

```python
from django.db import transaction

with transaction.atomic():
    pedido.save()
    item.save()
    # Se item.save() falhar, pedido.save() também é desfeito
```

---

### X. Dev/Prod Semelhantes

> *"Mantenha desenvolvimento, teste e produção o mais semelhante possível."*

#### O princípio

Historicamente, havia grandes diferenças entre os ambientes de desenvolvimento e produção:
o desenvolvedor usava Mac, produção rodava em Linux; dev usava SQLite, prod usava PostgreSQL; dev
processava e-mails localmente, prod usava SendGrid. Essas diferenças são fontes constantes de bugs
que aparecem apenas em produção — os piores tipos.

A metodologia doze-fatores defende **minimizar essas diferenças** ao máximo. O objetivo é que o
código que funciona no laptop do desenvolvedor seja, com máxima confiança, o mesmo que vai funcionar
em produção.

Os principais vetores de divergência são: **tempo** (código que demora muito para chegar à produção),
**pessoas** (devs que não fazem o deploy) e **ferramentas** (diferenças de OS, banco, serviços).

#### No nosso projeto

A principal diferença deliberada em nosso projeto é o banco de dados: **SQLite em desenvolvimento,
PostgreSQL em produção**. Isso é uma concessão pragmática — SQLite é simples de usar localmente,
não precisa de instalação. A variável `DATABASE_URL` garante que a **mesma linha de código** suporte
os dois:

```python
# app/settings.py — mesmo código funciona para SQLite e PostgreSQL
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',  # fallback para dev
        conn_max_age=600,
    )
}
```

```bash
# .env em desenvolvimento
DATABASE_URL=sqlite:///db.sqlite3

# Variável de ambiente no Fabroku (produção)
DATABASE_URL=postgresql://usuario:senha@host:5432/banco
```

Para minimizar surpresas, é recomendável usar PostgreSQL localmente também quando possível, especialmente
em funcionalidades que exploram recursos específicos do PostgreSQL (campos JSON, busca full-text, etc.):

```bash
# Para usar PostgreSQL localmente com Docker:
docker run -e POSTGRES_PASSWORD=senha -p 5432:5432 postgres
DATABASE_URL=postgresql://postgres:senha@localhost:5432/dev
```

### Docker

O Docker é uma ferramenta que pode ajudar a manter a paridade entre ambientes, pois permite criar um container com o mesmo sistema operacional, dependências e configurações que a produção. No entanto, para projetos pequenos ou acadêmicos, o overhead de configurar Docker pode não valer a pena — especialmente se as diferenças já estão bem controladas por variáveis de ambiente.


**Outros pontos de paridade:**

- O mesmo arquivo `settings.py` é usado em todos os ambientes (as diferenças estão nas env vars).
- O mesmo `requirements.txt` (gerado a partir do `pyproject.toml`) é usado no Fabroku.
- O código Python 3.x rodando localmente é o mesmo que roda no Fabroku.
- O `npm run build` gera exatamente os arquivos que o Vercel vai servir — sem surpresas.

---

### XI. Logs

> *"Trate logs como fluxo de eventos."*

#### O princípio

Uma aplicação doze-fatores **não gerencia seus próprios arquivos de log**. Ela simplesmente escreve
seus eventos no **stdout** (saída padrão) — um fluxo contínuo de linhas de texto.

Quem decide o que fazer com esse fluxo é o ambiente de execução: em desenvolvimento, o terminal do
desenvolvedor exibe o fluxo diretamente; em produção, a plataforma captura o stdout, indexa,
armazena e disponibiliza ferramentas de busca e alertas.

Essa separação é simples mas poderosa: a aplicação não precisa se preocupar com rotação de arquivos,
compressão, onde armazenar, etc. Isso é infraestrutura, não lógica de negócio.

#### No nosso projeto

**Backend — Django logando no stdout**

O Django, por padrão, já envia logs de requisição e erros para o stdout. O `Procfile` reforça isso com
o parâmetro `--log-file -` do Gunicorn (o `-` significa stdout):

```
# Procfile
web: gunicorn app.wsgi --log-file -
```

Em desenvolvimento, os logs aparecem diretamente no terminal ao rodar:

```bash
pdm run dev
# → [2026-05-18 10:00:00] GET /api/livros/ 200 (0ms)
# → [2026-05-18 10:00:01] POST /api/token/ 200 (12ms)
```

No Fabroku, os logs são capturados automaticamente e ficam disponíveis via painel ou CLI:

```bash
# No Fabroku (similar ao Heroku):
dokku logs meu-projeto --tail
```

Para adicionar logs customizados no Django:

```python
import logging

logger = logging.getLogger(__name__)

class LivroViewSet(viewsets.ModelViewSet):
    def create(self, request):
        logger.info(f"Novo livro criado por {request.user.email}")
        return super().create(request)
```

**Frontend — console do navegador e erros monitorados**

O Vue.js registra erros e avisos no console do navegador. Em produção, ferramentas como Sentry podem
capturar exceções JavaScript e enviar para um serviço de monitoramento — o mesmo princípio: a aplicação
gera o evento, a infraestrutura cuida do resto.

---

### XII. Processos Administrativos

> *"Execute tarefas de administração/gerenciamento como processos pontuais."*

#### O princípio

Toda aplicação tem tarefas administrativas pontuais: aplicar migrações, popular o banco com dados
iniciais, executar um script de limpeza, criar um superusuário, etc. Essas tarefas devem ser
executadas como **processos de única execução** no mesmo ambiente (e com o mesmo código) da aplicação
em produção.

O princípio desencoraja soluções improvisadas: não rode um script Python separado com a conexão ao
banco hardcoded, não abra o shell da produção e execute código diretamente sem rastreamento. Use as
ferramentas que o framework provê.

Esses processos administrativos devem ser **versionados junto com o código da aplicação**, para que
todos os ambientes tenham acesso ao mesmo conjunto de comandos.

#### No nosso projeto

**Backend — scripts PDM**

O `pyproject.toml` centraliza todos os comandos administrativos como scripts PDM:

```toml
# pyproject.toml — [tool.pdm.scripts]
dev            = "python manage.py runserver 127.0.0.1:8000"
createsuperuser = "python manage.py createsuperuser"
pre_migrate    = "python manage.py makemigrations"
migrate        = "python manage.py migrate"
post_migrate   = "python manage.py graph_models -S -g -o core.png core"
shell          = "python manage.py shell"
shellp         = "python manage.py shell_plus"
loaddata       = "python manage.py loaddata core.json"
dumpdata       = "python manage.py dumpdata --indent 2"
cria_api       = "python ./scripts/cria_api.py {args}"
check          = "ruff check"
format         = "ruff format"
```

Exemplos de uso:

```bash
pdm run migrate          # aplica migrações
pdm run createsuperuser  # cria usuário administrador
pdm run loaddata         # carrega dados iniciais do core.json
pdm run shellp           # shell interativo com modelos já importados
pdm run dumpdata > dump.json  # exporta dados do banco
```

Em produção no Fabroku, esses comandos são executados via SSH ou pelo painel da plataforma, **no mesmo
ambiente** da aplicação — com as mesmas variáveis de ambiente e a mesma versão do código em execução.

**Frontend — scripts NPM**

```bash
npm run dev      # servidor de desenvolvimento
npm run build    # gera o bundle de produção
npm run preview  # preview do build de produção
npm run lint     # verificação de código
```

> **Nunca** crie scripts Python avulsos que conectam diretamente ao banco de produção fora do Django.
> Use sempre o `manage.py` ou os scripts PDM — eles carregam o contexto completo da aplicação
> (configurações, modelos, ORM) de forma segura e rastreável.

---

## Tabela Resumo

| # | Fator | Princípio em uma linha | Ferramenta no nosso stack |
|---|-------|------------------------|--------------------------|
| I | Código-base | Um repo por aplicação, múltiplos deploys | GitHub (2 repos: backend + frontend) |
| II | Dependências | Declare e isole tudo explicitamente | PDM + `pyproject.toml` / NPM + `packages.json` |
| III | Configurações | Config no ambiente, nunca no código | `python-dotenv`, `dj-database-url`, `VITE_*` |
| IV | Serviços de Apoio | Serviços externos como recursos trocáveis | PostgreSQL, Cloudinary, SimpleJWT via env vars |
| V | Build, Release, Run | Separe construção, configuração e execução | Procfile, `pdm run migrate`, Vercel build |
| VI | Processos | Stateless e share-nothing | Gunicorn + JWT (sem sessão server-side) |
| VII | Vínculo de Porta | A app expõe a porta, a plataforma gerencia | `PORT` no Fabroku, `VITE_BASE_URL` no Vue |
| VIII | Concorrência | Escale adicionando processos | Workers Gunicorn, CDN automático do Vercel |
| IX | Descartabilidade | Inicie e pare rápido, sem perda de dados | Gunicorn graceful shutdown, deploy atômico Vercel |
| X | Dev/Prod Semelhantes | Minimize diferenças entre ambientes | Mesmo `settings.py`, `DATABASE_URL` troca o banco |
| XI | Logs | Escreva no stdout, deixe a plataforma cuidar | `gunicorn --log-file -`, Fabroku logs |
| XII | Processos Admin | Tarefas pontuais com o mesmo código da app | `pdm run migrate`, `pdm run createsuperuser` |

---

## Conclusão

Os 12 fatores não são regras inventadas por burocratas — eles são a destilação de anos de experiência
operando aplicações em escala real. Cada um deles resolve um problema concreto que aparece quando
projetos crescem, quando mais pessoas entram no time, quando o servidor falha às 3 da manhã.

Para um desenvolvedor em formação, a mensagem mais importante é esta: **boas práticas não são
opcionais para projetos sérios**. Um `SECRET_KEY` hardcoded no código, um `.env` commitado por engano,
um `makemigrations` rodando em produção — esses são os erros que custam dados, clientes e reputação.

Adotar os 12 fatores desde o início de um projeto tem um custo baixo e um benefício enorme: você
constrói software que pode ser entregue com confiança, mantido por qualquer pessoa do time e
evoluído sem reescritas traumáticas.

**O nosso stack — Django + DRF + Vue.js + GitHub + PDM + NPM + Fabroku + Vercel + Cloudinary — já implementa a grande maioria desses princípios por padrão, quando configurado corretamente. Conhecer a razão por trás de cada escolha é o que transforma um desenvolvedor que segue receitas em um desenvolvedor que toma decisões.**

---

## Referências

- [The Twelve-Factor App](https://12factor.net/pt_br/) — documentação oficial em português
- [A Forma Ideal de Projetos Web | Os 12 Fatores](https://www.youtube.com/watch?v=gpJgtED36U4) — Fábio Akita
- [PDM — Python Dependency Manager](https://pdm-project.org/)
- [dj-database-url](https://github.com/jazzband/dj-database-url)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [Gunicorn — WSGI HTTP Server](https://gunicorn.org/)
- [Cloudinary Django Storage](https://github.com/cloudinary/cloudinary-storage)
- [Whitenoise](https://whitenoise.readthedocs.io/)
- [Vite — Next Generation Frontend Tooling](https://vitejs.dev/)
- [Vercel Documentation](https://vercel.com/docs)

---

