from order_skew import list_order_sql, prefer_newest


def decorate_list(rows):
    return prefer_newest(rows)


def order_clause() -> str:
    return list_order_sql()
