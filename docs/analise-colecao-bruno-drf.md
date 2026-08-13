# Análise — Coleção Bruno para o tutorial Django + DRF

> **Status:** registro de decisão. Durante a elaboração deste documento **nenhuma coleção foi
> criada, modificada ou commitada**. Este texto consolida a análise arquitetural e as decisões
> fechadas para a futura coleção, seguindo o padrão dos demais registros em `docs/`.

Este documento **não altera** `drf-tutorial`, `template_django_pdm` nem `livraria-marrcandre-back`.
Ele apenas decide **onde** e **como** a coleção será criada.

---

## 0. Amostra analisada

- `drf-tutorial` (origin `github.com/marrcandre/django-drf-tutorial`) — README (~6.100 linhas,
  seções 1–40 + Apêndice A9) e `migracao_autenticacao.md` (material didático);
- `template_django_pdm` (origin `github.com/marrcandre/template_django_pdm`) — projeto que o aluno
  clona: `core/` (somente modelo `User`), `app/urls.py`, `app/settings.py`, `app/pagination.py`,
  `pyproject.toml` e `scripts/cria_api.py`;
- `livraria-marrcandre-back` (origin `github.com/marrcandre/livraria-marrcandre-back`) —
  implementação completa/referência (1.330 livros, Favoritos, uploads, papel `GERENTE`);
- Repositório externo `bsi4/fastapi-bsi4/http/fastapi/` e `bsi4/express-bsi4/http/express/` —
  referência do padrão de coleções Bruno já adotado (bruno.json, collection.bru, environments,
  pastas com folder.bru, assert e docs);
- Este próprio repositório (`drf-tutorial/docs/`) e `README.md` — padrão de documentação do curso;
  decisões didáticas já foram registradas em `migracao_autenticacao.md` e `docs/12-fatores.md`.

---

## 1. Contexto e problema

O curso da Livraria ensina o backend com **Django + DRF por etapas** (CRUD Categoria → Editora →
Autor → Livro → relacionamentos → upload → compras → ações → filtros/carrinho). O aluno clona o
**`template_django_pdm`** e implementa cada seção do tutorial nesse projeto. O backend completo
(`livraria-marrcandre-back`) é a implementação final do professor — **o aluno não o clona para
desenvolver**.

**Problema:** queremos uma coleção Bruno para validar cada etapa. Ela precisa (a) estar no ambiente
com o qual o aluno trabalha todos os dias, (b) funcionar em **qualquer ponto** do curso (do template
"vazio" ao projeto completo), e (c) nunca depender de features que o aluno ainda não implementou.

---

## 2. Projetos envolvidos e papéis

| Projeto | Papel | Relação com a coleção |
| --- | --- | --- |
| `drf-tutorial` | Material didático (sequência pedagógica) | Fonte da sequência; a coleção espelha o tutorial, não o contrário |
| `template_django_pdm` | **Ambiente de desenvolvimento do aluno** (clonado pela turma) | **Local da coleção** (decisão D1) |
| `http/drf/` | Coleção Bruno didática (a criar) | Validar etapa a etapa |
| `livraria-marrcandre-back` | Implementação completa/referência (professor) | **Fora** da coleção didática; mantém features extras |

Fluxo esperado:

```
drf-tutorial                    → explica o conceito (sequência pedagógica)
        ↓ como implementar
template_django_pdm             → aluno implementa (ambiente de desenvolvimento)
        ↓ contém / versiona
http/drf/  (coleção Bruno)      → aluno executa e valida cada etapa
        ®
livraria-marrcandre-back        → referência; não é a régua da coleção didática
```

---

## 3. Alternativas consideradas

### A. Coleção em `livraria-marrcandre-back/http/drf/`

| Critério | Avaliação |
| --- | --- |
| Finalidade do repo | Implementação completa/referência (estado final) |
| Público-alvo | Professor; demonstração |
| Evolução incremental | **Não acompanha** — vale só o estado final |
| Facilidade para o aluno | Baixa: o aluno não clona este repo para desenvolver |
| Risco de depender do que o aluno ainda não fez | **Altíssimo** |
| Tendência natural | Virar "catálogo" da API + features fora do tutorial |

### B. Coleção em `template_django_pdm/http/drf/` (ESCOLHIDA)

| Critério | Avaliação |
| --- | --- |
| Finalidade do repo | **Ambiente de desenvolvimento do aluno** |
| Público-alvo | Alunos (e professor, que clona como qualquer aluno) |
| Evolução incremental | Sim, **se** desenhada por estágios (seção 6) |
| Facilidade para o aluno | Máxima: já está no projeto clonado |
| Versionamento | Versionada no template; cada turma clona a versão atual |
| Manutenção | Professor atualiza o template quando o tutorial muda — fluxo único |
| Risco de dependência de features não implementadas | **Controlável por design** (pastas por estágio + asserts monotônicos) |
| Riscos | (1) resources do template servem a outros exercícios (ex.: Garagem) — mitigável com coleção enxuta + README; (2) versões do tutorial exigem versionar a coleção — organizável |

### C. Outras possibilidades

- **C1 — Duas coleções (aluno + referência):** vantajosa a longo prazo, mas duplicação e manutenção
  dupla. **Adiada**: a coleção do backend completo fica como Fase 2 opcional (seção 11).
- **C2 — Coleção no `drf-tutorial`:** o aluno clona o **template**, não o tutorial — geraria cópia
  manual e quebraria o padrão BSI4 ("coleção junto do código"). Não recomendado.
- **C3 — Repositório próprio / submodule para a coleção:** fricção desnecessária para alunos, sem
  precedente no projeto. Não recomendado como v1.
- **C4 — Compartilhamento sem duplicação (submodule/tree):** over-engineering para sala de aula.
  Não recomendado.

---

## 4. Decisões fechadas

| # | Decisão | Status |
| --- | --- | --- |
| D1 | Coleção didática em `template_django_pdm/http/drf/` | **Fechada** |
| D2 | A coleção contém **somente** o que o tutorial ensina; features do backend completo (Favoritos, carrinho do professor, documentos, `GERENTE`) ficam de fora | **Fechada** |
| D3 | Environments: apenas `Local` por ora (`baseUrl http://127.0.0.1:8000`); `Producao` adicionado depois, se necessário | **Fechada** |
| D4 | Credenciais de demonstração `a@a.com` / `teste.123` — **usadas somente a partir da seção 16** (nenhum login/credencial no piloto); senha do seed **já validada experimentalmente** (`check_password`) | **Fechada (revisada)** |
| D5 | Documento de decisão vive em `drf-tutorial/docs/analise-colecao-bruno-drf.md` (junto ao material didático) | **Fechada** |
| D6 | A coleção segue a **sequência pedagógica** do tutorial: uma pasta por estágio em que algo passa a existir; a **numeração das pastas é a sequência da coleção** (não o nº da seção). **`01 - Autenticacao` sai do início** — autenticação só tem pasta própria a partir da seção 16 | **Fechada (revisada)** |
| D7 | Validação por **asserts monotônicos** — nunca contagens/IDs fixos, nunca presença-de-campo que mude depois | **Fechada** |
| D8 | Estratégia de autenticação **revisada**: **sem JWT/bearer antes da seção 16**. Nas pastas do piloto (01–05) toda requisição é anônima (`auth: none`) e os asserts refletem o comportamento **real** do template (GET → 200; escrita → 401). O bearer entra **somente** na pasta da seção 16 (`07 - Autenticacao e permissoes/`), via login + Save-as-variable para `{{access_token}}`/`{{refresh_token}}`, com pastas `auth: inherit` a partir daí | **Fechada (revisada)** |

---

## 5. Comportamento real do template (validação experimental)

Antes de fixar convenções no piloto, o comportamento real do **`template_django_pdm`** foi validado
experimentalmente (DRF 3.17.1 / Django 5.2.15) e registrado aqui como referência.

### Configuração vigente (`app/settings.py`)

```python
DEFAULT_AUTHENTICATION_CLASSES = ('rest_framework_simplejwt.authentication.JWTAuthentication',)
DEFAULT_PERMISSION_CLASSES = ('rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',)
```

JWT é o **único** autenticador.

### Resultados observados (request anônima)

| Requisição | Status real | Observação |
| --- | --- | --- |
| `GET` (listar / por id) | **200** | leitura liberada (anon read-only) |
| `POST / PUT / PATCH / DELETE` | **401** (`NotAuthenticated`) | não é 403: como o JWT falha e é o único autenticador, `permission_denied` devolve `NotAuthenticated` (`rest_framework/views.py`) |
| mesmas escritas, **superuser autenticado** | **201 / 200 / 204** | escrita autorizada |

### Estado do banco do template

`db.sqlite3` traz **2 superusers** (`a@a.com` e `marcoandre@gmail.com`), ambos com senha
`teste.123` (validada via `check_password`) e **nenhuma entidade de domínio** (Categoria, Editora,
Autor, Livro). Ao fim da validação o banco foi restaurado ao estado original
(`git checkout -- db.sqlite3`).

### Consequências para a coleção

- O **comportamento real** (GET → 200; escrita anônima → 401) é a **referência** do piloto. Onde a
  API devolve 401, a coleção registra esse fato — não afirma 201/204.
- **Não alterar** `template_django_pdm` (auth/permissions) nem o tutorial para acomodar a coleção
  (não inflar a aula). A divergência "tutorial ensina CRUD de escrita nas seções 4–11 sem auth, mas
  o template bloqueia escrita anônima com 401" fica registrada como **pendência pedagógica do
  curso** (seção 12).
- JWT entra na coleção **apenas** a partir da seção 16 (pasta `07 - Autenticacao e permissoes/`).

---

## 6. Estratégia de evolução incremental

O aluno parte do template (só auth + usuários) e **adiciona** camadas. A coleção precisa funcionar
nessa progressão. Princípios:

- **P1. Uma pasta por estágio testável do tutorial** — não agrupar por modelo cegamente, mas por
  *momento em que aquilo passa a existir*; cada `.bru` marca no bloco `docs` a exigência "requer
  seção N do tutorial".
- **P2. Asserts monotônicos** — toda asserção continua verdadeira quando a API evolui:
  - status (`200/201/204/400/403/404`) — sempre válido;
  - eco dos campos enviados;
  - listagem paginada → checar `res.body.results` (forma do template), nunca contagens fixas;
  - busca determinística: criar registro com nome único → `GET ?search=<nome-unico>` →
    assert `results.length: eq 1`.
  - **nunca** asserir ausência de campo nem formato "congelado" que mudará depois.
- **P3. Endpoints que mudam de formato = pastas por estágio.** `Livro` e `Compra` evoluem no
  tutorial (serializers mudam nas seções 11 e 27–34). Pastas separadas: `Livros (básico)` vs
  `Livros (relacionamentos)`; `Compras CRUD` vs `Compras do usuário` vs `Preço/data/pagamento`.
- **P4. Autossuficiência de dados via "Save as variable".** A coleção cria seus próprios dados
  (categoria → `categoria_id`, editora → `editora_id`, autor → `autor_id`, livro → `livro_id`,
  compra → `compra_id`), eliminando dependência de seed/IDs fixos. Mesmo mecanismo usado para o
  token (seção 8).
- **P5. Regressão = reexecução acumulada.** Cada pasta começa com "01 - listar/revalidar" (BSI4);
  asserts monotônicos permitem reexecutar pastas anteriores após novas seções. No fim, uma pasta
  `Integração` reexecuta o ciclo completo.
- **P6. Sem engenharia reversa didática.** Não testar o *erro deliberado* que o tutorial usa para
  ensinar (ex.: `AssertionError` de itens aninhados da seção 27, que em DEBUG vira 500). Praticidade:
  valida-se o **resultado correto** após cada passo.
- **P7. Complemento + Binário (C+B).** Cada pasta documenta o comportamento **efetivo** da API
  naquele estágio do template — não o que ela "deveria" fazer. Quando uma seção nova muda o
  comportamento (ex.: seção 16 adiciona auth; seção 11 muda o serializer de Livro), a pasta daquele
  estágio registra a mudança. O Bruno **não é CI nem oráculo**: a régua pedagógica é a seção do
  tutorial; a regressão acontece porque os asserts são monotônicos.

Resultado: a coleção inteira é útil em **qualquer ponto** do curso — o aluno nunca recebe uma
coleção "quebrada", pois só executa o que já construiu.

---

## 7. Organização das pastas (revisada — piloto v1)

Estrutura em `template_django_pdm/http/drf/` (nomes no padrão BSI4 `NN - Conceito`; números *não*
são as seções do tutorial — cada pasta marca as seções que habilita):

```
http/drf/
├── bruno.json
├── collection.bru
├── environments/
│   └── Local.bru               # baseUrl 127.0.0.1:8000 (piloto: sem credenciais/IDs fixos)
├── 01 - Categorias CRUD/                # seção 4
├── 02 - Editoras CRUD/                  # seção 6
├── 03 - Autores CRUD/                   # seção 7
├── 04 - Livros basico/                  # seção 8 — payload sem FK, serializer sem depth
├── 05 - Livros relacionamentos/         # seções 9–11 — FKs, M2M, serializers
├── 06 - Upload de imagens/              # seção 12
├── 07 - Autenticacao e permissoes/      # seções 16–19 — JWT entra AQUI (D6/D8)
├── 08 - Compras CRUD/                   # seções 20–28
├── 09 - Compras do usuario/             # seções 29–30
├── 10 - Validacao/                      # seção 31 — 400s (quantidade, estoque)
├── 11 - Preco data pagamento/           # seções 32–34
├── 12 - Acoes personalizadas/           # seções 35a–35e
├── 13 - Filtros busca ordenacao/        # seções 36–38
├── 14 - Carrinho unico/                 # seções 39–40
└── 15 - Integracao/                     # cenário completo (regressão geral)
```

### Piloto v1 — pastas 01–05 (a criar nesta etapa)

Cada pasta terá `folder.bru` (`meta { name, seq }` + `auth { mode: inherit }`) e requisições
`NN - descricao.bru` com `docs{}`, asserts monotônicos e IDs capturados via Save-as-variable.

| Pasta | Seções | Requisições (`NN - descricao.bru`) |
| --- | --- | --- |
| `01 - Categorias CRUD/` | 4 | 01 listar categorias · 02 criar categoria · 03 buscar categoria por id · 04 atualizar categoria · 05 buscar categoria inexistente · 06 apagar categoria |
| `02 - Editoras CRUD/` | 6 | idem Categorias (validação espelhada) |
| `03 - Autores CRUD/` | 7 | idem Categorias (validação espelhada) |
| `04 - Livros basico/` | 8 | 01 criar livro (sem FK) · 02 listar livros · 03 buscar livro por id |
| `05 - Livros relacionamentos/` | 9–11 | 01 criar livro (com FK/M2M) · 02 listar/ler (serializer `depth=1` da seção 11) · 03 atualizar livro (serializer de escrita, sem depth) |

**Regra do piloto:** a convenção (estrutura, `docs`, asserts, tratamento das escritas anônimas 401)
é validada primeiro em `01 - Categorias CRUD/`; **só depois** replicada para `02`–`05`. Evita criar
mecanicamente pastas `buscar inexistente`/`apagar` em todos os modelos antes de a qualidade da
convenção ser aprovada. As escritas anônimas (POST/PATCH/DELETE → 401 real) seguem a decisão da
seção 12, item 2 — representadas como documentação/exemplo do estágio sem assert de 201, reduzindo
o piloto apenas quando necessário.

---

## 8. Autenticação e ambientes

O template **já vem com JWT funcionando**, mas a coleção é pedagógica: segue a sequência do
tutorial. Por isso **não há login no início da coleção** (D7/D8):

- **Nas pastas 01–05 (piloto):** toda requisição é **anônima** (`auth: none`). GET valida com 200;
  POST/PUT/PATCH/DELETE refletem o comportamento real (401, ver seção 5). O aluno primeiro
  implementa o CRUD (seções 4–11) e só na seção 16 vê autenticação.
- **Seção 16 em diante (`07 - Autenticacao e permissoes/`):** login 1×, reuso ∞. Executa
  `login.bru`; na resposta usa *Save response value as variable* (`access` → `access_token`,
  `refresh` → `refresh_token`), uma vez por sessão. A partir daí o bearer é definido **no nível da
  coleção** (`auth: bearer` com `{{access_token}}`); pastas herdam (`auth: inherit`); anônimos
  declaram `auth: none`. Nenhum token é colado manualmente. A pasta `07` demonstra a mudança de
  comportamento (regra C+B): a partir dela a escrita exige token.
- **Diferentes perfis:** o `Local.bru` guarda credenciais (`email_admin`, `email_comprador`);
  trocar de perfil = rodar `login.bru` com outro usuário e re-salvar `access_token`. Perfis:
  `a@a.com` (superuser, já no template) para "admin"; `comprador1@a.com` (criado na seção 16) para
  "comprador".
- **Ambientes:** `Local` (porta 8000) para a sala — decisão D3. Qualquer `Producao` (Fabroku) usa a
  mesma coleção trocando apenas o environment.
- **Segurança:** apenas credenciais de demonstração públicas no tutorial; enfatizar no README que
  não devem ir para produção. A senha real do seed já foi validada (D4) — credenciais entram no
  `Local.bru` somente quando a autenticação for incluída na coleção.

---

## 9. Estratégia de validação (asserts)

Objetivo: o Bruno como **validação manual/semiquantitativa de estágio**, não suíte formal (o template
já tem `pdm run test`; tanto CI quanto regressão automatizada ficam por conta dele).

Asserts recomendados (independentes de dados):

| Tipo | Exemplo |
| --- | --- |
| Status | `res.status: eq 200` (listar/ler), `401` (escrita anônima pré-seção 16 — comportamento real, seção 5), `404` (id inexistente), `400` (inválido) |
| Eco do payload | após criar Categoria com `descricao` única: `res.body.descricao: eq "<valor>"` |
| Estrutura paginada | listagem → `res.body.results` presente; nunca `length` fixo |
| Busca determinística | create com nome único → `GET ?search=<nome>` → `res.body.results.length: eq 1` |
| Relacionamento | após criar livro com `[X]` em `autores`: `res.body.autores: contains X` (validar sinônimo na gramática local durante o piloto; BSI4 usou apenas `eq`) |

Evitar: dados fixos (nº de livros), IDs fixos, ordem exata de resposta, campos que mudam de
significado entre seções.

**Limite pedagógico:** asserts checam o **contrato ensinado** (status, presença, eco — poucos por
requisição). Não virar suite de regressão nem CI; este é o papel de `pdm run test`. O Bruno fica
como "prova prática" de que a etapa da aula funcionou. Atenção: nas pastas 01–05 os asserts de
**escrita** não afirmam 201/204 (o template devolve 401 anônimo) — registram o estado real do
estágio (regra C+B).

---

## 10. Padrão BSI4 — o que manter e o que adaptar

### Manter

- Local: `http/<tecnologia>/` na raiz → `http/drf/`.
- `bruno.json` (`version/name/type`) + `collection.bru` (`meta.name`).
- `environments/` com arquivo por ambiente.
- `folder.bru` por pasta: `meta { name, seq }` + `auth { mode: inherit }`.
- Arquivos `NN - descricao.bru`; `meta { name, type: http, seq }`; método + `body:json`; `assert`; `docs`.
- Regressão: primeiro arquivo da pasta revalidando o que já deveria funcionar.
- Documentação de uso no README (estilo `fastapi-bsi4/README.md`).

### Adaptar

| Aspecto | BSI4 | Adaptação p/ Livraria |
| --- | --- | --- |
| Autenticação | não existe (`auth: none` em tudo) | **nova convenção**: bearer na coleção + `auth: none` pontual |
| Dados | fixos/em memória | **dinâmicos**: asserts monotônicos + variáveis capturadas da resposta |
| Paginação | mesma forma (`page/page_size/total_pages/results`) | idêntica — o template usa o **mesmo** `CustomPagination`; sem adaptação |
| Semântica das pastas | cada "Aula" = servidor separado | **estágio da mesma API** → pastas por estágio + asserts monotônicos |
| Environments | 1 (`Local`) só com `baseUrl` | manter, acrescentando credenciais/IDs |
| Regressão | re-testa o GET dentro do estágio | reexecutar pastas anteriores é natural (asserts monotônicos) |

---

## 11. Relação com o backend completo

O backend completo é **referência do professor**, não a régua da coleção do aluno. **Fora da coleção
didática** (presentes apenas em `livraria-marrcandre-back`):

- **Favoritos** (model/serializer/viewset; actions `POST/PUT/PATCH /api/livros/{id}/favoritar/`,
  `GET /api/favoritos/livros_com_estatisticas/`, CRUD `/api/favoritos/`);
- ações `adicionar_ao_carrinho` (`/api/livros/{id}/adicionar_ao_carrinho/` e
  `/api/compras/adicionar_ao_carrinho/`);
- **upload de documentos** (`/api/media/documents/`);
- papel `GERENTE` / campo `tipo_usuario`;
- `GET /api/schema/` e experimentações avulsas;
- qualquer feature adicionada **depois** do tutorial.

**Fase 2 (opcional):** se houver interesse em demonstrar a API completa, criar um **catálogo
separado** em `livraria-marrcandre-back/http/drf/` com essas features — como complemento, nunca
substituindo a coleção didática.

---

## 12. Pendências e divergências registradas

### Pendências resolvidas na validação experimental

1. ~~Validar a senha real do seed~~ — **feito**: `a@a.com` / `teste.123` e `marcoandre@gmail.com`
   validados (superusers, `check_password` OK); D4 condição cumprida.
2. ~~Confirmar nomenclatura das pastas~~ — **feito**: aprovado na revisão (seção 7).
3. ~~Validar suporte de asserts/Save-as-variable no Bruno~~ — **feito**: sintaxe confirmada nos
   exemplos BSI4 (`.bru`: `eq`, `docs{}`) e na documentação oficial (`https://docs.usebruno.com/
   testing/tests/assertions` e `https://docs.usebruno.com/testing/script/javascript-reference`);
   CLI disponível via `npx --yes @usebruno/cli` (v4.0.0) e GUI em `/opt/Bruno/bruno`.

### Pendências abertas

1. **Divergência pedagógica/arquitetural (decisão do curso):** o tutorial ensina CRUD de escrita
   nas seções 4–11 **sem autenticação**, mas o template bloqueia escrita anônima com **401**. A
   coleção não "conserta" isso; registra o comportamento real (C+B). O curso precisa decidir se
   ajusta o tutorial (ex.: adiar escrita anônima) ou se aceita que o aluno só consegue 201 após a
   seção 16.
2. **Representação das escritas anônimas no piloto (decisão desta etapa):** POST/PATCH/DELETE nas
   pastas 01–05 devolvem **401** de fato. Duas opções aprovadas para avaliar no piloto: (a) manter
   as requisições como **documentação/exemplo do estágio**, sem assert de 201 (o corpo mostra o
   payload que a seção ensina; o assert registra 401); (b) **reduzir o piloto** às requisições
   efetivamente validáveis (GETs). **Decisão tomada na implementação, não silenciosa** — registrada
   no relatório do piloto.
3. Confirmar em que momento a turma cria `admin1`/`comprador1` (seção 16) para os cenários de
   permissão da pasta `07`.
4. Repercussão no template (material específico da Livraria e impacto em outros usos, ex.:
   exercícios Garagem) e **README do template** com seção sobre a coleção — **só com autorização**.**

---

## 13. Próximos passos (sequência segura)

1. **Piloto v1 no template** (esta etapa): criar em `template_django_pdm/http/drf/` a base
   (`bruno.json`, `collection.bru`, `environments/Local.bru`) e as pastas **01–05**, com asserts
   monotônicos, sem JWT, sem IDs fixos, com `docs{}` e IDs via Save-as-variable. Validar a
   convenção primeiro em `01 - Categorias CRUD/` e só então replicar (seção 7). Decidir a
   representação das escritas anônimas 401 (seção 12, item 2) **sem decisão silenciosa**.
2. Validar o piloto com o Bruno (GUI `/opt/Bruno/bruno` e/ou `npx @usebruno/cli` 4.0.0) contra a
   API do template (`pdm run dev`, porta 8000).
3. Validar o piloto com um aluno fictício (banco zerado → criar dados → rodar pastas).
4. Adicionar a seção do README do template explicando o uso da coleção (**com autorização**).
5. Expandir para as pastas 06–16 após o piloto aprovado (autenticação entra na 07, seção 16).
   **06 implementada nesta etapa** (seção 14); **07 pronta** (folha à parte já criada).
6. Fase 2 (opcional): catálogo em `livraria-marrcandre-back`, somente se necessário.

---

## 14. Pasta 06 — Upload de imagens (seção 12, implementada)

**Status desta etapa:** pasta criada, validada e idempotente; artefatos de teste removidos do banco.

### Estrutura

```
http/drf/06 - Upload de imagens/
├── folder.bru                        # seq 6, auth inherit
├── 01 - login tecnico superuser.bru  # POST /api/token/ → access_token_upload (auth none)
├── 02 - listar imagens.bru           # GET /api/media/images/ → 200, results definido
├── 03 - enviar imagem.bru            # POST /api/media/images/ multipart → 201, image_key_capa/image_url_capa
├── 04 - criar livro com capa.bru     # POST /api/livros/ c/ capa_attachment_key → 201, livro_capa_id
└── 05 - consultar livro com capa.bru # GET /api/livros/{id}/ → 200 e capa.url == image_url_capa
```

### Autenticação técnica isolada (decisão desta etapa)

A seção 12 do tutorial apresenta o **upload sem autenticação**. O backend real (template e
referência) exige autenticação para escritas. Para **validar o fluxo real** mantendo a sequência
pedagógica (06 antes de 07, sem JWT formal antes da seção 16), a pasta 06 faz **login técnico**
do superuser `a@a.com`:

- `01 - login tecnico superuser.bru`: `POST /api/token/` com `auth: none`; salva `access_token_upload`
  (variável **própria da pasta**, NÃO `access_token` da coleção — que pertence à convenção pedagógica
  da pasta 07). Sem `refresh` (desnecessário). Não altera o bearer global da coleção.
- Nas requests 02–05, o token é enviado explicitamente por request (`auth: bearer` + `access_token_upload`).
- Os `docs{}` registram essa divergência e que o token é **mecanismo técnico de validação**, não
  introdução pedagógica de JWT na seção 12 (o ensino formal fica na seção 16 / pasta 07).

### Fluxo validado (ponta a ponta)

```
upload (03) → attachment_key → criação do livro c/ capa (04) → leitura da capa (05)
```

- `image_key_capa`/`image_url_capa` e `livro_capa_id` são variáveis próprias via Save-as-variable;
  sem IDs fixos; nome do livro usa `{{$guid}}`. Categoria, editora e autores são opcionais no
  backend, portanto a pasta não depende de IDs nem de dados de pastas anteriores.
- **Validação da resposta:** o `LivroRetrieveSerializer` não expõe `attachment_key` no objeto `capa`
  (só `url`, `description`, `uploaded_on`). A correspondência é provada por **`capa.url == url do upload`**
  — o equivalente observável de `capa.attachment_key` nesta resposta —, não por um campo ausente.

### Comportamento real registrado (divergência tutorial × backend)

| Ação | anônimo | comprador | admin | superuser |
| --- | --- | --- | --- | --- |
| `POST /api/media/images/` | 401 | 403 | 403 | 201 |

Assim, o tutorial continua apresentando upload sem autenticação na seção 12, enquanto a pasta usa
o token técnico apenas para validar a API real. JWT continua sendo introduzido pedagogicamente na
seção 16 / pasta 07.

### Idempotência e dependências

- Cada execução cria **sua própria imagem** e **seu próprio livro** (`{{$guid}}`); sem `results[0]`,
  sem imagens/livros pré-existentes, sem IDs fixos.
- **Sem dependência com a pasta 07**: a pasta é autossuficiente para o fluxo de upload (login técnico
  + `image_key_capa` próprios), sem reutilizar `access_token` nem `image_key` da pasta 07 e sem mover
  qualquer pasta.

### Validação

CLI `@usebruno/cli` 4.0.0 contra o backend real (`livraria-marrcandre-back`, porta 8011): **14/14
asserts** na execução e **14/14** na reexecução (idempotência). Banco de referência restaurado ao fim
(os dois livros e as duas imagens de teste, incluindo seus arquivos, foram removidos).

---

## 15. Pasta 08 — Compras CRUD (seções 20–28, implementada)

**Status desta etapa:** pasta criada, validada e idempotente; ambiente de teste descartável limpo após validação.

### Estrutura

```
http/drf/08 - Compras CRUD/
├── folder.bru                           # seq 8, auth inherit
├── 01 - listar compras.bru              # GET /api/compras/ → 200, results definido
├── 02 - criar livro para compra.bru     # POST /api/livros/ → 201, livro_compra_id e titulo_livro_compra
├── 03 - criar compra com itens aninhados.bru # POST /api/compras/ → 201, compra_id (capturado via res.body.id)
├── 04 - consultar compra criada.bru     # GET /api/compras/{id}/ → 200, compra_id e itens detalhados
├── 05 - substituir itens da compra.bru  # PUT /api/compras/{id}/ → 200, substituição atômica de itens
└── 06 - atualizar compra parcialmente.bru # PATCH /api/compras/{id}/ → 200, atualização parcial
```

### Ambiente e Backend de Referência

- **Projeto de referência:** `livraria_3info3_2026_2`
- **Commit de referência:** `686311b` (*feat: criação de um endpoint para atualizar compras*)
- **Configuração de execução:** Git worktree descartável isolado, servido em `127.0.0.1:8012` com banco SQLite descartável fora dos repositórios principais.
- **Correção pontual do serializer:** Inclusão de `'id'` na tupla `fields` de `CompraCreateUpdateSerializer` (`fields = ('id', 'usuario', 'itens')`). Essa adaptação permite que o `POST` de criação de compras retorne o ID gerado pelo servidor, possibilitando a captura dinâmica `bru.setVar('compra_id', res.body.id)` sem IDs fixos ou heurísticas.

### Validação HTTP e Comportamento dos Verbos

A validação direta via HTTP no backend de referência confirmou:
1. **`POST /api/compras/`**: Retorna `HTTP 201 Created` contendo `id`, `usuario` e `itens`.
2. **`GET /api/compras/{id}/`**: Retorna `HTTP 200 OK` contendo os detalhes da compra, dados aninhados do livro e totais calculados.
3. **`PUT /api/compras/{id}/`**: Retorna `HTTP 200 OK` realizando a substituição atômica dos itens via `update()` do serializer e devolvendo o `id`.
4. **`PATCH /api/compras/{id}/`**:
   - Sem envio de `itens`: Preserva os itens existentes e retorna `HTTP 200 OK`.
   - Com envio de `itens`: Substitui os itens conforme a lógica da Seção 28 do tutorial e retorna `HTTP 200 OK` com `id`.

### Métricas de Execução da Coleção (Bruno CLI 4.0.0)

- **Coleção / Pastas validadas:** `07 - Autenticacao e permissoes` + `08 - Compras CRUD`.
- **Total de requisições:** 27 requisições (21 da pasta 07 + 6 da pasta 08).
- **Total de asserções:** 67 asserções (41 da pasta 07 + 26 da pasta 08).
- **Taxa de sucesso:** 100% de aprovação (0 falhas).
- **Confirmação de Reexecução e Idempotência:** Duas execuções completas acumuladas foram executadas via Bruno CLI 4.0.0. Ambas obtiveram **67/67 asserções aprovadas**, confirmando autonomia total e ausência de acoplamento a IDs fixos.
