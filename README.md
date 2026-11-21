# Plintus Switcher 2.5

Лёгкий, быстрый и полностью автономный переключатель раскладки клавиатуры для **Fedora / KDE Plasma (Wayland)**. Работает «из коробки» сразу после установки без ручной настройки.

A lightweight, fast, zero-config keyboard layout switcher for **Fedora / KDE Plasma (Wayland)**. Works right out of the box immediately after installation with no manual configuration required.

---

## 🇷🇺 Возможности
- **Plug & Play:** автоматически определяет все подключённые клавиатуры и мыши, сам добавляется в автозапуск (`systemd`) и запускается сразу после установки пакета.
- **Исправление последнего слова (`Pause`):** мгновенно переводит последнее набранное слово в нужную раскладку (поддерживает любые языки).
- **Исправление всей фразы (`Scroll Lock`):** переводит всю набранную строку целиком (поддерживает любые языки).
- **Замена выделенного текста (`Pause` или `Scroll Lock`):** выделите любой фрагмент текста мышью или клавиатурой (`Shift + стрелки`) и нажмите клавишу исправления (`EN ↔ RU`).
- **Опциональная настройка:** при необходимости горячие клавиши и комбинацию смены раскладки можно переопределить командой `sudo plintus-switcher -c`.

### Установка (Fedora)
Скачайте `plintus-switcher-2.5-1.fc45.noarch.rpm` из раздела **[Releases](https://github.com)** и установите двойным кликом через **KDE Discover** или в терминале:
```bash
sudo dnf install ./plintus-switcher-2.5-1.fc45.noarch.rpm
```

---

## 🇬🇧 Key Features
- **True Plug & Play:** Automatically detects all connected keyboards and mice, enables and starts the background `systemd` service immediately upon installation.
- **Last Word Fix (`Pause`):** Instantly re-types the last mistyped word in the target layout (supports any language).
- **Entire Phrase Fix (`Scroll Lock`):** Re-types the entire typed line/phrase (supports any language).
- **Selection Replacement (`Pause` or `Scroll Lock`):** Select any text with your mouse or `Shift + Arrows` and press the hotkey to convert it in-place (`EN ↔ RU`).
- **Optional Customization:** Rebind hotkeys or system layout shortcut anytime via `sudo plintus-switcher -c`.

### Installation (Fedora)
Download `plintus-switcher-2.5-1.fc45.noarch.rpm` from **[Releases](https://github.com)** and install via **KDE Discover** (double-click) or terminal:
```bash
sudo dnf install ./plintus-switcher-2.5-1.fc45.noarch.rpm
```

---
**Author / Автор:** Plintus669 (<plintus669@gmail.com>) • **License / Лицензия:** MIT
