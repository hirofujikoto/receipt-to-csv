import flet as ft

def main(page: ft.Page):
    page.title = "領収書保管アプリ"
    # 画面に文字を表示
    text = ft.Text(value="こんにちは！iPhoneから更新しました。")
    page.add(text)

# アプリを実行
ft.app(target=main)
