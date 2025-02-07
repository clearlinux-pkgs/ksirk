#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksirk
Version  : 24.12.2
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.12.2/src/ksirk-24.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.2/src/ksirk-24.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.2/src/ksirk-24.12.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : A turn by turn multiplayer strategy game with AI (Risk clone)
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: ksirk-bin = %{version}-%{release}
Requires: ksirk-data = %{version}-%{release}
Requires: ksirk-license = %{version}-%{release}
Requires: ksirk-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KsirK is a computerized version of a well known strategy board game: Risk ! 

In the current version, KsirK is a usable multi-player mono-machine game with a basic AI. Planned future versions will be really network-enabled multi-playered with a better AI and a lot more enhancements (see Status for details).

The goal of the game is simply to conquer the World... It is done by attacking your neighbors with your armies.

%package bin
Summary: bin components for the ksirk package.
Group: Binaries
Requires: ksirk-data = %{version}-%{release}
Requires: ksirk-license = %{version}-%{release}

%description bin
bin components for the ksirk package.


%package data
Summary: data components for the ksirk package.
Group: Data

%description data
data components for the ksirk package.


%package doc
Summary: doc components for the ksirk package.
Group: Documentation

%description doc
doc components for the ksirk package.


%package license
Summary: license components for the ksirk package.
Group: Default

%description license
license components for the ksirk package.


%package locales
Summary: locales components for the ksirk package.
Group: Default

%description locales
locales components for the ksirk package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n ksirk-24.12.2
cd %{_builddir}/ksirk-24.12.2
pushd ..
cp -a ksirk-24.12.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738953521
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1738953521
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksirk
cp %{_builddir}/ksirk-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/ksirk/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/ksirk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ksirk/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4 || :
cp %{_builddir}/ksirk-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/ksirk/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
cp %{_builddir}/ksirk-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/ksirk/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang ksirk
%find_lang ksirkskineditor
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ksirk
/V3/usr/bin/ksirkskineditor
/usr/bin/ksirk
/usr/bin/ksirkskineditor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ksirk.desktop
/usr/share/applications/org.kde.ksirkskineditor.desktop
/usr/share/config.kcfg/ksirksettings.kcfg
/usr/share/config.kcfg/ksirkskineditorsettings.kcfg
/usr/share/icons/hicolor/128x128/apps/ksirk.png
/usr/share/icons/hicolor/16x16/apps/ksirk.png
/usr/share/icons/hicolor/22x22/apps/ksirk.png
/usr/share/icons/hicolor/32x32/apps/ksirk.png
/usr/share/icons/hicolor/48x48/apps/ksirk.png
/usr/share/icons/hicolor/64x64/apps/ksirk.png
/usr/share/icons/hicolor/scalable/apps/ksirk.svgz
/usr/share/knsrcfiles/ksirk.knsrc
/usr/share/ksirk/skins/default/Data/world.desktop
/usr/share/ksirk/skins/default/Images/2DownArrow.png
/usr/share/ksirk/skins/default/Images/2UpArrow.png
/usr/share/ksirk/skins/default/Images/arena.svg
/usr/share/ksirk/skins/default/Images/attackAuto.png
/usr/share/ksirk/skins/default/Images/attackOne.png
/usr/share/ksirk/skins/default/Images/attackThree.png
/usr/share/ksirk/skins/default/Images/attackTwo.png
/usr/share/ksirk/skins/default/Images/cancel.png
/usr/share/ksirk/skins/default/Images/defendOne.png
/usr/share/ksirk/skins/default/Images/defendTwo.png
/usr/share/ksirk/skins/default/Images/downArrow.png
/usr/share/ksirk/skins/default/Images/loader.gif
/usr/share/ksirk/skins/default/Images/logoLeft.png
/usr/share/ksirk/skins/default/Images/logoRight.png
/usr/share/ksirk/skins/default/Images/map-mask.png
/usr/share/ksirk/skins/default/Images/moveArmies.png
/usr/share/ksirk/skins/default/Images/moveBackFive.png
/usr/share/ksirk/skins/default/Images/moveBackOne.png
/usr/share/ksirk/skins/default/Images/moveBackTen.png
/usr/share/ksirk/skins/default/Images/moveFinish.png
/usr/share/ksirk/skins/default/Images/moveFive.png
/usr/share/ksirk/skins/default/Images/moveOne.png
/usr/share/ksirk/skins/default/Images/moveTen.png
/usr/share/ksirk/skins/default/Images/newNetGame.png
/usr/share/ksirk/skins/default/Images/nextPlayer.png
/usr/share/ksirk/skins/default/Images/pool.svg
/usr/share/ksirk/skins/default/Images/recycling.png
/usr/share/ksirk/skins/default/Images/recyclingFinished.png
/usr/share/ksirk/skins/default/Images/snapshot.jpg
/usr/share/ksirk/skins/default/Images/soldierKneeling.png
/usr/share/ksirk/skins/default/Images/stopAttackAuto.png
/usr/share/ksirk/skins/default/Images/upArrow.png
/usr/share/ksirk/skins/default/Sounds/cannon.wav
/usr/share/ksirk/skins/default/Sounds/crash.wav
/usr/share/ksirk/skins/default/Sounds/roll.wav
/usr/share/ksirk/skins/skinsdir
/usr/share/ksirkskineditor/cross.png
/usr/share/ksirkskineditor/target.png
/usr/share/metainfo/org.kde.ksirk.appdata.xml
/usr/share/qlogging-categories6/ksirk.categories
/usr/share/qlogging-categories6/ksirk.renamecategories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ksirk/index.cache.bz2
/usr/share/doc/HTML/ca/ksirk/index.docbook
/usr/share/doc/HTML/ca/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/ca/ksirkskineditor/index.docbook
/usr/share/doc/HTML/de/ksirk/index.cache.bz2
/usr/share/doc/HTML/de/ksirk/index.docbook
/usr/share/doc/HTML/de/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/de/ksirkskineditor/index.docbook
/usr/share/doc/HTML/en/ksirk/application-exit.png
/usr/share/doc/HTML/en/ksirk/attackOne.png
/usr/share/doc/HTML/en/ksirk/attackThree.png
/usr/share/doc/HTML/en/ksirk/attackTwo.png
/usr/share/doc/HTML/en/ksirk/attackmenu.png
/usr/share/doc/HTML/en/ksirk/autoattack.png
/usr/share/doc/HTML/en/ksirk/defensedialog.png
/usr/share/doc/HTML/en/ksirk/displaygoalmessage.png
/usr/share/doc/HTML/en/ksirk/displaygoalwarningmessage.png
/usr/share/doc/HTML/en/ksirk/document-new.png
/usr/share/doc/HTML/en/ksirk/firing-screenshot.png
/usr/share/doc/HTML/en/ksirk/index.cache.bz2
/usr/share/doc/HTML/en/ksirk/index.docbook
/usr/share/doc/HTML/en/ksirk/introscreen.png
/usr/share/doc/HTML/en/ksirk/invasionslider.png
/usr/share/doc/HTML/en/ksirk/joinnetgame.png
/usr/share/doc/HTML/en/ksirk/joueurSuivant.png
/usr/share/doc/HTML/en/ksirk/justjoined.png
/usr/share/doc/HTML/en/ksirk/messagesent.png
/usr/share/doc/HTML/en/ksirk/moveArmies.png
/usr/share/doc/HTML/en/ksirk/newgamedialog.png
/usr/share/doc/HTML/en/ksirk/numnetplayersdialog.png
/usr/share/doc/HTML/en/ksirk/placingarmies.png
/usr/share/doc/HTML/en/ksirk/playersetupdialog.png
/usr/share/doc/HTML/en/ksirk/preferences.png
/usr/share/doc/HTML/en/ksirk/recycling.png
/usr/share/doc/HTML/en/ksirk/recyclingFinished.png
/usr/share/doc/HTML/en/ksirk/shownumberofarmies.png
/usr/share/doc/HTML/en/ksirkskineditor/alaska.png
/usr/share/doc/HTML/en/ksirkskineditor/attackOne.png
/usr/share/doc/HTML/en/ksirkskineditor/attackThree.png
/usr/share/doc/HTML/en/ksirkskineditor/attackTwo.png
/usr/share/doc/HTML/en/ksirkskineditor/bluedices.png
/usr/share/doc/HTML/en/ksirkskineditor/cannon.png
/usr/share/doc/HTML/en/ksirkskineditor/cavalry.png
/usr/share/doc/HTML/en/ksirkskineditor/defendOne.png
/usr/share/doc/HTML/en/ksirkskineditor/defendTwo.png
/usr/share/doc/HTML/en/ksirkskineditor/document-open.png
/usr/share/doc/HTML/en/ksirkskineditor/document-save.png
/usr/share/doc/HTML/en/ksirkskineditor/exploding.png
/usr/share/doc/HTML/en/ksirkskineditor/firing.png
/usr/share/doc/HTML/en/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/en/ksirkskineditor/index.docbook
/usr/share/doc/HTML/en/ksirkskineditor/infantry.png
/usr/share/doc/HTML/en/ksirkskineditor/italy.png
/usr/share/doc/HTML/en/ksirkskineditor/main-snapshot.png
/usr/share/doc/HTML/en/ksirkskineditor/map-mask.png
/usr/share/doc/HTML/en/ksirkskineditor/map.png
/usr/share/doc/HTML/en/ksirkskineditor/mark1.png
/usr/share/doc/HTML/en/ksirkskineditor/moveArmies.png
/usr/share/doc/HTML/en/ksirkskineditor/newNetGame.png
/usr/share/doc/HTML/en/ksirkskineditor/nextPlayer.png
/usr/share/doc/HTML/en/ksirkskineditor/recycling.png
/usr/share/doc/HTML/en/ksirkskineditor/recyclingFinished.png
/usr/share/doc/HTML/en/ksirkskineditor/reddices.png
/usr/share/doc/HTML/es/ksirk/index.cache.bz2
/usr/share/doc/HTML/es/ksirk/index.docbook
/usr/share/doc/HTML/es/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/es/ksirkskineditor/index.docbook
/usr/share/doc/HTML/et/ksirk/index.cache.bz2
/usr/share/doc/HTML/et/ksirk/index.docbook
/usr/share/doc/HTML/et/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/et/ksirkskineditor/index.docbook
/usr/share/doc/HTML/fr/ksirk/index.cache.bz2
/usr/share/doc/HTML/fr/ksirk/index.docbook
/usr/share/doc/HTML/it/ksirk/index.cache.bz2
/usr/share/doc/HTML/it/ksirk/index.docbook
/usr/share/doc/HTML/it/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/it/ksirkskineditor/index.docbook
/usr/share/doc/HTML/nl/ksirk/index.cache.bz2
/usr/share/doc/HTML/nl/ksirk/index.docbook
/usr/share/doc/HTML/nl/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/nl/ksirkskineditor/index.docbook
/usr/share/doc/HTML/pt/ksirk/index.cache.bz2
/usr/share/doc/HTML/pt/ksirk/index.docbook
/usr/share/doc/HTML/pt/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/pt/ksirkskineditor/index.docbook
/usr/share/doc/HTML/pt_BR/ksirk/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksirk/index.docbook
/usr/share/doc/HTML/pt_BR/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksirkskineditor/index.docbook
/usr/share/doc/HTML/ru/ksirk/index.cache.bz2
/usr/share/doc/HTML/ru/ksirk/index.docbook
/usr/share/doc/HTML/ru/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/ru/ksirkskineditor/index.docbook
/usr/share/doc/HTML/sv/ksirk/index.cache.bz2
/usr/share/doc/HTML/sv/ksirk/index.docbook
/usr/share/doc/HTML/sv/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/sv/ksirkskineditor/index.docbook
/usr/share/doc/HTML/uk/ksirk/attackmenu.png
/usr/share/doc/HTML/uk/ksirk/defensedialog.png
/usr/share/doc/HTML/uk/ksirk/displaygoalmessage.png
/usr/share/doc/HTML/uk/ksirk/displaygoalwarningmessage.png
/usr/share/doc/HTML/uk/ksirk/firing-screenshot.png
/usr/share/doc/HTML/uk/ksirk/index.cache.bz2
/usr/share/doc/HTML/uk/ksirk/index.docbook
/usr/share/doc/HTML/uk/ksirk/introscreen.png
/usr/share/doc/HTML/uk/ksirk/invasionslider.png
/usr/share/doc/HTML/uk/ksirk/joinnetgame.png
/usr/share/doc/HTML/uk/ksirk/justjoined.png
/usr/share/doc/HTML/uk/ksirk/newgamedialog.png
/usr/share/doc/HTML/uk/ksirk/numnetplayersdialog.png
/usr/share/doc/HTML/uk/ksirk/placingarmies.png
/usr/share/doc/HTML/uk/ksirk/playersetupdialog.png
/usr/share/doc/HTML/uk/ksirk/preferences.png
/usr/share/doc/HTML/uk/ksirk/shownumberofarmies.png
/usr/share/doc/HTML/uk/ksirkskineditor/index.cache.bz2
/usr/share/doc/HTML/uk/ksirkskineditor/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksirk/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/ksirk/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
/usr/share/package-licenses/ksirk/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/ksirk/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f ksirk.lang -f ksirkskineditor.lang
%defattr(-,root,root,-)

