<div align="center">

# Steam Price Checker

**A sleek terminal tool to check Steam game prices across different regions**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-TUI-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey?style=for-the-badge&logo=windows)

<br/>

> Search Steam prices in any region right from your terminal - no browser needed.

</div>

---

## ✨ Features

- 🔍 **Game Search** — find any game price in any Steam region instantly
- 🌍 **Region Comparison** — compare prices across multiple countries *(coming soon)*
- 💸 **Lowest Price Finder** — find the cheapest available region *(coming soon)*
- 🎨 **Beautiful TUI** — rich terminal interface with colors, spinners and tables
- 📦 **Portable .exe** — run on any Windows machine, no Python required

---
## Preview
<img width="1102" height="335" alt="image" src="https://github.com/user-attachments/assets/64e415d9-2189-4617-aafe-1dff6872dfae" />

---

## 🚀 Quick Start

### Option 1 — Download .exe *(Windows, no Python needed)*

Head to [**Releases**](../../releases/latest) and download `steam_checker.exe`. Just run it.

### Option 2 — Run from source

**Clone the repo:**
```bash
git clone https://github.com/YOUR_USERNAME/steam-price-checker.git
cd steam-price-checker
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run:**
```bash
python richmain.py
```

---

## 🌍 Supported Regions

| Code | Country        |
|------|----------------|
| `us` | United States  |
| `ru` | Russia         |
| `ua` | Ukraine        |
| `kz` | Kazakhstan     |
| `tr` | Turkey         |
| `ar` | Argentina      |
| `br` | Brazil         |
| `eu` | Europe         |

Any valid [Steam country code](https://store.steampowered.com/api/) works.

---

## 🛠 Build .exe Yourself

```bash
pip install pyinstaller
python -m PyInstaller --onefile --console --icon=icon.ico richmain.py
```

Output: `dist/richmain.exe`

---

## 📦 Tech Stack

| Library | Purpose |
|---------|---------|
| [Rich](https://github.com/Textualize/rich) | Terminal UI — colors, tables, spinners |
| [Requests](https://docs.python-requests.org/) | HTTP requests |
| [CheapShark API](https://apidocs.cheapshark.com/) | Game search by name |
| [Steam Store API](https://store.steampowered.com/api/) | Prices by region |

---

## 📁 Project Structure

```
steam-price-checker/
├── richmain.py        ← main script
├── requirements.txt   ← dependencies
└── README.md
```

---

## 📄 License

MIT © 2026 — free to use, modify and distribute.

---

<div align="center">
  <sub>Built with ❤️ and too much free time</sub>
</div>
