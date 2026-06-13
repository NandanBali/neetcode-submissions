class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets: List[tuple[int, int, int]] = []
        self.following: dict[int, set[int]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.time, userId, tweetId))
        if userId not in self.following:
            self.following[userId] = set()
            self.following[userId].add(userId)
        self.time += 1
        print(f"{self.time}: {self.tweets} {self.following}")

    def getNewsFeed(self, userId: int) -> List[int]:

        print(f"{self.time}: {self.tweets} {self.following}")
        if userId not in self.following:
            return []
        tweets = [(x[0], x[2]) for x in self.tweets if x[1] in self.following[userId]]
        return [ x[1] for x in heapq.nlargest(10, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
            self.following[followerId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)