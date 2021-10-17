#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : pim-sieve-editor
Version  : 21.08.2
Release  : 30
URL      : https://download.kde.org/stable/release-service/21.08.2/src/pim-sieve-editor-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/pim-sieve-editor-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/pim-sieve-editor-21.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: pim-sieve-editor-bin = %{version}-%{release}
Requires: pim-sieve-editor-data = %{version}-%{release}
Requires: pim-sieve-editor-lib = %{version}-%{release}
Requires: pim-sieve-editor-license = %{version}-%{release}
Requires: pim-sieve-editor-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kbookmarks-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kiconthemes-dev
BuildRequires : kimap-dev
BuildRequires : kio-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libksieve-dev
BuildRequires : libsecret-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtkeychain-dev
BuildRequires : syntax-highlighting-dev

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
%setup -q -n pim-sieve-editor-21.08.2
cd %{_builddir}/pim-sieve-editor-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634444448
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634444448
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pim-sieve-editor
cp %{_builddir}/pim-sieve-editor-21.08.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/pim-sieve-editor/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/pim-sieve-editor-21.08.2/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/pim-sieve-editor-21.08.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/pim-sieve-editor-21.08.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/pim-sieve-editor-21.08.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/pim-sieve-editor-21.08.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/pim-sieve-editor/a4c60b3fefda228cd7439d3565df043192fef137
pushd clr-build
%make_install
popd
%find_lang sieveeditor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sieveeditor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.sieveeditor.desktop
/usr/share/config.kcfg/sieveeditorglobalconfig.kcfg
/usr/share/kconf_update/sieveeditor-15.08-kickoff.sh
/usr/share/kconf_update/sieveeditor.upd
/usr/share/metainfo/org.kde.sieveeditor.appdata.xml
/usr/share/qlogging-categories5/sieveeditor.categories
/usr/share/qlogging-categories5/sieveeditor.renamecategories

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
/usr/lib64/libsieveeditor.so.5
/usr/lib64/libsieveeditor.so.5.18.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pim-sieve-editor/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/pim-sieve-editor/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/pim-sieve-editor/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/pim-sieve-editor/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/pim-sieve-editor/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/pim-sieve-editor/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f sieveeditor.lang
%defattr(-,root,root,-)

