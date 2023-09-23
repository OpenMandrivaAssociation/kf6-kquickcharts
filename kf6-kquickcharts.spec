%define devname %mklibname KF6QuickCharts -d
%define git 20230924

Name: kf6-kquickcharts
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kquickcharts/-/archive/master/kquickcharts-master.tar.bz2#/kquickcharts-%{git}.tar.bz2
Summary: QtQuick plugin providing high-performance charts
URL: https://invent.kde.org/frameworks/kquickcharts
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(EGL)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6ShaderTools)
BuildRequires: cmake(Qt6ShaderToolsTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)

%description
QtQuick plugin providing high-performance charts

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

QtQuick plugin providing high-performance charts

%prep
%autosetup -p1 -n kquickcharts-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt6/qml/org/kde/quickcharts
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_libdir}/cmake/KF6QuickCharts
