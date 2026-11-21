Name:           plintus-switcher
Version:        2.5
Release:        1%{?dist}
Summary:        Plug-and-play Wayland keyboard layout switcher with smart selection
License:        MIT
Packager:       Plintus669 <plintus669@gmail.com>
URL:            https://github.com
BuildArch:      noarch
Requires:       python3, python3-evdev, wl-clipboard

Source0:        plintus-switcher
Source1:        plintus-switcher.service

%description
Zero-config Wayland/KDE keyboard layout switcher created by Plintus669 <plintus669@gmail.com>.
Auto-detects keyboards and mice, starts immediately on install, and fixes
selected text (EN <-> RU) or last typed word/phrase with a single key press.

%prep
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/plintus-switcher
install -m 0755 plintus-switcher %{buildroot}%{_bindir}/plintus-switcher
install -m 0644 plintus-switcher.service %{buildroot}%{_unitdir}/plintus-switcher.service

%post
systemctl daemon-reload >/dev/null 2>&1 || :
systemctl enable --now plintus-switcher.service >/dev/null 2>&1 || :
systemctl restart plintus-switcher.service >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
    systemctl stop plintus-switcher.service >/dev/null 2>&1 || :
    systemctl disable plintus-switcher.service >/dev/null 2>&1 || :
fi

%files
%{_bindir}/plintus-switcher
%{_unitdir}/plintus-switcher.service
%dir %{_sysconfdir}/plintus-switcher

%changelog
* Sat Nov 21 2026 Plintus669 <plintus669@gmail.com> - 2.5-1
- Release 2.5: instant Wayland layout switching, smart EN/RU selection replacement, and zero-config setup
