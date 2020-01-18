# brew install poppler
# brew cask install pdftotext


from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTs 

Tk().withdraw() 
filelocation = askopenfilename()

# store
with open(filelocation, 'rd') as f:
    pdf = pdftotext.PDF(f)

text_as_one_string = ''

for text in pdf:
    text_as_one_string += text 
    
all_done = gTTs(text=text_as_one_string, lang='en')
all_done.save("pdf2speech.mp3")
    
