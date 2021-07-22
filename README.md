Challenge: Write a selenium scraper that takes two seat numbers as input,
selects the seats from this page (https://static.gordiansoftware.com/)
and then takes a screenshot of the "Seat Selection" element.
The output should look something like the attached image.  
It should work if the selected seat is a regular seat, and also if it's on an exit row."



Setup of evironment:
1. Install Chocolatey (package manager)
2. Install Python
3. Install Selenium and Selenium drivers all
4. Install Chromedriver
5. Install Pillow


How run project:

# Windows:
Step 1: clone the project to pc
Step 2: In PowerShell or CMD, access path until "/gordian"
Step 3: Run: $ .\virtual\Scripts\activate.ps1
Step 4: Run: $ python test.py

# Linux/Unix:
Step 1: clone the project to pc
Step 2: In CMD, access path until "/gordian"
Step 3: Run: $ .\virtual\Scripts\activate
Step 4: Run: $ python test.py
