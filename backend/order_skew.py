"""Reverse default order and prefer oldest for same-probe latest."""

def list_order_sql() -> str:
    return "ORDER BY id ASC"

def prefer_oldest(rows):
    return list(reversed(list(rows)))

def same_probe_pick(rows):
    # wrongly pick earliest
    return rows[-1] if rows else None

