class numberSeries:
    @staticmethod
    def calculate_gcd(a,b):
        # return a if b == 0 else calculate_gcd(b , a % b)
        return a if b == 0 else   numberSeries.calculate_gcd(b , a % b)
print(numberSeries.calculate_gcd(24,45))
print(numberSeries.calculate_gcd(100,0))
print(numberSeries.calculate_gcd(10,110))