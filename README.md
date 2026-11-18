# ClipOCR
A simple script to run Tesseract OCR on screenshots, or really any image file. This is designed to be used with a screenshot tool like [Greenshot](https://getgreenshot.org/) which can run external commands. The script either takes a file path to an image as an argument OR will use a file path of an image from your clipboard (CTRL-C on a file in explorer) OR an image directly from the clipboard.   

This was made for windows, linux users may have to slightly modify the script to fit their systems / screenshot program.


## Install
Install tesseract using the windows installer from the tesseract [releases page](https://github.com/tesseract-ocr/tesseract/releases)
Install the following python modules: pytesseract, pyperclip, and notify-py
In Greenshot's settings go to plugins and configure the external command plugin. Create a new entry with the command:
C:\Program Files\Python311\pythonw.exe
and the argument:
T:\Program Files\Shystudios\ClipOCR\ClipOCR.py" "{0}"

or whatever paths are appropriate for you. If you installed tesseract in a non standard location you need to edit the script.

I use this mostly by selecting the script in greenshot after taking a screenshot. You can also copy an image to the clipboard and then run the script. A custom sound and image can be added to make the notification nicer (coming soon tm)
