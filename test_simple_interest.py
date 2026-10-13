from simple_interest import sim_int

def test_simple_interest_pos():
    assert sim_int(20000,8,12) == 19200

def test_simple_interest_zer():
    assert sim_int(10000,7,0) == 0  
