%define name	vigra
%define version	1.5.0
%define release	%mkrel 5
%define major	2
%define libname	%mklibname %{name} %{major}
%define olddevel %libname-devel
%define libnamedevel %mklibname %{name} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Generic Programming for Computer Vision
License:	MIT
Group:		Development/C
Source0:	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}%{version}.tar.bz2
URL:		http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	zlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	fftw-devel > 3

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel computer vision
library that puts its main emphasize on customizable algorithms and data
structures. By using template techniques similar to those in the C++ Standard
Template Library, you can easily adapt any VIGRA component to the needs of your
application, without thereby giving up execution speed.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{libnamedevel}
Summary:        Development header files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{olddevel}
%description -n %{libnamedevel}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q -n %{name}%{version}

%build
#cd config
#aclocal
#autoconf
#cp -f configure ../
#cd ..
#ln -s config/configure.in
#libtoolize --force
./configure --prefix=%_prefix --libdir=%_libdir --bindir=%_bindir \
	--includedir=%_includedir --docdir=%buildroot/%_docdir/%name  \
	--with-tiff \
	--with-jpeg \
	--with-png \
	--with-zlib \
	--with-fftw
%make CXXFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/vigra-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr (-,root,root)
%doc LICENSE.txt README.txt
%{_libdir}/*.so.*

%files -n %{libnamedevel}
%defattr (755,root,root,755)
%multiarch %{multiarch_bindir}/vigra-config
%{_bindir}/vigra-config
%defattr (644,root,root,755)
%doc %{_docdir}/%name
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
