%define major 4
%define libname	%mklibname %{name} %{major}
%define olddevel %libname-devel
%define libnamedevel %mklibname %{name} -d

Summary:	Generic Programming for Computer Vision
Name:		vigra
Version:	1.8.0
Release:	3
License:	MIT
Group:		Development/C
URL:		http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
Source0:	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}-%{version}-src.tar.gz
Patch0:		vigra-1.8.0.lib_suffix.patch
Patch1:		vigra-1.8.0.gcc47.patch
BuildRequires:	boost-devel
#BuildRequires:	boost-python ?
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	fftw-devel > 3
BuildRequires:	hdf5-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	tiff-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	python-devel
BuildRequires:	python-numpy
BuildRequires:	python-numpy-devel
BuildRequires:	python-sphinx
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel computer vision
library that puts its main emphasize on customizable algorithms and data
structures. By using template techniques similar to those in the C++ Standard
Template Library, you can easily adapt any VIGRA component to the needs of your
application, without thereby giving up execution speed.

%package -n	python-vigra
Summary:	Python interface for the vigra computer vision library
Requires:	%{libname} >= %{version}-%{release}
Requires:	python-numpy

%description -n	python-vigra
The vigra-python package provides python bindings for vigra

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n	%{libnamedevel}
Summary:	Development header files for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{name} -d 2}

%description -n	%{libnamedevel}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake
%make VERBOSE=1

%install
rm -rf %{buildroot}

%makeinstall_std -C build

rm -rf %{buildroot}/usr/doc

%multiarch_binaries %{buildroot}%{_bindir}/vigra-config

# cleanup
rm -f doc/vigranumpy/.buildinfo
find doc -type d | xargs chmod 755
find doc -type f | xargs chmod 644

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr (-,root,root)
%doc LICENSE.txt README.txt
%{_libdir}/libvigraimpex.so.%{major}*

%files -n %{libnamedevel}
%defattr (0755,root,root,0755)
%{multiarch_bindir}/vigra-config
%{_bindir}/vigra-config
%defattr (0644,root,root,0755)
%doc doc/vigra doc/vigranumpy
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_libdir}/*.so

%files -n python-vigra
%defattr(-, root, root,-)
%{python_sitearch}/vigra


%changelog
* Tue Jul 03 2012 Crispin Boylan <crisb@mandriva.org> 1.8.0-3
+ Revision: 807909
- Patch1: gcc 4.7 build fix from fedora
- Rebuild for new boost

* Thu Dec 22 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-2
+ Revision: 744418
- rebuilt against libtiff.so.5

* Sun Oct 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-1
+ Revision: 702476
- 1.8.0
- sync a bit with fedora
- attempt to relink against libpng15.so.15

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-8
+ Revision: 661755
- multiarch fixes

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-7mdv2011.0
+ Revision: 608124
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-6mdv2010.1
+ Revision: 488807
- rebuilt against libjpeg v8

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.5.0-5mdv2010.0
+ Revision: 434673
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-3mdv2009.0
+ Revision: 255552
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.5.0-1mdv2008.1
+ Revision: 136570
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Couriousous <couriousous@mandriva.org> 1.5.0-1mdv2008.0
+ Revision: 54863
- 1.5.0
- Import vigra

