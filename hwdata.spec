Name:		hwdata
Summary:	Hardware identification and configuration data
Version:	0.44
Release:	1
License:	GPL/XFree86
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Conflicts:	Xconfigurator < 4.9.42-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hwdata contains various hardware identification and configuration
data, such as the pci.ids database, the XFree86 Cards and MonitorsDb
databases.

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
%{_prefix}/X11R6/lib/X11/Cards
