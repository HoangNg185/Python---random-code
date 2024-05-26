# return column letter according to column number. Simple code as:
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            digit = columnNumber % 26
            result = chr(ord('A') + digit) + result
            columnNumber //= 26
        return result
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            print(f'Origin: {columnNumber}')
            columnNumber -= 1
            remainder = columnNumber % 26
            ordr = ord('A')
            chrr = chr(ordr + remainder)
            result = chrr + result
            print(f'columnNumber: {columnNumber}\nremainder: {remainder}\nord: {ordr}\nchr: {chrr}\nresult: {result}')
            columnNumber //= 26

            print('divided: ',columnNumber, '-------------')
        return result

sol = Solution()
print(sol.convertToTitle(321321213))