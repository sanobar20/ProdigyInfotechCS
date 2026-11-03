<div align="center">

# 🛡️ Prodigy InfoTech — Cyber Security Internship

### Five hands-on security tasks, from classical ciphers to live packet capture

*A collection of Python programs completed during the Prodigy InfoTech Cyber Security internship.*

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Image%20Security-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/Scapy-Packet%20Analysis-2C8EBB?style=for-the-badge" alt="Scapy">
  <img src="https://img.shields.io/badge/pynput-Key%20Events-orange?style=for-the-badge" alt="pynput">
</p>

</div>

---

## 📖 Overview

This repository contains the five tasks from the Prodigy InfoTech Cyber Security internship. Each task is a self-contained Python script that demonstrates a different area of security: cryptography, image encryption, password auditing, keylogging and network traffic analysis.

## 🧪 Tasks at a glance

| # | Task | File | Concepts |
|:-:|:--|:--|:--|
| 1 | **Caesar Cipher** | `task 1.py` | Classical encryption, modular arithmetic, encrypt/decrypt CLI |
| 2 | **Image Encryption** | `task2.py` | XOR encryption with a seeded random key matrix, OpenCV I/O |
| 3 | **Password Strength Checker** | `task3.py` | Length and character-class scoring, actionable feedback |
| 4 | **Keylogger** | `task 4.py` | Keyboard event listeners with `pynput`, file logging |
| 5 | **Network Packet Sniffer** | `task5.py` | Packet capture with Scapy, IP/TCP/UDP parsing, protocol counts |

## 🔍 Task details

### 1. Caesar Cipher

Encrypts and decrypts text by shifting alphabetic characters while leaving spaces, digits and punctuation untouched. The CLI accepts a shift value between 1 and 25.

```bash
python "task 1.py"
```

### 2. Image Encryption

Generates a random key matrix from a numeric seed and XORs it with the image pixels. Because XOR is reversible, the same key decrypts the image. Requires an input image path and a key.

```bash
python task2.py
```

### 3. Password Strength Checker

Scores a password using length, uppercase and lowercase letters, digits and special characters, then reports specific suggestions for improvement.

```bash
python task3.py
```

### 4. Keylogger

Listens for key presses and appends them to `keylog.txt`. Built with `pynput` to demonstrate how keystroke monitoring works — and why endpoint protection matters.

```bash
python "task 4.py"
```

### 5. Network Packet Sniffer

Captures live traffic or reads a `.pcap` file, prints source and destination IPs, and keeps a running count of TCP, UDP and other protocols.

```bash
python task5.py
```

## 🚀 Getting started

### 1. Clone the repository

```bash
git clone https://github.com/sanobar20/ProdigyInfotechCS.git
cd ProdigyInfotechCS
```

### 2. Install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

pip install opencv-python numpy pynput scapy
```

### 3. Run a task

```bash
python task3.py
```

## ⚠️ Platform notes

- **Packet sniffing** needs administrator/root privileges and a capture driver. On Windows, install [Npcap](https://npcap.com/). On Linux, run with `sudo`.
- **Keylogging** may be flagged by antivirus software — this is expected behaviour for keyboard hooks.
- The scripts are intentionally simple and console-driven so the underlying concepts stay visible.

## 🧰 Tech stack

| Area | Tools |
|:--|:--|
| Language | Python 3 |
| Image handling | OpenCV, NumPy |
| Keyboard events | pynput |
| Packet capture | Scapy |

## ⚖️ Ethical use

These programs were written for educational purposes. Only run the keylogger and packet sniffer on machines and networks you own or have explicit permission to test. Do not use them to collect data from other people.

## 🛣️ Possible improvements

- [ ] Add a proper CLI with `argparse` for every task.
- [ ] Store encryption keys securely instead of using a numeric seed.
- [ ] Add unit tests for the cipher and password checker.
- [ ] Save captured packets to a `.pcap` file for later analysis.

---

<div align="center">

**Learn the attack to build the defence. 🔐**

</div>