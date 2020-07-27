

#  שלב 1: כרגע הצלחתי לגשת לקובץ ולהדפיס אותו

#שלב 2: המטרה כרגע תהיה לאסוף את כל הלינקים ולרכז אותם לקבוץ אחד

#שלב 3: על מנת שהספיידר יוכל לזחול על הלינקים יש להמיר אותם 
#utf-8
#https://www.webatic.com/url-convertor
#http://www.ask-tal.co.il/בלעדיות
#http://www.ask-tal.co.il/%D7%91%D7%9C%D7%A2%D7%93%D7%99%D7%95%D7%AA

#utf-8 decode
#https://stackoverflow.com/questions/52470518/parsing-xml-file-using-python3-and-beautifulsoup

"""
This program get xml map and break it into links to a text file
1.grab an xml site map

"""


from bs4 import BeautifulSoup


#Project Start
print('Start Scraping XML\n')



#Open the file and eneter it to soap object
with open("sitemap.xml") as fp:
    soup = BeautifulSoup(fp,'xml')

#print(soup.prettify())

#Find all the links

links_collection = soup.find_all("loc")

#now i got all the links and i need to throw them to a file


#after throw them to a file do some string manipulation

#print(links_collection[0])

#print(type(links_collection))

#Open a file.
f = open("sitemap.txt", "w")


#get all the link and enter them to a file.
for line in links_collection:
    #print(line.get_text())
    f.write(line.get_text()+ '\n')
f.close()

#open and read the file after the appending:
f = open("sitemap.txt", "r")
print(f.read())








