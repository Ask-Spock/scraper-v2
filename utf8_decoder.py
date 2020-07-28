"""
This file conatains only one function with Decode the Hebrew UTF-8  from the hebrew sitmap 
to a URL with can be open by Python.

The function get a UTF8 URL  and return  an encoded URL that can be open by the browser


Input: "<loc>http://www.ask-tal.co.il/קניית-דירה-התהליך-המשפטי</loc>"

Output: "http://www.ask-tal.co.il/%D7%A7%D7%A0%D7%99%D7%99%D7%AA-%D7%93%D7%99%D7%A8%D7%94-%D7%94%D7%AA%D7%94%D7%9C%D7%99%D7%9A-%D7%94%D7%9E%D7%A9%D7%A4%D7%98%D7%99"


***This function have some problems that should be solve***
1.It uppercase the middle of the url :http://www.ask-tal.co.il/CALC/
  and that should be open

2.It add some wierd chars at end of lines "%N" maybe because of the cating str()
  anyway it should be recostracted better

3.There should not be base URL Hard coded just a url that will be pass as a parameter.
"""


import webbrowser



def Decode_UTF8_URL(Web_Heb_Url,base_Url):


    #base_Url = "http://www.ask-tal.co.il/"


    #Remove <loc> from the string
    Web_Heb_Url = Web_Heb_Url.replace("<loc>", "")


    #Remove </loc> from the string
    Web_Heb_Url = Web_Heb_Url.replace("</loc>", "")


    #Remove all spaces from a the string
    Web_Heb_Url = Web_Heb_Url.replace(" ", "")


    #Cutting the Base Url to get only the Hebrew Part
    tempHebUrl = Web_Heb_Url.replace(base_Url,'')


    #print("This is the Hebrew format from the url that should be convert: \n\n" + tempHebUrl)


    #encode the Hebrew to Itf-8
    utf8_Url = tempHebUrl.encode()
    #print("The Hebrew after incoding to UTF-8 : \n\n" + str(utf8_Url))


    #Convert bytes to String
    Utf8_end_url = str(utf8_Url)


    #Replaceing \ with %
    new_Url_Utf8 = Utf8_end_url.replace('\\','%')
    #print("\n\n Replaceing \\ with % : \n\n" + new_Url_Utf8)


    #remove first 2 tabs b'   and '
    new_Url_Utf8 = new_Url_Utf8.replace("b'",'')


    #remove the '  at the end of the string
    new_Url_Utf8 = new_Url_Utf8.replace("'",'')

    #remove the 'x' char
    new_Url_Utf8 = new_Url_Utf8.replace("x",'')

    #capitalize the string
    new_Url_Utf8 = new_Url_Utf8.upper() 

    #now i need to join the unicode url to base website url it to a link
    final_Link =  base_Url + str(new_Url_Utf8)
    #This the error ptinting: print(final_Link)

    #Remove the unexplainable %B
    return_url = final_Link[:-2]
    
    #I should understand what are those "%N" that add in the end of the line and tirims
    #return_url = final_Link.strip()
    #print(return_url)
    #https://appdividend.com/2019/05/25/python-trim-string-tutorial-rstrip-lstrip-strip-example/
    #strip() -  this function maybe solve the "%N"

    return return_url





if __name__ == '__main__':

   
    print("utf8_decoder Start Running:")



"""

---trying to slove the triming problem----

example_url = "<loc>http://www.ask-tal.co.il/קניית-דירה-התהליך-המשפטי</loc>"

trimmed_url = Decode_UTF8_URL(example_url)

print(trimmed_url)

webbrowser.open(trimmed_url, new=2)
"""