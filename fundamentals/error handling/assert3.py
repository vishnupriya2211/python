def max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
def test_max():

    assert max(10,30)==30,"failed"

    assert max(10,5)==10,"failed"

try:

    test_max()
    print("ran test passed")

except Exception as e:
    print("test failed",e)