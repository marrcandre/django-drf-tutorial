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



# 34. Adicionando o tipo de usuário à model de Usuário

Inicialmente, utilizamos os grupos do Django para diferenciar os usuários. Uma outra forma de diferenciar os usuários é através de um campo tipo de usuário. Vamos adicionar o tipo de usuário na entidade  **User**.

- Em `models/user.py`, vamos incluir o campo `tipo_usuario` na entidade `User`:

```python
...
class User(AbstractBaseUser, PermissionsMixin):
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

**Adicionando o campo ao Admin**

Vamos adicionar o campo `tipo_usuario` ao Admin.

- Em `admin/user.py`, vamos incluir o campo `tipo_usuario` no `UserAdmin`:

```python
...
class UserAdmin(BaseUserAdmin):
    fieldsets = (
...
        (_("Personal Info"), {"fields": ("name", "foto", "tipo_usuario")}),
    )
...
```

> O campo `tipo_usuario` foi incluído no campo `Personal info`.


**Utilizando o tipo de usuário**

Uma forma de utilizar o tipo de usuário é verificando se o usuário é `GERENTE` e então permitir que ele tenha acesso a todas as compras. Vamos ver como fazer isso.

- No `views/compra.py`, vamos alterar o método `get_queryset` para permitir que o usuário `GERENTE` tenha acesso a todas as compras:

```python
...
class CompraViewSet(ModelViewSet):
...
    def get_queryset(self):
        usuario = self.request.user
...
        if usuario.tipo == User.Tipos.GERENTE:
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
...
```

> O método `get_queryset` é chamado quando uma compra é listada. Ele retorna apenas as compras do usuário autenticado, exceto se o usuário for `GERENTE`, que retorna todas as compras.

- Para testar, autentique-se com um usuário normal e depois com um que seja `GERENTE`. Você verá que o `GERENTE` consegue ver todas as compras, enquanto o usuário normal só consegue ver as suas compras.
- Faça o _commit_ com a mensagem `Adicionando o tipo de usuário à model de Usuário`.

