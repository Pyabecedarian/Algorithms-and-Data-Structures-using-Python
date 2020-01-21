"""
Simulate a browser, write an algorithm to simulate `forward` and `backward` functions
"""
from datastruct import Stack


class Browser(object):

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.activated_url = Stack()

    def click(self, url):
        """s1 <- curr <- new_url  &  clear s2"""
        prev_url = self.activated_url.pop()
        self.activated_url.push(url)
        if prev_url:
            self.s1.push(prev_url)

        if not self.s2.isEmpty():
            self.s2.clear()

        print(f'Current page: {self.activated_url.peek()}')

    def backward(self):
        """s1 -> curr -> s2"""
        prev_url = self.s1.pop()
        if prev_url:
            curr_url = self.activated_url.pop()
            self.activated_url.push(prev_url)
            self.s2.push(curr_url)

        print(f'Current page: {self.activated_url.peek()}')

    def forward(self):
        """s1 <- curr <- s2"""
        last_url = self.s2.pop()
        if last_url:
            curr_url = self.activated_url.pop()
            self.activated_url.push(last_url)
            self.s1.push(curr_url)

        print(f'Current page: {self.activated_url.peek()}')


if __name__ == '__main__':
    url_base = 'www.simbrower.com/'
    browser = Browser()

    print('click 5 times')
    [browser.click(url_base + str(i)) for i in range(5)]

    print('\nbackward 4 times')
    [browser.backward() for _ in range(4)]

    print('\nforward 6 times')
    [browser.forward() for _ in range(6)]

    print('\nbackward 6 times')
    [browser.backward() for _ in range(6)]

    print('\nclick 5 more times')
    [browser.click(url_base + str(i)) for i in range(5, 11)]

    print('\nbackward 6 times')
    [browser.backward() for _ in range(6)]

    print('\nforward 10 times')
    [browser.forward() for _ in range(10)]