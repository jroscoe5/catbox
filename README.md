## catbox
Catbox is an entertainment system for cats (and other pets).

Designed for Rapberry Pi 4 with some future modules integrating sensors, can be
run on a pc as long as the relevant sensor modules are left out of the 
modules_list. Tested on Windows and Ubuntu.

---

**Setup**
1. Clone or download the repo and ensure Python 3.6 or greater is installed.

2. **POSIX** Chromedriver installation - ask Jonnie

2. Navigate to the root project directory and create a virtual environment.

    `python -m venv .env`

3. Activate virtual environment.
    
    **Windows**
    
    `.env\Scripts\activate.bat`

    **POSIX**

    `.env/bin/activate`

4. Ensure pip is up to date.

    `pip install --upgrade pip`

5. Install required modules.
    `sudo apt-get install chromium-chromedriver`
    `pip install -r requirements.txt`

6. Launch catbox :)

    `python src/catbox.py`

---

**Adding Modules**


1. To add your own custom modules, create a sub folder under `src\modules` and 
title it with the name of your new module.

2. Create the `module.py` file inside and inherit from the BaseModule.

3. Write your module and make sure any new signals are added to the BaseModule's 
codes dictionary.

4. Once finished, remember to add your module to the modules_list in 
`src\modules\__init__.py`

5. Remember, each module runs in it's own thread! 
Lastly, PR your module if you think its cool!
