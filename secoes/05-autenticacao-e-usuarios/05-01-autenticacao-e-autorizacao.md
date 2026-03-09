[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](05-02-utilizacao-das-permissoes-do-drf.md)

# 5.1 Autenticação e autorização

## Objetivo da aula

Entender a diferença entre autenticação e autorização e configurar grupos, usuários e permissões básicas no Admin.

## Introdução

Nesta etapa, o foco passa a ser segurança. Autenticação responde quem é o usuário; autorização define o que ele pode fazer dentro da aplicação.

Uma estratégia prática para isso no Django é:

- criar grupos para perfis específicos;
- definir permissões nesses grupos;
- criar usuários reais;
- adicionar cada usuário aos grupos adequados;
- manter mudanças de acesso centralizadas nos grupos.

## Desenvolvimento

### 1. Relacionando CRUD, Admin, HTTP e DRF

| Ação | CRUD | Admin | Verbos HTTP | Ações do DRF |
| --- | --- | --- | --- | --- |
| Criar | Create | add | POST | create |
| Ler | Read | view | GET | retrieve, list |
| Atualizar | Update | change | PUT, PATCH | update, partial_update |
| Deletar | Delete | delete | DELETE | destroy |

Essa equivalência ajuda a entender como as permissões do Django se refletem no comportamento da API.

### 2. Criando grupos

No Admin, crie os grupos abaixo.

Grupo `administradores`:

- adicionar, editar, visualizar e remover autor, categoria e editora;
- adicionar, editar e visualizar livro.

Grupo `compradores`:

- visualizar autor, categoria e editora;
- adicionar, editar e visualizar livro.

### 3. Criando usuários

Crie os usuários abaixo e associe-os aos grupos correspondentes:

- `admin1@a.com` no grupo `administradores`;
- `comprador1@a.com` no grupo `compradores`.

### 4. Testando o acesso

Valide no Admin se cada usuário herda corretamente as permissões do grupo.

O usuário administrador deve conseguir:

- adicionar, editar, visualizar e remover autor, categoria e editora;
- adicionar, editar e visualizar livro.

O usuário comprador deve conseguir:

- apenas visualizar autor, categoria e editora;
- adicionar, editar e visualizar livro.

## Hora do commit

Mensagem sugerida na nova convenção:

```text
feat(5.1): documenta autenticacao e autorizacao
```

## Prática

- Crie os grupos e usuários propostos.
- Confirme no Admin que as permissões herdadas estão corretas.
- Revise como os nomes `add`, `view`, `change` e `delete` aparecem nas telas do Django.

## Conclusão

O projeto passa a ter uma base organizada de autorização ao usar grupos e permissões nativas do Django.

## Próxima aula

- [5.2 Utilização das permissões do DRF](05-02-utilizacao-das-permissoes-do-drf.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](README.md) | [Próxima](05-02-utilizacao-das-permissoes-do-drf.md)