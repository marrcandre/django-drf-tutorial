[Início](../../README.md) | [Seção](README.md) | [Anterior](09-02-publicacao-do-projeto-no-render.md) | [Próxima](../10-ferramentas-operacao-e-apoio/README.md)

# 9.3 Armazenamento de arquivos no Cloudinary

## Objetivo da aula

Usar o Cloudinary como armazenamento persistente de arquivos e imagens do projeto.

## Introdução

Depois que o projeto vai para produção, salvar arquivos apenas no disco local deixa de ser uma boa ideia. Em plataformas modernas de deploy, o mais comum é usar um serviço externo especializado para armazenar mídias.

## Desenvolvimento

### 1. Configurando a conta

- Crie uma conta no Cloudinary.
- Copie os dados do painel para montar a `CLOUDINARY_URL`.

### 2. Variável de ambiente

```ini
CLOUDINARY_URL=cloudinary://your_api_key:your_api_secret@your_cloud_name
```

Inclua essa variável tanto no `.env` local quanto no serviço hospedado.

### 3. Teste funcional

- Coloque `MODE=MIGRATE` no `.env`.
- Faça upload de uma imagem pelo Admin.
- Confirme o arquivo no `Media Explorer` do Cloudinary.

## Hora do commit

```text
feat(9.3): implementa cloudinary para armazenamento de arquivos
```

## Prática

- Configure a variável de ambiente.
- Faça upload de uma imagem.
- Verifique o comportamento do app após novo deploy.

## Conclusão

As mídias deixam de depender do disco local do deploy e passam a ter um armazenamento externo mais adequado para aplicações reais.

## Próxima aula

- [Seção 10. Ferramentas, operação e apoio](../10-ferramentas-operacao-e-apoio/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](09-02-publicacao-do-projeto-no-render.md) | [Próxima](../10-ferramentas-operacao-e-apoio/README.md)