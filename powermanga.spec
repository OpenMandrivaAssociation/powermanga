%define	name	powermanga
%define	version	0.90
%define	Summary	Shoot 'em up game with 3D graphics

Summary: 	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel 8
License:	GPLv3+
Group:		Games/Arcade
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://linux.tlk.fr/games/Powermanga/download/%{name}-%{version}.tgz
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
URL:		http://linux.tlk.fr/games/Powermanga/

Requires(post):		rpm-helper
Requires(postun):	rpm-helper

%description
In this "shoot 'em up" with 3d graphics, you'll have to face and destroy
more than 60 different types of opponents. Nice musics, many weapons, and
a ton of surprises.

%prep
%setup -q
#(peroyvind) fix path to scoredir
perl -pi -e "s#/var/games#%{_localstatedir}/lib/games#g" src/Makefile.in

%build
%configure2_5x	--mandir=%{_mandir}/man6
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

install -d install %{buildroot}%{_gamesdatadir}/%{name}/texts
install -m 644 texts/*.txt texts/*.ini %{buildroot}%{_gamesdatadir}/%{name}/texts


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=PowerManga
Comment=%{summary}
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
%if %mdkversion < 200900
%{update_menus}
%endif
%create_ghostfile %{_localstatedir}/lib/games/%{name}.hi root games 664
%create_ghostfile %{_localstatedir}/lib/games/%{name}.hi-easy root games 664
%create_ghostfile %{_localstatedir}/lib/games/%{name}.hi-hard root games 664

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README
%attr(-, root, games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%attr(664, root, games) %ghost %{_localstatedir}/lib/games/%{name}.hi
%attr(664, root, games) %ghost %{_localstatedir}/lib/games/%{name}.hi-easy
%attr(664, root, games) %ghost %{_localstatedir}/lib/games/%{name}.hi-hard

