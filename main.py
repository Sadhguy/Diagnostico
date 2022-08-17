import topRetweets
def main():
    inp = input("what do you whant to do?:\n1) Top 10 retweeted tweets\n2) Top 10 users\n3) Top 10 tweet days\n4) Top 10 HashTags\nChoose (1,2,3 or 4):")
    if inp == "1":
        topRetweets.retweets()

main()
