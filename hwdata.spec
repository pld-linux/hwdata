# TODO
# - make this primary db of oui/pnp/blacklist db (merge ieee-oui, pnputils, kmod/module-init-tools) ?
# - merge (switch?) with http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/sys-apps/hwids ?
#   their db contains also OUI, IAB IDs databases: https://github.com/gentoo/hwids
Summary:	Hardware identification and configuration data
Summary(pl.UTF-8):	Dane do identyfikacji i konfiguracji sprzętu
Name:		hwdata
# see hwdata.spec inside of tarball
Version:	0.243
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/h/w/hwdata/%{name}-%{version}.tar.bz2
# Source0-md5:	98615d098bafb7bad1ae5912c073edc7
Requires:	ieee-oui
Requires:	pnputils
Conflicts:	Xconfigurator < 4.9.42-1
Conflicts:	pciutils < 3.1.10-3
Conflicts:	usbutils < 006-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

ln -sf %{_datadir}/misc/pnp.ids $RPM_BUILD_ROOT%{_datadir}/%{name}/pnp.ids
ln -sf %{_datadir}/oui.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/oui.txt
%{__rm} $RPM_BUILD_ROOT/etc/modprobe.d/blacklist.conf

gzip -9 $RPM_BUILD_ROOT%{_datadir}/%{name}/pci.ids

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/oui.txt
%{_datadir}/%{name}/pci.ids.gz
%{_datadir}/%{name}/pnp.ids
%{_datadir}/%{name}/usb.ids
