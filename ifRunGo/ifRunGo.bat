@echo off
dir /b /s %1 | findstr /r /x "^.*\.run\.go$" && go run %1 || ( start "" "C:\Users\maxon201901001\AppData\Local\Programs\Microsoft VS Code\Code.exe" %1 & exit )