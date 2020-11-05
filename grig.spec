#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grig
Version  : 0.8.1
Release  : 7
URL      : https://sourceforge.net/projects/groundstation/files/Grig/0.8.1/grig-0.8.1.tar.gz
Source0  : https://sourceforge.net/projects/groundstation/files/Grig/0.8.1/grig-0.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: grig-bin = %{version}-%{release}
Requires: grig-data = %{version}-%{release}
Requires: grig-license = %{version}-%{release}
Requires: grig-locales = %{version}-%{release}
Requires: grig-man = %{version}-%{release}
BuildRequires : gettext
BuildRequires : hamlib-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtk+-2.0)

%description
1. About Grig
Grig is a graphical user interface for the Ham Radio Control Libraries. It is
intended to be simple and generic, presenting the user to the same interface
regardless of which radio he or she uses.

%package bin
Summary: bin components for the grig package.
Group: Binaries
Requires: grig-data = %{version}-%{release}
Requires: grig-license = %{version}-%{release}

%description bin
bin components for the grig package.


%package data
Summary: data components for the grig package.
Group: Data

%description data
data components for the grig package.


%package license
Summary: license components for the grig package.
Group: Default

%description license
license components for the grig package.


%package locales
Summary: locales components for the grig package.
Group: Default

%description locales
locales components for the grig package.


%package man
Summary: man components for the grig package.
Group: Default

%description man
man components for the grig package.


%prep
%setup -q -n grig-0.8.1
cd %{_builddir}/grig-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604620689
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604620689
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grig
cp %{_builddir}/grig-0.8.1/COPYING %{buildroot}/usr/share/package-licenses/grig/b47456e2c1f38c40346ff00db976a2badf36b5e3
%make_install
%find_lang grig

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/grig

%files data
%defattr(-,root,root,-)
/usr/share/grig/AUTHORS
/usr/share/grig/COPYING
/usr/share/grig/ChangeLog
/usr/share/grig/NEWS
/usr/share/grig/README
/usr/share/pixmaps/grig/digits_normal.png
/usr/share/pixmaps/grig/digits_small.png
/usr/share/pixmaps/grig/grig-logo.png
/usr/share/pixmaps/grig/ic910.png
/usr/share/pixmaps/grig/smeter.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grig/b47456e2c1f38c40346ff00db976a2badf36b5e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/grig.1

%files locales -f grig.lang
%defattr(-,root,root,-)

