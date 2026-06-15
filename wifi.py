import subprocess
import time
import re
import os
from collections import deque

WINDOW_SIZE = 10
MOVEMENT_THRESHOLD = 5   # Increase if too sensitive, decrease if not detecting
SLEEP_TIME = 0.5

signals = deque(maxlen=WINDOW_SIZE)

def get_wifi_signal_percent():
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        match = re.search(r"Signal\s*:\s*(\d+)%", result)
        if match:
            return int(match.group(1))

        return None

    except Exception as e:
        print("Error reading Wi-Fi signal:", e)
        return None

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def draw_stick_figure(state, signal, change):
    clear_screen()

    print("Wi-Fi Stick Figure Demo - Wifi Router RSSI Mode")
    print("=" * 55)
    print(f"Current Signal : {signal}%")
    print(f"Signal Change  : {change}")
    print(f"State          : {state}")
    print("=" * 55)
    print()

    if state == "NO DATA":
        print("Waiting for Wi-Fi signal data...")
        return

    if state == "STILL":
        print("       O       ")
        print("      /|\\      ")
        print("       |       ")
        print("      / \\      ")
        print()
        print("Person estimate: still / low movement")

    elif state == "MOVING":
        print("      \\O/      ")
        print("       |       ")
        print("      / \\      ")
        print()
        print("Person estimate: movement detected")

    elif state == "BIG MOVEMENT":
        print("    \\  O  /    ")
        print("       |       ")
        print("     _/ \\_     ")
        print()
        print("Person estimate: strong movement near signal path")

def classify_movement(signals):
    if len(signals) < WINDOW_SIZE:
        return "NO DATA", 0

    change = max(signals) - min(signals)

    if change < MOVEMENT_THRESHOLD:
        return "STILL", change
    elif change < MOVEMENT_THRESHOLD * 2:
        return "MOVING", change
    else:
        return "BIG MOVEMENT", change

def main():
    print("Starting Wi-Fi stick figure demo...")
    print("Connect your laptop to the D-Link Wi-Fi first.")
    time.sleep(2)

    while True:
        signal = get_wifi_signal_percent()

        if signal is not None:
            signals.append(signal)
            state, change = classify_movement(signals)
            draw_stick_figure(state, signal, change)
        else:
            draw_stick_figure("NO DATA", "N/A", "N/A")

        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()