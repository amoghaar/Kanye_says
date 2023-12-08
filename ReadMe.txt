# Kanye Says...

## Overview
Kanye Says... is a simple Python application that fetches a random Kanye West quote from the [kanye.rest API](https://kanye.rest/) and displays it on a graphical user interface (GUI) built using the Tkinter library.

## Features
- Click the Kanye West image to fetch and display a new random quote.
- Background image and quote text are displayed on a canvas for a visually appealing interface.

## Getting Started

### Prerequisites
- Python installed (https://www.python.org/downloads/)

### Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/kanye-says.git
    ```

2. Navigate to the project directory:

    ```bash
    cd kanye-says
    ```

3. Install the required libraries:

    ```bash
    pip install requests
    ```

### Usage
1. Run the application:

    ```bash
    python kanye_says.py
    ```

2. Click the Kanye West image to get a new random quote.

## Project Structure
- `kanye_says.py`: Main Python script containing the application code.
- `background.png`: Background image used in the GUI.
- `kanye.png`: Kanye West image used as a button trigger.

## API Skills Showcase
This project demonstrates the following skills related to working with APIs:
- Using the `requests` library to make HTTP requests.
- Handling API responses, including error checking.
- Extracting and utilizing data from a JSON response.

## Dependencies
- [requests](https://docs.python-requests.org/en/latest/): A Python library for making HTTP requests.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): The standard GUI toolkit for Python.

## Acknowledgments
- Kanye.rest API for providing the random Kanye West quotes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
