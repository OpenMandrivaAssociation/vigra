%define major   5
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

%package -n python-vigra
Summary: Python interface for the vigra computer vision library
Requires: %{libname} >= %{version}-%{release}
Requires: python-numpy

%description -n python-vigra
The vigra-python package provides python bindings for vigra

%package -n %{libname}
Summary: Main library for %{name}
Group: System/Libraries
Provides: lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{libnamedevel}
Summary: Development header files for %{name}
Group: Development/C
Requires: %{libname} >= %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname %{name} -d 4}

%description -n %{libnamedevel}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DDOCINSTALL=share/doc/%{name}

%make VERBOSE=1
# cleanup
rm -f doc/vigranumpy/.buildinfo
rm -f %{buildroot}/%{_datadir}/doc/vigra/vigranumpy/.buildingo
rm -f %{buildroot}/%{_datadir}/doc/vigra-devel/vigranumpy/.buildingo

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libvigraimpex.so.%{major}*

%files -n %{libnamedevel}
%doc %{_datadir}/doc/%{name}
%{_bindir}/vigra-config
%{_includedir}/vigra
%{_libdir}/libvigraimpex.so
%{_libdir}/vigra
%{_libdir}/vigranumpy/VigranumpyConfig.cmake
%doc doc/vigra doc/vigranumpy

%files -n python-vigra
%{python_sitearch}/vigra
