Summary:        Simple desklets for Unix
Name:           adesklets
Version:        0.6.1
Release:        10
License:        GPL
URL:            http://adesklets.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:		adesklets-0.6.1-fix-str-fmt.patch
Patch1:		adesklets-0.6.1-linkage.patch
Group:          Graphical desktop/Other
Requires:	tkinter
BuildRequires:  imlib2-devel 
BuildRequires:  python-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  readline-devel
BuildRequires:  perl-devel

%description
adesklets is an interactive Imlib2 console for the X Window system. It provides
to scripted languages a clean and simple way to write great looking, mildly
interactive desktop integrated graphic applets (aka "desklets").

%prep
%setup -q
%patch0 -p0
%patch1 -p0
find . -name "*.py" |xargs 2to3 -w

%build
export LDFLAGS="-lm"
%configure
pushd scripting/perl/
%{__perl} Makefile.PL INSTALLDIRS=vendor
popd
%make

%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
%makeinstall_std


%files
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS 
%{_bindir}/*
%{_infodir}/*
%py_platsitedir/*
%{perl_vendorlib}/*
%{_datadir}/adesklets
%{_mandir}/*/*

