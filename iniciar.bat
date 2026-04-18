@echo off
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dp0iniciar.bat"
goto :EOF

:minimized
echo Iniciando o Analisador de Sentimentos...
call .venv\Scripts\activate
streamlit run app.py