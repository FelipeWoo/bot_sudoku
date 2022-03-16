# Instructions

## Install virtual env

    $ pip install virtualenv

## Create a virtual enviroment with a name

    $ virtualenv sudoku

## Activate the enviroment

    $ source ./sudoku/bin/activate

## Install webdriver manager

    $ pip install webdriver_manager

## Install selenium

    $ pip install selenium

1. Install google chrome driver

2. Open a termianl and check for google chrome version

```
$ google-chrome --version
```

3. Open a browser and from https://chromedriver.chromium.org/ download de compatible version

4. Open a terminal, unzip the file

```
$ unzip ./chromedriver_linux64.zip
```

5. Make it executable

```
$ chmod +x ./chromedriver
```

6. Move the file

```
$ sudo mv ./chromedriver /usr/local/share/chromedriver
```
7. Make a link

```
$ sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

$ sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
8. Check the version

```
$ chromedriver --version
```

# $ whereis chromedriver
#driver_location = "/usr/bin/chromedriver"
# $ whereis google-chrome
#binary_location = "/usr/bin/google-chrome"

#options = webdriver.ChromeOptions()
#options.binary_location = binary_location


#driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)


## Instal Pyautogui

    $ pip install pyautogui

## Install Tkinter

    $ pip install tk


## For linux install 

    sudo apt-get install scrot

    sudo apt-get install python3-tk

    sudo apt-get install python3-dev