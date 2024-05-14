#!/usr/bin/env python3
import os

def detect_shell():
    shell = os.environ.get('SHELL', '').lower()
    if 'bash' in shell:
        return 'bash'
    elif 'zsh' in shell:
        return 'zsh'
    else:
        return None

def execute_commands(shell):
    commands = {
        'bash': [
            'curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -',
            'echo \'export PATH="$HOME/.local/bin:$PATH"\' >> ~/.bashrc',
            'pdm completion bash >> ~/.bash_completion',
            'pdm --pep582 >> ~/.bashrc',
            'pdm config python.use_venv false',
            'pdm plugin add pdm-vscode pdm-autoexport pdm-django',
            'echo \'[[tool.pdm.autoexport]]\nfilename = "requirements.txt"\nwithout-hashes = "true"\' >> pyproject.toml',
            'source ~/.bashrc'
        ],
        'zsh': [
            'curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -',
            'pdm completion zsh >> ~/.zshrc',
            '[ ! -d $ZSH_CUSTOM/plugins/pdm ] && mkdir $ZSH_CUSTOM/plugins/pdm',
            'pdm completion zsh > $ZSH_CUSTOM/plugins/pdm/_pdm',
            'pdm --pep582 zsh > $ZSH_CUSTOM/plugins/pdm/_pdm_pep582',
            'pdm config python.use_venv false',
            'pdm plugin add pdm-vscode pdm-autoexport pdm-django',
            'echo \'[[tool.pdm.autoexport]]\nfilename = "requirements.txt"\nwithout-hashes = "true"\' >> pyproject.toml',
            'source ~/.zshrc'
        ]
    }

    if shell in commands:
        for cmd in commands[shell]:
            os.system(cmd)
    else:
        print("Shell não suportado ou não detectado.")

if __name__ == "__main__":
    detected_shell = detect_shell()
    if detected_shell:
        execute_commands(detected_shell)
    else:
        print("Shell não detectado.")
