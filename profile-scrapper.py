# Scraps images from instagram of a specifc user and saves them in a folder
import requests 
import os
import time
import random

# get images from user profile
def get_images(username):
    url = "https://www.instagram.com/" + username + "/"
    print(url)

    # get the webpage
    response = requests.get(url)

    # parse the html
    html = response.text

    # find the image url
    start = html.find("\"display_url\":\"") + len("\"display_url\":\"")
    end = html.find("\",\"is_video")
    image_url = html[start:end]
    
    # Downloads the image
    print(image_url)
    response = requests.get(image_url)
    image = response.content
    
    # Saves the image
    with open(username + ".jpg", "wb") as f:
        f.write(image)
    time.sleep(random.randint(1, 3))
    return image_url

  
# Gets the user names
def get_users():
    # gets the tags
    url = "https://www.instagram.com/explore/tags/"
    response = requests.get(url)
    html = response.text
    start = html.find("<meta property=\"og:description\"") + len("<meta property=\"og:description\"")
    end = html.find("\"/>")
    users = html[start:end]
    users = users.split(",")
    return users

  
# main
def main():
    # get the tags
    users = get_users()
    # get the images
    for user in users:
        get_images(user)
         
if __name__ == "__main__":
    main()
     
# end of file
#!/usr/bin/env python3