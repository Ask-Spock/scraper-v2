"""
What the builder should do :

0.Create a website folder.

1. Get a ready to parse url.

1.1 Create am Html Static File with a name of the URL in Hebrew.

2.Using beautiful soap open the html page.

3.Extrat the following Data:

3.1 The page Title.

3.2 The page Contet.

3.3 The page Images.

4.Enter all the Data to the Html file.

6.Close the file.


###Testing###

webbrowser.open(sampleUrl, new=2)


"""




import webbrowser
import os
import sys
import shutil
from bs4 import BeautifulSoup


folderName = "Ask-Tal"


#moudlue costractor that callrd every time the module import
#creating a new working folder
def Moudle_init():
    
    print(" Builder Moudle is Activated \n")
    #The script need a new working folder every time its run so i delete the previes
    #and create a new one.
    deleteFolder()
    createFolder()



    #Change path to  the new dirctory
    os.chdir('./' + folderName)
    path = os.getcwd()
    print("The new path is: " + path)




#Create a folder for the website files
def createFolder():
    try:
        # Create target Directory
        os.mkdir(folderName)
        print("Directory " , folderName ,  " Created ")
    except FileExistsError:
        print("Directory " , folderName ,  " already exists")


#Delete a folder for the website files
def deleteFolder():
    # Try to remove tree; if failed show an error using try...except on screen
    try:
        shutil.rmtree(folderName)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))





def Page_Builder(Heb_Url,Soup_Url):

    #Create  file name from the URL
    #print("This is the Hebrew name of the writing file: " + Heb_Url)

    """

    There are problems with the hebrew name it should be trim
    before adding it to the ".html"


    """

    ####Remove the 'calc/'

    if Heb_Url.find('calc/') != -1:
        Heb_Url = Heb_Url.replace('calc/', "")



    #remove end of line of the str
    Heb_Url = Heb_Url.rstrip()
    #concatnating the html ending
    Heb_Url = Heb_Url + ".html"


    """
    I detected that when you created a file neame you can use special chars
    and so they should all be deleted befor the file creation
    in a trim function that will isolate only the hebrew

    """


    print(Heb_Url)



    
    #f = open(Heb_Url, "w")

    #checking if the path changed
    #path = os.getcwd()
    #print("The  path in Page_Builder is : " + path)

    """
    scraping content to the html files:
    1.Title

    2.discreoption.
    3.H1
    4.page content.
    
    """

    #Scrap Title
    #soup = BeautifulSoup(response.body, 'html.parser')
    print(Soup_Url)
 


    #close the file after the data has been writen
    #f.close()
    


#Moudlue main for testing only
if __name__ == '__main__':

    #Change path to  the new dirctory
    os.chdir('./' + folderName)
    path = os.getcwd()
    print("The new path in main is : " + path)

    #testing Url name
    page_Heb_name_Url = "בלעדיות"

    sampleUrl = "http://www.ask-tal.co.il/%D7%91%D7%9C%D7%A2%D7%93%D7%99%D7%95%D7%AA"


    #Page_Builder(page_Heb_name_Url + ".html" )

"""

***Moudlu Constractor***

"""
#This is a constrator just to create a clean folder everytime this model run
#Moudle_init()

