# Plintus Switcher 2.5

Лёгкий, быстрый и автономный переключатель раскладки клавиатуры для **Fedora / KDE Plasma (Wayland)** / Zero-config keyboard layout switcher for **Fedora / KDE Plasma (Wayland)**.

## 🇷🇺 Возможности / 🇬🇧 Key Features
- **Plug & Play:** Автозапуск через `systemd`, определение клавиатур / Auto-detection and background `systemd` service.
- **Исправление слова / Last Word (`Pause`):** Перевод последнего слова / Re-types the last word.
- **Исправление фразы / Entire Phrase (`Scroll Lock`):** Перевод всей строки / Re-types the entire line.
- **Замена выделения / Selection Replacement (`Pause` / `Scroll Lock`):** Конвертация выделенного текста / Convert selected text (`EN ↔ RU`).
- **Настройка / Customization:** `sudo plintus-switcher -c`.

### Установка (Fedora) / Installation
Скачайте `plintus-switcher-2.5-1.fc45.noarch.rpm` из **[Releases (v2.5)](https://github.com/plintus669-collab/plintus-switcher/releases/tag/v2.5)** и установите через KDE Discover или терминал:
```bash
sudo dnf install ./plintus-switcher-2.5-1.fc45.noarch.rpm
```
*(Полное описание функционала и исходный код вы можете найти в репозитории проекта).*

---
**Author / Автор:** Plintus669 (<plintus669@gmail.com>) • **License / Лицензия:** MIT
