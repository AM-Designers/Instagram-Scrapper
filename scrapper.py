# Scrapes images from instagram and saves them in a folder
 
import requests
import os
import time
import random
  
   
def get_images(tag):
    url = "https://www.instagram.com/explore/tags/" + tag + "/"
    print(url)

    # get the webpage
    response = requests.get(url)

    # parse the html
    html = response.text

    # find the image url
    start = html.find("\"display_url\":\"") + len("\"display_url\":\"")
    end = html.find("\",\"is_video")
    image_url = html[start:end]
    # download the image
    print(image_url)
    response = requests.get(image_url)
    image = response.content
    # save the image
    with open(tag + ".jpg", "wb") as f:
        f.write(image)
    time.sleep(random.randint(1, 3))
    return image_url
 
def get_tags():
    # get the tags
    url = "https://www.instagram.com/explore/tags/"
    response = requests.get(url)
    html = response.text
    start = html.find("<meta property=\"og:description\"") + len("<meta property=\"og:description\"")
    end = html.find("\"/>")
    tags = html[start:end]
    tags = tags.split(",")
    return tags

  
def main():
    # get the tags
    tags = get_tags()
    # get the images
    for tag in tags:
        get_images(tag)
          
if __name__ == "__main__":
    main()
     
# end of file
#!/usr/bin/env python3
