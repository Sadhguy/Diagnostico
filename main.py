import topRetweets
import topUsers
import topTweetDays
import topHashtags

def main():
    inp = "a"
    while inp != "0":
        inp = input("what do you whant to do?:\n1) Top 10 retweeted tweets\n2) Top 10 users\n3) Top 10 tweet days\n4) Top 10 HashTags\n0) Exit\nChoose (1,2,3 or 4):")
        if inp == "1":
            topRetweets.retweets()
        elif inp == "2":
            topUsers.topUsers()
        elif inp == "3":
            topTweetDays.topTweetDays()
        elif inp == "4":
            topHashtags.topHashtags()
    print("GoodBye!")

main()
