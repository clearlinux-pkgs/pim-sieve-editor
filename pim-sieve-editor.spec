#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : pim-sieve-editor
Version  : 24.02.0
Release  : 62
URL      : https://download.kde.org/stable/release-service/24.02.0/src/pim-sieve-editor-24.02.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.0/src/pim-sieve-editor-24.02.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.0/src/pim-sieve-editor-24.02.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: pim-sieve-editor-bin = %{version}-%{release}
Requires: pim-sieve-editor-data = %{version}-%{release}
Requires: pim-sieve-editor-lib = %{version}-%{release}
Requires: pim-sieve-editor-license = %{version}-%{release}
Requires: pim-sieve-editor-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kimap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : libksieve-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qtkeychain-dev
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the pim-sieve-editor package.
Group: Binaries
Requires: pim-sieve-editor-data = %{version}-%{release}
Requires: pim-sieve-editor-license = %{version}-%{release}

%description bin
bin components for the pim-sieve-editor package.


%package data
Summary: data components for the pim-sieve-editor package.
Group: Data

%description data
data components for the pim-sieve-editor package.


%package doc
Summary: doc components for the pim-sieve-editor package.
Group: Documentation

%description doc
doc components for the pim-sieve-editor package.


%package lib
Summary: lib components for the pim-sieve-editor package.
Group: Libraries
Requires: pim-sieve-editor-data = %{version}-%{release}
Requires: pim-sieve-editor-license = %{version}-%{release}

%description lib
lib components for the pim-sieve-editor package.


%package license
Summary: license components for the pim-sieve-editor package.
Group: Default

%description license
license components for the pim-sieve-editor package.


%package locales
Summary: locales components for the pim-sieve-editor package.
Group: Default

%description locales
locales components for the pim-sieve-editor package.


%prep
%setup -q -n pim-sieve-editor-24.02.0
cd %{_builddir}/pim-sieve-editor-24.02.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710525218
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710525218
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pim-sieve-editor
cp %{_builddir}/pim-sieve-editor-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/pim-sieve-editor-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/pim-sieve-editor-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/pim-sieve-editor-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/pim-sieve-editor-%{version}/src/org.kde.sieveeditor.desktop.license %{buildroot}/usr/share/package-licenses/pim-sieve-editor/864bc0eb28c73bd997ac19ff91935ab771846615 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang sieveeditor
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/sieveeditor
/usr/bin/sieveeditor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.sieveeditor.desktop
/usr/share/config.kcfg/sieveeditorglobalconfig.kcfg
/usr/share/icons/hicolor/16x16/apps/sieveeditor.png
/usr/share/icons/hicolor/22x22/apps/sieveeditor.png
/usr/share/icons/hicolor/32x32/apps/sieveeditor.png
/usr/share/icons/hicolor/48x48/apps/sieveeditor.png
/usr/share/icons/hicolor/64x64/apps/sieveeditor.png
/usr/share/icons/hicolor/scalable/apps/sieveeditor.svg
/usr/share/metainfo/org.kde.sieveeditor.appdata.xml
/usr/share/qlogging-categories6/sieveeditor.categories
/usr/share/qlogging-categories6/sieveeditor.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/sieveeditor/first-start.png
/usr/share/doc/HTML/ca/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/ca/sieveeditor/index.docbook
/usr/share/doc/HTML/de/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/de/sieveeditor/index.docbook
/usr/share/doc/HTML/en/sieveeditor/first-start.png
/usr/share/doc/HTML/en/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/en/sieveeditor/index.docbook
/usr/share/doc/HTML/en/sieveeditor/script-edit.png
/usr/share/doc/HTML/en/sieveeditor/script-help.png
/usr/share/doc/HTML/en/sieveeditor/script-tools.png
/usr/share/doc/HTML/es/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/es/sieveeditor/index.docbook
/usr/share/doc/HTML/et/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/et/sieveeditor/index.docbook
/usr/share/doc/HTML/it/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/it/sieveeditor/index.docbook
/usr/share/doc/HTML/nl/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/nl/sieveeditor/index.docbook
/usr/share/doc/HTML/pt/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/pt/sieveeditor/index.docbook
/usr/share/doc/HTML/pt_BR/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/pt_BR/sieveeditor/index.docbook
/usr/share/doc/HTML/ru/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/ru/sieveeditor/index.docbook
/usr/share/doc/HTML/sv/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/sv/sieveeditor/index.docbook
/usr/share/doc/HTML/uk/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/uk/sieveeditor/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libsieveeditor.so.6.0.0
/usr/lib64/libsieveeditor.so.6
/usr/lib64/libsieveeditor.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pim-sieve-editor/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/pim-sieve-editor/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/pim-sieve-editor/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/pim-sieve-editor/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/pim-sieve-editor/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f sieveeditor.lang
%defattr(-,root,root,-)

