%define upstream_name    String-Perl-Warnings
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Determine if a string looks like a perl warning
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/String-Perl-Warnings-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Regexp::Assemble)
BuildRequires:	perl(Test::More)
Requires:	perl(Regexp::Assemble)
BuildArch:	noarch

%description
String::Perl::Warnings can be used to determine if a string of arbitary
text appears to look like a warning generated by perl.

It includes all warnings for every stable perl release from '5.6.0' to
'5.12.0'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 686999
- update to new version 1.06

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.40.0-4
+ Revision: 658267
- rebuild

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 1.40.0-3
+ Revision: 658214
- add runtime req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2
+ Revision: 657834
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 624963
- import perl-String-Perl-Warnings


