import area
def test_areaRec():
    x=5
    y=7
    result=area.arearec(x,y)
    assert x*y==result

def test_periRec():
    x=5
    y=8
    result=area.periRec(x,y)
    assert x+x+y+y==result

def test_areaSquare():
    x=8
    result=area.areaSquare(x)
    assert x*x==result