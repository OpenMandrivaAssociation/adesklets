%define	name	adesklets
%define	version	0.6.1
%define	release	%mkrel 7

Summary:        Simple desklets for Unix
Name:           %name
Version:        %version
Release:        %release
License:        GPL
URL:            http://adesklets.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:		adesklets-0.6.1-fix-str-fmt.patch
Patch1:		adesklets-0.6.1-linkage.patch
Group:          Graphical desktop/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tkinter
BuildRequires:  imlib2-devel python-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel

%description
adesklets is an interactive Imlib2 console for the X Window system. It provides
to scripted languages a clean and simple way to write great looking, mildly
interactive desktop integrated graphic applets (aka "desklets").

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x
pushd scripting/perl/
%{__perl} Makefile.PL INSTALLDIRS=vendor
popd
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_infodir}
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{_infodir}/%{name}*

%preun
%_remove_install_info %{_infodir}/%{name}*

%files
%defattr(-,root,root)
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS 
%{_bindir}/*
%{_infodir}/*
%py_platsitedir/*
%{perl_vendorlib}/*
%{_datadir}/adesklets
%{_mandir}/*/*


