Summary:	A library for media streaming
Summary(pl.UTF-8):	Biblioteka obsługująca strumienie multimedialne
Name:		vale
Version:	0.0.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.soft-switch.org/downloads/vale/%{name}-%{version}.tgz
# Source0-md5:	3fb64157abb4ab3cd260e74a7cd599b0
URL:		http://www.soft-switch.org/
BuildRequires:	automake
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for media streaming.

%description -l pl.UTF-8
Biblioteka obsługująca strumienie multimedialne.

%package devel
Summary:	Header files to develop applications using vale
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia aplikacji używających vale
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the vale library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki vale.

%package static
Summary:	Static vale library
Summary(pl.UTF-8):	Statyczna biblioteka vale
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vale library.

%description static -l pl.UTF-8
Statyczna biblioteka vale.

%prep
%setup -q -n vale-0.0.1

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
%attr(755,root,root) %{_libdir}/libvale.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvale.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvale.so
%{_libdir}/libvale.la
%{_includedir}/vale
%{_includedir}/vale.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvale.a
