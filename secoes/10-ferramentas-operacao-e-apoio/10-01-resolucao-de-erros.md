[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](10-02-configuracao-do-git.md)

# 10.1 Resolução de erros

## Objetivo da aula

Reunir procedimentos rápidos para tratar problemas recorrentes do ambiente de desenvolvimento.

## Introdução

Todo tutorial longo acumula pequenas dores de ambiente, configuração e execução. Esta aula funciona como um ponto de apoio para esses momentos, deixando reunidas soluções que costumam economizar bastante tempo.

## Desenvolvimento

Casos cobertos nesta aula:

- liberar uma porta ocupada com `fuser -k 8000/tcp`;
- remover temporários, migrations e banco local quando necessário;
- corrigir projeto configurado com `.venv` em vez de `__pypackages__`;
- gerar nova `SECRET_KEY`;
- abrir SQLite em visualizador web;
- aumentar tempo de vida dos tokens JWT.

## Hora do commit

```text
docs(secao-10): implementa resolucao de erros
```

## Conclusão

Ter um bloco consolidado de troubleshooting reduz atrito nas próximas aulas e ajuda bastante quando alguma configuração sai do esperado.

## Próxima aula

- [10.2 Configuração do Git](10-02-configuracao-do-git.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](10-02-configuracao-do-git.md)