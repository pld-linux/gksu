#
# TODO:
# - nautilus subpackage
#
Summary:	GKsu is a GTK+ frontend to the su program
Summary(pl):	GKsu to nak³adka graficzna na program su
Name:		gksu
Version:	1.9.4
Release:	0.1
License:	GPL
Vendor:		Gustavo Noronha Silva <kov@debian.org>
Group:		Applications/System
Source0:	http://people.debian.org/~kov/gksu/gksu/%{name}-%{version}.tar.gz
# Source0-md5:	fe5ac944ca1a86b931290971dc8c3da6
URL:		http://www.nongnu.org/gksu/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libgksu-devel >= 1.2.3
BuildRequires:	libgksuui-devel >= 1.0
BuildRequires:	gtk+2-devel >= 2:2.2
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
Requires:	/bin/su
Requires:	nautilus
Obsoletes:	gksu-devel
Obsoletes:	gksu-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKsu is a GTK+ frontend to the su program.

%description -l pl
GKsu to graficzna nak³adka na program su.

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
%dir %{_datadir}/gksu
%{_datadir}/gksu/gksu-migrate-conf.sh
%{_libdir}/nautilus/extensions-1.0/libnautilus-gksu.so
