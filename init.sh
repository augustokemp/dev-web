#!/bin/bash

# Open a new terminal tab for SPA
gnome-terminal -- bash -c "
# Step 1: Abrir diretório SPA
cd spa

# Step 2: Instalar dependências do SPA
npm install

# Step 3: Inicializar servidor NPM
npm run serve
"

# Open a new terminal tab for API
gnome-terminal -- bash -c "
# Step 4: Abrir diretório API
cd api

# Step 5: Criar ambiente virtual do Python
python3 -m venv .venv

# Step 6: Ativar o ambiente virtual
source .venv/bin/activate

# Step 7: Instalar as dependências do API com o requirements.txt
pip install -r requirements.txt

# Step 8: Inicialiazr o APP Uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
"
