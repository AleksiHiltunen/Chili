@echo off
set /p ip="Enter Robots IP address:"
set /p port="Enter Robots port:"

C:\Python27\python.exe C:\Python27\Lib\chili\middleware.py --ip %ip% --port %port%
pause