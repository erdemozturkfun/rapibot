

# importing pafy module
import pafy


def geturl(url):
    
  
 
    video = pafy.new(url)
  

    best = video.getbestaudio()
    return best.url





# creating vlc media player object

 

