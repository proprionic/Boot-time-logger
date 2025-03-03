# Boot Time Logger 🕒

This project automatically logs your system's boot time into two formats:
- **Excel (.xlsx)**
- **Text (.txt)**

The logs are appended every time the system starts, without overwriting previous records.

## Features 🔥
- Logs boot times with the exact date and time
- Automatically appends logs to the existing file
- Supports both **Windows** and **Linux**
- Compatible with **Python 3.10+**
- Easy to set up for automatic startup

## Installation 📄
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/boot-time-logger.git
cd Boot-time-logger
```

### 2. Install Dependencies
```bash
pip install -r openpyxl
pip install twilio
```

### 3. Run the Script
```bash
python app.py
```

---

## Automatic Startup 🔌
### Windows Setup
1. Press **Windows + R** and type:
   ```
shell:startup
```
2. Create a `.bat` file inside the **Startup Folder** with this content:
```bat
@echo off
"C:\Program Files\Python313\python.exe" "C:\path\to\your\project\app.py"
exit
```
3. Save the file as **boot_time.bat**

✅ Now your script will run automatically every time your PC starts.

### Linux Setup
1. Create a **systemd service**:
```bash
sudo nano /etc/systemd/system/boot_time.service
```
2. Paste this:
```ini
[Unit]
Description=Boot Time Logger
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/your/project/app.py
Restart=always
User=yourusername

[Install]
WantedBy=multi-user.target
```
3. Enable the service:
```bash
sudo systemctl enable boot_time.service
sudo systemctl start boot_time.service
```

---

## Logs Example 📄
### boot_logs.txt
```
Boot time: 2025-03-02 21:11:43
Boot time: 2025-03-03 10:45:32
```

### boot_logs.xlsx
| Boot Times       |
|----------------|
| 2025-03-02 21:11:43 |
| 2025-03-03 10:45:32 |

---

## Contributing 🤝
Feel free to fork this repo and submit a pull request.
