Summary:	An action game for the Gnome desktop environment
Summary(pl):	Gra akcji dla Gnome
Name:		monster-masher
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.cs.auc.dk/~olau/%{name}/source/%{name}-%{version}.tar.gz
# Source0-md5:	baaa49448e98384c59183ed97cab0f35
Patch0:		%{name}-desktopdir.patch
URL:		http://www.cs.auc.dk/~olau/monster-masher/
Buildrequires:	autoconf
BuildRequires:	automake
Buildrequires:	gconfmm-devel >= 2.0.1
Buildrequires:	libglademm-devel >= 1.3.0
BuildRequires:	libgnomeuimm-devel >= 1.3.11
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monster Masher is an action game for the Gnome desktop environment.
The basic idea is that you, has to clean the caves for monsters. You
do the cleaning by mashing the monsters with stone blocks.

%description -l pl
Monster Masher jest gr± akcji dla Gnome. Podstawowym celem gry jest
wyczyszczenie jaskiñ z potworów. Cel ten osi±ga siê t³uk±c potwory
kamieniami.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
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
%{_desktopdir}/*
%{_pixmapsdir}/*
