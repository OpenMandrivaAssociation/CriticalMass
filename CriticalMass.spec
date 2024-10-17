%define name	CriticalMass
%define version	1.0.2
%define release 8
%define Summary Arcade Shooter

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://criticalmass.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		%{name}-1.0.2-fix-gcc-43.patch
Patch1:		criticalmass-1.0.2-libpng14.patch
Patch2:		criticalmass-1.0.2-libpng15.patch
Patch3:		criticalmass-1.0.2-system_curl.patch
License:	GPLv2
Group:		Games/Arcade
URL:		https://criticalmass.sourceforge.net
Summary:	%{Summary}
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(glw)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(libcurl)
#Requires:	SDL_mixer SDL_image zlib

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game.

%prep
%setup -q
%patch0 -p1 -b .gcc43
%patch1 -p0 -b .png14
%patch2 -p0 -b .png15
%patch3 -p0 -b .curl

rm -rf curl/
touch NEWS README AUTHORS ChangeLog

%build
autoreconf -fi
%configure2_5x --prefix=%{_gamesbindir} --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir} --libdir=%_libdir --enable-dyngl
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesbindir}
install -m755 game/critter tools/Packer -D %{buildroot}%{_gamesbindir}
install -d %{buildroot}%{_gamesdatadir}/Critical_Mass
install -m644 data/music/lg-criti.xm %{buildroot}%{_gamesdatadir}/Critical_Mass
install -m644 game/resource.dat %{buildroot}%{_gamesdatadir}/Critical_Mass
install -d %{buildroot}%{_mandir}/man6
install -m644 critter.6 %{buildroot}%{_mandir}/man6


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
