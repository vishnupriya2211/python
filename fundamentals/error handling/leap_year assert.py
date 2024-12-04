def is_leap_year(year):
    if year<0:
        return False
    if year % 400 == 0 and year % 100 == 0 or year % 4 ==0 and year % 100 != 0:
        return True
    else:
        return False
    
def test_leap_yaer():

    assert is_leap_year(2024)==True,"non century year"

    assert is_leap_year(2000)==False,"invalid century year"
try:
    test_leap_yaer()
    print("test case passed")

except Exception as e:
    print("test failed",e)


