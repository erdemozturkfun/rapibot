import urllib.request
import re
import youtubeplayer


def searchyoutube(query):
  newquery = query.replace(" ", "+")
  html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + newquery)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  first_result = "https://www.youtube.com/watch?v=" + video_ids[0]
  return youtubeplayer.geturl(first_result)