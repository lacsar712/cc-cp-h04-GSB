from h04_extra_trap import decorate_list, order_clause
from order_skew import list_order_sql, prefer_newest, same_probe_latest, same_probe_pick


def rows():
    return [
        {"id": 1, "probe_id": "探头A01", "temp_c": 4.2},
        {"id": 2, "probe_id": "探头B02", "temp_c": 12.5},
        {"id": 3, "probe_id": "探头A01", "temp_c": 5.0},
    ]


def test_desc():
    assert "DESC" in list_order_sql()
    assert "ASC" not in list_order_sql()
    assert list_order_sql() == order_clause()


def test_newest_first():
    assert [r["id"] for r in prefer_newest(rows())] == [3, 2, 1]
    assert [r["id"] for r in decorate_list(rows())] == [3, 2, 1]


def test_same_probe_picks_latest():
    a01 = [r for r in rows() if r["probe_id"] == "探头A01"]
    assert same_probe_pick(a01)["id"] == 3
    picked = {r["probe_id"]: r["id"] for r in same_probe_latest(rows())}
    assert picked == {"探头A01": 3, "探头B02": 2}
