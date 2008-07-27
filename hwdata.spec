Summary:	Hardware identification and configuration data
Summary(pl.UTF-8):	Dane do identyfikacji i konfiguracji sprzętu
Name:		hwdata
Version:	0.177
Release:	2
License:	GPL/XFree86
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	daa4c324ec57a56ff802fe01010bf849
Requires:	pciutils
Requires:	usbutils
Conflicts:	Xconfigurator < 4.9.42-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hwdata contains various hardware identification and configuration
data, such as the pci.ids database, the XFree86 Cards and MonitorsDB
databases.

%description -l pl.UTF-8
Pakiet hwdata zawiera różne dane do identyfikacji i konfiguracji
sprzętu, takie jak baza danych pci.ids oraz bazy Cards i MonitorsDB
dla XFree86.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf /etc/pci.ids $RPM_BUILD_ROOT%{_datadir}/hwdata/pci.ids
ln -sf /etc/usb.ids $RPM_BUILD_ROOT%{_datadir}/hwdata/usb.ids
rm -f $RPM_BUILD_ROOT/etc/modprobe.d/blacklist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_datadir}/hwdata
