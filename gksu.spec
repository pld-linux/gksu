Summary:	GKsu is a GTK+ frontend to the su program
Summary(pl):	GKsu to nak³adka graficzna na program su
Name:		gksu
Version:	1.0.4
Release:	1
License:	GPL
Vendor:		Gustavo Noronha Silva <kov@debian.org>
Group:		Applications/System
Source0:	http://people.debian.org/~kov/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	b8e38f8eda1ce32a299fcaa5c70390f5
URL:		http://www.nongnu.org/gksu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
Requires:	/bin/su
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKsu is a GTK+ frontend to the su program.

%description -l pl
GKsu to graficzna nak³adka na program su.

%package devel
Summary:	Header files for gksu library
Summary(pl):	Pliki nag³ówkowe biblioteki gksu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gksu library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gksu.

%package static
Summary:	Static gksu library
Summary(pl):	Statyczna biblioteka gksu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gksu library.

%description static -l pl
Statyczna biblioteka gksu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/gksu-run-helper
%{_desktopdir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
