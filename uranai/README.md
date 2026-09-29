# 占いbot ハンズオン

このフォルダには、Claude Codeの使い方を学ぶためのサンプルコードが入っています。

## ファイル構成

```
uranai/
├── fortune.py   ← 占いbotのスターターコード
├── CLAUDE.md    ← Claude Codeへの指示書（あなたが書く）
└── README.md    ← このファイル（人間向けの説明）
```

## 動かし方

### Google Colabで試す場合

1. [Google Colab](https://colab.research.google.com/) を開く
2. 新しいノートブックを作成
3. 以下のセルを順に実行する

```python
# fortune.pyの中身をここに貼り付けて実行
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

### ローカルで実行する場合

```bash
python fortune.py
```

## ハンズオンの進め方

1. まず `fortune.py` をそのまま動かして、現状を確認する
2. Claude Codeで「`fortune.py` をもっと面白くしてください」と依頼する
3. `CLAUDE.md` に自分のコンセプトを書く（次のセクション参照）
4. 同じ依頼をもう一度 → 結果の違いを観察する

## CLAUDE.mdに書くこと

`CLAUDE.md` はClaude Codeへの指示書です。README.mdが**人間向け**の説明なのに対し、CLAUDE.mdは**Claude向け**の説明です。

以下を参考に、自由に書いてみてください。

- このbotは何のためのもの？
- キャラクターや口調は？
- 運勢のカテゴリや表示形式は？
- 絵文字や言語のルールは？

---

> **ポイント**: CLAUDE.mdに何も書かれていないと、ClaudeはREADME.mdやコードだけを頼りに判断します。どちらが意図通りの結果になるか、比べてみましょう。
