class Foo:
    def __init__(self):
        pass
        self.state = [False, False, False]

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.state[0] = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while not self.state[0]:
            time.sleep(0.1)
        printSecond()
        self.state[1] = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while not self.state[1]:
            time.sleep(0.1)
        printThird()
