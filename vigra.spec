%define major 4
%define libname	%mklibname %{name} %{major}
%define olddevel %libname-devel
%define libnamedevel %mklibname %{name} -d

Summary:	Generic Programming for Computer Vision
Name:		vigra
Version:	1.8.0
Release:	%mkrel 2
License:	MIT
Group:		Development/C
URL:		http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
Source0:	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}-%{version}-src.tar.gz
Patch0:		vigra-1.8.0.lib_suffix.patch
BuildRequires:	boost-devel
#BuildRequires:	boost-python ?
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	fftw-devel > 3
BuildRequires:	hdf5-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
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
