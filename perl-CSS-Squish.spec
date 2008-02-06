#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CSS
%define		pnam	Squish
Summary:	CSS::Squish - Compact many CSS files into one big file
Summary(pl.UTF-8):	CSS::Squish - Compact many CSS files into one big file
Name:		perl-CSS-Squish
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CSS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d992129bf96368a504fe9c67b6d3e622
URL:		http://search.cpan.org/dist/CSS-Squish/
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module takes a list of CSS files and concatenates them, making
sure to honor any valid @import statements included in the files.

%description -l pl.UTF-8
Ten moduł łączy podaną listę plikół CSS w jeden uwzględniając
polecenia @import wewnątrz plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/CSS/*.pm
%{_mandir}/man3/*
