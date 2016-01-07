%define api_version 0.0
%define lib_major   0
%define lib_name    %mklibname uhttpmock %{api_version} %{lib_major}
%define gi_name     %mklibname uhttpmock-gir %{api_version}
%define develname   %mklibname -d uhttpmock

%define url_ver     %(echo %{version}|cut -d. -f1,2)

Summary:	HTTP web service mocking library
Name:		uhttpmock
Version:	0.5.0
Release:	1
Epoch:		1
Group:		System/Libraries
License:	LGPL-2.1+
URL:		https://gitlab.com/uhttpmock/uhttpmock
Source0:	https://tecnocode.co.uk/downloads/uhttpmock/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.16.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.16
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.4
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	gtk-doc
BuildRequires:	intltool

%description
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package -n %{lib_name}
Summary:  %{summary}
Group: %{group}

%description -n %{lib_name}
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request/response traces.

%package -n %develname
Summary: Support files necessary to compile applications with %{name}
Group: Development/C
Requires: %{lib_name} = %epoch:%{version}
Provides: %{name}-%{api_version}-devel = %epoch:%{version}-%{release}
Provides: %{name}-devel = %epoch:%{version}-%{release}

%description -n %develname
Libraries, headers, and support files necessary to compile
applications using %{name}.

%package -n %{gi_name}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{lib_name} = %epoch:%{version}-%{release}

%description -n %{gi_name}
GObject Introspection interface library for %{name}.

%prep
%setup -q

%build
%configure --enable-gtk-doc --disable-static --enable-introspection --enable-vala
%make

%install
%makeinstall_std

# remove unpackaged files
rm -rf %{buildroot}%{_datadir}/../doc/lib%{name}
rm -f %{buildroot}%{_libdir}/*.la

%files -n %{lib_name}
%doc AUTHORS COPYING README NEWS
%{_libdir}/lib%{name}*-%{api_version}.so.%{lib_major}*

%files -n %develname
%doc %{_datadir}/gtk-doc/html/lib%{name}-%{api_version}
%{_datadir}/gir-1.0/Uhm-%{api_version}.gir
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/vala/vapi/lib%{name}-%{api_version}.*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Uhm-%{api_version}.typelib
