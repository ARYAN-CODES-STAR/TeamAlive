import pyautogui
import time
import sys

#  2+ minutes less than the minimum threshold 3 minutes.
DELAY = 160

pyautogui.FAILSAFE = True

print("=" * 50)
print("  HARDWARE WAKE-UP SCRIPT RUNNING")
print("  Press Ctrl+C to stop.")
print("=" * 50)

try:
    while True:
        # 1. Save current position
        original_x, original_y = pyautogui.position()
        
        # 2. Small mouse move to trigger OS activity
        pyautogui.moveRel(1, 1, duration=0.1)
        pyautogui.moveRel(-1, -1, duration=0.1)
        
        # 3. Simulate pressing the Shift key (This forces the screen awake)
        pyautogui.press('shift')
        
        # 4. Return mouse to original position
        pyautogui.moveTo(original_x, original_y)
        
        print(f"[{time.strftime('%H:%M:%S')}] Sent hardware Shift key signal.")
        
        # Wait for 4 minutes
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("\n[+] Script stopped.")
    sys.exit()