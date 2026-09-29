# 占いbot ハンズオン

## ファイル構成

```
uranai/
├── fortune.py   ← 占いbotのスターターコード
├── CLAUDE.md    ← Claude Codeへの指示書（あなたが書く）
└── README.md    ← このファイル
```

> **README.md** は人間向けの説明書、**CLAUDE.md** はClaude向けの指示書です。

---

## Step 1：動かしてみる

### Google Colabの場合

新しいノートブックを開き、以下を貼り付けて実行してください。

```python
import random

FORTUNES = [
    "今日はいい日です。",
    "注意が必要な一日です。",
    "チャンスが訪れるでしょう。",
    "休息を大切にしてください。",
    "人との出会いがありそうです。",
]

def tell_fortune(name):
    fortune = random.choice(FORTUNES)
    print(f"{name}さんの今日の運勢: {fortune}")

name = input("名前を入力してください: ")
tell_fortune(name)
```

### ローカルの場合

```bash
python fortune.py
```

---

## Step 2：CLAUDE.mdなしで依頼する

Claude Codeを起動し、以下をそのまま送ってください。

```
fortune.pyをもっと面白くしてください。
```

どんな結果になったか、メモしておきましょう。

---

## Step 3：CLAUDE.mdを書く

`CLAUDE.md` を開いて、自分が作りたい占いbotのコンセプトを自由に書いてください。

書くヒント：
- **このbotは何のためのもの？**（例：学園祭 / 職場の朝礼 / 子ども向けアプリ）
- **キャラクターや口調は？**（例：ミステリアスな占い師 / 明るいアイドル）
- **運勢のカテゴリは？**（例：恋愛・仕事・健康 / ラッキーフード）
- **絵文字や言語のルールは？**

---

## Step 4：同じ依頼をもう一度

```
fortune.pyをもっと面白くしてください。
```

Step 2の結果と何が変わりましたか？

---

## ふりかえり

- CLAUDE.mdがないとき、Claudeは何を根拠に判断したと思いますか？
- README.mdとCLAUDE.mdの役割はどう違うでしょう？
- 「良いCLAUDE.mdを書くこと」は、誰に向けた作業だと思いますか？
