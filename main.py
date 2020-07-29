"""
---------------------------------------------

Prerquests:

set the following:
sitemap_url = "http://www.nadlandeal.co.il/map.asp"
base_url = "http://www.nadlandeal.co.il/"
folderName ="NadlanDeal"

Work-Summery

1.get website maplink

2.run on the links and activating a function that will build an HTML file from each  one.

---------------------------------------------
"""
from bs4 import BeautifulSoup
import os
import urllib
import utf8_decoder as link_decoder
import webbrowser
import get_heb_url as heb_extractor
import page_builder as builder
import urllib.request
import shutil




#moudlue costractor that callrd every time the module import
#creating a new working folder
def Moudle_init(folderName):
    
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





def start_scrap(sitemap_url,base_url):


    file = urllib.request.urlopen(sitemap_url)



    #Run on sitemap and isolate all the the relevent Links
    for line in file:
        decoded_line = line.decode("utf-8")
        # * ! if there is a <loc> tag in the line extracting data function will be activated.
        if decoded_line.find('loc') != -1:
            
            """
            ---First Test---
            <loc> extraction test.
            This print test will show onlu th <loc> 
            is the Raw line from the website map: <loc>http://www.ask-tal.co.il/calc/חישוב-החזר-חודשי</loc>
            output: only the <loc> line from the sitemap
            print(decoded_line)
            """
            
            """ 
            ---Decode function expalined ---> decoder.Decode_UTF8_URL()---

            Decoder function take the xml hebrew line clean it and decode it so it be usable for handling.
            Call the decoder function - extract  the url that python can handle
            input: <loc>http://www.ask-tal.co.il/המשכנתא</loc>/
            output: "http://www.ask-tal.co.il/%D7%A7%D7%A0%D7%99%D7%99%D7%AA-%D7%93%D7%99%D7%A8%D7%94

            browser_url: a Url can be open by browser in order to extract data from the page in next

            """
           
            browser_url = link_decoder.Decode_UTF8_URL(decoded_line,base_url)
            #print(browser_url)
            

            """
            ---Function Info: extract the Hebrew Url so a file with this name can be created---
            input: <loc>http://www.ask-tal.co.il/המשכנתא</loc>/
            output: משכנתא.html      
            """

            heb_url = heb_extractor.Extract_Hebrew_Url(decoded_line,base_url)
            #print(heb_url)
        
            
            """
            ---This function in this version should take all the content of the file and insert him to a html file so it will be ready to deploy---
            This is the page builder function that  get two argument the heb string  url  which will be scrap.
            and the hebrew name of the file that the content will be insert into.
            """
            
            builder.Page_Builder(heb_url,browser_url,folderName)

            """


            #print(browser_url)
            #print(heb_url)
            #webbrowser.open(trim_url, new=2)

            ###***Calling the Page Builder Function OR Enter the both URLs to a Data Structer***###

    ###***Decode_UTF8_URL function - There is a Bug with the calularioe URL
    ### that turn to capitlize / check if its occur in other URLS***


    #After the url are in a data structer, script should run on links and build a HTML file with the content
    #that is  needed for Google Hugo
    """



"""

App instrauction - there are two parampters that should be change the URL that will be scan and the Base-Url


"""


if __name__ == '__main__':

   
    print("Main Start Running:")

    """
    1.Run on All sitemap.
    2.get info from each file.
    3.build html file and enter it to a relevent folder.

    """




    #Open SiteMap URL File Nadlan Deal Group
    sitemap_url = "http://www.nadlandeal.co.il/map.asp"

    #The Base URL that will be Scan
    base_url = "http://www.nadlandeal.co.il/"

    #The Folder name all the file will be build into
    folderName = "NadlanDeal"

    Moudle_init(folderName)

    start_scrap(sitemap_url,base_url )

    print("Main End its Running.")

    

   

