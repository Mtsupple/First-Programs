import time
import praw
import random
from random import randint

r = praw.Reddit(user_agent = "Test Python Program /u/Swift_Bot")
r.login('Swift_Bot','1spot1')

print("Logging in...")
# things to look for in comments

words_to_match = ["my life sucks", "i hate my life", "i hate everything", "i hate everyone", "fuck everything",
                  "i hate her", "i hate him","fuck her", "fuck him", "i wish i was dead"]


#responses
print ("Loading Swiftisms")


swift_quote = random.choice(open('JustSwiftThings.txt').readlines())

#prevent reposting
cache = []

def run_bot():
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit=100)
    print('reading comments...')
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print('Replying to comment...')
            comment.reply(swift_quote +
                          "\n \n" +
                          "\n \n -----------------------------------------------------------------------------------"+
                          "\n \n \n Now dont you feel better that Taylor Swift cares?")

            cache.append(comment.id)

while True:
    run_bot()
    time.sleep(1000)
    print("sleep time")
