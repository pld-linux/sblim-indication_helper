Summary:	SBLIM indication_helper library
Summary(pl.UTF-8):	Biblioteka SBLIM indication_helper
Name:		sblim-indication_helper
Version:	0.5.0
Release:	1
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	521d90a99b21bce4d65adb3cee8b436e
URL:		http://sblim.sourceforge.net/
BuildRequires:	gcc >= 5:3.2.0
BuildRequires:	sblim-cmpi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an implementation of a toolkit to help developers implement
CMPI indication providers.

%description -l pl.UTF-8
Ten pakiet to implementacja toolkitu pomagającego programistom przy
implementacji dostarczycieli oznaczeń CMPI.

%package devel
Summary:	Header files for SBLIM indication_helper library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SBLIM indication_helper
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sblim-cmpi-devel

%description devel
Header files for SBLIM indication_helper library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SBLIM indication_helper.

%package static
Summary:	Static SBLIM indication_helper library
Summary(pl.UTF-8):	Statyczna biblioteka SBLIM indication_helper
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SBLIM indication_helper library.

%description static -l pl.UTF-8
Statyczna biblioteka SBLIM indication_helper.

%prep
%setup -q

%build
%configure

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
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libind_helper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libind_helper.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libind_helper.so
%{_libdir}/libind_helper.la
# XXX: dir shared between some sblim-* packages
%dir %{_includedir}/sblim
%{_includedir}/sblim/ind_helper.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libind_helper.a
