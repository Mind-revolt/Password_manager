# Password_manager
Store, generate, and search through your passwords with this useful app. 

Usage:
After running the program there are three buttons you can use. 
1. Search for searching the credentials of the website;
2. Generate which generates a random password from all standard characters.
3. Add password to store the provided credentials in a data.json file.

For additional security use an encryption tool such as gpg.

Technical Description:
The code provided is a Python script that implements a password manager using the Tkinter graphical user interface library. The program allows the user to generate a random password, save login credentials for different websites, and search for saved passwords by website name.

The password generator creates a password of length 12 that includes digits, uppercase and lowercase letters, and special characters. The generated password is copied to the system clipboard, and it can be displayed in a text box in the GUI by clicking the "Generate Password" button.

The "Add Password" functionality allows the user to store login credentials for a website. The user enters the website URL, email or username, and password in text boxes in the GUI. The program then creates a nested dictionary with the website URL as the key and the email and password as the values. The dictionary is stored in a JSON file named "data.json" using the "dump" method from the "json" library. If the file already exists, the program reads the existing data from the file and updates it with the new data.

The "Search" functionality allows the user to retrieve stored login credentials for a website by entering the website URL in the GUI. If the website URL is found in the JSON file, the program displays the email and password associated with that website in a message box.

The GUI is built using the Tkinter library, and it includes labels and text boxes for the website URL, email, and password inputs, as well as buttons for generating a password, saving login credentials, and searching for passwords. The GUI also includes a logo image. The program ends when the user closes the GUI window.
