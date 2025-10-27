class number_series():
    @staticmethod
    def reverse_num(num):
        rev = 0
        while num > 0:
            rev = rev*10 + num % 10
            num //= 10
        return rev
if __name__ == "__main__":
    ans = number_series.reverse_num(56787654)
    print(ans)#45678765
    ans = number_series.reverse_num(1000001)
    print(ans)#1000001