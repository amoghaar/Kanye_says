# Import necessary libraries
import requests
from tkinter import *


# Function to get a Kanye West quote from the API
def get_quote():
    # Make a GET request to the Kanye West quote API
    response = requests.get(url="https://api.kanye.rest")

    # Check if the request was successful
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the quote from the response data
    quote = data["quote"]

    # Update the text on the canvas with the retrieved quote
    canvas.itemconfig(quote_text, text=quote)


# Create the main Tkinter window
window = Tk()

# Set the window title
window.title("Kanye Says...")

# Configure padding for the window
window.config(padx=50, pady=50)

# Create a canvas for displaying the background image and quote text
canvas = Canvas(width=300, height=414)

# Load the background image
background_img = PhotoImage(file="background.png")

# Create an image on the canvas using the background image
canvas.create_image(150, 207, image=background_img)

# Create a text element on the canvas for displaying the quote
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")

# Grid the canvas in the main window
canvas.grid(row=0, column=0)

# Load the Kanye West image
kanye_img = PhotoImage(file="kanye.png")

# Create a button with the Kanye West image that triggers the get_quote function
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)

# Grid the button in the main window
kanye_button.grid(row=1, column=0)

# Start the Tkinter event loop
window.mainloop()
