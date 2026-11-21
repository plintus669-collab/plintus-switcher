Name:           plintus-switcher
Version:        2.5
Release:        1%{?dist}
Summary:        Plug-and-play Wayland keyboard layout switcher with smart selection
License:        MIT
Packager:       Plintus669 <plintus669@gmail.com>
URL:            https://github.com
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       python3, python3-evdev, wl-clipboard, systemd

Source0:        plintus-switcher
Source1:        plintus-switcher.service

%description
Zero-config Wayland/KDE keyboard layout switcher created by Plintus669 <plintus669@gmail.com>.
Auto-detects keyboards and mice, starts immediately on install, and fixes
selected text (EN <-> RU) or last typed word/phrase with a single key press.

%prep
%setup -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/plintus-switcher
install -m 0755 plintus-switcher %{buildroot}%{_bindir}/plintus-switcher
install -m 0644 plintus-switcher.service %{buildroot}%{_unitdir}/plintus-switcher.service

%post
%systemd_post plintus-switcher.service
systemctl enable --now plintus-switcher.service >/dev/null 2>&1 || :

%preun
%systemd_preun plintus-switcher.service

%postun
%systemd_postun_with_restart plintus-switcher.service

%files
%{_bindir}/plintus-switcher
%{_unitdir}/plintus-switcher.service
%dir %{_sysconfdir}/plintus-switcher

%changelog
* Sat Nov 21 2026 Plintus669 <plintus669@gmail.com> - 2.5-1
- Release 2.5: instant Wayland layout switching, smart EN/RU selection replacement, and zero-config setup
