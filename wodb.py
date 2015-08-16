
import requests,bs4,os
os.makedirs('wodbimages',exist_ok=True) # Creates a directory for the images being downloaded



photolinks = [] #Array for storing the links for all of the photos

res = requests.get('http://wodb.ca/shapes.html') #This makes a request to download the entire web page from the web address.

res.raise_for_status() #If there are any errors, this will stop the program.

html = bs4.BeautifulSoup(res.text,"html.parser") #Use Beautiful Soup to create a searchable HTML object

imageDivs = html.select(".displayed") #Store all of the div tags containing images with the class "displayed"

size = len(imageDivs) #Find the number of images in the array

for image in imageDivs: #For each of the images on the page...
    address = "http://wodb.ca/"+image.get('src')
    photolinks.append(address) #...store the URL for the image in the photolinks array. 




for photolink in photolinks[:]: #For each of the links for the images on the page:
    print(photolink)
    res = requests.get(photolink) #Request the image be sent from the server
    res.raise_for_status()
    imageFile = open(os.path.join('wodbimages',os.path.basename(photolink)),'wb') #Save the image data to a file on the local computer
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close() 
 

#Now you have all of the shape images in the directory wodbimages.
#Can you change this to download the other categories of WODB images?
