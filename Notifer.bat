@echo off
SET LOGFILE="C:\Users\imash\Documents\notifier\log.txt"
(echo====================================================================================================== >> %LOGFILE%)
(echo Script Start Running at - ^ %date% %time% >> %LOGFILE%)
call "C:\ProgramData\Anaconda3\Scripts\activate.bat"
"C:\ProgramData\Anaconda3\python.exe" "C:\Users\imash\Documents\notifier\Notifier.py"
(echo Script Successfully Executed at - ^ %date% %time% >> %LOGFILE%)
(echo====================================================================================================== >> %LOGFILE%)
pause