%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-XML_RDB perl module
Summary(pl):	Modu³ perla DBIx-XML_RDB
Name:		perl-DBIx-XML_RDB
Version:	0.03
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-XML_RDB-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI
BuildRequires:	perl-XML-Parser
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
