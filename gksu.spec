Summary:	GKsu is a GTK+ frontend to the su program
Summary(pl):	GKsu to nak³adka graficzna na program su
Name:		gksu
Version:	1.2.2
Release:	1
License:	GPL
Vendor:		Gustavo Noronha Silva <kov@debian.org>
Group:		Applications/System
Source0:	http://people.debian.org/~kov/gksu/gksu/%{name}-%{version}.tar.gz
# Source0-md5:	564504badbd41fbe554a8133d07b5e94
URL:		http://www.nongnu.org/gksu/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libgksu-devel >= 1.2.3
BuildRequires:	libgksuui-devel >= 1.0
BuildRequires:	gtk+2-devel >= 2:2.2
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
Requires:	/bin/su
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
