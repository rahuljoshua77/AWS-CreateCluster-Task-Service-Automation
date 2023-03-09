AWS-CreateCluster-Task-Service-Automation Tool
=====================================================

Introduction
------------

This tool is a Python-based automation tool using Selenium and ChromeDriver to create clusters and tasks in Amazon Web Services (AWS). It reads input data from a file named data.txt, which contains user information and task parameters, and uses that information to automate the creation of clusters and tasks in AWS.

Requirements
------------

To use this tool, you will need to install the following:

*   Python 3.x
*   Selenium
*   ChromeDriver
*   Chrome browser
*   webdriver_manager

Installation
------------

To install the required Python packages, run the following command:

    pip install selenium webdriver_manager

You will also need to download and install the Chrome browser and ChromeDriver. ChromeDriver can be downloaded from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). After downloading, add the path to the ChromeDriver executable to your system's PATH environment variable.

Alternatively, you can use webdriver\_manager to automatically download and install ChromeDriver:

    pip install webdriver_manager

After installation, you can use the following code to download and install ChromeDriver automatically:

    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())

Usage
-----

To use this tool, first create a file named data.txt in the same directory as the tool. The file should contain the following information for each user, separated by a pipe symbol (|):

*   typeuser: The type of user (e.g. root, iam)
*   email: The user's email address
*   password: The user's password
*   limitcountry: The country limit for the task
*   numberoftask: The number of tasks to create

Example data.txt file:
    
    root|admin@example.com|password123|12|1500
    root|user1@example.com|password456|11|200
    root|user2@example.com|password789|5|1002

To run the tool, execute the following command:

    python AWS-CreateCluster-Task-Service-Automation.py

The tool will read the data.txt file and use the information to automate the creation of clusters and tasks in AWS.
