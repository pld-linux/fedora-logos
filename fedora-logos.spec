Summary:	Red Hat-related icons and pictures
Name:		fedora-logos
Version:	1.1.42
Release:	0.1
Group:		Base
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	d814bc0a885c4b1364187c9902dcaf2f
License:	Copyright (c) 1999-2005 Red Hat, Inc.  All rights reserved.
Provides:	redhat-logos
Provides:	system-logos
Obsoletes:	redhat-logos
Conflicts:	anaconda-images <= 10
Conflicts:	kdebase <= 3.1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fedora-logos package (the "Packages") contain image files which
incorporate the Fedora trademark and the RPM logo (the "Marks"). The
Marks are trademarks or registered trademarks of Red Hat, Inc. in the
United States and other countries and are used by permission.

See the included COPYING file for information on copying and
redistribution.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}/redhat
for i in redhat-pixmaps/*; do
	install -m 644 $i $RPM_BUILD_ROOT%{_pixmapsdir}/redhat
done
(cd $RPM_BUILD_ROOT%{_pixmapsdir}/redhat; \
for i in *-mini.xpm; do \
	linkfile=`echo $i | sed -e "s/\(.*\)-mini/mini-\1/"` ; \
	ln -s $i $linkfile ; \
done)

# should be ifarch i386
install -d $RPM_BUILD_ROOT/boot/grub
install bootloader/grub-splash.xpm.gz $RPM_BUILD_ROOT/boot/grub/splash.xpm.gz
# end i386 bits

install -d $RPM_BUILD_ROOT%{_datadir}/firstboot/pixmaps
for i in firstboot/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/pixmaps
done

install -d $RPM_BUILD_ROOT%{_datadir}/rhgb
for i in rhgb/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/rhgb
done

install -d $RPM_BUILD_ROOT%{_pixmapsdir}/splash
for i in gnome-splash/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_pixmapsdir}/splash
done

install -d $RPM_BUILD_ROOT%{_datadir}/gnome-screensaver/themes
for i in gnome-screensaver/themes/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/gnome-screensaver/themes
done

install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/BlueCurve
for i in kde-splash/BlueCurve/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/BlueCurve
done

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
for i in pixmaps/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_pixmapsdir}
done

for size in 16x16 24x24 32x32 36x36 48x48 96x96 ; do
	install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
	install -d $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/$size/apps
	for i in icons/hicolor/$size/apps/* ; do
		install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
		cd $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/$size/apps
		ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png icon-panel-menu.png
		ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png gnome-main-menu.png
		ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png kmenu.png
		ln -s ../../../hicolor/$size/apps/fedora-logo-icon.png gnome-logo-icon-transparent.png
		cd -
	done
done

install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bluecurve
for i in gdm/Bluecurve/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bluecurve
done

install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/FedoraBubbles
for i in gdm/FedoraBubbles/* ; do
	install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/gdm/themes/FedoraBubbles
done

# kdmtheme
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/Bluecurve
cd $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/Bluecurve
ln -s ../../../../gdm/themes/Bluecurve/rh_logo-header.png .
ln -s ../../../../gdm/themes/Bluecurve/screenshot.png
cd -

ln -s ../../firstboot/pixmaps/shadowman-round-48.png \
 $RPM_BUILD_ROOT%{_pixmapsdir}/redhat/

%{__make} -C anaconda install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%{_datadir}/firstboot
%{_datadir}/apps/ksplash/Themes/BlueCurve
%{_pixmapsdir}
%{_datadir}/gdm
%{_datadir}/apps/kdm/themes/Bluecurve
%{_datadir}/rhgb
%{_datadir}/anaconda/pixmaps/*
%{_iconsdir}
%{_datadir}/gnome-screensaver/themes/*

%{_prefix}/lib/anaconda-runtime/boot/*png
%{_prefix}/lib/anaconda-runtime/*.sh
# should be ifarch i386
/boot/grub/splash.xpm.gz
# end i386 bits
