Summary:	GKsu is a GTK+ frontend to the su program
Summary(pl):	GKsu to nak³adka graficzna na program su
Name:		gksu
Version:	0.9.15
Release:	1
License:	GPL
Vendor:		Gustavo Noronha Silva <kov@debian.org>
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	14e3440ace72df90f1fdd695deef737c
URL:		http://www.nongnu.org/gksu/
BuildRequires:	gtk+2-devel >= 2.2
BuildRequires:	gdk-pixbuf-devel >= 0.22
BuildRequires:	pango-devel
Requires:	/bin/su
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKsu is a GTK+ frontend to the su program.

%description -l pl
GKsu to graficzna nak³adka na program su.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/System

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/gnome/apps/System/*desktop $RPM_BUILD_ROOT%{_applnkdir}/System

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/System/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
