[Início](../../README.md) | [Seção](README.md) | [Anterior](01-02-instalacao-e-sincronizacao-de-extensoes-do-vscode.md) | [Próxima](../02-inicio-do-projeto/README.md)

# 1.3 Instalação e configuração do PDM

## Objetivo da aula

Instalar e configurar o PDM para gerenciar dependências e o ambiente Python dos projetos do curso.

## Introdução

O PDM será usado para instalar dependências, executar comandos e manter o ambiente Python padronizado entre as aulas. Ele é o correspondente ao `npm` do JavaScript, mas para Python.

## Desenvolvimento

### 1. Instalação do PDM no Linux

As instruções a seguir são para Linux Manjaro e Ubuntu. Se você estiver usando outra distribuição ou quiser mais informações, consulte a documentação do [PDM](https://pdm.fming.dev/latest/).

- Abra um terminal com `Ctrl + Alt + T`.
- Verifique se o PDM está instalado:

```shell
pdm -V
```

- Se não estiver instalado, instale a versão mais recente:

```shell
curl -sSL https://pdm-project.org/install.sh | bash
```

- Após a instalação, feche o terminal com `Ctrl + D` e abra um novo terminal com `Ctrl + Alt + T` e verifique novamente a instalação.

### 2. Configuração do PDM

Execute os seguintes comandos, copiando e colando em seu terminal:

```shell
pdm --pep582 >> ~/.bashrc
pdm config python.use_venv false
pdm plugin add pdm-vscode pdm-autoexport pdm-django
```

O comando `pdm --pep582 >> ~/.bashrc` adiciona a configuração necessária para o PDM funcionar corretamente no terminal.

O comando `pdm config python.use_venv false` configura o PDM para não usar virtualenv, evitando a criação de uma pasta `.venv` no diretório do projeto. Em vez disso, ele criará uma pasta `__pypackages__` para armazenar as dependências do projeto.

Os comandos `pdm plugin add` adicionam plugins úteis para o desenvolvimento com Django e integração com o VS Code.

### 3. Verificação da configuração do PDM

Verifique se o PDM está configurado para não usar virtualenv:

```shell
pdm config
```

A saída deve conter a linha:

```text
python.use_venv: False
```

### 4. Instalação do PDM no Windows

Execute o comando abaixo no PowerShell, inclusive se estiver usando o terminal do VS Code:

```shell
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install.ps1 | iex"
```

Após instalar, no PowerShell, siga os passos de configuração do PDM conforme explicado para o Linux.

## Prática

- Verifique a versão instalada do PDM.
- Rode `pdm config` e confira o valor de `python.use_venv`.
- Confirme se os plugins foram instalados corretamente.

## Conclusão

Com o PDM configurado, o ambiente base do curso está pronto e você já pode iniciar a criação do projeto da livraria.

## Próxima aula

- [Seção 2. Início do projeto](../02-inicio-do-projeto/README.md)

[Início](../../README.md) | [Seção](README.md) | [Anterior](01-02-instalacao-e-sincronizacao-de-extensoes-do-vscode.md) | [Próxima](../02-inicio-do-projeto/README.md)