[Início](../../README.md) | [Seção](README.md) | [Anterior](06-12-visualizacao-de-compras-por-perfil-de-usuario.md) | [Próxima](06-14-gravacao-do-preco-do-livro-no-item-da-compra.md)

# 6.13 Validação dos campos no serializer

## Objetivo da aula

Aplicar regras de validação no serializer para impedir compras inválidas.

## Introdução

À medida que a regra de negócio cresce, não basta mais apenas aceitar dados e salvar no banco. Também é preciso proteger a aplicação contra situações inconsistentes, como quantidades inválidas ou pedidos acima do estoque disponível.

## Desenvolvimento

### 1. Validando quantidade maior que zero

```python
from rest_framework.serializers import ValidationError


def validate_quantidade(self, quantidade):
    if quantidade <= 0:
        raise ValidationError('A quantidade deve ser maior do que zero.')
    return quantidade
```

### 2. Validando estoque disponível

```python
def validate(self, item):
    if item['quantidade'] > item['livro'].quantidade:
        raise ValidationError('Quantidade de itens maior do que a quantidade em estoque.')
    return item
```

### 3. Formatando dados na validação

O mesmo mecanismo pode normalizar dados antes da gravação, como no caso de e-mails convertidos para minúsculas em serializers de editora.

## Hora do commit

```text
feat(6.13): implementa validacao dos campos no serializer
```

## Prática

- Tente criar itens com quantidade zero.
- Tente exceder o estoque disponível.
- Teste um caso de normalização de dados em outro serializer do projeto.

## Conclusão

O serializer deixa de ser apenas uma camada de transformação de dados e passa a funcionar também como um ponto importante de proteção das regras do domínio.

## Próxima aula

- [6.14 Gravação do preço do livro no item da compra](06-14-gravacao-do-preco-do-livro-no-item-da-compra.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](06-12-visualizacao-de-compras-por-perfil-de-usuario.md) | [Próxima](06-14-gravacao-do-preco-do-livro-no-item-da-compra.md)