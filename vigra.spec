%define major   2
%define libname %mklibname %{name} %{major}
%define olddevel %libname-devel
%define libnamedevel %mklibname %{name} -d

Name:           vigra
Version:        1.10.0
Release:        2
Summary:        Generic Programming for Computer Vision
License:        MIT
Group:          Development/C
Source0:        http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}-%{version}-src-with-docu.tar.gz
URL:            http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
BuildRequires:  zlib-devel jpeg-devel libpng-devel libtiff-devel fftw-devel >= 3
BuildRequires:  cmake hdf5-devel boost-devel doxygen python-sphinx python-numpy-devel

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel computer vision
library that puts its main emphasis on customizable algorithms and data
structures. By using template techniques similar to those in the C++ Standard
Template Library, you can easily adapt any VIGRA component to the needs of your
application without thereby giving up execution speed.

%package devel
Summary: Development tools for programs which will use the vigra library
Group: Development/C
Requires: vigra = %{version}-%{release}
Requires: jpeg-devel tiff-devel png-devel zlib-devel fftw-devel >= 3
Requires: hdf5-devel boost-devel python-sphinx python-numpy

%description devel
The vigra-devel package includes the header files necessary for developing
programs that use the vigra library.

%package python
Summary: Python interface for the vigra computer vision library
Group: Development/Python
Requires: vigra = %{version}-%{release}
Requires: python-numpy-devel 

%description python
The vigra-python package provides python bindings for vigra

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DDOCINSTALL=share/doc/%{name}

%make VERBOSE=1
# cleanup
rm -f doc/vigranumpy/.buildinfo

%install
%makeinstall_std -C build

%files
%{_libdir}/libvigraimpex.so.*

%files devel
%doc %{_datadir}/doc/%{name}
%{_bindir}/vigra-config
%{_includedir}/vigra
%{_libdir}/libvigraimpex.so
%{_libdir}/vigra
%{_libdir}/vigranumpy/VigranumpyConfig.cmake
%doc doc/vigra doc/vigranumpy

%files python
%{python_sitearch}/vigra
