%include	/usr/lib/rpm/macros.perl
Summary:	DBIx-XML_RDB perl module
Summary(pl):	Modu³ perla DBIx-XML_RDB
Name:		perl-DBIx-XML_RDB
Version:	0.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBIx/DBIx-XML_RDB-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx-XML_RDB - creates XML from existing DBI datasources.

%description -l pl
DBIx-XML_RDB - tworzy pliki XML ze ¼róde³ danych DBI.

%prep
%setup -q -n DBIx-XML_RDB-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/DBIx/*
%{_mandir}/man3/*
