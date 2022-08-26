#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ksirk
Version  : 22.08.0
Release  : 42
URL      : https://download.kde.org/stable/release-service/22.08.0/src/ksirk-22.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.0/src/ksirk-22.08.0.tar.xz
Summary  : A turn by turn strategy game
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: ksirk-bin = %{version}-%{release}
Requires: ksirk-data = %{version}-%{release}
Requires: ksirk-lib = %{version}-%{release}
Requires: ksirk-license = %{version}-%{release}
Requires: ksirk-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : phonon-dev
BuildRequires : qca-qt5-dev
BuildRequires : zlib-dev

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


%package dev
Summary: dev components for the ksirk package.
Group: Development
Requires: ksirk-lib = %{version}-%{release}
Requires: ksirk-bin = %{version}-%{release}
Requires: ksirk-data = %{version}-%{release}
Provides: ksirk-devel = %{version}-%{release}
Requires: ksirk = %{version}-%{release}

%description dev
dev components for the ksirk package.


%package doc
Summary: doc components for the ksirk package.
Group: Documentation

%description doc
doc components for the ksirk package.


%package lib
Summary: lib components for the ksirk package.
Group: Libraries
Requires: ksirk-data = %{version}-%{release}
Requires: ksirk-license = %{version}-%{release}

%description lib
lib components for the ksirk package.


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
%setup -q -n ksirk-22.08.0
cd %{_builddir}/ksirk-22.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661537430
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
export SOURCE_DATE_EPOCH=1661537430
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksirk
cp %{_builddir}/ksirk-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/ksirk/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/ksirk-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ksirk/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4 || :
cp %{_builddir}/ksirk-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/ksirk/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
cp %{_builddir}/ksirk-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/ksirk/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/ksirk-%{version}/ksirk/iris/COPYING %{buildroot}/usr/share/package-licenses/ksirk/caeb68c46fa36651acf592771d09de7937926bb3 || :
pushd clr-build
%make_install
popd
%find_lang ksirk
%find_lang ksirkskineditor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/ksirk/jabber.png
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
/usr/share/kxmlgui5/ksirk/ksirkui.rc
/usr/share/kxmlgui5/ksirkskineditor/ksirkskineditorui.rc
/usr/share/metainfo/org.kde.ksirk.appdata.xml
/usr/share/qlogging-categories5/ksirk.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/libiris_ksirk.so

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libiris_ksirk.so.2
/usr/lib64/libiris_ksirk.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksirk/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/ksirk/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
/usr/share/package-licenses/ksirk/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/ksirk/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/ksirk/caeb68c46fa36651acf592771d09de7937926bb3

%files locales -f ksirk.lang -f ksirkskineditor.lang
%defattr(-,root,root,-)

