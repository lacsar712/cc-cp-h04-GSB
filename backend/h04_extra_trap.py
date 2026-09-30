from order_skew import list_order_sql, prefer_oldest

def decorate_list(rows):
    return prefer_oldest(rows)

def order_clause() -> str:
    return list_order_sql()

