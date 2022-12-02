# TODO
# - make this primary db of blacklist db (merge kmod/module-init-tools) ?
# - merge (switch?) with http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/sys-apps/hwids ?
#   their db contains also OUI, IAB IDs databases: https://github.com/gentoo/hwids
# - enable .gz if lshw, usbip, usbutils/lsusb.py have .gz support
# - package Individual Address Blocks file (iab.txt)?
# NOTE: pnp.ids in pnputils package differ from that in hwdata
# (hwdata pnp.ids contain only vendor IDs, pnputils pnp.ids contains only
#  device IDs of (some) PNPACPI, PNPBIOS and ISAPNP devices)
# - update to use oui.txt from this package:
#   - hwdata-0.225-0.20090808.1.noarch
#   - lshw-B.02.14-1.i686
#   - python-netaddr-0.7.3-1.noarch
Summary:	Hardware identification and configuration data
Summary(pl.UTF-8):	Dane do identyfikacji i konfiguracji sprzętu
Name:		hwdata
Version:	0.364
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/vcrhonek/hwdata/releases
Source0:	https://github.com/vcrhonek/hwdata/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	626a5fa96e02c35457fb1aa1c4b024e4
URL:		https://github.com/vcrhonek/hwdata
Obsoletes:	ieee-oui
Conflicts:	Xconfigurator < 4.9.42-1
Conflicts:	ntop < 4.1.0-2
Conflicts:	pciutils < 3.1.10-6
Conflicts:	usbutils < 006-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/lib
%define		modprobe_d	/usr/lib/modprobe.d

%description
hwdata contains various hardware identification and configuration
data, such as pci.ids, usb.ids, oui.txt and pnp.ids (vendor IDs)
databases.

%description -l pl.UTF-8
Pakiet hwdata zawiera różne dane do identyfikacji i konfiguracji
sprzętu, takie jak bazy danych pci.ids, usb.ids, oui.txt i pnp.ids.

%prep
%setup -q

# if git-generated ChangeLog is missing in release, make one from included .spec
if [ ! -f ChangeLog ]; then
	%{__sed} -ne '/^%changelog/,$p' hwdata.spec | tail -n +2 > ChangeLog
fi

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	libdir=%{_prefix}/lib \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_npkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{modprobe_d}/dist-blacklist.conf

%{__mv} $RPM_BUILD_ROOT%{_datadir}/pkgconfig/hwdata.pc $RPM_BUILD_ROOT%{_npkgconfigdir}

# disabled: some applications don't support compressed formats
%if 0
gzip -n9 $RPM_BUILD_ROOT%{_datadir}/%{name}/pci.ids
gzip -n9 $RPM_BUILD_ROOT%{_datadir}/%{name}/usb.ids
gzip -n9 $RPM_BUILD_ROOT%{_datadir}/%{name}/oui.txt
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/iab.txt*
%{_datadir}/%{name}/oui.txt*
%{_datadir}/%{name}/pci.ids*
%{_datadir}/%{name}/pnp.ids
%{_datadir}/%{name}/usb.ids*
%{_npkgconfigdir}/hwdata.pc
