# Discord-Automation
# 🤖 Discord Automation using Selenium

This project uses **Python + Selenium** to automate sending messages to Discord channels via the web interface. It simulates user interactions such as logging in, navigating to a channel, and sending text — all from a script.

> ⚠️ This project is for **educational purposes only**. Automating Discord through browser scripting **violates Discord's Terms of Service** and may result in account bans.

## 📂 Project Structure
discord-automation/
├── main.py # Main automation script
├── config.py / .env # Configuration (credentials, URLs, message content)
├── requirements.txt # Dependencies
├── README.md # Project documentation

---

## 🚀 Features

- Automates Discord login using Selenium
- Navigates to a specific server and text channel
- Sends a custom message
- Configurable and beginner-friendly

---

## 🧰 Requirements

- Python 3.x
- Google Chrome installed
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (must match your Chrome version)
- pip (Python package manager)

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/saphala2712sneha/Discord-Automation.git
   cd Discord-Automation/discord-automation-main

2. Install Dependencies
   pip install -r requirements.txt

3.Configure your details

   Open config.py or .env file (whichever is used).

   Set your:

   Email and password

   Discord channel URL

   Message to send

4. Run the script

python main.py

