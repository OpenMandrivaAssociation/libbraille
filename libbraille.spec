%define major 14
%define libname	%mklibname braille %{major}
%define devname	%mklibname braille -d

%define _disable_lto 1
%define _disable_rebuild_configure 1

Summary:	Easy access to Braille displays and terminals
Name:		libbraille
Version:	0.19.0
Release:	26
License:	LGPLv2
Group:		System/Libraries
Url:		http://libbraille.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		libbraille-libtool_fixes.diff
Patch1:		libbraille-0.19.0-ltdl_fixes.diff
Patch2:		libbraille-automake-1.13.patch

BuildRequires:	libtool
BuildRequires:	swig
BuildRequires:	libtool-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libusb)
Conflicts:	%{_lib}braille14 < 0.19.0-13

%description
This library makes it possible to easily access Braille displays and
terminals : you can write text on the braille display, directly draw braille
dots, or get the value of pressed keys. It is compatible with a wide range
of braille displays.

The features contain:
* usable from C, C++, Python and Java
* supports over 10 braille displays (including some recent models)
* easy configuration of the braille table
* distributed under the LGPL Free Software Licence
* portable (currently linux and win32)
* packages available
* easy to incorporate in any application wanting to use braille displays
(simple shared library)
* uses autoconf, automake and libtool for easier installation and portability
* contains a virtual graphical terminal made with Gtk+ for developers testing

%package -n %{libname}
Summary:	Shared libbraille library
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Header files, libraries and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n python-braille
Summary:	Python bindings for libbraille
Group:		Development/Python
Requires:	%{libname} = %{version}

%description -n	python-braille
This package contains Python bindings for libbraille.

%prep
%setup -q
%autopatch -p1

rm -rf libltdl
libtoolize --force --copy --install --ltdl
autoreconf -fi

%build
%serverbuild

%configure \
	--without-included-ltdl \
	--with-ltdl-include=%{_includedir} \
	--with-ltdl-lib=%{_libdir} \
	--with-pic \
	--enable-python \
	--with-pythoninc=/usr/include/python3.9 \
	--enable-usb

%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog README TODO
%config(noreplace) %{_sysconfdir}/libbraille.conf
%{_bindir}/*
%dir %{_libdir}/libbraille
%{_libdir}/libbraille/*.so
%{_datadir}/libbraille

%files -n %{libname}
%{_libdir}/libbraille.so.%{major}*

%files -n python-braille
%{py_puresitedir}/*.py*
%{py_platsitedir}/*.so

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
