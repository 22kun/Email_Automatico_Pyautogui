import pyautogui, pyperclip, time

## Enviar email
# Abrir navegador
pyautogui.hotkey("Win")
time.sleep(1)
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(5)

# Abrir email
pyautogui.write("gmail.com")
pyautogui.press("enter")
time.sleep(7)

# Escrever
pyautogui.click(x=161, y=231, clicks=1)
time.sleep(2)
pyautogui.write("arturdemaria7@gmail.com")
pyautogui.press("tab")

pyautogui.press("tab")
pyperclip.copy("Email Automático - Artur")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyperclip.copy("Este é um email automático.")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

## Pyautogui and Pyperclip installation required.


