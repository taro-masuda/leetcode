class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l_out = [''] * n
        for i in range(1,n+1):
            if i % 15 == 0:
                l_out[i-1] = 'FizzBuzz'
            elif i % 3 == 0:
                l_out[i-1] = 'Fizz'
            elif i % 5 == 0:
                l_out[i-1] = 'Buzz'
            else:
                l_out[i-1] = str(i)
                
        return l_out
