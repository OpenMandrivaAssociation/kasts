%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		kasts
Version:	23.08.4
Release:	%{?git:0.%{git}.}3
Summary:	Podcast application for Plasma Mobile
%if 0%{?git:1}
Source0:        https://invent.kde.org/plasma-mobile/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5KirigamiAddons)
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
%{_datadir}/metainfo/org.kde.kasts.appdata.xml
%{_libdir}/libKastsSolidExtras.so
%{_libdir}/qt5/qml/org/kde/kasts
%{_libdir}/libKMediaSession.so
%{_libdir}/qt5/qml/org/kde/kmediasession/libkmediasession-qmlplugin.so
%{_libdir}/qt5/qml/org/kde/kmediasession/qmldir
%{_datadir}/icons/hicolor/*/*/*
