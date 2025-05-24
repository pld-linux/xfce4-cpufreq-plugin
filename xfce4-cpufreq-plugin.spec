Summary:	A cpufreq plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka cpufreq dla panelu Xfce
Name:		xfce4-cpufreq-plugin
Version:	1.3.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-cpufreq-plugin/1.3/%{name}-%{version}.tar.xz
# Source0-md5:	5fadf039add3819180fd076318584ccc
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.17.2
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	xfce4-dev-tools >= 4.17.2
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays the current frequency of the CPU, in GHz or MHz
as necessary. It also displays the frequency relative to the maximum
CPU frequency as an accordingly colored progress bar.

%description -l pl.UTF-8
Ta wtyczka wyświetla aktualną częstotliwość procesora w GHz lub MHz.
Wyświetla także częstotliwość względem maksymalnej częstotliwości
procesora jako odpowiednio pokolorowany pasek.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libcpufreq.so*
%{_datadir}/xfce4/panel/plugins/cpufreq.desktop
%{_iconsdir}/hicolor/*/*/*.png
