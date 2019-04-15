Summary:	proxychains
Name:		proxychains-ng
Version:	4.14
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	GPLv2
Group:		Applications/System
URL:		https://github.com/rofl0r/proxychains-ng
Source0:	%{name}-%{version}.tar.xz
BuildRequires:  gcc, make
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
ProxyChains is a UNIX program, that hooks network-related libc functions
in DYNAMICALLY LINKED programs via a preloaded DLL (dlsym(), LD_PRELOAD)
and redirects the connections through SOCKS4a/5 or HTTP proxies.
It supports TCP only (no UDP/ICMP etc).

%prep
%setup -q -n %{name}-%{version}

%build

%configure
%__make

%install
%makeinstall PREFIX=%{buildroot}
%{__install} -p -D -m 0755 proxychains4 %{buildroot}%{_bindir}/proxychains4
%{__install} -p -D -m 0644 libproxychains4.so %{buildroot}%{_libdir}/libproxychains4.so
%{__install} -p -D -m 0644 src/proxychains.conf %{buildroot}%{_sysconfdir}/proxychains.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/proxychains4
/usr/lib64/libproxychains4.so
%config(noreplace) /etc/proxychains.conf
%doc AUTHORS README TODO

%changelog
* Mon Apr 15 2019 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 4.14-1.vortex
- Initial packaging.
