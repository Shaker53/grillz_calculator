![first release](https://img.shields.io/badge/release-v1.0-brightgreen.svg#alignright "")

## About Grillz calculator
**Grillz calculator** is a program for calculation and 
accounting cost of supplies, employee income and other 
order details.  
It can be used by dentistry companies, particularly by the
grillz-making dentistry companies.

## Requirements

To run this program, you need to be installed on your PC:
  - Python 3
  - PyQt5

## Installation and quick start

#### First method
Use "git clone" to copy repository to your PC and then 
in the project directory run setup.py via python

```
# Makes your own copy of repository
git clone https://github.com/Shaker53/grillz_calcuator.git

# Goes to the project directory. Plese put the directory path instead "..." !
cd .../grillz_calcuator

# Runs the program
python3 setup.py
```

#### Second method
On GitHub click "Clone or download" and then "Download ZIP".
Unzip downloaded archive, go to extracted folder and
run setup.py via python
<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calcuator/release-1.0/images/demo/ZIP.png" 
  title="Download button is highlighted" alt="Download ZIP" width="600" height="369"/>
</p>

```
# Goes to the project directory. Plese put the directory path instead "..." !
cd .../grillz_calcuator

# Runs the program
python3 setup.py
```

## How to use

1.  Enter all order information and press **"Calculate"**
<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calcuator/release-1.0/images/demo/calculate.png" 
  title="Calculate button is highlighted" alt="Calculate" width="600" height="369"/>
</p>
2.  Check all the costs and income
<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calcuator/release-1.0/images/demo/check.png" 
  title="You can see most of all order details" alt="check" width="600" height="369"/>
</p>
3. To save order information press **"Save"**; 
program will create .xls file in the root directory of the 
project and will put all the information into it
<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calcuator/release-1.0/images/demo/save.png" 
  title="Save button is highlighted" alt="save" width="600" height="369"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calcuator/release-1.0/images/demo/save_ok.png" 
  title="When order is saved, you will see a notification" alt="save_ok" width="600" height="369"/>
</p>

4. You can open the file with any EXEL-like app 
(Microsoft Excel, LibreOffice, OpenOffice, etc.)
![xls1](https://clck.ru/NUUX6 "You can use it like any other Exel table")
![xls2](https://clck.ru/NUUbk "You can use it like any other Exel table")
5. All subsequent times program will save orders details in 
the same file (will not create another one), on a new
string
![xls2](https://clck.ru/NUVQE "New order - new string")
6. If you delete file or replace it to another directory
(e.g. to make an archive with the "old" orders), program 
will make a new one, as in the step 3

##### P.S.

- In the step 1 if you forget to fill in the important fields 
or make a mistake(e.g. use letters where numbers 
were expected), program will notify you about it
![wrong](https://clck.ru/NUViE "Try again and press 'Calculate'")
- In the step 2 if you want to change something, you can press "Back"
and do it
![back](https://clck.ru/NUVwR "Back button is highlighted")

## Tools/Library Used
  - Python 3
  - PyQt5 (Python binding of Qt)
  - xlwt (Python library for writing data to .xls files)
  - xlrt (Python library for reading data from .xls files)
