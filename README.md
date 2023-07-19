# Sudoku Solver

This is a Sudoku solver script that automates the solving process using Selenium and Python. It is a bot scraper that reads a Sudoku puzzle from a web page and solves it. The solved solution is then automatically filled in on the Sudoku web page.

## Instructions

To use the Sudoku solver, follow the instructions below:

## Installation

1. Install virtualenv:

    ```shell
    $ pip install virtualenv
    ```

2. Create a virtual environment with the name "sudoku":

    ```shell
    $ virtualenv sudoku
    ```

3. Activate the virtual environment:

    ```shell
    $ source ./sudoku/bin/activate
    ```

4. Install the required dependencies:

    ```shell
    $ pip install -r requirements.txt
    ```

## Setup WebDriver

1. Download the compatible version of ChromeDriver based on your Google Chrome version from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/).

2. Unzip the downloaded file.

3. Make the ChromeDriver executable:

    ```shell
    $ chmod +x ./chromedriver
    ```

4. Move the ChromeDriver executable to the appropriate location:

    ```shell
    $ sudo mv ./chromedriver /usr/local/share/chromedriver
    ```

5. Create symbolic links:

    ```shell
    $ sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    $ sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    ```

6. Verify the installation:

    ```shell
    $ chromedriver --version
    ```

## Install Additional Packages

1. Install PyAutoGUI:

    ```shell
    $ pip install pyautogui
    ```

2. Install Tkinter:

    ```shell
    $ pip install tk
    ```

3. For Linux, install additional dependencies:

    ```shell
    $ sudo apt-get install scrot
    $ sudo apt-get install python3-tk
    $ sudo apt-get install python3-dev
    ```

## Running the Sudoku Solver

1. Update the URL in the script (`SolveSudoku`) to the desired Sudoku puzzle source.

2. Run the script:

    ```shell
    $ python sudoku_solver.py
    ```

3. The solved Sudoku puzzle will be printed to the console, and the solution will be automatically filled in on the Sudoku web page.

That's it! You can now solve Sudoku puzzles automatically using this script. Enjoy!
