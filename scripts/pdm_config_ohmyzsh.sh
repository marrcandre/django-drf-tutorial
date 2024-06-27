#!/usr/bin/zsh

pdm completion zsh >> ~/.zshrc

# se não existe, cria o diretório
[ ! -d $ZSH_CUSTOM/plugins/pdm ] && mkdir $ZSH_CUSTOM/plugins/pdm

# pdm completion zsh > $ZSH_CUSTOM/plugins/pdm/_pdm

pdm --pep582 zsh > $ZSH_CUSTOM/plugins/pdm/_pdm_pep582

pdm config python.use_venv false

pdm plugin add pdm-vscode pdm-autoexport pdm-django

echo '
[[tool.pdm.autoexport]]
filename = "requirements.txt"
without-hashes = "true"
' >> pyproject.toml

source ~/.zshrc