class TimeStamp:
    """
    24小时制，以分钟为基本单位的时间戳类
    """

    __stamp: int

    def checkFormat(self, time: str) -> bool:
        """
        true:如果是正确时间格式
        """
        if not (4 <= len(time) <= 5) or time.count(':') != 1:
            return False
        timeList = time.split(':')
        return 0 <= int(timeList[0]) <= 24 and 0 <= int(timeList[1]) <= 60

    def __init__(self, time: float | int | str, minute: int = 0) -> None:
        """
        e.g. TimeStamp(5.7)
        """
        if isinstance(time, float):
            if time < 0 or time >= 25:
                raise ValueError('Time is not like that!')
            self.__stamp = round(time * 60)

        elif isinstance(time, str):
            if not self.checkFormat(time):
                raise ValueError('Time is not like that!')
            list0 = time.split(':')
            self.__stamp = int(list0[0]) * 60 + int(list0[1])

        elif isinstance(time, int):
            if time < 0 or time > 24 or minute < 0 or minute > 60:
                raise ValueError('Time is not like that!')
            self.__stamp = time * 60 + minute
        else:
            raise TypeError('Unsupported')

    def __repr__(self) -> str:
        return str(self.__stamp)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, TimeStamp):
            return False
        if self is __o:
            return True
        return __o.__stamp == self.__stamp

    def __sub__(self, another: object) -> int:
        if not isinstance(another, TimeStamp):
            raise ValueError('Can not apply two different type')
        return self.__stamp - another.__stamp


if __name__ == '__main__':
    print(
        'Input your learned times, like "15:00-17:00", end with an empty line:'
    )
    timeList = []
    line = input()
    while line != '':
        times = line.split('-')
        timeList.append(TimeStamp(times[1]) - TimeStamp(times[0]))
        line = input()
    print('You learned', sum(timeList) / 60, 'h')
