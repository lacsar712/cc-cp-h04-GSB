"""List ordering helpers: newest first, and same-probe pick returns the latest."""


def list_order_sql() -> str:
    return "ORDER BY id DESC"


def prefer_oldest(rows):
    # 历史函数名保留以兼容既有引用；不再倒排，原样透传（新交读数靠前）。
    return list(rows)


def same_probe_pick(rows):
    # 同代号取最新：编号最大的一条才是最新读数，与传入顺序无关。
    rows = list(rows)
    if not rows:
        return None
    return max(rows, key=lambda r: r["id"])
