%define name	CriticalMass
%define version	1.0.2
%define release %mkrel 7
%define Summary Arcade Shooter

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://criticalmass.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		%{name}-1.0.2-fix-gcc-43.patch
License:	GPLv2
Group:		Games/Arcade
URL:		http://criticalmass.sourceforge.net
Summary:	%{Summary}
BuildRequires:	SDL_mixer-devel SDL_image-devel zlib-devel libpng-devel MesaGL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#Requires:	SDL_mixer SDL_image zlib

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game.

%prep
%setup -q
%patch0 -p1 -b .gcc43

%build
%configure --prefix=%{_gamesbindir} --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir} --libdir=%_libdir --enable-dyngl
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamesbindir}
install -m755 game/critter tools/Packer -D $RPM_BUILD_ROOT%{_gamesbindir}
install -d $RPM_BUILD_ROOT%{_gamesdatadir}/Critical_Mass
install -m644 data/music/lg-criti.xm $RPM_BUILD_ROOT%{_gamesdatadir}/Critical_Mass
install -m644 game/resource.dat $RPM_BUILD_ROOT%{_gamesdatadir}/Critical_Mass
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -m644 critter.6 $RPM_BUILD_ROOT%{_mandir}/man6


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Critical Mass
Comment=%{Summary}
Exec=%{_gamesbindir}/critter
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.html COPYING TODO
%{_gamesdatadir}/Critical_Mass
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}*.png
%{_miconsdir}/%{name}*.png
%{_mandir}/man6/critter.6*
%defattr(755,root,root,755)
%{_gamesbindir}/critter
%{_gamesbindir}/Packer

