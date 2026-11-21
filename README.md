# ⌨️ Plintus Switcher 2.5
**Умный и молниеносный переключатель раскладки клавиатуры для Fedora / KDE Plasma (Wayland).**
Никаких костылей с X11 и сложных настроек: установили пакет — и он уже работает в фоне.

**A fast, zero-config keyboard layout switcher for Fedora / KDE Plasma (Wayland).**
Works directly at the Linux kernel level (`evdev` + `uinput`) — just install the package and start typing.

---

## 📦 Скачать и установить / Download & Install

### Вариант 1: Через официальный репозиторий Fedora COPR (рекомендуется / recommended)
Устанавливается в две команды и автоматически обновляется вместе с системой через `dnf` и **KDE Discover**:
```bash
sudo dnf copr enable plintus669/plintus-switcher
sudo dnf install plintus-switcher
```

### Вариант 2: Готовый RPM-пакет с GitHub / Direct RPM Download
👉 **Скачать релиз / Download Release:** https://github.com/plintus669-collab/plintus-switcher/releases/tag/v2.5

1. Скачайте файл **`plintus-switcher-2.5-1.fc45.noarch.rpm`** по ссылке выше.
2. Откройте скачанный файл двойным кликом через **KDE Discover** и нажмите **«Установить»** — *на этом всё, программа уже запущена!*

*(Или установите локальный файл через терминал / Or install local file via terminal)*:
```bash
sudo dnf install ./plintus-switcher-2.5-1.fc45.noarch.rpm
```

---

## ✨ Возможности / Key Features

| Клавиша / Hotkey | Действие (RU) | Action (EN) | Языки / Languages |
| :--- | :--- | :--- | :--- |
| **`Pause`** | Исправляет **последнее набранное слово** и переключает раскладку | Re-types the **last mistyped word** and switches layout | Любые / Any |
| **`Scroll Lock`** | Исправляет **всю набранную строку** целиком и переключает раскладку | Re-types the **entire typed line** and switches layout | Любые / Any |
| **`Pause` / `Scroll Lock`** *(с выделением)* | Переводит **выделенный мышью или клавиатурой текст** прямо на месте | Converts **selected text** in-place | `EN ↔ RU` |

- **🔌 Настоящий Plug & Play:** сам находит все подключённые клавиатуры и мыши, сам прописывается в автозагрузку (`systemd`) и стартует сразу после установки.
- **🛡️ Защита от дублирования:** корректно работает в `KWrite`, `Kate`, браузерах и мессенджерах без случайного копирования строк.

---

## 🛠️ Настройка и решение проблем / Configuration & Troubleshooting

### 1. Смена горячих клавиш / Customizing Hotkeys
Если у вас компактная клавиатура без клавиш `Pause` или `Scroll Lock`, либо вы переключаете язык через `Win + Пробел` / `Caps Lock`, запустите интерактивный мастер настройки:
```bash
sudo plintus-switcher -c
```

### 2. Что делать, если клавиатура не подхватилась сразу после установки?
*(What if the keyboard wasn't detected automatically?)*

1. **Если клавиатура подключена через беспроводной донгл или USB-хаб**, переподключите её или перезапустите службу:
   ```bash
   sudo systemctl restart plintus-switcher
   ```
2. **Если у вас нестандартная клавиатура** (игровая или разделённая), найдите её интерфейс в системе:
   ```bash
   ls -l /dev/input/by-id/
   ```
   Скопируйте путь (обычно заканчивается на `-event-kbd`) и укажите его в `/etc/plintus-switcher/config.ini`:
   ```ini
   [Switcher]
   keyboard = /dev/input/by-id/ваша_клавиатура-event-kbd
   ```
   После сохранения перезапустите службу:
   ```bash
   sudo systemctl restart plintus-switcher
   ```
3. **Проверка статуса службы / Check service status:**
   ```bash
   systemctl status plintus-switcher
   ```

---

## 👤 Автор и лицензия / Author & License
- **Автор / Author:** Plintus669 (<plintus669@gmail.com>)
- **Лицензия / License:** MIT (свободное использование и распространение)

## ☕ Поддержать проект / Support the Project

Если **Plintus Switcher** оказался полезным и сэкономил вам время, вы можете поддержать развитие этого и будущих open-source проектов для Linux:

- **ETH / USDT / USDC (Ethereum / Polygon / Arbitrum / BEP20):** `0x06f165470B35E4a584B27F91E0F64E8De9e3b841`
