#!/bin/bash

chmod +x script/convert-jupyter-quarto.sh
# Конвертация Jupyter Notebook в Quarto
quarto render EDA.ipynb --to html