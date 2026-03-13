---
description: 輸入一手牌，驗證是否胡牌或聽什麼牌
argument-hint: "例：s1 s2 s3 s1 g  或  ♠A ♠2 ♠3 ♠A 魃"
allowed-tools: Bash
---

使用者提供的牌：$ARGUMENTS

目前 win_checker.py 的邏輯摘要：
!`head -40 "C:/Users/Username/Desktop/program/python/poker game/draw-and-win/core/win_checker.py"`

請按照以下步驟：

1. **解析牌面**
   - suit：♠/s → s，♣/c → c，♥/h → h，♦/d → d，魃/g/ghost → g
   - rank：A=1，J=11，Q=12，K=13，ghost=0

2. **寫一段 Python 腳本並用 Bash 執行**：

```python
import sys
sys.path.insert(0, r"C:/Users/Username/Desktop/program/python/poker game/draw-and-win")
from core.card import Card, Suit, Color
from core.win_checker import check_win
from core.tenpai_checker import get_winning_cards

# 根據解析結果建立 cards（在這裡填入）
cards = [...]

if len(cards) == 5:
    result = check_win(cards)
    print("胡牌：", result)
elif len(cards) == 4:
    winning = get_winning_cards(cards)
    if winning:
        print("聽牌，可胡：", [str(c) for c in winning])
    else:
        print("未聽牌")
else:
    print(f"牌數錯誤：{len(cards)} 張（需要 4 或 5 張）")
```

3. **用中文解釋結果**，說明為什麼胡 / 不胡，或聽哪些牌
