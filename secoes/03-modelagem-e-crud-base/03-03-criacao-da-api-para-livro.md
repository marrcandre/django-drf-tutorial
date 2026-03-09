[Início](../../README.md) | [Seção](README.md) | [Anterior](03-02-criacao-da-api-para-autor.md) | [Próxima](03-04-inclusao-das-chaves-estrangeiras-no-modelo-livro.md)

# 3.3 Criação da API para Livro

## Objetivo da aula

Criar a model `Livro` e disponibilizar sua API inicial, aproveitando o padrão já estabelecido para as demais entidades.

## Introdução

Agora vamos criar a principal entidade do domínio da livraria. Como ela já nasce mais rica, vamos usar um script auxiliar para acelerar a geração da estrutura inicial.

## Desenvolvimento

### 1. Criação automática dos arquivos necessários

Para facilitar a criação dos arquivos necessários para a model `Livro`, vamos utilizar um script que cria automaticamente os arquivos necessários. Além disso, ele abre todos os arquivos necessários para criar a API, na ordem correta.

- Antes de executar o script, feche todas as abas do VS Code com o atalho `Ctrl+K W`.
- Execute o seguinte comando no terminal:

```shell
pdm cria_api livro
```

> O comando `pdm cria_api livro` executa um script Python que cria automaticamente os arquivos necessários para a model `Livro` e abre os arquivos relevantes no editor.

### 2. Criando o modelo de dados `Livro`

No arquivo `models/livro.py`:

```python
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f'({self.id}) {self.titulo} ({self.quantidade})'
```

Inclua o modelo no arquivo `models/__init__.py`:

```python
from .livro import Livro
```

Faça as migrações e observe o resultado no banco de dados.

Seu projeto deve ficar assim:

![Projeto com a model Livro](../../diagramas/core_categoria_editora_autor_livro1.png "Projeto com a model Livro")

### 3. Criando a API para a classe `Livro`

Da mesma forma que foi feito para `Categoria`, `Editora` e `Autor`, crie a API para a classe `Livro`.

Use os passos já estabelecidos como referência e, ao final, teste todas as operações de CRUD para a classe `Livro`.

## Hora do commit

Mensagem sugerida na nova convenção:

```text
feat(3.3): cria entidade e api para livro
```

## Prática

- Execute o script auxiliar.
- Crie a model.
- Faça as migrações.
- Teste o CRUD completo da API de `Livro`.

## Conclusão

Com `Livro`, o domínio principal da livraria começa a tomar forma e abre espaço para relacionamentos mais complexos.

## Próxima aula

- [3.4 Inclusão das chaves estrangeiras no modelo Livro](03-04-inclusao-das-chaves-estrangeiras-no-modelo-livro.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](03-02-criacao-da-api-para-autor.md) | [Próxima](03-04-inclusao-das-chaves-estrangeiras-no-modelo-livro.md)