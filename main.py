"""
---------------------------------------------

Work-Summery

1.get website maplink

2.run on the links and activating a function that will build an HTML file from each  one.

---------------------------------------------
"""
from bs4 import BeautifulSoup
import os
import urllib
import utf8_decoder as decoder
import webbrowser
import get_heb_url as heb_extractor
import page_builder as builder






def start_scrap(sitemap_url):
    file = urllib.request.urlopen(url)



    #Run on sitemap and isolate all the the Links
    for line in file:
        decoded_line = line.decode("utf-8")
        # * ! if there is a <loc> tag in the line extracting data function will be activated.
        if decoded_line.find('loc') != -1:
            
            #This is the Raw line from the website map: <loc>http://www.ask-tal.co.il/calc/חישוב-החזר-חודשי</loc>
            #print(decoded_line)
            
            """ decode function expalined ---> decoder.Decode_UTF8_URL()
            #Call the decoder function - get the url that python can handle
            #input: <loc>http://www.ask-tal.co.il/המשכנתא</loc>/
            #output: "http://www.ask-tal.co.il/%D7%A7%D7%A0%D7%99%D7%99%D7%AA-%D7%93%D7%99%D7%A8%D7%94

            # This Url can be open by browser in order to extract data from the page in next
            
            #Decoder function take the xml hebrew line clean it and decode it so it be usable for handling.
            """
            browser_url = decoder.Decode_UTF8_URL(decoded_line)
            print(browser_url)
            

            """
            #extract the Hebrew Url so a file with this name can be created.
            heb_url = heb_extractor.Extract_Hebrew_Url(decoded_line)
            #print(heb_url)
        
        """
            #This is the page builder function that should get two argument the heb string which will be
            #the html name and the url from it the data will be extracted.
            #Page_builder_funcrtion(heb_url,browser_url)
            
            #This is a temppry function just to create the files in the folders
            #builder.Page_Builder(heb_url,browser_url)

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


if __name__ == '__main__':

   
    print("Main Start Running:")

    """
    open the XML map of a website and  get the releven lines and encode the to handle url and
    enter the url to a Data structuer

    """


    #Open SiteMap URL File Ask-Tal
    #url = "http://www.ask-tal.co.il/map.asp"


    #Open SiteMap URL File Nadlan Deal Group
    url = "http://www.nadlandeal.co.il/map.asp"

    start_scrap(url)

    print("Main Emd its Running.")

    

   

