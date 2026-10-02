"""列表排序与同探头取数规则：默认最新靠前，同探头取最新一条。"""


def list_order_sql() -> str:
    # 新交读数排最前，避免沉到队尾
    return "ORDER BY id DESC"


def prefer_newest(rows):
    """按 id 从新到旧排列（输入为任意顺序的可迭代对象）。"""
    return sorted(rows, key=lambda r: r["id"], reverse=True)


def same_probe_latest(rows):
    """同一探头编号只保留最新（id 最大）的一条，结果整体按最新靠前排列。"""
    latest_by_probe = {}
    for r in rows:
        probe = r["probe_id"]
        cur = latest_by_probe.get(probe)
        if cur is None or r["id"] > cur["id"]:
            latest_by_probe[probe] = r
    return prefer_newest(latest_by_probe.values())


def same_probe_pick(rows):
    """取同探头若干读数中的最新一条。"""
    return max(rows, key=lambda r: r["id"]) if rows else None
