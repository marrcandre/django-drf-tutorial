[Início](../../README.md) | [Seção](README.md) | [Anterior](05-03-autenticacao-com-o-simplejwt.md) | [Próxima](../06-compras-e-regras-de-negocio/README.md)

# 5.4 Inclusão da foto de perfil no usuário

## Objetivo da aula

Estender o modelo de usuário para associar uma imagem de perfil e expor esse campo pela API e pelo Admin.

## Introdução

Depois de estruturar autenticação e autorização, o próximo passo é evoluir o cadastro do usuário. Aqui, a aplicação `uploader` será reutilizada para armazenar a foto de perfil.

## Desenvolvimento

### 1. Criando o campo `foto`

No arquivo `models/user.py`, adicione:

```python
from uploader.models import Image


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

Essa configuração indica que:

- a foto é opcional;
- o valor padrão é nulo;
- ao excluir a imagem, o campo volta para `null`.

Depois disso, execute as migrações do projeto.

### 2. Exibindo a foto no Admin

No `admin.py`, ajuste a definição do `UserAdmin` para incluir o campo `foto`:

```python
class UserAdmin(BaseUserAdmin):
    ...
        (_('Personal Info'), {'fields': ('name', 'foto')}),
    ...
```

Teste a edição de um usuário no Admin para confirmar que a imagem pode ser associada.

### 3. Atualizando o serializer

Substitua o serializador de usuário em `serializers/user.py` por:

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

Com esse formato:

- `foto_attachment_key` serve para escrita;
- `foto` fica disponível apenas para leitura na resposta da API.

### 4. Testando a API

Envie uma atualização de usuário com a chave de attachment da imagem e confirme o retorno com os dados da foto associados ao usuário.

## Hora do commit

Sugestão de mensagem:

```text
feat(5.4): implementa  foto de perfil no usuario
```

## Prática

- Adicione o campo `foto` ao modelo.
- Atualize o Admin.
- Atualize o serializer.
- Associe uma imagem real a um usuário pela API ou pelo Admin.

## Conclusão

A model de usuário passa a reaproveitar a infraestrutura de upload já existente e fica pronta para cenários mais completos de perfil.

## Próxima aula

- [Seção 6. Compras e regras de negócio](../06-compras-e-regras-de-negocio/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](05-03-autenticacao-com-o-simplejwt.md) | [Próxima](../06-compras-e-regras-de-negocio/README.md)