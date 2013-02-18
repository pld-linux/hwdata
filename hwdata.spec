# TODO
# - make this primary db of oui/pnp/blacklist db (merge ieee-oui, kmod/module-init-tools) ?
# - merge (switch?) with http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/sys-apps/hwids ?
#   their db contains also OUI, IAB IDs databases: https://github.com/gentoo/hwids
# - enable .gz if lshw has .gz support
Summary:	Hardware identification and configuration data
Summary(pl.UTF-8):	Dane do identyfikacji i konfiguracji sprzętu
Name:		hwdata
# see hwdata.spec inside of tarball
Version:	0.244
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/h/w/hwdata/%{name}-%{version}.tar.bz2
# Source0-md5:	bab206d2e66aeb7e6dd6043c802d0fac
Requires:	ieee-oui
Conflicts:	Xconfigurator < 4.9.42-1
Conflicts:	pciutils < 3.1.10-6
Conflicts:	usbutils < 006-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/lib

%description
hwdata contains various hardware identification and configuration
data, such as pci.ids, usb.ids, oui.txt and pnp.ids databases.

%description -l pl.UTF-8
Pakiet hwdata zawiera różne dane do identyfikacji i konfiguracji
sprzętu, takie jak bazy danych pci.ids, usb.ids, oui.txt i pnp.ids.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf /usr/share/oui.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/oui.txt
%{__rm} $RPM_BUILD_ROOT/etc/modprobe.d/blacklist.conf

%if 0
gzip -n9 $RPM_BUILD_ROOT%{_datadir}/%{name}/pci.ids
gzip -n9 $RPM_BUILD_ROOT%{_datadir}/%{name}/usb.ids
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/oui.txt
%{_datadir}/%{name}/pci.ids*
%{_datadir}/%{name}/pnp.ids
%{_datadir}/%{name}/usb.ids*
