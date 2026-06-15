# Wi-Fi Stick Figure Motion Demo

A simple Python-based Wi-Fi sensing experiment that detects movement-like changes in Wi-Fi signal strength and displays a stick figure animation in the terminal.

This project reads the current Wi-Fi signal percentage from a Windows laptop using the `netsh wlan show interfaces` command. It then tracks recent signal values, calculates signal variation, and classifies the environment as **Still**, **Moving**, or **Big Movement**.

> This is an educational demo project. It does not directly detect or track humans. It only observes changes in Wi-Fi signal strength, which may be affected by movement, distance, walls, router placement, interference, and other nearby devices.

---

## Demo Concept

Wi-Fi signals can slightly change when objects or people move near the signal path between a router and a laptop. This project uses that idea in a simple way:

* Read Wi-Fi signal strength
* Store recent signal readings
* Measure how much the signal changes
* Classify the movement level
* Display a stick figure in the terminal

---

## Features

* Reads Wi-Fi signal percentage using Windows `netsh`
* Uses a sliding window to store recent signal readings
* Detects signal variation over time
* Classifies signal state as:

  * `STILL`
  * `MOVING`
  * `BIG MOVEMENT`
* Displays a terminal-based stick figure animation
* Simple beginner-friendly Python code
* No external libraries required

---

## How It Works

The program continuously runs the following command:

```bash
netsh wlan show interfaces
```

From the command output, it extracts the Wi-Fi signal percentage.

Example:

```text
Signal : 78%
```

The program stores the latest signal values in a queue. Then it calculates:

```text
change = maximum signal value - minimum signal value
```

Based on this change value, it decides the movement state.

| Signal Change | State        |
| ------------- | ------------ |
| Low change    | STILL        |
| Medium change | MOVING       |
| High change   | BIG MOVEMENT |

---

## Requirements

* Windows OS
* Python 3.x
* Laptop or PC connected to Wi-Fi
* A Wi-Fi router nearby

No extra Python packages are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Harshith-Builds/Wifi_analyzer/
```

Go into the project folder:

```bash
Wifi_analyzer
```

---

## Usage

Run the Python file:

```bash
python wifi.py
```

Make sure your laptop is connected to Wi-Fi before running the program.

---

## Configuration

You can change these values in the code:

```python
WINDOW_SIZE = 10
MOVEMENT_THRESHOLD = 5
SLEEP_TIME = 0.5
```

### `WINDOW_SIZE`

Controls how many recent Wi-Fi signal readings are stored.

Higher value:

* More stable output
* Slower reaction

Lower value:

* Faster reaction
* More sensitive to small changes

### `MOVEMENT_THRESHOLD`

Controls how sensitive the movement detection is.

Increase this value if the program is too sensitive.

Decrease this value if the program is not detecting movement.

### `SLEEP_TIME`

Controls how often the signal is checked.

Example:

```python
SLEEP_TIME = 0.5
```

This means the signal is checked every 0.5 seconds.

---

## Example Output

```text
Wi-Fi Stick Figure Demo - D-Link Router RSSI Mode
=======================================================
Current Signal : 76%
Signal Change  : 2
State          : STILL
=======================================================

       O
      /|\
       |
      / \

Person estimate: still / low movement
```

When movement is detected:

```text
Wi-Fi Stick Figure Demo - D-Link Router RSSI Mode
=======================================================
Current Signal : 71%
Signal Change  : 7
State          : MOVING
=======================================================

      \O/
       |
      / \

Person estimate: movement detected
```

For stronger movement:

```text
Wi-Fi Stick Figure Demo - D-Link Router RSSI Mode
=======================================================
Current Signal : 65%
Signal Change  : 12
State          : BIG MOVEMENT
=======================================================

    \  O  /
       |
     _/ \_

Person estimate: strong movement near signal path
```

---

## Project Structure

```text
Wifi_analyzer/
│
├── wifi.py
└── README.md
```

---

## Limitations

This project is only a basic experiment. It is not a professional motion detection system.

Wi-Fi signal changes can happen because of:

* Router distance
* Walls and furniture
* Other connected devices
* Network interference
* Laptop antenna position
* Router signal strength changes
* People moving nearby

The result should be treated as an estimate, not an accurate detection.

---

## Educational Purpose

This project is useful for learning about:

* Python scripting
* Wi-Fi signal monitoring
* RSSI-style signal analysis
* Sliding window logic
* Basic movement classification
* Terminal-based visual output
* Beginner-level wireless sensing concepts

---

## Future Improvements

Possible improvements:

* Add graph visualization for signal changes
* Save signal logs to a CSV file
* Add support for Linux Wi-Fi commands
* Add a web dashboard using Flask
* Improve movement classification logic
* Add sound alerts for big movement
* Compare multiple Wi-Fi networks
* Use actual RSSI value instead of signal percentage

---

## Disclaimer

This project is created only for educational and experimental purposes. It does not hack, attack, or interfere with any Wi-Fi network. It only reads the signal strength of the Wi-Fi network that your own laptop is already connected to.

Use it only on your own device and your own network.

---

## Author

Made by Harshith Vadlamudi

---

## License

This project is open-source and available under the MIT License.
