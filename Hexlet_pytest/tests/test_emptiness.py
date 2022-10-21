def test_emptiness():
    stack = []
    assert not stack  # check initial status
    stack.append('one')
    assert bool(stack)  # not not stack, check the status after elements are added

    stack.pop()
    assert not stack  # check the status after the elements are extracted
