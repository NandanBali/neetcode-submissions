import bisect

class TimedValues:
    def __init__(self):
        self.time: List[int] = []
        self.values: List[str] = []

class TimeMap:

    def __init__(self):
        self.db: dict[str, TimedValues] = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = TimedValues()
        self.db[key].time.append(timestamp)
        self.db[key].values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        
        index = bisect.bisect_left(self.db[key].time, timestamp)
        if index == len(self.db[key].time):
            return self.db[key].values[-1]
        elif self.db[key].time[index] == timestamp:
            return self.db[key].values[index]
        else:
            if index == 0:
                return ""
            return self.db[key].values[index - 1]
