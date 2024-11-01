from win10toast import ToastNotifier
import pyperclip
import time

toaster = ToastNotifier()
last_clipboard = pyperclip.paste()

while True:
    current_clipboard = pyperclip.paste()
    if current_clipboard != last_clipboard:
        toaster.show_toast("剪贴板更新", f"新内容: {current_clipboard}")
        last_clipboard = current_clipboard
    time.sleep(1)
