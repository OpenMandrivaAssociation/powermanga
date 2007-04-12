%define	name	powermanga
%define	version	0.80
%define	release	%mkrel 2
%define	Summary	Shoot them up with 3d graphics

Summary: 	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Games/Arcade
BuildRequires:	XFree86-devel SDL_mixer-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://linux.tlk.fr/games/Powermanga/download/%{name}-%{version}.tgz
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
ExclusiveArch:	%{ix86} ppc
URL:		http://linux.tlk.fr/games/Powermanga/
Requires(post):	rpm-helper
Requires(postun):	rpm-helper

%description
In this "shoot 'em up" with 3d graphics, you'll have to face and destroy
more than 60 different types of opponents. Nice musics, many weapons, and
a ton of surprises..

%prep
%setup -q
#(peroyvind) fix path to scoredir
perl -pi -e "s#/var/games#%{_localstatedir}/games#g" src/Makefile.in

%build
%configure2_5x	--mandir=%{_mandir}/man6
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

install -d install %{buildroot}%{_gamesdatadir}/%{name}/texts
install -m 644 texts/*.txt texts/*.ini %{buildroot}%{_gamesdatadir}/%{name}/texts

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" icon="%{name}.png" \
  needs="x11" section="More Applications/Games/Arcade" title="Power Manga" \
  longtitle="%{Summary}" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Power Manga
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%{update_menus}
%create_ghostfile %{_localstatedir}/games/%{name}.hi root games 664
%create_ghostfile %{_localstatedir}/games/%{name}.hi-easy root games 664
%create_ghostfile %{_localstatedir}/games/%{name}.hi-hard root games 664

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%attr(-, root, games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%attr(664, root, games) %ghost %{_localstatedir}/games/%{name}.hi
%attr(664, root, games) %ghost %{_localstatedir}/games/%{name}.hi-easy
%attr(664, root, games) %ghost %{_localstatedir}/games/%{name}.hi-hard


