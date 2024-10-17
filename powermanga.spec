Summary:	Shoot 'em up game with 3D graphics
Name:		powermanga
Version:	0.91
Release:	2
License:	GPLv3+
Group:		Games/Arcade
URL:		https://linux.tlk.fr/games/Powermanga/
Source0:	http://linux.tlk.fr/games/Powermanga/download/%{name}-%{version}.tgz
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		powermanga-0.91-zlib.patch
Patch1:		powermanga-0.91-gcc4.7.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(libpng)

Requires(post):		rpm-helper
Requires(postun):	rpm-helper

%description
In this "shoot 'em up" with 3d graphics, you'll have to face and destroy
more than 60 different types of opponents. Nice musics, many weapons, and
a ton of surprises.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

install -d install %{buildroot}%{_gamesdatadir}/%{name}/texts
install -m 644 texts/*.txt texts/*.ini %{buildroot}%{_gamesdatadir}/%{name}/texts

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=PowerManga
Comment=Shoot 'em up game with 3D graphics
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%post
%create_ghostfile %{_localstatedir}/games/%{name}/%{name}.hi root games 664
%create_ghostfile %{_localstatedir}/games/%{name}/%{name}.hi-easy root games 664
%create_ghostfile %{_localstatedir}/games/%{name}/%{name}.hi-hard root games 664

%files
%doc README
%attr(-, root, games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%attr(664, root, games) %ghost %{_localstatedir}/games/%{name}/%{name}.hi
%attr(664, root, games) %ghost %{_localstatedir}/games/%{name}/%{name}.hi-easy
%attr(664, root, games) %ghost %{_localstatedir}/games/%{name}/%{name}.hi-hard



%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.90-10mdv2011.0
+ Revision: 667812
- mass rebuild

* Mon Feb 07 2011 Funda Wang <fwang@mandriva.org> 0.90-9
+ Revision: 636577
- tighten BR
- tighten BR

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.90-8mdv2011.0
+ Revision: 607198
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.90-7mdv2010.1
+ Revision: 523698
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.90-6mdv2010.0
+ Revision: 426774
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.90-5mdv2009.1
+ Revision: 351634
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.90-4mdv2008.1
+ Revision: 179249
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 25 2007 Adam Williamson <awilliamson@mandriva.org> 0.90-3mdv2008.0
+ Revision: 92912
- drop the patch again (the bug was fixed upstream with a silent tarball replacement)
- replace tarball from upstream
- fd.o icons
- improve summary and description a bit
- add powermanga-0.90-fontpath.patch to fix font path (#34094)

* Tue Sep 04 2007 Funda Wang <fwang@mandriva.org> 0.90-2mdv2008.0
+ Revision: 79011
- build on x86_64 too
- GPLv3 now

* Tue Sep 04 2007 Funda Wang <fwang@mandriva.org> 0.90-1mdv2008.0
+ Revision: 78987
- BR png-devel
- Newversion 0.90

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Dec 01 2006 Olivier Blin <oblin@mandriva.com> 0.80-2mdv2007.0
+ Revision: 89894
- install texts files to be able to start the game (#23612)
- remove old comment
- Import powermanga

* Fri Jun 30 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.80-1mdv2007.0
- 0.80
- %%mkrel
- add xdg menu
- update url
- fix prereq-use

* Thu Aug 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.79-1mdk
- 0.79
- cosmetics

* Tue Aug 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.78-4mdk
- Rebuild with new menu

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 0.78-3mdk
- Rebuild

