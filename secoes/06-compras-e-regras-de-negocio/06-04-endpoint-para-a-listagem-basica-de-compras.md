[Início](../../README.md) | [Seção](README.md) | [Anterior](06-03-uso-de-tabularinline-no-admin-para-itens-da-compra.md) | [Próxima](06-05-visualizacao-dos-itens-da-compra-na-listagem.md)

# 6.4 Endpoint para a listagem básica de compras

## Objetivo da aula

Criar serializer, viewset e rota para expor a entidade `Compra` na API.

## Desenvolvimento

### 1. Serializer inicial

```python
from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True)
    status = CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Compra
        fields = '__all__'
```

### 2. Viewset

```python
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
```

### 3. Registro da rota

Inclua o viewset em `core/views/__init__.py` e registre `compras` no router principal.

## Hora do commit

```text
feat(6.4): documenta listagem basica de compras
```

## Prática

- Crie o serializer.
- Publique a viewset.
- Valide a listagem no navegador ou no Swagger.

## Conclusão

A entidade de compra passa a ter uma representação mínima na API, pronta para ser enriquecida nas próximas aulas.

## Próxima aula

- [6.5 Visualização dos itens da compra na listagem](06-05-visualizacao-dos-itens-da-compra-na-listagem.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-03-uso-de-tabularinline-no-admin-para-itens-da-compra.md) | [Próxima](06-05-visualizacao-dos-itens-da-compra-na-listagem.md)