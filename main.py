import json
import random
from datetime import date

# ===== 读取城市池 =====
with open("cities.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cities = data["cities"]
finished = data.get("progress", {}).get("finished", [])

# ===== 选一个没写过的城市 =====
available = [c for c in cities if c["name"] not in finished]

if not available:
    print("🎉 红河城市已经全部记录完成")
    exit()

city = random.choice(available)
city_name = city["name"]
highlight = random.choice(city["highlights"])
tone = city["tone"]

# ===== 标题模板（可持续扩展）=====
title_templates = [
    f"记录红河 · 在{city_name}，把{highlight}装进书签里",
    f"记录红河第{len(finished)+1}站｜在{city_name}，遇见时间慢下来的地方",
    f"如果说红河有一页诗，那一定写在{city_name}",
    f"我在{city_name}，用一枚纸雕记住这座城"
]

title = random.choice(title_templates)

# ===== 正文模板（你现在账号的成熟风格）=====
body = f"""
如果说红河是时间走过的痕迹，
那{city_name}，就是被慢慢保留下来的一页。

在{highlight}前，
我看着光一点点落下，
把山、水、城，
一层一层装进黄昏。

于是我把这一刻，
刻进今天的纸雕书签里。 ✂️

在这里，时间似乎走得很慢，
慢到可以看清
每一道线条的纹理。

下一站，
你想让我去红河的哪里取景？
""".strip()

# ===== 输出 =====
print("\n📌 今日标题：\n")
print(title)
print("\n📖 正文内容：\n")
print(body)

# ===== 记录进度 =====
data.setdefault("progress", {}).setdefault("finished", []).append(city_name)

with open("cities.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 已记录完成：{city_name}")
print(f"📅 日期：{date.today()}")