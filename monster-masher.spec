Summary:	An action game for the GNOME desktop environment
Summary(pl):	Gra akcji dla GNOME
Name:		monster-masher
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.cs.auc.dk/~olau/%{name}/source/%{name}-%{version}.tar.gz
# Source0-md5:	9c878fe00894ba58a4f3f93c944dd49f
Patch0:		%{name}-desktopdir.patch
URL:		http://www.cs.auc.dk/~olau/monster-masher/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gconfmm-devel >= 2.0.1
BuildRequires:	libglademm-devel >= 1.3.0
BuildRequires:	libgnomeuimm-devel >= 1.3.11
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monster Masher is an action game for the GNOME desktop environment.
The basic idea is that you have to clean the caves of monsters. You
do the cleaning by mashing the monsters with stone blocks.

%description -l pl
Monster Masher jest gr� akcji dla GNOME. Podstawowym celem gry jest
wyczyszczenie jaski� z potwor�w. Cel ten osi�ga si� t�uk�c potwory
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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
