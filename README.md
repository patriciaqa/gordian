Challenge: Write a selenium scraper that takes two seat numbers as input,
selects the seats from this page (https://static.gordiansoftware.com/)
and then takes a screenshot of the "Seat Selection" element.
The output should look something like the attached image.  
It should work if the selected seat is a regular seat, and also if it's on an exit row."



#Setup of evironment:
1. Install Chocolatey (package manager)
* https://chocolatey.org/install
2. Install Python
$ choco install python
3. Install Selenium
$ choco install selenium
4. Install Selenium drivers all
$ choco install selenium-all-drivers
5. Install Chromedriver
$ choco install chromedriver
6. Install Pillow
$  pip install Pillow
7. Install opencv-python
$ pip install opencv-python


How run project:

# Windows:
* Step 1: clone the project to pc
* Step 2: In PowerShell or CMD, access until path "/gordian"
* Step 3: Run: $ .\virtual\Scripts\activate.ps1
* Step 4: Run: $ python test.py

# Linux/Unix:
* Step 1: clone the project to pc
* Step 2: In CMD, access until path "/gordian"
* Step 3: Run: $ .\virtual\Scripts\activate
* Step 4: Run: $ python test.py
