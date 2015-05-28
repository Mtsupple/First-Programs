import time
import praw
import random

r = praw.Reddit(user_agent = "Test Python Bot /u/Swift_Bot")
r.login('Swift_Bot','1spot1')

print("Logging in...")
# things to look for in comments
words_to_match = ['taylor swift','tay tay','t swifty','t-swifty','t swift','t-swifty', 't-swizzle' ]

#responses
Swiftisms = []

#prevent reposting
cache = []

def run_bot():
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit=25)
    print('reading comments...')
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print('Replying to comment...')
            comment.reply('test')
            cache.append(comment.id)

while True:
    run_bot()
    time.sleep(10)
    print("sleep time")