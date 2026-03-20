[Início](../../README.md) | [Seção](README.md) | [Anterior](04-03-customizacao-do-admin.md) | [Próxima](../05-autenticacao-e-usuarios/README.md)

# 4.4 Uso do Django Shell e do Django Shell Plus

## Objetivo da aula

Usar o Django Shell Plus para criar, consultar, atualizar e remover dados diretamente pelo terminal.

## Introdução

O shell do Django é uma ferramenta importante para inspecionar o banco, testar relações e executar operações rápidas sem passar pela interface web.

## Desenvolvimento

### 1. Acessando o shell

```shell
pdm run shellp
```

### 2. Operações básicas

Crie um objeto:

```python
categoria = Categoria.objects.create(descricao='Desenvolvimento Web')
```

Observe que o objeto foi criado:

```python
categoria
```

Liste os objetos:

```python
Categoria.objects.all()
```

Obtenha o objeto:

```python
categoria = Categoria.objects.get(descricao='Desenvolvimento Web')
```

Atualize o objeto:

```python
categoria.descricao = 'Desenvolvimento Web com Django'
categoria.save()
```

Remova o objeto:

```python
categoria.delete()
```

### 3. Usando o atributo `related_name`

Acesso a todos os livros de um autor:

```python
Autor.objects.get(id=1).livros.all()
```

Acesso a todos os livros de uma categoria:

```python
Categoria.objects.get(id=1).livros.all()
```

Acesso a todos os livros de uma editora:

```python
Editora.objects.get(id=1).livros.all()
```

Encerre o shell:

```python
exit()
```

Para mais exemplos, consulte futuramente a seção de ferramentas do tutorial reorganizado.

## Hora do commit

Sugestão de mensagem:

```text
feat(4.4): documenta uso do django shell plus
```

## Prática

- Crie, consulte, atualize e apague um objeto pelo shell.
- Teste os acessos reversos com `related_name`.

## Conclusão

O shell interativo complementa o Admin e ajuda a entender com mais profundidade o comportamento das models e dos relacionamentos.

## Próxima aula

- [Seção 5. Autenticação e usuários](../05-autenticacao-e-usuarios/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](04-03-customizacao-do-admin.md) | [Próxima](../05-autenticacao-e-usuarios/README.md)