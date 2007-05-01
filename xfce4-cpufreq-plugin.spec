Summary:	A cpufreq plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka cpufreq dla panelu Xfce
Name:		xfce4-cpufreq-plugin
Version:	0.0.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-cpufreq-plugin/%{name}-%{version}.tar.gz
# Source0-md5:	7ad41541d8065aab941de7d62857aa8b
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpufreq-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays the current frequency of the CPU, in GHz or MHz
as necessary. It also displays the frequency relative to the maximum
CPU frequency as an accordingly colored progress bar.

%description -l pl.UTF-8
Ta wtyczka wy¶wietla aktualn± czêstotliwo¶æ procesora w GHz lub MHz.
Wy¶wietla tak¿e czêstotliwo¶æ wzglêdem maksymalnej czêstotliwo¶ci
procesora jako odpowiednio pokolorowany pasek.

%prep
%setup -q -n xfce4-cpu-freq-plugin-%{version}

%build
%{__intltoolize}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-cpu-freq-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-cpu-freq-plugin.desktop
%{_iconsdir}/hicolor/*/apps/cpu.*
