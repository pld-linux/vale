Summary:	A library for media streaming
Name:		vale
Version:	0.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.soft-switch.org/downloads/vale/%{name}-%{version}.tgz
# Source0-md5:	ec4f119a4799b6fcbc6bde71a7ae4599
URL:		http://www.soft-switch.org/
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for media streaming.

%package devel
Summary:	Header files to develop applications using vale
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji używających vale
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for the vale library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki vale.

%package static
Summary:	Static vale library
Summary(pl.UTF-8):	Statyczna biblioteka vale
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static vale library.

%description static -l pl.UTF-8
Statyczna biblioteka vale.

%prep
%setup -q

%build
install /usr/share/automake/config.* config
%configure \
%ifarch athlon pentium3 pentium4
	--enable-mmx \
%endif
%ifarch pentium3 pentium4
	--enable-sse \
%endif
	--enable-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
