# File Copy System

## Description

The **File Copy System** is a Python application with a graphical user interface (GUI) for copying files from one directory to another. It allows users to select a source and destination folder, and it efficiently copies files while providing visual feedback through a progress bar and log.

The program also includes features for handling file overwriting, where the user is prompted to decide if existing files in the destination folder should be replaced.

## Features

- Simple and intuitive GUI built with Tkinter.
- Select source and destination folders for file copying.
- Progress bar indicating file copy progress.
- Log panel displaying the status of copied files.
- Option to overwrite existing files, with the ability to apply the decision to all files.

## Requirements

- Python 3.x
- Required libraries:
  - `tkinter` (included in standard Python distribution)
  - `shutil` (included in standard Python distribution)
  - `os` (included in standard Python distribution)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/FileCopySystem.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FileCopySystem
   ```

3. Ensure you have Python 3 installed on your machine.

   ```bash
   python --version
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Usage Instructions

Once you run the application, the GUI will appear. Follow the steps below to use the File Copy System:

## 1. Selecting Source Folder:

- Click the **"Seleziona Cartella Sorgente"** button to open a file dialog and choose the folder that contains the files you want to copy.
- The path of the selected folder will be displayed in the corresponding text box.

## 2. Selecting Destination Folder:

- Click the **"Seleziona Cartella Destinazione"** button to open a file dialog and choose the folder where you want to copy the files.
- The path of the destination folder will appear in the destination text box.

## 3. Copying Files:

- Once both the source and destination folders are selected, press the **"Copia e Incolla"** button to start copying the files.
- The progress bar will show the percentage of completion.
- A log of each copied file will be displayed in the log area below.

## 4. Handling File Overwrites:

If a file with the same name already exists in the destination folder, the application will prompt you with a dialog asking if you want to overwrite the file. You can either:

- Click **Yes** to overwrite the file.
- Click **No** to skip that file.
- Check the **"Applica a tutti i file"** checkbox to apply your decision to all subsequent files.

## 5. Completion:

When the file copying process is completed, a popup message will inform you that the operation was successful.
