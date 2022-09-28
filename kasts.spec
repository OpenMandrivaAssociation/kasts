#define snapshot 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		kasts
Version:	22.09
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	Podcast application for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/kasts/-/archive/v%{version}/kasts-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(Qt5Keychain)

%description
Podcast application for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kasts

%files -f kasts.lang
%{_bindir}/kasts
%{_datadir}/applications/org.kde.kasts.desktop
%{_datadir}/icons/hicolor/scalable/apps/kasts.svg
%{_datadir}/metainfo/org.kde.kasts.appdata.xml
%{_libdir}/libKastsSolidExtras.so
%{_libdir}/qt5/qml/org/kde/kasts
