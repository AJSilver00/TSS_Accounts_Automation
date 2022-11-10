class settle_Accounts:

    def __init__(self):
        import pyautogui
        import time
        import os
        import pyperclip
        import keyboard

        def __init__(self):
            self.os.chdir(r'C:\Users\Aimee\Pictures\TSS Python Screenshots\Settle Accounts')

        def open_CashAC(self):
            while True:
                location = self.pyautogui.locateOnScreen('open_CashAC.png', confidence=0.8)
                location2 = self.pyautogui.locateOnScreen('open_CashAC2.png', confidence=0.8)
                if location != None:
                    settle_Accounts().go()
                    settle_Accounts().refresh()
                elif location2 != None:
                    settle_Accounts().go()
                    settle_Accounts().refresh()

        def go(self):
            location = self.pyautogui.locateOnScreen('open_CashAC.png', confidence=0.8)
            location = self.pyautogui.center(location)
            x, y = location
            self.pyautogui.click(x, y)

        def refresh(self):
            location = self.pyautogui.locateOnScreen('process.png', confidence=0.8)
            location = self.pyautogui.center(location)
            x, y = location
            self.pyautogui.click(x, y)
