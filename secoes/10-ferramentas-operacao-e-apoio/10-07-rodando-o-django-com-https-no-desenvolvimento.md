[Início](../../README.md) | [Seção](README.md) | [Anterior](10-06-aplicando-os-12-fatores-ao-projeto.md) | [Próxima](../11-exercicios/README.md)

# 10.7 Rodando o Django com HTTPS no desenvolvimento

## Objetivo da aula

Executar o servidor local com HTTPS para testar fluxos que exigem conexão segura.

## Introdução

Alguns recursos simplesmente não se comportam do mesmo jeito fora de uma conexão segura. Quando isso entra em cena, testar apenas com HTTP local pode esconder problemas que só aparecem mais tarde.

## Desenvolvimento

### 1. Dependências

```bash
pdm add django-extensions werkzeug pyOpenSSL
```

### 2. Execução com certificado autoassinado

```bash
pdm run python manage.py runserver_plus --cert-file cert.pem
```

### 3. Script no `pyproject.toml`

```toml
[tool.pdm.scripts]
devssl = "python manage.py runserver_plus --cert-file cert.pem"
```

Depois disso, basta executar:

```bash
pdm devssl
```

## Hora do commit

```text
docs(secao-10): documenta https no ambiente de desenvolvimento
```

## Conclusão

Esse fluxo ajuda a testar cenários com OAuth, cookies seguros e integrações que exigem HTTPS, deixando o ambiente local mais próximo do mundo real.

## Próxima aula

- [Seção 11. Exercícios](../11-exercicios/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](10-06-aplicando-os-12-fatores-ao-projeto.md) | [Próxima](../11-exercicios/README.md)