
### Aula 28b. Criação de um serializador específico para a listagem de compras

Como fizemos com o Livro, vamos criar um serializador específico para a listagem de compras, que vai mostrar apenas os campos necessários. Com isso, a listagem de compras ficará mais enxuta e legível.

---

**1. Criação do `ItensCompraListSerializer`**

Antes de criar o serializer principal da listagem de compras, criamos um serializer auxiliar para os itens:

```python
# em serializers/compra.py

class ItensCompraListSerializer(ModelSerializer):
    livro = CharField(source='livro.titulo', read_only=True)

    class Meta:
        model = ItensCompra
        fields = ('quantidade', 'livro')
        depth = 1
```

Esse serializer transforma o relacionamento com o `Livro` em uma string legível (o título do livro) e exibe apenas a quantidade e o nome do livro.

---

**2. Criação do `CompraListSerializer`**

Agora sim, o serializer principal da listagem de compras:

```python
# em serializers/compra.py

class CompraListSerializer(ModelSerializer):
    usuario = CharField(source='usuario.e-mail', read_only=True)
    itens = ItensCompraListSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'itens')
```

Ele mostra apenas o id da compra, o e-mail do usuário e a lista de itens com seus respectivos livros e quantidades.

---

**3. Atualize o `__init__.py` do módulo de serializers**

```python
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer,  # novo
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer,  # novo
    ItensCompraSerializer,
)
```

---

**4. Ajuste no `CompraViewSet`**

Modifique a view para retornar o serializer correto dependendo da ação:

```python
class CompraViewSet(ModelViewSet):
    ...

    def get_serializer_class(self):
        if self.action == 'list':
            return CompraListSerializer
        if self.action in ('create', 'update', 'partial_update'):
            return CompraCreateUpdateSerializer
        return CompraSerializer
```

---

**5. Teste**

Acesse o endpoint de listagem de compras no navegador ou no Swagger e veja a resposta simplificada.

---

**6. Commit**

```bash
git add .
git commit -m "feat: criação de um serializador específico para a listagem de compras"
```

---

**Discussão**

> **Pergunta:** Em quais outras situações da nossa API seria útil usar serializers diferentes para listagem, criação ou visualização?

**Resposta:** Sempre que a estrutura de dados exibida for diferente da que recebemos ao criar ou editar registros. Por exemplo:
- Ao listar livros, podemos mostrar apenas o título e o autor, sem todos os detalhes.
- Na visualização detalhada de uma compra, podemos incluir mais dados, como a data da compra ou endereço de entrega.
- Na criação de um recurso, muitas vezes esperamos apenas IDs de relacionamento, enquanto na visualização queremos os dados completos.

---

**Nota:** O `ItensCompraCreateUpdateSerializer` já foi introduzido anteriormente, pois ele é usado para *criação e atualização* de compras. Nesta aula estamos focando no `ItensCompraListSerializer`, que é usado apenas para a *listagem*.
