@echo off
echo Iniciando o Analisador de Sentimentos...
call .venv\Scripts\activate
streamlit run app.py
pause