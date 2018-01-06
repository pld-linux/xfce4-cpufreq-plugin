Summary:	A cpufreq plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka cpufreq dla panelu Xfce
Name:		xfce4-cpufreq-plugin
Version:	1.1.1
Release:	1.2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpufreq-plugin/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	cc3447ee6663f2946fce86308ba3566b
Patch0:		no-freq-in-proc-cpuinfo.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.12.0
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libcpufreq.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libcpufreq.so*
%{_datadir}/xfce4/panel/plugins/cpufreq.desktop
%{_iconsdir}/hicolor/*/*/*.png
