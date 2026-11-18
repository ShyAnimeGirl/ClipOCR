import pyperclip #https://pypi.org/project/pyperclip/   required for clipboard
from notifypy import Notify #https://pypi.org/project/notify-py/  notifs, not required. 
import sys
import pytesseract
from PIL import Image, ImageGrab

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  #on the tesseract github releases page you might have to look at a previous version for it to have the windows installer
)

def send_notif(text,title):
	notification = Notify()
	notification.title = title
	notification.message = text
	notification.application_name = "ClipOCR"
	if(icon):
		notification.icon = icon_path
	if(sound):
		notification.audio = sound_path
	notification.send()

	
notifications = 1 #these settings effect the windows pop up notification
icon = 0
icon_path = "path_to_icon.png"
sound = 0
sound_path = "path_to_sound.wav"


def ocr(image):
	text = pytesseract.image_to_string(image)
	pyperclip.copy(text)
	if(notifications):
		send_notif(text,"Copied")
		
		
if len(sys.argv) > 1:
	img_path = sys.argv[1] #should prob check if it is a filepath
	
	img = Image.open(img_path)
	ocr(img)

else: #if you don't pass a file path or image 
	img = ImageGrab.grabclipboard()
	if isinstance(img, Image.Image): #actual image file is in clipboard (like with greenshot copy to clipboard)
		ocr(img)
	elif isinstance(img, list):#copying a file with explorer just creates a list of paths, only use the first one
		image_file = Image.open(img[0]) 
		ocr(image_file)
		
sys.exit(0)