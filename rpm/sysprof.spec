%global glib2_version 2.61.3

Name:           sysprof
Version:        3.36.0
Release:        1
Summary:        A system-wide Linux profiler

License:        GPLv3+
URL:            http://www.sysprof.com
Source0:        https://download.gnome.org/sources/sysprof/3.36/sysprof-%{version}.tar.xz

# disable localization
Patch1: 0001-i18n-disable-localization.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)

%description
Sysprof is a sampling CPU profiler for Linux that collects accurate,
high-precision data and provides efficient access to the sampled
calltrees.


%package        cli
Summary:        Sysprof command line utility

%description    cli
The %{name}-cli package contains the sysprof-cli command line utility.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}/sysprof
%patch1 -p1


%build
%meson -Denable_gtk=false -Dhelp=false
%meson_build


%install
%meson_install
%find_lang sysprof --with-gnome


%post cli -p /sbin/ldconfig
%postun cli -p /sbin/ldconfig


%files cli
%license COPYING
%{_bindir}/sysprof-cli
%{_libdir}/libsysprof-3.so
%{_libdir}/libsysprof-memory-3.so
%{_libexecdir}/sysprofd
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof2.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof2.conf
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof3.conf
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof2.service
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof3.service
%{_datadir}/polkit-1/actions/org.gnome.sysprof3.policy
%{_unitdir}/sysprof2.service
%{_unitdir}/sysprof3.service

%files devel
%{_includedir}/sysprof-3/
%{_libdir}/pkgconfig/sysprof-3.pc
%{_libdir}/pkgconfig/sysprof-capture-3.pc
%{_libdir}/libsysprof-capture-3.a

%files doc -f sysprof.lang
%doc NEWS README.md AUTHORS
