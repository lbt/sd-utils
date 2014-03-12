Name:       sd-utils
Summary:    SailfishOS scripts to mount/umount external sdcard.
Version:    0.3
Release:    1
Group:      System/Base
License:    MIT
BuildArch:  noarch
URL:        https://github.com/nemomobile/sd-utils/
Source0:    %{name}-%{version}.tar.gz
BuildRequires:   oneshot
Requires(post):  oneshot

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
# mounting script
mkdir -p %{buildroot}%{_sbindir}
cp scripts/mount-sd.sh %{buildroot}%{_sbindir}
# systemd service install
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system
cp scripts/mount-sd@.service %{buildroot}%{_sysconfdir}/systemd/system/
# udev rules for mmcblk1*
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
cp rules/90-mount-sd.rules %{buildroot}%{_sysconfdir}/udev/rules.d/
# oneshot run in install
mkdir -p %{buildroot}%{_oneshotdir}
cp scripts/tracker-sd-indexing.sh %{buildroot}%{_oneshotdir}

%post
add-oneshot --user --now tracker-sd-indexing.sh

%files
%defattr(-,root,root,-)
%{_sbindir}/mount-sd.sh
%{_sysconfdir}/systemd/system/mount-sd@.service
%{_sysconfdir}/udev/rules.d/90-mount-sd.rules
%{_oneshotdir}/tracker-sd-indexing.sh
