%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit cc1ac2462e41873741c8b6f3fcafa29ae3ce6a30

Name:		kasts
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Summary:	Podcast application primarily for Plasma Mobile
%if 0%{?git:1}
Source0:        https://invent.kde.org/multimedia/kasts/-/archive/%{gitbranch}/kasts-%{gitbranchd}.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/kasts-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Syndication)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6BreezeIcons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake(KF6NetworkManagerQt)
BuildRequires:	cmake(Qt6Keychain)

%rename plasma6-kasts

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Podcast application for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/kasts
%{_datadir}/applications/org.kde.kasts.desktop
%{_datadir}/metainfo/org.kde.kasts.appdata.xml
%{_libdir}/libKMediaSession.so
#{_libdir}/qt6/qml/org/kde/kmediasession/libkmediasession-qmlplugin.so
#{_libdir}/qt6/qml/org/kde/kmediasession/qmldir
%{_qtdir}/qml/org/kde/kmediasession/
%{_datadir}/icons/hicolor/*/*/*
