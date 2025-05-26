
# Encrypting and Decrypting app

I created this app for an NSI project at school and the goal was to make this app using the ROT13, Ceasar code, Vigenere cipher and the Polybius cipher. So this app can do all these encryptment methods.

## Installation

To run the project you'll need two things:
- 3.12.8 python version
- install requirement.txt

## Python version

First let's check your python version. If not installed yet, go to https://www.python.org/downloads/release/python-3128/.

If it's already installed go to the **cmd** and enter :
~~~
python -v
~~~
Then if it's the **3.12.8** version go to the next section, otherwise click on the previous link and install this version.

# Run the app

## With the HUB file

Double click  onto the *Hub.bat* file.

Then enter the number 1 to install all dependencies.   
After that enter 2 to run the app.

There you go, you should be running the app now !

## In the *CMD*

### Create a virtual environnement

First go in the CryptX-2000 folder using this command :

~~~
cd path\to\the\folder
~~~

**Create** a virtual environnement using the built-in package of python. Enter this command line :

~~~
python -m venv <name of the venv>
~~~

Then **activate** it :

~~~
<name of the venv>\Scripts\activate.bat
~~~

From now on you'll need to activate this venv each time you close the project and reopen it.

### Pip installation

Now before you install the 2 modules, let's check if you have any of the modules needed.

In the **cmd**, enter :

~~~
pip install -r requirement.txt
~~~

Now you should have **both** needed modules, so let's go on the next section.
You won't need to install this again if you keep opening the project in the **venv**.

### Run the app

Now go in the app folder. To do so, you have to **follow** the tree to this folder:

In the **cmd** enter this : 

~~~
cd path\to\your\folder
~~~

Then you can run it by entering :

~~~
python app.py
~~~

There you go, you should be running the app now !