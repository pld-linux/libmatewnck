#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc

Summary:	MATE Desktop Window Navigator Construction Kit libraries
Name:		libmatewnck
Version:	1.5.0
Release:	1
License:	LGPL v2+ and GPL v2+
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	0ab7beab37cd27b3b9624e31ea2716ad
URL:		http://wiki.mate-desktop.org/roadmap:transition_to_libmatewnck
BuildRequires:	cairo-gobject-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.9}
BuildRequires:	mate-common
BuildRequires:	pkgconfig >= 0.14.0
BuildRequires:	startup-notification-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Window navigator construction Kit for MATE Desktop

%package devel
Summary:	Development libraries and headers for libmatewnck
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development libraries and headers for libmatewnck

%package apidocs
Summary:	libmatewnck API documentation
Summary(pl.UTF-8):	Dokumentacja API libmatewnck
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmatewnck API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libmatewnck.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	%{__enable_disable apidocs gtk-doc} \
	--with-html-dir=%{_gtkdocdir} \
	--disable-static \

%{__make} \
	V=1

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
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/matewnck-urgency-monitor
%attr(755,root,root) %{_bindir}/matewnckprop
%attr(755,root,root) %{_libdir}/libmatewnck.so.*.*.*
%ghost %{_libdir}/libmatewnck.so.0
%{_libdir}/girepository-1.0/Matewnck-1.0.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmatewnck.so
%{_pkgconfigdir}/libmatewnck.pc
%{_includedir}/libmatewnck
%{_datadir}/gir-1.0/Matewnck-1.0.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmatewnck
%endif
