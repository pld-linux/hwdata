Summary:	Hardware identification and configuration data
Summary(pl):	Dane do identyfikacji i konfiguracji sprzêtu
Name:		hwdata
Version:	0.61
Release:	1
License:	GPL/XFree86
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
#Requires:	XFree86-Xserver
Conflicts:	Xconfigurator < 4.9.42-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hwdata contains various hardware identification and configuration
data, such as the pci.ids database, the XFree86 Cards and MonitorsDb
databases.

%description -l pl
Pakiet hwdata zawiera ró¿ne dane do identyfikacji i konfiguracji
sprzêtu, takie jak baza danych pci.ids oraz bazy Cards i MonitorsDb
dla XFree86.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE COPYING
%dir %{_datadir}/hwdata
%config %{_datadir}/hwdata/*
