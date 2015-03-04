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
Requires:	python2

BuildRequires:  imlib2-devel 
BuildRequires:  python2-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  readline-devel
BuildRequires:  perl-devel
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  bison


%description
adesklets is an interactive Imlib2 console for the X Window system. It provides
to scripted languages a clean and simple way to write great looking, mildly
interactive desktop integrated graphic applets (aka "desklets").

%prep
%setup -q
%patch0 -p0
%patch1 -p0


%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH
export CPPFLAGS=-I/usr/local/include
export LDFLAGS="-lm"
autoreconf -fiv
%configure
pushd scripting/perl/
%{__perl} Makefile.PL INSTALLDIRS=vendor
popd
%make

%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
%makeinstall_std

pushd %{buildroot}%{_bindir}
find . -type f -name "%{name}_*" -exec sed -i -e 's,env python,python2,'{} \;
popd

%files
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS 
%{_bindir}/*
%{_infodir}/*
%{py2_platsitedir}/*
%{perl_vendorlib}/*
%{_datadir}/adesklets
%{_mandir}/*/*

