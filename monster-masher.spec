Summary:	An action game for the GNOME desktop environment
Summary(pl):	Gra akcji dla GNOME
Name:		monster-masher
Version:	1.8
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.cs.auc.dk/~olau/monster-masher/source/%{name}-%{version}.tar.bz2
# Source0-md5:	c51913f62c23d6502b30bf7c6e0cffc5
Patch0:		%{name}-locale-names.patch
URL:		http://www.cs.auc.dk/~olau/monster-masher/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gconfmm-devel >= 2.6.0
BuildRequires:	libglademm-devel >= 2.4.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomecanvasmm-devel >= 2.6.0
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monster Masher is an action game for the GNOME desktop environment.
The basic idea is that you have to clean the caves of monsters. You
do the cleaning by mashing the monsters with stone blocks.

%description -l pl
Monster Masher jest gr± akcji dla GNOME. Podstawowym celem gry jest
wyczyszczenie jaskiñ z potworów. Cel ten osi±ga siê t³uk±c potwory
kamieniami.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
