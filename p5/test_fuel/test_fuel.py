from fuel import gauge
from fuel import convert
import pytest
def main():
    test_convert()
    test_gauge()
def test_convert():
    assert convert("3/4")==75
    assert convert('1/2')==50
    with pytest.raises(ZeroDivisionError):
        convert('3/0')
    with pytest.raises(ValueError):
        convert('cat/dog')
def test_gauge():
    assert gauge(75)=='75%'
    assert gauge(99)=="F"
    assert gauge(1)=='E'
if __name__=='__main__':
    main()
