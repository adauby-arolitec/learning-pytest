import time
class LongTimeOperation():

    @classmethod
    def calculate(cls, a:int, b:int, c:int) -> int:
        time.sleep(1)
        return a + (b * c)

