# 25- Acesso a campos relacionados

- Acesse o shell:

```bash
python manage.py shell
```

- Importe os modelos de `core.models`:
  
# DRAFT: Fake data

- Instale o pacote `django-faker`:

```bash
poetry add faker
```

- Edite o arquivo `core/admin.py`:

```python
...
from faker import Faker
...

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')
    actions = ['gerar_autores']

    def gerar_autores(self, request, queryset):
        faker = Faker()
        for _ in range(10):
            Autor.objects.create(
                nome=faker.name(),
                email=faker.email(),
            )
        self.message_user(request, 'Autores gerados com sucesso!')
    gerar_autores.short_description = 'Gerar autores'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    actions = ['gerar_categorias']

    def gerar_categorias(self, request, queryset):
        faker = Faker()
        for _ in range(10):
            Categoria.objects.create(
                descricao=faker.word(),
            )
        self.message_user(request, 'Categorias geradas com sucesso!')
    gerar_categorias.short_description = 'Gerar categorias'

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    ...
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    actions = ['gerar_editoras']

    def gerar_editoras(self, request, queryset):
        faker = Faker()
        for _ in range(10):
            Editora.objects.create(
                nome=faker.company(),
            )
        self.message_user(request, 'Editoras geradas com sucesso!')
    gerar_editoras.short_description = 'Gerar editoras'

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...
    list_display = ('titulo', 'editora', 'categoria')
    search_fields = ('titulo', 'editora__nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('titulo', 'editora', 'categoria')
    list_per_page = 25
    actions = ['gerar_livros']

    def gerar_livros(self, request, queryset):
        faker = Faker()
        for _ in range(10):
            Livro.objects.create(
                titulo=faker.sentence(nb_words=3, variable_nb_words=True),
                editora=Editora.objects.order_by('?').first(),
                categoria=Categoria.objects.order_by('?').first(),
            )
        self.message_user(request, 'Livros gerados com sucesso!')
    gerar_livros.short_description = 'Gerar livros'
```

- Acesse o Admin:

    http://localhost:8000/admin/


# DRAFT: Pre-commit 

- Instale o pacote `pre-commit`:

```bash
poetry add pre-commit
```

- Edite o arquivo `pyproject.toml`:

```python

[tool.poetry.scripts]
pre-commit = "pre_commit:main"


[tool.poetry.dev-dependencies]
pre-commit = "^2.9.3"
```

- Execute o comando `poetry install`:

```bash
poetry install
```

- Execute o comando `pre-commit install`:

```bash
pre-commit install
```

- Edite o arquivo `.pre-commit-config.yaml`:

```python
repos:
-   repo:
    url:
    rev:
    hooks:
    -   id: check-merge-conflict
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
    -   id: flake8
        args: [--max-line-length=120]
    -   id: isort
            args: [--profile=black]
    -   id: black
            args: [--line-length=120]
```

- Execute o comando `pre-commit run --all-files`:

```bash
pre-commit run --all-files
```
-->

