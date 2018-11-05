#del 0supslist.txt
#for %%i in (*.exe) do @echo %%i >> 0supslist.txt
#for %%i in (*.tgz) do @echo %%i >> 0supslist.txt
#for %%i in (*.bin) do @echo %%i >> 0supslist.txt
#for %%i in (*.uxz) do @echo %%i >> 0supslist.txt


del 0supslist.txt
for %%i in (*.exe) do @echo %%~ni >> 0supslist.txt
for %%i in (*.tgz) do @echo %%~ni >> 0supslist.txt
for %%i in (*.bin) do @echo %%~ni >> 0supslist.txt
for %%i in (*.uxz) do @echo %%~ni >> 0supslist.txt
