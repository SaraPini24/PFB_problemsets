#Write a function to reverse complement a DNA sequence, then write unit tests for it


def rev_compl(seq):
    valid = {'A', 'a', 'C', 'c', 'G', 'g', 'T', 't', 'N', 'n'}
    translation_tab = str.maketrans('ACTG', 'TGAC')
    seq = seq.upper()
    if not set(seq).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    else:
        seq_rev = seq[::-1]
        seq_rev_compl = seq_rev.translate(translation_tab)
    if len(seq) == 0:
        return 0
    return seq_rev_compl

def test_rev_compl():
    expected = 'ACGT'
    observed = rev_compl('acgt')
    assert expected == observed, f'expected reverse complement {expected}, got {observed}'
def test1_rev_compl():
    expected = 'ACGT'
    observed = rev_compl('ACGT')
    assert expected == observed, f'expected reverse complement {expected}, got {observed}'
def test2_rev_compl():
    expected = 'ACGT'
    observed = rev_compl('aCgT')
    assert expected == observed, f'expected reverse complement {expected}, got {observed}'
def test3_rev_compl():
    try:
        observed = rev_compl('ACGTBE')
    except ValueError:
        return
    assert False, f'expected ValueError, got {observed}'