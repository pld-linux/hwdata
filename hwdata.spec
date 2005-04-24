# TODO: use system {usb,pci}.ids (or symlink them)?
Summary:	Hardware identification and configuration data
Summary(pl):	Dane do identyfikacji i konfiguracji sprzêtu
Name:		hwdata
Version:	0.156
Release:	1
License:	GPL/XFree86
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	28f8e4d0a2f230346de86ca46f30760e
#Requires:	XFree86-Xserver
Conflicts:	Xconfigurator < 4.9.42-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hwdata contains various hardware identification and configuration
data, such as the pci.ids database, the XFree86 Cards and MonitorsDB
databases.

%description -l pl
Pakiet hwdata zawiera ró¿ne dane do identyfikacji i konfiguracji
sprzêtu, takie jak baza danych pci.ids oraz bazy Cards i MonitorsDB
dla XFree86.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%dir /etc/pcmcia
%config(noreplace) %verify(not md5 mtime size) /etc/hotplug/blacklist
%config /etc/pcmcia/config
%dir %{_datadir}/hwdata
%{_datadir}/hwdata/*
