Name:           libimagequant
Version:        2.17.0
Release:        1
Summary:        Palette quantization library
License:        GPLv3+ and MIT
URL:            https://github.com/ImageOptim/libimagequant
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
The portable C library can convert RGBA images into
8-bit indexed color images with high quality.

%package        devel
Summary:        Development files for libimagequant
Requires:       %{name} = %{version}-%{release}

%description    devel
The libimagequant-deve package contains the libraries
and header files for the application.

%prep
%autosetup -p1

%build
%configure --with-openmp
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/%{name}.a

%ldconfig_scriptlets

%files
%license COPYRIGHT
%{_libdir}/%{name}.so.0
%doc README.md CHANGELOG

%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/imagequant.pc

%changelog
* Fri Aug 05 2022 tianlijing <tianlijing@kylinos.cn> - 2.17.0-1
- update to 2.17.0

* Fri Dec 03 2021 xingxing <xingxing9@huawei.com> - 2.15.1-1
- update to 2.15.1

* Tue Jun 08 2021 liuyumeng <liuyumeng5@huawei.com> - 2.14.0-2
- Add a BuildRequires for gcc

* Tue Feb 02 2021 zhanzhimin <zhanzhimin@huawei.com> - 2.14.0-1
- update to 2.14.0

* Thu Nov 14 2019 wangye<wangye54@huawei.com> - 2.12.5-2
- Package init

