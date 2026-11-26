# 第 2 題：整理兩場電子報活動的個人優惠碼

def collect_codes(raw_codes, saved=None):
    """整理優惠碼，回傳新的串列，不修改 saved 與 raw_codes"""
    if saved is None:
        result = []
    else:
        result = saved.copy()
    for code in raw_codes:
        cleaned = code.strip().upper()
        if cleaned == "":
            continue
        if cleaned not in result:
            result.append(cleaned)
    return result


student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

saved = ["BASE"]
raw_a = [" welcome" + tail + " ", "vip" + tail, "",
         "WELCOME" + tail, " "]
raw_b = [" new" + tail + " ", " welcome" + tail + " "]

activity_a = collect_codes(raw_a, saved=saved)
activity_b = collect_codes(raw_b)

print(f"學號：{student_id}")
print(f"活動A：{activity_a}")
print(f"活動B：{activity_b}")
print(f"原始saved：{saved}")
print(f"原始raw_a：{raw_a}")
print(f"空資料：{collect_codes([])}")
