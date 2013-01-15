# TODO
# - make this primary db of pci/usb/oui/pnp/blacklist db (merge usbutils, pciutils, ieee-oui, pnputils, kmod/module-init-tools) ?
# - merge (switch?) with http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/sys-apps/hwids ?
#   their db contains Hardware (PCI, USB, OUI, IAB) IDs databases: https://github.com/gentoo/hwids
Summary:	Hardware identification and configuration data
Summary(pl.UTF-8):	Dane do identyfikacji i konfiguracji sprzętu
Name:		hwdata
# see hwdata.spec inside of tarball
Version:	0.241
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/h/w/hwdata/%{name}-%{version}.tar.bz2
# Source0-md5:	32dd541d778cfe0dd6100f88433bbc90
Requires:	pciutils
Requires:	usbutils
Requires:	pnputils
Conflicts:	Xconfigurator < 4.9.42-1
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

ln -sf /etc/pci.ids $RPM_BUILD_ROOT%{_datadir}/hwdata/pci.ids
ln -sf /etc/usb.ids $RPM_BUILD_ROOT%{_datadir}/hwdata/usb.ids
ln -sf /usr/share/misc/pnp.ids $RPM_BUILD_ROOT%{_datadir}/hwdata/pnp.ids
%{__rm} $RPM_BUILD_ROOT/etc/modprobe.d/blacklist.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_datadir}/hwdata
