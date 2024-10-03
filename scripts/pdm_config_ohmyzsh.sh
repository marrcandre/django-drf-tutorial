#!/usr/bin/zsh

pdm completion zsh >> ~/.zshrc

# se não existe, cria o diretório
[ ! -d $ZSH_CUSTOM/plugins/pdm ] && mkdir $ZSH_CUSTOM/plugins/pdm

pdm --pep582 zsh > $ZSH_CUSTOM/plugins/pdm/_pdm_pep582

pdm config python.use_venv false

pdm plugin add pdm-vscode pdm-autoexport pdm-django

source ~/.zshrc