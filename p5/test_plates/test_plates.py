from plates import is_valid
def main():
    test_1()
    test_2()
    test_3()
    test_4()
def test_1():
    assert is_valid('HELLO')==True
    assert is_valid('H')==False
    assert is_valid('20')==False
def test_2():
    assert is_valid('20HELL')==False
    assert is_valid('HELL20')==True
    assert is_valid('2HELL0')==False
    assert is_valid('HEL50L')==False
def test_3():
    assert is_valid('CS02')==False
    assert is_valid('CS50')==True
def test_4():
    assert is_valid('Lucas, ola')==False
    assert is_valid('LUC_AS')==False
    assert is_valid('LUCAS')==True
if __name__=="__main__":
    main()
