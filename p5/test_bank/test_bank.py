from bank import value
def main():
    test_value1()
    test_value2()
    test_value3()
def test_value1():
    assert value("Hello, David")==0
def test_value2():
    assert value("How are you doing?")==20
def test_value3():
    assert value("Whats up?")==100
if __name__=='__main__':
    main()
