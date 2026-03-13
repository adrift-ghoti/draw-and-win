---
description: 根據描述新增 win_checker 或 tenpai_checker 測試案例
argument-hint: "win: <描述> 或 tenpai: <描述>"
allowed-tools: Read, Edit, Bash
---

使用者想新增的測試：$ARGUMENTS

目前 test_win_checker.py 最後 20 行：
!`tail -20 "C:/Users/Username/Desktop/program/python/poker game/draw-and-win/tests/test_win_checker.py"`

目前 test_tenpai_checker.py 最後 20 行：
!`tail -20 "C:/Users/Username/Desktop/program/python/poker game/draw-and-win/tests/test_tenpai_checker.py"`

請按照以下步驟：

1. **判斷加到哪個檔案**
   - 測試「這手牌能不能胡」→ `tests/test_win_checker.py`
   - 測試「這手牌聽什麼牌」→ `tests/test_tenpai_checker.py`

2. **讀取目標檔案**，了解現有的 `c()` helper 和命名慣例

3. **設計測試案例**
   - suit: 's'=♠, 'c'=♣, 'h'=♥, 'd'=♦, 'g'=ghost，rank 1–13
   - 函式名 `test_` 開頭，清楚描述場景
   - 加一行中文註解說明在驗證什麼

4. **把測試加到檔案最後**

5. **執行新加的測試確認通過**：
```bash
cd "C:/Users/Username/Desktop/program/python/poker game/draw-and-win" && C:/Users/User/AppData/Local/Programs/Python/Python312/python.exe -m pytest tests/ -v -k "<新測試名稱>" 2>&1
```

6. 告訴使用者加了什麼、在哪一行
