from tkinter import *
import pytesseract
from pytesseract import image_to_string
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import cv2
import numpy as np

root = Tk()

root.iconbitmap('logo.ico')
root.title("Text Extractor")
root.geometry("550x550")

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract"


class Extraction:
    def mfileopen(self):
        file1 = filedialog.askopenfilename(initialdir='/', title="Select File",
                                           filetype=(("JPEG", "*.JPG;*.JPEG"), ("PNG", "*.PNG"), ("BMP", "*.BMP"),
                                                     ("PNM", "*.PNM"), ("JFIF", "*.JFIF"), ("TIFF", "*TIF;*.TIFF"),
                                                     ("All Files", "*.*")))
        content = image_to_string(file1)

        label = Label(text=file1)
        label.place(x=130, y=310)

        file2 = filedialog.asksaveasfile(mode='w', defaultextension=".txt")

        if file2 is NONE:
            return

        file2.write(content)

    def savefile(self):
        filedialog.asksaveasfile()


    def confirmation(self):
        messagebox.showinfo("Extraction Message", "Text Extracted")


class Editor:
    def open1(self):
        open_return = filedialog.askopenfile(title="Open file")
        if (open_return != NONE):
            self.text_area.delete(1.0, END)
            for line in open_return:
                self.text_area.insert(1.0, line)

    def open(self):
        window = tk.Toplevel(root)
        window.geometry("400x400")
        window.title("TextPad")
        self.text_area = Text(window)
        self.text_area.pack(fill=BOTH, expand=1)
        menu = Menu(window)
        window.config(menu=menu)

        FileMenu = Menu(menu)
        menu.add_cascade(label="File", menu=FileMenu)
        FileMenu.add_command(label="Open", command=object1.open1)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=FileMenu.quit)

    def about(self):
        window1 = tk.Toplevel(root)
        #window1.geometry("300x300")
        window1.title("About")
        ''''
        logo = tk.PhotoImage(file="python-logo-with_list.png")
        label = tk.Label(window1, image=logo)
        label.pack(side="right")
        '''
        content = "The purpose of the project is to extract text from image\n" \
                  " in readable and writeable form which reduces the human work\n " \
                  "like typing each and every word after looking in an image\n\n " \
                  "Coded in Language: Python 3.7"

        label1 = Label(window1, justify=LEFT, height=10, text=content).pack(side="left")
        #label.pack()

def create_window():
    window = tk.Toplevel(root)
    window.geometry("800x600")

    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract"

    class Pre:

        def original(self):
            self.image = cv2.imread(filedialog.askopenfilename(title="Select Image", filetype=(("JPEG", "*.JPG;*.JPEG"), ("PNG", "*.PNG"), ("BMP", "*.BMP"),
                                                     ("PNM", "*.PNM"), ("JFIF", "*.JFIF"), ("TIFF", "*TIF;*.TIFF"),
                                                     ("All Files", "*.*"))))
            img = cv2.imshow("Original Image", self.image)
            # return img

        def gray(self):
            self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Grayscale Image", self.gray)

        def dilation(self):
            kernel = np.ones((1, 1), np.uint8)

            # Dilation
            self.image1 = cv2.dilate(self.gray, kernel, iterations=1)
            cv2.imshow("Dilation", self.image1)

        def erosion(self):
            kernel = np.ones((1, 1), np.uint8)

            # Erosion
            self.image2 = cv2.erode(self.image1, kernel, iterations=1)
            cv2.imshow("Erosion", self.image2)

        def thresholding(self):
            ret, self.thres = cv2.threshold(self.image2, 127, 255, cv2.THRESH_BINARY)
            cv2.imshow("Threshold Binary", self.thres)

        def edgedetection(self):
            edges = cv2.Canny(self.thres, 100, 200)
            cv2.imshow("Edges Detection", edges)

        def recognition(self):
            h, w, _ = self.image.shape  # assumes color image

            # run tesseract, returning the bounding boxes
            boxes = pytesseract.image_to_boxes(self.image)  # also include any config options you use

            # draw the bounding boxes on the image
            for b in boxes.splitlines():
                b = b.split(' ')
                self.image = cv2.rectangle(self.image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])),
                                           (0, 255, 0), 2)

            cv2.imshow("Detect", self.image)

    Object = Pre()

    HeadLabel = Label(window, text="Processing of Images", height=5, font="times 24")
    HeadLabel.pack()

    preprocessinglabel = Label(window, text="Preprocessing of Images :", font="times 14")
    preprocessinglabel.place(x=100, y=180)

    Original_Image = Button(window, text="Original Image", command=Object.original)
    Original_Image.place(x=160, y=220)

    GrayButton = Button(window, text="Grayscale", command=Object.gray)
    GrayButton.place(x=280, y=220)

    DilationButton = Button(window, text="Dilation", command=Object.dilation)
    DilationButton.place(x=380, y=220)

    ErosionButton = Button(window, text="Erosion", command=Object.erosion)
    ErosionButton.place(x=480, y=220)

    segmentlabel = Label(window, text="Segmentation of Images :", font="times 14")
    segmentlabel.place(x=100, y=300)

    ThresButton = Button(window, text="Thresholding", command=Object.thresholding)
    ThresButton.place(x=160, y=340)

    edgebutton = Button(window, text="Edge Detection", command=Object.edgedetection)
    edgebutton.place(x=280, y=340)

    recognitionlabel = Label(window, text="Recognition of Images :", font="times 14")
    recognitionlabel.place(x=100, y=420)

    recognitionbutton = Button(window, text="Recognition", command=Object.recognition)
    recognitionbutton.place(x=160, y=460)

    window.mainloop()


ClassObject = Extraction()

object1 = Editor()

menu = Menu(root)
root.config(menu=menu)

FileMenu = Menu(menu)
menu.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="Open", command=object1.open)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=FileMenu.quit)

HelpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="About", command=object1.about)

image = tk.PhotoImage(file="newprojectlogo.gif")
label = tk.Label(root, image=image)
#label.place(x=0, y=0)
label.pack()

#HeadLabel = Label(root, text="Text Extraction from Images", height=5, font="times 24")
# HeadLabel.place(x=20, y=20)
#HeadLabel.pack()

SelectFile = Label(root, text="Select File for Text Extraction")
SelectFile.place(x=130, y=250)

InputButton = Button(root, text="Browse..", command=ClassObject.mfileopen)
InputButton.place(x=130, y=280)
''''
SetLocation = Label(root, text="Set Output Location")
SetLocation.place(x=130, y=340)


SetOutput = Button(root, text="Browse..", command=ClassObject.savefile)
SetOutput.place(x=130, y=380)
'''
ExtractButton = Button(root, text="Extract Text", command=ClassObject.confirmation)
ExtractButton.place(x=400, y=420)

ProcessingButton = Button(root, text="Processing", command=create_window)
ProcessingButton.place(x=300, y=420)

root.mainloop()