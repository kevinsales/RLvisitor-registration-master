<header>
  
# RLvisitor-registration
Visitort Registration System for Rizal Library
  
</header>
Please download the additional packages from

```
pip install -r requirements.txt
```
or

```
pip install qrcode
pip install opencv-python
pip install numpy
pip install pyzbar
python -m pip install Pillow
```

error handling
</br>
if you encounter this,
```
C:\Users\STUDENT\AppData\Local\Programs\Python\Python311\Lib\site-packages\django\core\management\commands\makemigrations.py:143: RuntimeWarning: Got an error checking a consistent migration history performed for database connection 'default': (1049, "Unknown database 'rlibrary'")

```
create a database from mysql
```
create database rlibrary
```
then it will properly migrate to django


error handling 2

if you encounter this,
```
FileNotFoundError: Could not find module 'C:\pyvenv\venv\Lib\site-packages\pyzbar\libzbar-64.dll' (or one of its dependencies). Try using the full path with constructor syntax.

```
download this file and run
```
https://www.microsoft.com/en-gb/download/details.aspx?id=40784
```
