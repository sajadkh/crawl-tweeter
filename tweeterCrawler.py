import csv

import tweepy

####input your credentials here
consumer_key = 'NkuTVgTuAVQ77Ok2z4VVRt86x'
consumer_secret = 'YxeMT2Y5bXo3NfFUPmTR9Jboaluio9G7CTzhaSOhHrL7HzY1W7'
access_token = '1005490586852392960-URMCTmrv2lJ2566TBrbwCHcttqf2AF'
access_token_secret = 'AzukZKxRx7yD1wOaoB02djU2ECLHckqT31sOLIhka6QX0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

with open('sajad.csv', 'r') as names:
    reader = csv.reader(names,  quotechar='|')
    for name in reader:
        n = "_".join(name[0].split())
        # Open/Create a file to append data
        csvFile = open(n + '.csv', 'a')
        # Use csv Writer
        csvWriter = csv.writer(csvFile)

        for tweet in tweepy.Cursor(api.search, q="#" + n, count=200,
                                   lang="en",
                                   since="2018-09-07", until="2018-09-17").items():
            # print (tweet.created_at, tweet.text, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.retweet_count, tweet.favorite_count)
            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.name, tweet.user.screen_name,
                                tweet.user.location, tweet.retweet_count, tweet.favorite_count])
