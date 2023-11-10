<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/SiddheshDongare/AmIVisible/main/static/assets/images/logo.png" width="100" />
<br>AmIVisible</h1>

<h3>◦ Be Connectable, Be Reachable</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=plastic&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=plastic&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=plastic&logo=javascript&logoColor=black" alt="Javascript">
<img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=plastic&logo=PyCharm&logoColor=white" alt="PyCharm">
</p>
<img src="https://badgen.net/static/version/0.1.0/" alt="Version" />
<img src="https://badgen.net/static/license/MIT/blue" alt="MIT License">
</div>

---

##  Table of Contents
- [ Table of Contents](#-table-of-contents)
- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#modules)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running AmIVisible](#-running-AmIVisible)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---


##  Overview

A simple Flask application that allows users to check if a specific port is open on a given IP address.

---

##  Features

|  	    | Type     | Description                |
| :-------- | :------- | :------------------------- |
| 🔍 | Port Checking | Allows users to check if a specific port is open on a given IP address. |
| ✅ | Dynamic Form Validation | JavaScript code is used to validate the form input fields for IP address and port, ensuring they are not empty and satisfy the required input type before submitting the form. |
| ⏬ | Dropdown Menu for Port Selection | Includes a dropdown menu with predefined ports, allowing users to select a port instead of manually entering it. |
| 👍 | Accurate Results | Displays the result of the port check on the web page, indicating whether the port is open or closed. |
| 🛑 | Error Handling | The project includes error handling for invalid input values and non-HTTP exceptions. |
---


##  Repository Structure

```sh
└── AmIVisible/
    └── static/
        ├── script.js        
        ├── style.css    
        └── assets/
            └── images/
                └── screenshots/
                    ├── homepage.jpg
                    ├── open.jpg
                    ├── closed.jpg
                ├── background.jpg
                ├── logo.png        
    └── templates/
        ├── index.html
    ├── .gitignore
    ├── LICENSE.md          
    ├── main.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
    ├── requirements.txt        
```

---


##  Modules

<details closed><summary>root</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [main.py](https://github.com/SiddheshDongare/AmIVisible/blob/main/main.py)                   | This is a simple Flask application that allows users to check if a specific port is open on a given IP address. It includes a function called `is_port_open` that uses a socket to establish a TCP connection to the specified IP and port. The user can input an IP address and a port number via a web interface. Upon submission, the entered IP and port numbers are validated, and if they are valid, the `is_port_open` function is called to check if the port is open. The result of the check is then displayed as a message on the webpage. In case of any errors during the process, appropriate error messages are displayed to the user. The application also includes an error handler to handle non-HTTP exceptions. |
| [requirements.txt](https://github.com/SiddheshDongare/AmIVisible/blob/main/requirements.txt) | The requirements.txt file lists the dependencies of the project, which include Flask, Werkzeug, socket, beautifulsoup4, render_template and requests to name a few.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

</details>

<details closed><summary>templates</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [index.html](https://github.com/SiddheshDongare/AmIVisible/blob/main/templates\index.html) | The provided code is an HTML template file that complements the Flask application mentioned earlier. It defines the structure and layout of the web form used to input the IP address and port number for port checking. It contains an HTML form with input fields for the IP address and port number. The form also includes a dropdown menu with predefined port values and an option to enter a custom port number. Upon form submission, the entered IP address and port number are sent as a POST request to the Flask application's `/` route.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

</details>

<details closed><summary>static</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [script.js](https://github.com/SiddheshDongare/AmIVisible/blob/main/templates\script.js) |  The script.js file is responsible for handling form submissions and updating the input fields dynamically. It validates the input field and populates data when a pre-defined value from the dropdown menu is selected. |
| [style.css](https://github.com/SiddheshDongare/AmIVisible/blob/main/templates\style.css) | The style.css file adds CSS style to the webpage.  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

</details>



---

##  Getting Started

###  Installation

1. Clone the AmIVisible repository:
```sh
git clone https://github.com/SiddheshDongare/AmIVisible
```

2. Change to the project directory:
```sh
cd AmIVisible
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

###  Running AmIVisible

```sh
python main.py
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/SiddheshDongare/AmIVisible/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/SiddheshDongare/AmIVisible/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/SiddheshDongare/AmIVisible/issues)**: Submit bugs found or log feature requests.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## Screenshots

![Homepage Screenshot](https://raw.githubusercontent.com/SiddheshDongare/AmIVisible/main/static/assets/images/screenshots/homepage.png)

![Open Port Screenshot](https://raw.githubusercontent.com/SiddheshDongare/AmIVisible/main/static/assets/images/screenshots/open.png)

![Closed Port Screenshot](https://raw.githubusercontent.com/SiddheshDongare/AmIVisible/main/static/assets/images/screenshots/closed.png)

---

##  License


This project is protected under the [MIT](https://choosealicense.com/mit) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit) file.

---

##  Acknowledgments

- Frontend Design Inspiration: [rickyeckhardt](https://codepen.io/rickyeckhardt/pen/poJwRRb)

[**Return**](#Top)

---

