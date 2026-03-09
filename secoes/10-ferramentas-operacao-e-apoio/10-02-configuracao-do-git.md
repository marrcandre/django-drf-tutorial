[Início](../../README.md) | [Seção](README.md) | [Anterior](10-01-resolucao-de-erros.md) | [Próxima](10-03-uso-do-curl-para-testar-a-api.md)

# 10.2 Configuração do Git

## Objetivo da aula

Configurar corretamente o Git do ambiente e evitar erros comuns de identidade ou repositório global indevido.

## Introdução

Mesmo quando o foco principal do curso é Django e DRF, a organização do código com Git faz diferença desde o começo. Uma configuração errada aqui costuma gerar confusão depois, especialmente em commits, autoria e sincronização com o GitHub.

## Desenvolvimento

Pontos principais:

- inicializar o repositório no VS Code;
- verificar se não existe um `.git` indevido na raiz do usuário;
- configurar `user.name` e `user.email` globais;
- revisar `git config -l`;
- remover `~/.gitconfig` apenas se a configuração global estiver corrompida.

## Hora do commit

```text
docs(secao-10): documenta configuracao do git
```

## Conclusão

Uma configuração correta do Git evita ruído em commits, reduz erros de autoria e deixa o trabalho com o repositório muito mais tranquilo.

## Próxima aula

- [10.3 Uso do curl para testar a API](10-03-uso-do-curl-para-testar-a-api.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](10-01-resolucao-de-erros.md) | [Próxima](10-03-uso-do-curl-para-testar-a-api.md)