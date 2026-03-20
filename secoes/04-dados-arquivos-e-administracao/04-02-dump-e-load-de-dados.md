[Início](../../README.md) | [Seção](README.md) | [Anterior](04-01-upload-e-associacao-de-imagens.md) | [Próxima](04-03-customizacao-do-admin.md)

# 4.2 Dump e Load de dados

## Objetivo da aula

Salvar e restaurar dados do projeto usando comandos de dump e load, entendendo como preparar uma carga inicial utilizável.

## Introdução

Exportar e importar dados é útil para backup, replicação de ambiente, distribuição de dados iniciais e testes de consistência entre instalações.

## Desenvolvimento

### 1. Carga inicial de dados

Acesse o Admin do projeto indicado pelo professor e cadastre pelo menos 10 livros com autor e editora.

Cuidados:

- evite duplicidade;
- não use caixa alta;
- use nomes consistentes, como `O Senhor dos Anéis - A Sociedade do Anel`.

### 2. Cópia de segurança dos dados

Execute:

```shell
pdm run dumpdata > core.json
code core.json
```

Se o arquivo tiver linhas iniciais de configuração como `MODE`, `MEDIA_URL` ou `DATABASES`, apague essas linhas.

### 3. Baixando um arquivo exemplo

No Linux:

```shell
wget https://raw.githubusercontent.com/marrcandre/django-drf-tutorial/refs/heads/main/scripts/core.json
```

No Windows:

```shell
Invoke-WebRequest -Uri "https://github.com/marrcandre/django-drf-tutorial/raw/main/scripts/core.json" -OutFile core.json
```

### 4. Carga dos dados

Execute:

```shell
pdm run loaddata
```

O comando espera um arquivo `core.json` na pasta raiz do projeto.

### 5. Ajustando a model `Editora`

Se ocorrer erro ao carregar os dados, adicione os campos `email` e `cidade` à model `Editora`:

```python
class Editora(models.Model):
    ...
    email = models.EmailField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
```

Faça a migração e tente novamente.

### 6. Verificando se a carga funcionou

Use o Django Shell Plus:

```shell
pdm run shellp
```

Dentro dele:

```python
Livro.objects.all()
```

## Hora do commit

Sugestão de mensagem:

```text
feat(4.2): adiciona fluxo de dump e load de dados
```

## Prática

- Gere um arquivo de dump.
- Rode o load.
- Corrija a model `Editora`, se necessário.
- Valide a presença dos dados no shell, no Admin ou no Swagger.

## Conclusão

Com dump e load, você passa a ter um caminho mais seguro para distribuir e recuperar dados do projeto entre ambientes.

## Próxima aula

- [4.3 Customização do Admin](04-03-customizacao-do-admin.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](04-01-upload-e-associacao-de-imagens.md) | [Próxima](04-03-customizacao-do-admin.md)