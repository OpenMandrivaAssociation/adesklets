%define	name	adesklets
%define	version	0.6.1
%define	release	%mkrel 8

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
BuildRequires:  perl-devel

%description
adesklets is an interactive Imlib2 console for the X Window system. It provides
to scripted languages a clean and simple way to write great looking, mildly
interactive desktop integrated graphic applets (aka "desklets").

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
export LDFLAGS="-lm"
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




%changelog
* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-8mdv2010.0
+ Revision: 436625
- rebuild

* Mon Mar 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-7mdv2009.1
+ Revision: 356239
- rebuild

* Thu Jan 22 2009 Funda Wang <fwang@mandriva.org> 0.6.1-6mdv2009.1
+ Revision: 332420
- fix building

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.6.1-4mdv2008.1
+ Revision: 151759
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.6.1-3mdv2008.1
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.6.1-3mdv2007.0
+ Revision: 96503
- Rebuild against new python
- Import adesklets

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 0.6.1-2mdv2007.0
- rebuild

* Sat May 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.1-1mdk
- New release 0.6.1

* Wed Mar 29 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.0-2mdk
- requires tkinter (Fabrice Facorat, #20404)

* Tue Mar 28 2006 Pascal Terjan <pterjan@mandriva.org> 0.6.0-1mdk
- 0.6.0

* Wed Dec 14 2005 Pascal Terjan <pterjan@mandriva.org> 0.5.0-1mdk
- 0.5.0

* Fri Oct 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.11-2mdk
- Fix BuildRequires

* Sat Sep 03 2005 Pascal Terjan <pterjan@mandriva.org> 0.4.11-1mdk
- 0.4.11

* Mon Aug 15 2005 Pascal Terjan <pterjan@mandriva.org> 0.4.10-1mdk
- First Mandriva package

