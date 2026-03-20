[Início](../../README.md) | [Seção](README.md) | [Anterior](02-03-criacao-de-uma-api-rest.md) | [Próxima](../03-modelagem-e-crud-base/README.md)

# 2.4 Conectando a API ao frontend com Vue 3

## Objetivo da aula

Criar a base do frontend em Vue 3 e confirmar a comunicação entre a aplicação cliente e a API da `Categoria`.

## Introdução

Até aqui, a API de `Categoria` já foi criada e testada no backend. Agora vamos consumir essa API em uma aplicação real de frontend.

## Desenvolvimento

### 1. Objetivo da etapa

Nesta aula você vai:

- criar uma aplicação Vue 3 a partir de um template;
- executar o projeto localmente;
- conectar o frontend com a API da `Categoria`;
- confirmar que os dados estão vindo do backend.

### 2. Criando o projeto a partir do template

Vamos usar um template já estruturado para acelerar o processo.

Acesse o repositório:

https://github.com/marrcandre/template-vue3

Passos:

1. Clique em `Use this template`.
2. Escolha `Create a new repository`.
3. Dê um nome para o projeto, por exemplo `livraria-frontend`.
4. Clone o repositório para o seu computador.

### 3. Instalando as dependências

Entre na pasta do projeto e execute:

```bash
npm install
```

### 4. Executando a aplicação

Depois da instalação, execute:

```bash
npm run dev
```

Se tudo estiver correto, a aplicação será iniciada em:

```text
http://localhost:3000
```

### 5. Conectando com a API da Categoria

Certifique-se de que sua API Django esteja rodando em:

```text
http://127.0.0.1:8000
```

E que o endpoint funcione:

```text
http://127.0.0.1:8000/api/categorias/
```

Se a aplicação Vue estiver configurada corretamente, ela deverá buscar os dados da API e exibir as categorias na tela.

### 6. Se os dados não aparecerem

Caso nada seja exibido:

1. Pressione `F12` no navegador.
2. Vá até a aba `Network`.
3. Verifique se a requisição foi feita.
4. Observe possíveis erros:
   - erro de CORS;
   - erro 404;
   - erro 500;
   - URL incorreta.

Lembre-se:

- Vue roda na porta 3000;
- Django roda na porta 8000.

### 7. Entendendo o que está acontecendo

Quando a página carrega:

1. o Vue faz uma requisição HTTP com GET;
2. a API responde com JSON;
3. o Vue armazena os dados;
4. o template renderiza na tela.

### 8. Importante: NodeJS

Se você tiver problemas com `npm`, verifique se está usando a versão LTS do NodeJS.

Consulte o material do Prof. Eduardo da Silva:

https://eduardo-da-silva.github.io/aula-desenvolvimento-web/ambiente

## Prática

1. Confirme se as categorias aparecem corretamente.
2. Adicione uma nova categoria pelo backend.
3. Atualize a página do frontend.
4. Verifique se o novo dado aparece.
5. Tente desligar o backend e atualizar a página.

## Conclusão

Você acabou de conectar frontend e backend, estabelecendo a base da arquitetura que será expandida nas próximas aulas.

## Próxima aula

- [Seção 3. Modelagem e CRUD base](../03-modelagem-e-crud-base/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](02-03-criacao-de-uma-api-rest.md) | [Próxima](../03-modelagem-e-crud-base/README.md)