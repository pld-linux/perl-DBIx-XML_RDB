%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	DBIx-XML_RDB perl module
Summary(pl):	Modu³ perla DBIx-XML_RDB
Name:		perl-DBIx-XML_RDB
Version:	0.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-XML_RDB-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-DBI
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-DBI
BuildRoot:	/tmp/%{name}-%{version}-root

%description
DBIx-XML_RDB - creates XML from existing DBI datasources.

%description -l pl
DBIx-XML_RDB - tworzy pliki XML ze ¼róde³ danych DBI.

%prep
%setup -q -n DBIx-XML_RDB-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/DBIx/XML_RDB
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitelib}/DBIx/*
%{perl_sitearch}/auto/DBIx/XML_RDB

%{_mandir}/man3/*
