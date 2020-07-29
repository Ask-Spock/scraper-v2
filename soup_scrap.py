"""

--------Function Details-----------

function recive Recive:  File Hand + page Url that it should scrap from

function return : 1 for sucsess / -1 for fail

----------Function Description-----------

This function call each time with diffrent website Url and return 1 if succeded and -1 if not

Its insett a data to the relevent page.

? - Target of this page is to get the relevan part of the page.

? - Title / Description / H1 / Keywords / Content / Images if there are.

* - The content must be clean from any other non-releven objects

* - Images should be inserted to a new folder that will contain all the website images


"""


from bs4 import BeautifulSoup
import requests


def scrap_page(sample_url):
    
    page = requests.get(sample_url)


    #print(page.text)

    soup = BeautifulSoup(page.text, 'html.parser')

    print("--------script running----------------\n")


    print(soup.prettify())

   # print(soup.title)
    #print(soup.h1)

    #keywords = soup.findAll("meta",  property="keywords")
    #keywords =  soup.find(name="keywords")
    #title = soup.find("meta",  property="og:title")



    #print(keywords)




#Moudlue main for testing only
if __name__ == '__main__':

    

    sample_url = "http://www.ask-tal.co.il/%D7%91%D7%9C%D7%A2%D7%93%D7%99%D7%95%D7%AA"
    
    
    scrap_page(sample_url)


