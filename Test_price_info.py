from price_info import total_cost_shopping, cost_of_fruits

def test_total_cost_shopping():
    expected_total_cost = 5*1.20 + 5*1.40 + 1*6.50 + 2*2.70 + 10*0.90 + 1*2.95 + 2*4.95
    assert total_cost_shopping() == expected_total_cost

def test_cost_of_fruits():
    assert cost_of_fruits('apple', 10) == 10 * 1.20