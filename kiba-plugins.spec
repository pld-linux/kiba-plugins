######		Unknown group!
Summary:	Funky application dock for X11
Name:		kiba-plugins
Version:	0.0.731
Release:	1
Group:		System/X11
URL:		http://kiba-plugins.org/
Source0:	%{name}-r731.tar.bz2
# Source0-md5:	20af42d79de9fe321b16ca50276a5934
Patch0:		%{name}-debugfix.patch
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Funky dock for X11

%prep
%setup -q -n %{name}
%patch -P0 -p0

%build
# This is a CVS snapshot, so we need to generate makefiles.
sh autogen.sh -V

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kiba-dock/lib*.so
%dir %{_datadir}/kiba-dock/config_schemas/plugins
%{_datadir}/kiba-dock/config_schemas/plugins/*.xml
%{_datadir}/kiba-dock/icons/clock_theme/clock-drop-shadow.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-face-shadow.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-face.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-frame.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-glass.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-hour-hand-shadow.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-hour-hand.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-marks.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-minute-hand-shadow.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-minute-hand.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-second-hand-shadow.svg
%{_datadir}/kiba-dock/icons/clock_theme/clock-second-hand.svg
%{_datadir}/kiba-dock/icons/dbus.png
%{_datadir}/kiba-dock/icons/sysinfo_themes/custom_tango/sysinfo-face.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/custom_tango/sysinfo-frame.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/custom_tango/sysinfo-hand.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/default/sysinfo-face.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/default/sysinfo-frame.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/default/sysinfo-hand.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/gold/sysinfo-face.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/gold/sysinfo-frame.svg
%{_datadir}/kiba-dock/icons/sysinfo_themes/gold/sysinfo-hand.svg
%{_datadir}/kiba-dock/icons/taskbar.svg

%clean
rm -rf $RPM_BUILD_ROOT
