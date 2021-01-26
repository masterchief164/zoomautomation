echo hey
tskill zoom
start zoom
set a=\windows.py
CD>tmpfile
set /p b=<tmpfile
del tmpfile
set newvar=%b%%a%
python %newvar%
echo %newvar%