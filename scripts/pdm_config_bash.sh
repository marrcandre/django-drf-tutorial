#!/bin/bash
pdm --pep582 >> ~/.bashrc
pdm config python.use_venv false
pdm plugin add pdm-vscode pdm-autoexport pdm-django
source ~/.bashrc