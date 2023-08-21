# 21. Implantação no Render

Link para o tutorial: [https://render.com/docs/deploy-django](https://render.com/docs/deploy-django)

**Modificações no projeto:**

- Abra o arquivo `settings.py` e encontre a linha que contém a variável` SECRET_KEY`. Não queremos armazenar segredos de produção no código fonte, então vamos pegá-los de variáveis de ambiente que criaremos depois:

```python
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
```

- Para que esse comando funcione, precisamos importar a biblioteca `os` no início do arquivo:

```python  
import os
```

- Encontre a declaração da configuração `DEBUG`. Essa configuração nunca deve ser definida como `True` em um ambiente de produção. Você pode detectar se está sendo executado no Render verificando se a variável de ambiente `RENDER` está presente no ambiente da aplicação.

```python
DEBUG = 'RENDER' not in os.environ
```

- Quando `DEBUG = False`, o Django não funcionará sem um valor adequado para `ALLOWED_HOSTS`. Você pode obter o nome do host do seu serviço web da variável de ambiente `RENDER_EXTERNAL_HOSTNAME`, que é definida automaticamente pelo Render. Adicione o seguinte código ao arquivo `settings.py`:

```python
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
```

**Arquivos estáticos**

Websites geralmente precisam servir arquivos adicionais, como imagens, JavaScript e CSS. No Django, esses arquivos são chamados de arquivos estáticos, e ele fornece um módulo dedicado para coletá-los em um único local para servir em produção.

Nesta etapa, vamos configurar o `WhiteNoise`, que é uma solução muito popular para esse problema. 

- Adicione `WhiteNoise` como uma dependência (adicionar suporte para `Brotli` é opcional, mas recomendado):

```shell
pdm add 'whitenoise[brotli]'
``` 

- Abra o arquivo `settings.py`, encontre a lista `MIDDLEWARE` e adicione o middleware `WhiteNoise` logo após o `SecurityMiddleware`:

```python
MIDDLEWARE = [
    ...
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ....
]
```

- Encontre a seção onde os arquivos estáticos são configurados. Aplique as seguintes modificações:

```python
# Essa configuração informa ao Django em qual URL os arquivos estáticos serão servidos ao usuário.
# Aqui, eles estarão acessíveis em seu-domínio.onrender.com/static/...
STATIC_URL = '/static/'

# As seguintes configurações só fazem sentido em produção e podem causar problemas em ambientes de desenvolvimento.
if not DEBUG:
    # Indica ao Django para copiar os arquivos estáticos para o diretório `staticfiles` 
    # no diretório da sua aplicação no Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Ativa o backend de armazenamento WhiteNoise, que cuida da compressão dos arquivos estáticos
    # e cria nomes únicos para cada versão, permitindo que sejam armazenados em cache com segurança para sempre.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

**Criação de um Script de Build**

Precisamos executar uma série de comandos para construir nosso aplicativo. Podemos fazer isso com um script de construção (build script). Crie um script chamado build.sh na raiz do seu repositório:

- Crie um arquivo chamado `build.sh` na raiz do projeto com o seguinte conteúdo:

```shell
#!/usr/bin/env bash

# sai do script se algum comando falhar
set -o errexit

# atualiza o pip
/opt/render/project/src/.venv/bin/python3.9 -m pip install --upgrade pip

# Instala as dependências do projeto
pip install -r requirements.txt

# Coleta os arquivos estáticos em um único diretório
python manage.py collectstatic --no-input

# Executa as migrações
python manage.py migrate
```

> Nosso projeto utiliza o `pdm` para gerenciar as dependências do projeto. No entanto, o Render ainda não suporta o `pdm`. Por isso, vamos usar o `pip` para instalar as dependências.

- Certifique-se de que o arquivo `build.sh` tenha permissão de execução, antes de fazer o commit:

```shell
chmod a+x build.sh
```

> Posteriormente, vamos configurar o **Render** para executar esse script de construção antes de iniciar o aplicativo a cada nova implantação.

- Vamos executar nossa aplicação usando o `gunicorn`, que é um servidor HTTP WSGI para Python. Adicione o `gunicorn` como uma dependência:

```shell
pdm add gunicorn
```

**Implantação**

- Crie um arquivo chamado `render.yaml` na raiz do seu repositório com o seguinte conteúdo:

```yaml
databases:
  - name: config
    databaseName: config
    user: config

services:
  - type: web
    name: config
    runtime: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn config.wsgi:application"
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: config
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: WEB_CONCURRENCY
        value: 4
```

- No site do [Render](https://dashboard.render.com/), crie um novo Serviço Web (`Web Service`), apontando-o para o repositório do seu aplicativo (conceda permissão ao **Render** para acessá-lo, se ainda não o fez).
  
- Selecione Python como `runtime` e configure as seguintes propriedades:

| Propriedade  | Valor                               |
|--------------|-------------------------------------|
| Build Command| `./build.sh`                        |
| Start Command| `gunicorn config.wsgi:application ` |
| Auto Deploy  | `Yes`                               |

- Adicione as seguintes variáveis de ambiente em `Environment Variables` (variáveis de ambiente), na opção `Advanced Settings`:

| Key (Chave)  | Value (Valor)                             |
|--------------|-------------------------------------------|
| PYTHON_VERSION  | 3.9.9                                  |
| SECRET_KEY      | Clique em `Generate` para obter um valor aleatório seguro  |
| WEB_CONCURRENCY | 4                                      |

- É isso! Salve seu serviço web para implantar sua aplicação Django no **Render**. Ela estará disponível na URL `seu_projeto.onrender.com` assim que a construção for concluída.
