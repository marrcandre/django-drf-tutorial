[Início](../../README.md) | [Seção](README.md) | [Anterior](03-01-inclusao-da-editora-no-projeto-livraria.md) | [Próxima](03-03-criacao-da-api-para-livro.md)

# 3.2 Criação da API para Autor

## Objetivo da aula

Criar a API da entidade `Autor`, reutilizando o padrão já aplicado em `Categoria` e `Editora`.

## Introdução

Depois de criar a API de `Editora`, o próximo passo é repetir a mesma lógica para `Autor`, com ainda menos orientação detalhada.

## Desenvolvimento

Vamos continuar a criação da API REST para o projeto `livraria`, criando a model `Autor` e a API para ela. Os passos são os mesmos que foram aplicados nas classes `Categoria` e `Editora`.

Crie a API para a classe `Autor`.

O autor terá os seguintes atributos:

- `nome`: string de no máximo 100 caracteres;
- `email`: campo do tipo e-mail de no máximo 100 caracteres, que pode ser nulo.

## Hora do commit

Sugestão de mensagem:

```text
feat(3.2): cria aula de api para autor
```

## Prática

- Teste a API completa de `Autor`.
- Teste a aplicação vuejs para verificar se a API de autores está funcionando corretamente.

## Conclusão

Com `Autor`, o padrão da API já começa a se consolidar como um fluxo repetível dentro do projeto.

## Próxima aula

- [3.3 Criação da API para Livro](03-03-criacao-da-api-para-livro.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](03-01-inclusao-da-editora-no-projeto-livraria.md) | [Próxima](03-03-criacao-da-api-para-livro.md)