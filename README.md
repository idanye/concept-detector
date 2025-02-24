# Concept Detector

## Overview
This application extracts text from a file or URL, identifies key terms using TF-IDF, and highlights them in a GUI. It continuously transcribes speech and displays it in real-time, with keywords clickable for contextual information via Wikipedia.

## Features
- Extracts text from URLs or local files
- Identifies and highlights important keywords
- Listens to speech and transcribes in real-time
- Highlights spoken keywords in a graphical interface
- Clickable keywords show definitions

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed along with the required dependencies.

### Install Dependencies
Run the following command to install dependencies:
```sh
pip install -r requirements.txt
```

## Running the Application
To start the application, run:
```sh
python run_application.py
```

### Steps:
1. Choose an input source:
   - Press `1` to extract text from a URL.
   - Press `2` to extract text from a file.
2. The application extracts text and identifies keywords.
3. The GUI opens, continuously transcribing speech and displaying detected keywords.
4. Click on highlighted words to see Wikipedia-based explanations.
5. Close the GUI to stop the application.

## Stopping the Application
- Close the GUI window to stop transcription.
- Press `Ctrl+C` in the terminal to force exit.

## Troubleshooting
- **No text extracted?** Ensure the input URL or file is valid.
- **No keywords detected?** The input text may not contain enough significant terms.
- **Speech transcription not working?** Ensure your microphone is connected and permissions are granted.

## License
This project is open-source and available under the MIT License.

