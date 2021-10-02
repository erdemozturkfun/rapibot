import praw

reddit = praw.Reddit(
    client_id="MFTZx6wu8I6lG-Fbi7j2lw",
    client_secret="tGMzNhKV23yRH7scYQB67XDLfUXVLg",
    user_agent="https://github.com/erdemozturkfun/rapibot",
    username="Asrielthemonster3",
    password="erdem2009.",
)

subreddit = reddit.subreddit("memes")


print(subreddit.title)
# Output: False
