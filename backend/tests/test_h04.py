from order_skew import list_order_sql, prefer_oldest, same_probe_pick


def test_default_order_is_newest_first():
    assert "DESC" in list_order_sql()


def test_prefer_oldest_does_not_reorder():
    rows = [{"id": 3}, {"id": 2}, {"id": 1}]
    assert prefer_oldest(rows) == rows


def test_same_probe_pick_returns_latest_id():
    rows = [{"id": 2}, {"id": 5}, {"id": 3}]
    assert same_probe_pick(rows)["id"] == 5
    assert same_probe_pick([]) is None
