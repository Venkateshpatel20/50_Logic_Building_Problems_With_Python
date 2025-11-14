# Calculate the angle between hour hand and minute hand
# Given a string s represents time in 24-hour format ("HH:MM"), determine the minimum angle between /
# the hour and minute hands of an analog clock.
# Input: s = "06:00"
# Output: 180.000
# Explanation: When the time is 06:00, the angle between the /
# hour and minute hands of the clock is 180.000 degrees.

# Input: s = "03:15"
# Output: 7.500
# Explanation: When the time is 03:15, the angle between the /
# hour and minute hands of the clock is 7.500 degrees.

# Input: s = "00:00"
# Output: 0.000
# Explanation: When the time is 00:00, the angle between /
# the hour and minute hands of the clock is 0.000 degrees.



class clock_Angle:
    def calculate_angle(self,s:str):
        hours = int(s[:2])
        minutes = int(s[3:])
        hours = hours % 12 #convert 24 hours based to 12 hours based
        hours_angle = 0.5 * (hours * 60 + minutes)
        minutes_angle = 6 * minutes
        result_angle = abs(hours_angle - minutes_angle)
        return min(result_angle,360 - result_angle)

if __name__ == "__main__":
    obj = clock_Angle()
    s1 = "03:15"
    s2 = "04:15"
    print(f"angle between {s1} is : ",end="")
    print(obj.calculate_angle(s1))
    print(f"angle between {s2} is : ",end="")
    print(obj.calculate_angle(s2))
