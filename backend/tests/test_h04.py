from order_skew import list_order_sql

def test_asc():
    assert "ASC" in list_order_sql()

