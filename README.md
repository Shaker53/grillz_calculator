<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/bombucha.png" 
  title="Download button is highlighted" alt="Download_ZIP_image" width="200" height="194"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/release-v1.1-brightgreen.svg" alt="first release"/>
  <img src="https://camo.githubusercontent.com/e65c945b219ec6c6f63826a83df905b3191ae52c/68747470733a2f2f706f7365722e707567782e6f72672f6c61726176656c2f6672616d65776f726b2f6c6963656e73652e737667" 
  alt="license MIT"/>
</p>

## About Grillz calculator
**Grillz calculator** is a program for calculation and 
accounting cost of supplies, employee income and other 
order details.  
It can be used by dentistry companies, particularly by the
grillz-making dentistry companies.

## Requirements

To run this program in easy way, you need to be installed on your PC*:
  - Python 3.7 ([Mac OS](https://docs.python-guide.org/starting/install3/osx) / 
              [Linux](https://opensource.com/article/20/4/install-python-linux))
  - pip ([For all operating systems](https://pip.pypa.io/en/stable/installing))
  - xlwt**
  - xlrt**
  - PyQt5**

\* If you want to install **Grillz calculator** on **Windows**, 
please go to the [another repository](https://github.com/Shaker53/grillz_calculator_for_windows).

\** To install all additional packages in easy way, see instructions below, 
in **Installation and quick start** part.

## Installation and quick start

#### First method
Use "git clone" to copy repository to your PC and then 
in the project directory run setup.py via python.

```
# Makes your own copy of repository
git clone https://github.com/Shaker53/grillz_calculator.git

# Goes to the project directory. Plese put the directory path instead "..." !
cd .../grillz_calculator

# Install all additional libraries that are needed to run this program*
pip install -r requirements.txt

# Runs the program
python3 setup.py
```
\* In case of ```pip``` doesn't work, use ```pip3``` instead.

#### Second method
On GitHub click "Clone or download" and then "Download ZIP".
Unzip downloaded archive, go to extracted folder and
run setup.py via python
<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/ZIP.png" 
  title="Download button is highlighted" alt="Download_ZIP_image" width="600" height="304"/>
</p>

```
# Goes to the project directory. Plese put the directory path instead "..." !
cd .../grillz_calculator

# Install all additional libraries that are needed to run this program*
pip install -r requirements.txt

# Runs the program
python3 setup.py
```
\* In case of ```pip``` doesn't work, use ```pip3``` instead.

## How to use

1.  Enter all order information and press **"Calculate"**

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/calculate.png" 
  title="Calculate button is highlighted" alt="Calculate_button_image" width="600" height="369"/>
</p>

2.  Check all the costs and income

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/check.png" 
  title="You can see most of all order details" alt="Check_image" width="600" height="369"/>
</p>

3. To save order information press **"Save"**; 
program will create .xls file in the root directory of the 
project and will put all the information into it

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/save.png" 
  title="Save button is highlighted" alt="Save_button_image" width="600" height="369"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/save_ok.png" 
  title="When order is saved, you will see a notification" alt="Save_ok_image" width="600" height="369"/>
</p>

4. You can open the file with any EXEL-like app 
(Microsoft Excel, LibreOffice, OpenOffice, etc.)

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/xls1.png" 
  title="You can use it like any other Exel table" alt="xls_image_1" width="600" height="369"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/xls2.png" 
  title="You can use it like any other Exel table" alt="xls_image_2" width="600" height="369"/>
</p>

5. All subsequent times program will save orders details in 
the same file (will not create another one), on a new
string

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/xls_another.png" 
  title="New order - new string" alt="xls_another_order_image" width="600" height="369"/>
</p>

6. If you delete file or replace it to another directory
(e.g. to make an archive with the "old" orders), program 
will make a new one, as in the step 3

##### P.S.

- In the step 1 if you forget to fill in the important fields 
or make a mistake(e.g. use letters where numbers 
were expected), program will notify you about it

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/wrong.png" 
  title="Try again and press 'Calculate'" alt="Wrong_input_image" width="600" height="369"/>
</p>

- In the step 2 if you want to change something, you can press "Back"
and do it

<p align="center">
  <img src="https://raw.githubusercontent.com/Shaker53/grillz_calculator/release-1.0/resources/images/demo/back.png" 
  title="Back button is highlighted" alt="Back_button_image" width="600" height="369"/>
</p>

## Tools/Library Used
  - Python 3.7
  - PyQt5 (Python binding of Qt)
  - xlwt (Python library for writing data to .xls files)
  - xlrt (Python library for reading data from .xls files)
