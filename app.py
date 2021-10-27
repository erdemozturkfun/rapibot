
from random import randint
import os
import praw


reddit = praw.Reddit(
    client_id=os.environ['CLIENTID'],
    client_secret=os.environ['CLIENTSECRET'],
    user_agent="https://github.com/erdemozturkfun/rapibot",
    username=os.environ['USERNAME'],
    password=os.environ['PASSWORD'],
)


def getrandomsubm():
  

  subreddit0 = reddit.subreddit("memes")
  subreddit1 = reddit.subreddit("DankMemes")
  number = randint(0, 1)
  if(number == 0):
    submission = subreddit0.random()
  else:
    submission = subreddit1.random()
  

  
  if submission.over_18:
    return "Sorry this submission is inapporiate"
  else:
    return  submission

print(getrandomsubm().title)

def getearthporn():
  subreddit = reddit.subreddit("EarthPorn")
  submission = subreddit.random()
  return submission

def getfoodporn():
  subreddit = reddit.subreddit("FoodPorn")
  submission = subreddit.random()
  return submission



def searchpost(subredditquery, postquery):
  subreddit = reddit.subreddits.search_by_name(subredditquery, include_nsfw = False, exact = False)
  firstresult = subreddit[0]

  submission  = firstresult.search(postquery)
  submission = list(submission)
  return submission[0]
    


  

# Output: False
