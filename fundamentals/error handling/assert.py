def check_number(number):
    if number >0:
        return "+ve"
    elif number <0:
        return "-ve"
    elif number==0:
        return "zero"
    
def test_num_chk():

    assert check_number(10)=="+ve","+ve number check failed"

    assert check_number(-10)=="-ve","-ve number check failed"

    assert check_number(10)=="zero","zero number check failed"

test_num_chk()