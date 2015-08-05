__author__ = 'Perkins'

import numpy as np
import cv2

from tkinter import *
from tkinter import filedialog,StringVar
from PIL import Image, ImageFilter

class Application(Frame):
    def __init__(self,master,str_filename='coins_nonover_s.png'):
        super(Application,self).__init__(master)
        self.str_filename = str_filename
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #general instructions
        Label(self,text="This application calculates the value of\n a picture of change",justify=LEFT).grid(row=0,column=0,columnspan=5,sticky=W)
        Label(self,text="Pic File:",justify=LEFT, pady=15).grid(row=1,column=0,sticky=W)

        #create a file textbox
        self.entry_file_name = Entry(self)
        self.entry_file_name.insert(0,self.str_filename)
        self.entry_file_name.grid(row=1,column=1,columnspan=3,sticky=W)
        #this is a commentbbb
        #and another
        #create a file find button
        self.find_file_button=Button(self,text="...",command = self.find_file)
        self.find_file_button.grid(row=1,column=4,sticky=W)

        #create answer box
        self.result_button = Button(self,text="Total money =",command = self.process_image)
        self.result_button.grid(row=2,column=0,columnspan=2,sticky=W)

        self.inst_lbl3 = Label(self,text="???",justify=LEFT)
        self.inst_lbl3.grid(row=2,column=3,columnspan=2,sticky=W)

    def find_file(self):
        #TODO filepicker
        file_path = filedialog.askopenfilename()
        self.entry_file_name.delete(0,END)
        self.entry_file_name.insert(0,file_path)
        return file_path

    def opencv_contours(self):
        # Read in the image as grayscale - Note the 0 flag
        img = cv2.imread(self.entry_file_name.get(), 0)

        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        cv2.imwrite('tmp_gray.png',cimg)

        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img,(5,5),0)
        cv2.imwrite("tmp_gray_gb.png",blur)

        ret3,thresh = cv2.threshold(blur,130,255,cv2.THRESH_BINARY)
        cv2.imshow('Otsu Thresh and Gaussian Filtering',thresh)

        #imgGB = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        #image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.imshow('Contours',image)

        circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1,20, param1=90,param2=35,minRadius=0,maxRadius=0)

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('detected circles',cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''#img = cv2.medianBlur(img,9)
        #img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

        ret3,imgG = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow("Otsu's thresholding",imgG)

        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img,(5,5),0)
        ret3,imgGB = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow("Otsu's thresholding after gaussian blur",imgGB)

        circles = cv2.HoughCircles(imgGB,cv2.HOUGH_GRADIENT,1,20,
                                    param1=50,param2=30,minRadius=0,maxRadius=0)

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(imgGB,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(imgGB,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('detected circles',imgGB)
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''

    def process_image(self):
        #open file
        try:
            im = Image.open(self.entry_file_name.get())
        except:
            print ("Unable to load image " + self.entry_file_name.get())
            return

        #im.show()
        #im=im.filter(ImageFilter.FIND_EDGES)
        #im.show()

        #contours
        self.opencv_contours()
        #count size

        #add it up




#main
root = Tk()
root.title("How much money in a picture")
#root.geometry("300x500")
app=Application(root)
root.mainloop()

'''window = tkinter.Tk()
window.title("Calculate value of money")
window.geometry("200x100")

#create a frame
app = tkinter.Frame(window)
app.grid()

lbl = tkinter.Label(window,text="This application calculates the value \n of a picture of change")
lbl.grid()


window.mainloop()
window._displayof()
print("hello")'''