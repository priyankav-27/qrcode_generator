# Streamlit QR Code Generator

This is a Streamlit application for generating QR codes. The app is styled with a dark blackish-blue background and blue buttons for a modern look.

## Features

- **Generate QR Codes**: Enter text to generate and display QR codes.
- **Customizable Theme**: Dark theme with blue buttons.

## Prerequisites

Ensure you have Python and pip installed. You will also need the following Python libraries:

- Streamlit
- Pillow
- qrcode

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory> ```
2. **Install Required Libraries**

    Install the required libraries using pip:

   ```bash
   pip install streamlit pillow qrcode
   ```
## Setting Up the Theme

1. Create a .streamlit Directory

In the root directory of your project, create a folder named .streamlit.

2. Create a Configuration File

Inside the .streamlit folder, create a file named config.toml.

3. Add Theme Configuration

Open config.toml in a text editor and add the following content:

```bash
  [theme]
primaryColor = "#007bff"                # Blue color for buttons
backgroundColor = "#0a0a0a"            # Dark blackish-blue background
secondaryBackgroundColor = "#1e1e1e"  # Slightly lighter dark blue for secondary areas
textColor = "#ffffff"                  # White text color for contrast
```
4. Save the File

Save config.toml with the above content.

## Running the App

To run the Streamlit app, use the following command:

```bash
   streamlit run your_app.py
```
Replace your_app.py with the filename of your Streamlit app.
