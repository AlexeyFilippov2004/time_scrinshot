import os
import win32api
import pyautogui
import datetime
import time
from PIL import Image
l=[]
while not l:
    try:
        with open('set.txt', 'r') as f:
            l = f.readlines()
    except FileNotFoundError:
        continue

delay = int(l[0])
output_format = l[3].strip().rsplit('.', 3)[-1]

# Создаем директорию для сохранения скриншотов
os.makedirs(l[1].strip(), exist_ok=True)

while True:
    # Получаем текущую дату и время
    now = datetime.datetime.now()
    y, mo, d, h, m, s = now.year, now.strftime('%m'), now.day, now.hour, now.minute, now.second

    format_dir_template = str(l[2].strip())
    format_name_template = str(l[3].strip())
    variables = {
        "y": y,
        "mo": mo,
        "d": d,
        "h": h,
        "m": m,
        "s": s,
    }

    format_dir = format_dir_template.format_map(variables)
    format_name = format_name_template.format_map(variables)

    format_name = format_name.replace(output_format, "", 1)
    format_name = format_name[:-1]

    screenshot_dir = os.path.join(l[1].strip(), format_dir)
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_name = f"{format_name}.{output_format}"

    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
    if win32api.GetKeyState(0x01) >= 0 and win32api.GetKeyState(0x02) >= 0:
        pyautogui.screenshot(screenshot_path)
    time.sleep(delay)
