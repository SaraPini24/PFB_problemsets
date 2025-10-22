#

def isnumeric(input):
    try:
        float(input)
        output=True
    except:
        output=False
    return output

def test_isnumeric():
    expected = True
    observed = isnumeric(1.3)
def test1_isnumeric():
    expected = True
    observed = isnumeric('1.3')
def test2_isnumeric():
    expected = True
    observed = isnumeric('1e-6')
def test3_isnumeric():
    expected = True
    observed = isnumeric('-0.0001')
def test4_isnumeric():
    expected = False
    observed = isnumeric('not-a-number')