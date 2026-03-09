[Início](../../README.md) | [Seção](README.md) | [Anterior](10-02-configuracao-do-git.md) | [Próxima](10-04-django-shell-comandos-uteis.md)

# 10.3 Uso do curl para testar a API

## Objetivo da aula

Executar testes rápidos de endpoints pela linha de comando com `curl`.

## Desenvolvimento

Exemplos úteis:

```shell
curl -X GET http://127.0.0.1:8000/api/categorias/
curl -X GET http://127.0.0.1:8000/api/categorias/1/
curl -X POST http://127.0.0.1:8000/api/categorias/ -d "descricao=Teste"
curl -X PUT http://127.0.0.1:8000/api/categorias/1/ -d "descricao=Teste 2"
curl -X DELETE http://127.0.0.1:8000/api/categorias/1/
```

## Hora do commit

```text
docs(secao-10): documenta uso do curl na api
```

## Conclusão

`curl` continua sendo uma ferramenta rápida para validar fluxos simples sem depender de interface gráfica.

## Próxima aula

- [10.4 Django Shell: comandos úteis](10-04-django-shell-comandos-uteis.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](10-02-configuracao-do-git.md) | [Próxima](10-04-django-shell-comandos-uteis.md)