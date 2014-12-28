#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc

Summary:	MATE Desktop Window Navigator Construction Kit library
Summary(pl.UTF-8):	Biblioteka Window Navigator Construction Kit dla środowiska MATE Desktop
Name:		libmatewnck
Version:	1.6.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	30c96e0120b0c709b417d787b2aa3033
URL:		http://wiki.mate-desktop.org/roadmap:transition_to_libmatewnck
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gobject-introspection-devel >= 0.6.14
BuildRequires:	gtk+2-devel >= 2:2.19.7
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.9}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig >= 1:0.14.0
BuildRequires:	startup-notification-devel >= 0.4
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xz
Requires:	glib2 >= 1:2.16.0
Requires:	gtk+2 >= 2:2.19.7
Requires:	startup-notification >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Window Navigator Construction Kit (WNCK) library for MATE Desktop.

%description -l pl.UTF-8
Biblioteka WNCK (Window Navigator Construction Kit) do tworzenia
nawigatorów okien dla środowiska MATE Desktop.

%package devel
Summary:	Header files for libmatewnck
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmatewnck
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0
Requires:	gtk+2-devel >= 2:2.19.7
Requires:	startup-notification-devel >= 0.4
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXres-devel

%description devel
Header files for libmatewnck.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmatewnck.

%package apidocs
Summary:	libmatewnck API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmatewnck
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmatewnck API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmatewnck.

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	%{__enable_disable apidocs gtk-doc} \
	--disable-silent-rules \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmatewnck.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/matewnck-urgency-monitor
%attr(755,root,root) %{_bindir}/matewnckprop
%attr(755,root,root) %{_libdir}/libmatewnck.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmatewnck.so.0
%{_libdir}/girepository-1.0/Matewnck-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmatewnck.so
%{_includedir}/libmatewnck
%{_datadir}/gir-1.0/Matewnck-1.0.gir
%{_pkgconfigdir}/libmatewnck.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmatewnck
%endif
