#  67 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry > 0:
            a_digit = int(a[i]) if i >= 0 else 0
            b_digit = int(b[j]) if j >= 0 else 0
            sum_digit = a_digit + b_digit + carry
            carry = sum_digit // 2
            result.append(str(sum_digit % 2))
            i -= 1
            j -= 1

        return ''.join(result[::-1])
    
'''
while loop iterating for least significant digit of both binary strings 

extract the current digits
calc the sum, carry and store it
update the carry for  next iteration and append the least sigfig digit 
decrement the index of both strings
reverse result list  and join
'''