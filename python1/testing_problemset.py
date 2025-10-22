#Using the following simple function write pytest unit tests for this function
import pytest

def gc_content(seq):
    valid = {'A', 'a', 'C', 'c', 'G', 'g', 'T', 't', 'N', 'n'}
    seq = seq.upper()
    if not set(seq).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(seq) == 0:
        return 0
    return (seq.count('G') + seq.count('C')) / len(seq)

def test_gc_content():
    expected = 1.0
    observed = gc_content('GCGC')
    assert expected == observed, f'Expected {expected}, got {observed}'
def test1_gc_content():    
    expected = 0.0
    observed = gc_content('ATAT')
    assert expected == observed, f'Expected {expected}, got {observed}'
def test2_gc_content():    
    expected = 0.5
    observed = gc_content('ATGC')
    assert expected == observed, f'Expected {expected}, got {observed}'
def test3_gc_content():    
    expected = 0
    observed = gc_content('')
    assert expected == observed, f'Expected {expected}, got {observed}'
def test4_gc_content():
    try:
        observed = gc_content('ATGXB')
    except ValueError:
        return
    assert False, f'expected ValueError, got {observed}'
def test5_gc_content():    
    expected = 0.3
    observed = gc_content('ATGNNNTAGC')
    assert expected == observed, f'Expected {expected}, got {observed}'
def test6_gc_content():    
    expected = 0.25
    observed = gc_content('gattacaa')
    assert expected == observed, f'Expected {expected}, got {observed}'
