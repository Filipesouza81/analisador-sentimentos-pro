@echo off
echo ======================================================
echo   Instalador do Analisador de Sentimentos IA
echo ======================================================
echo.
echo 1. Criando ambiente virtual (venv)...
python -m venv .venv

echo 2. Ativando ambiente e instalando dependencias...
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ======================================================
echo   Instalacao concluida com sucesso!
echo   Use o 'iniciar.bat' para abrir a interface web.
echo ======================================================
pause