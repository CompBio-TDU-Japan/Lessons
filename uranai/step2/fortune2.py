import random

DAIKICHI_FORTUNES = [
    "Leo ni siku yako ya ushindi mkubwa! 今日は大勝利の日です！\n全てのことが輝き、幸運の風があなたを包んでいます。\n勇敢に前へ進んでください！ Nenda mbele!",
    "Bahati njema inakungoja! 素晴らしい幸運があなたを待っています！\n思い切って行動することで、夢が現実になる一日です。\nFuraha kubwa! 大きな喜びが訪れるでしょう！",
    "Nyota zinakuangazia! 星々があなたを照らしています！\n素晴らしい出会いと新しいチャンスが舞い込む予感。\nNdoto yako inakuwa kweli! あなたの夢が叶います！",
]

DAIKYOU_FORTUNES = [
    "Leo kuna hatari... 今日は危険が潜んでいます…\n全ての行動を三度考えてから動いてください。\nTabadhali! 慎重に、慎重に…",
    "Mawingu meusi yanakufunika... 暗雲があなたを覆っています…\n今日は嵐の前の静けさ。軽率な行動は避けるべし。\nAngalia sana... くれぐれも気をつけて…",
    "Jaribio kubwa linakuja... 大きな試練が迫っています…\nこの試練を乗り越えられるか？覚悟を決めよ。\nMungu akuwe nawe... 神があなたと共にありますように…",
]

BRIGHT = "\033[93m"  # 黄色（大吉）
DARK   = "\033[90m"  # 暗いグレー（大凶）
BOLD   = "\033[1m"
RESET  = "\033[0m"

def tell_fortune(name: str) -> None:
    is_daikichi = random.random() < 0.5
    
    if is_daikichi:
        result = "大吉"
        fortune = random.choice(DAIKICHI_FORTUNES)
        color = BRIGHT
        stars = "★★★★★"
        swahili_label = "BAHATI NJEMA SANA ✦ 最高の幸運"
    else:
        result = "大凶"
        fortune = random.choice(DAIKYOU_FORTUNES)
        color = DARK
        stars = "☠️ ☠️ ☠️ ☠️ ☠️"
        swahili_label = "BAHATI MBAYA SANA ✦ 最大の凶"

    print()
    print(color + BOLD + "=" * 50 + RESET)
    print(color + BOLD + f"  {name}さん / {name} Ndugu Yangu!" + RESET)
    print(color + BOLD + "=" * 50 + RESET)
    print()
    print(color + BOLD + f"  【 {result} 】  {swahili_label}" + RESET)
    print(color + f"  {stars}" + RESET)
    print()
    print(color + fortune + RESET)
    print()
    print(color + BOLD + "=" * 50 + RESET)
    print()

def main() -> None:
    print()
    print(BOLD + "🔮 Bahati Yako — 運命の占い 🔮" + RESET)
    print("Karibu! ようこそ！スワヒリの星があなたの運命を読み解きます。")
    print()
    name = input("Jina lako ni nani? お名前を教えてください: ").strip()
    if not name:
        name = "旅人"
    tell_fortune(name)

if __name__ == "__main__":
    main()
