%define major 11
%define libname %mklibname %{name} %{major}
%define olddevel %libname-devel
%define libnamedevel %mklibname %{name} -d
%bcond_with python

Name:		vigra
Version:	1.11.1
Release:	9
Summary:	Generic Programming for Computer Vision
License:	MIT
Group:		Development/C
Source0:	https://github.com/ukoethe/vigra/releases/download/Version-%(echo %{version}|sed -e 's,\.,-,g')/vigra-%{version}-src.tar.gz
URL:		http://ukoethe.github.io/vigra
Patch0:		vigra-openexr3.patch
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	fftw-devel >= 3
BuildRequires:	cmake
BuildRequires:	hdf5-devel
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(OpenEXR)
%if %{with python}
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-numpy-devel
%endif

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel computer vision
library that puts its main emphasis on customizable algorithms and data
structures. By using template techniques similar to those in the C++ Standard
Template Library, you can easily adapt any VIGRA component to the needs of your
application without thereby giving up execution speed.

%package -n python-vigra
Summary:	Python interface for the vigra computer vision library
Requires:	%{libname} >= %{version}-%{release}
Requires:	python-numpy

%description -n python-vigra
The vigra-python package provides python bindings for vigra.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{libnamedevel}
Summary:	Development header files for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname %{name} -d 4}

%description -n %{libnamedevel}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%autosetup -n %{name}-%{version} -p1

%build
export CXXFLAGS=-ftemplate-depth-1024
%cmake -DDOCINSTALL=share/doc/%{name} -DPYTHON_EXECUTABLE=/usr/bin/python2 -DWITH_OPENEXR=ON \
%if %{without python}
	-DWITH_VIGRANUMPY=0
%endif

%make_build VERBOSE=1
# cleanup
rm -f doc/vigranumpy/.buildinfo
rm -f %{buildroot}/%{_datadir}/doc/vigra/vigranumpy/.buildingo
rm -f %{buildroot}/%{_datadir}/doc/vigra-devel/vigranumpy/.buildingo

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libvigraimpex.so.%{major}*

%files -n %{libnamedevel}
%doc %{_datadir}/doc/%{name}
%{_bindir}/vigra-config
%{_includedir}/vigra
%{_libdir}/libvigraimpex.so
%{_libdir}/vigra
%doc doc/vigra doc/vigranumpy

%if %{with python}
%files -n python-vigra
%{python2_sitearch}/vigra
%{_libdir}/vigranumpy/VigranumpyConfig.cmake
%endif
