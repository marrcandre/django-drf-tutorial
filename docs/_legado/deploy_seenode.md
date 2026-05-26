# A4. Publicando o projeto no Seenode

O **Seenode** é uma plataforma de hospedagem que permite publicar aplicações web, bancos de dados e outros serviços. No site existe um link para o [tutorial oficial](hhttps://docs.seenode.com/docs).

## **Criando um Banco de Dados no Seenode**

Para criar o banco de dados no **Seenode**, siga as instruções a seguir, ou leia a [documentação oficial](https://docs.seenode.com/docs/getting-started/create-database):

- Acesse o site do [Seenode](https://seenode.com/).
- Crie uma conta ou conecte-se no **Seenode**.
- Clique na opção **Create - Database**.
    - Escolha o tipo **MySQL**.
    - Escolha uma **região** onde criar o banco de dados.
    - Escolha o tipo de pacote **Free**.
    - Se preferir, mude o nome do banco de dados.
  - Clique em **Create database**.

  Obtendo as informações do banco de dados:

- Acesse o banco de dados criado.
- Em **Connection Details**, clique em **show password**.
- Em **Connection Parameters**, clique em URI.
- Copie a **URI** do banco de dados, sem o "db:" inicial.
- Armazene a **URI** do banco de dados no arquivo `.env` do projeto, como no exemplo:

```shell
# Seenode
DATABASE_URL=mysql://user:password@host:port/database
```

> Com essa informação no arquivo `.env`, o Django vai usar o banco de dados do **Seenode**. Você já pode executar o projeto, migrar a base de dados, criar um superuser ou fazer o upload dos dados e testar a aplicação executando localmente mas acessando o banco de dados remotamente.

## **Incluindo suporte ao MySQL no projeto**

**Instale o MySQL no sistema:**

- No Ubuntu:

```shell
sudo apt install mysql-server
```

- No Manjaro:

```shell
sudo pacman -S mysql
```

**Instale o pacote `mysqlclient` no projeto:**

```shell
pdm add mysqlclient
```

## Criando uma aplicação no Seenode

Vamos criar uma aplicação no Seenode para publicar o projeto. Para isso, siga as instruções a seguir ou leia a [documentação oficial](https://docs.seenode.com/docs/getting-started/create-web):

- Escolha a opção **Create - Web**.
- Escolha um repositorio do **GitHub** e clique em **Continue**.
- Escolha a branch **main** e clique em **Continue**.
- Escolha a versão do **Python** de acordo com o seu projeto.
- Em **Build Command**, coloque o comando `pip install -r requirements.txt`
- Em Run Command, coloque o comando `gunicorn app.wsgi --workers 2 --bind :80 --access-logfile -`
- Escolha uma região para hospedar a aplicação.
- Escolha o tipo de pacote **Free**.
- Clique em **Create service**.

## Adicionando variáveis de ambiente

- Adicione as variáveis de ambiente do arquivo `.env` no Seenode, em **Variables**.

## Testando a aplicação

- Acesse a URL da aplicação no Seenode e verifique se a aplicação está funcionando corretamente. Ela aparece na aba **Domains**.
