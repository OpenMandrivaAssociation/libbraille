%define	major 14
%define	libname %mklibname braille %{major}
%define develname %mklibname braille -d

Summary:	Easy access to Braille displays and terminals
Name:		libbraille
Version:	0.19.0
Release:	%mkrel 12
License:	LGPL
Group:		System/Libraries
URL:		http://libbraille.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		libbraille-libtool_fixes.diff
Patch1:		libbraille-0.19.0-ltdl_fixes.diff
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	libusb-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libtool-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{libname}
Summary:	Shared libbraille library
Group:		System/Libraries

%description -n	%{libname}
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

%package -n	%{develname}
Summary:	Header files, libraries and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
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

This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n	python-braille
Summary:	Python bindings for libbraille
Group:		Development/Python
Requires:	%{libname} = %{version}

%description -n	python-braille
This package contains Python bindings for libbraille.

%prep

%setup -q
%patch0 -p1
%patch1 -p0

%build
%serverbuild

rm -rf libltdl
libtoolize --force --copy --install --ltdl
autoreconf -fi

%configure2_5x \
    --without-included-ltdl \
    --with-ltdl-include=%{_includedir} \
    --with-ltdl-lib=%{_libdir} \
    --with-pic \
    --disable-rpath \
    --enable-python \
    --enable-usb

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# antibork
find %{buildroot}%{_libdir} -name "*.la" | xargs perl -pi -e "s|\ -L%{_builddir}/%{name}-%{version}/lib||g"

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog README TODO
%config(noreplace) %{_sysconfdir}/libbraille.conf
%{_bindir}/*
%{_libdir}/*.so.*
%dir %{_libdir}/libbraille
%{_libdir}/libbraille/*.so
%{_datadir}/libbraille

%files -n python-braille
%defattr(-,root,root)
%{py_sitedir}/*.py*
%{py_platsitedir}/*.so

%files -n %{develname}
%defattr(-,root,root,0755)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/libbraille/*.*a
%{py_platsitedir}/*.*a



%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.19.0-10mdv2011.0
+ Revision: 660220
- mass rebuild

* Wed Nov 18 2009 Oden Eriksson <oeriksson@mandriva.com> 0.19.0-9mdv2011.0
+ Revision: 467253
- link against system libltdl.so.7

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 0.19.0-8mdv2010.0
+ Revision: 439788
- rebuild for new libusb

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.19.0-7mdv2010.0
+ Revision: 425520
- rebuild

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.19.0-6mdv2009.1
+ Revision: 319057
- rebuild for python 2.6

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.19.0-5mdv2009.1
+ Revision: 316999
- really use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.19.0-4mdv2009.0
+ Revision: 222508
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Mar 10 2008 Antoine Ginies <aginies@mandriva.com> 0.19.0-3mdv2008.1
+ Revision: 183934
- rebuild for 2008 spring

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0.19.0-2mdv2008.0
+ Revision: 79448
- fix deps

* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0.19.0-1mdv2008.0
+ Revision: 79399
- Import libbraille



* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0.19.0-1mdv2008.0
- initial Mandriva package (opensuse import)
