@echo off
dir /b /s %1 | findstr /r /x "^.*\.run\.go$" && go run %1 || ( start "" "C:\Users\naratteu\AppData\Local\Programs\Microsoft VS Code\Code.exe" %1 & exit )