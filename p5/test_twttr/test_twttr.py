from twttr import shorten
def main():
    test_twttr()
def test_twttr():
    assert shorten('hello')=='hll'
    assert shorten('HELLO')=='HLL'
    assert shorten('23')=='23'
    assert shorten('HELLO, world')=='HLL, wrld'
    assert shorten('_,.-')=='_,.-'
    assert shorten('HLL')=='HLL'
if __name__=='__main__':
    main()
