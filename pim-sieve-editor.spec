#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : pim-sieve-editor
Version  : 18.12.2
Release  : 4
URL      : https://download.kde.org/stable/applications/18.12.2/src/pim-sieve-editor-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/pim-sieve-editor-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/pim-sieve-editor-18.12.2.tar.xz.sig
Summary  : Mail sieve editor
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: pim-sieve-editor-bin = %{version}-%{release}
Requires: pim-sieve-editor-data = %{version}-%{release}
Requires: pim-sieve-editor-lib = %{version}-%{release}
Requires: pim-sieve-editor-license = %{version}-%{release}
Requires: pim-sieve-editor-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kimap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libksieve-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
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
%setup -q -n pim-sieve-editor-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549939733
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549939733
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pim-sieve-editor
cp COPYING %{buildroot}/usr/share/package-licenses/pim-sieve-editor/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/pim-sieve-editor/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/pim-sieve-editor/COPYING.LIB
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
/usr/share/xdg/sieveeditor.categories
/usr/share/xdg/sieveeditor.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/sieveeditor/first-start.png
/usr/share/doc/HTML/ca/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/ca/sieveeditor/index.docbook
/usr/share/doc/HTML/ca/sieveeditor/script-edit.png
/usr/share/doc/HTML/ca/sieveeditor/script-help.png
/usr/share/doc/HTML/ca/sieveeditor/script-tools.png
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
/usr/share/doc/HTML/sv/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/sv/sieveeditor/index.docbook
/usr/share/doc/HTML/uk/sieveeditor/index.cache.bz2
/usr/share/doc/HTML/uk/sieveeditor/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsieveeditor.so.5
/usr/lib64/libsieveeditor.so.5.10.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pim-sieve-editor/COPYING
/usr/share/package-licenses/pim-sieve-editor/COPYING.DOC
/usr/share/package-licenses/pim-sieve-editor/COPYING.LIB

%files locales -f sieveeditor.lang
%defattr(-,root,root,-)

