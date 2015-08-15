
import requests,bs4,os
os.makedirs('wodbimages',exist_ok=True) # Creates a directory for the images being downloaded



photolinks = [] #Array for storing the links for all of the photos

res = requests.get('http://wodb.ca/shapes.html')

res.raise_for_status()

html = bs4.BeautifulSoup(res.text,"html.parser") #Use BS to create a searchable HTML object

imageDivs = html.select(".displayed") #Store all of the div tags containing displayed images

size = len(imageDivs) #Find the number of images in the array

for image in imageDivs:
    address = "http://wodb.ca/"+image.get('src')
    photolinks.append(address)




for photolink in photolinks[:]:
    print(photolink)
    res = requests.get(photolink)
    res.raise_for_status()
    imageFile = open(os.path.join('wodbimages',os.path.basename(photolink)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
 

