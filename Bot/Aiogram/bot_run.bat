@echo off

call %~dp0Pizza_shit\venv\Scripts\activate

cd %~dp0Pizza_shit

set TOKEN=5602698004:AAEu7iUYzQB_0voKsyLr8j1x25KbWN7ICjE

python bot_telegram.py

pause