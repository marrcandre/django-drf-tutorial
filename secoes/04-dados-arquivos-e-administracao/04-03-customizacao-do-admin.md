[Início](../../README.md) | [Seção](README.md) | [Anterior](04-02-dump-e-load-de-dados.md) | [Próxima](04-04-uso-do-django-shell-e-do-django-shell-plus.md)

# 4.3 Customização do Admin

## Objetivo da aula

Melhorar a experiência de uso do Django Admin com registros explícitos, listagens configuradas, filtros e campos de busca.

## Introdução

O Admin já funciona por padrão, mas pode ficar muito mais útil quando configuramos como cada model deve aparecer, ser filtrada e pesquisada.

## Desenvolvimento

### 1. Importação explícita das models

Edite `core/admin.py` e importe as models de forma explícita:

```python
from core.models import Autor, Categoria, Editora, Livro, User
```

### 2. Registro das models com `@admin.register`

Vamos registrar as models através do decorator `@admin.register`, em vez de usar `admin.site.register()`.

Por exemplo, para a model `User`:

```python
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ...
```

Remova a linha `admin.site.register(User, BaseUserAdmin)`.

### 3. Customização do Admin

Configure as models `Autor`, `Categoria`, `Editora` e `Livro`:

```python
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

Os atributos mais importantes aqui são:

- `list_display`;
- `search_fields`;
- `list_filter`;
- `ordering`.

### 4. Testando o resultado

Acesse o Admin e veja as modificações:

```text
http://127.0.0.1:8000/api/admin/
```

## Hora do commit

Mensagem sugerida na nova convenção:

```text
feat(4.3): customiza admin das models principais
```

## Prática

- Verifique as novas listagens no Admin.
- Teste busca, filtro e ordenação.
- Compare a experiência com a versão anterior do painel.

## Conclusão

Um Admin bem configurado economiza tempo e melhora muito o trabalho de cadastro, revisão e conferência dos dados.

## Próxima aula

- [4.4 Uso do Django Shell e do Django Shell Plus](04-04-uso-do-django-shell-e-do-django-shell-plus.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](04-02-dump-e-load-de-dados.md) | [Próxima](04-04-uso-do-django-shell-e-do-django-shell-plus.md)