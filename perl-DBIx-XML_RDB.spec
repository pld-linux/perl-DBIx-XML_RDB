%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	XML_RDB
Summary:	DBIx::XML_RDB perl module
Summary(pl):	Modu³ perla DBIx::XML_RDB
Name:		perl-DBIx-XML_RDB
Version:	0.05
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::XML_RDB - creates XML from existing DBI datasources.

%description -l pl
DBIx::XML_RDB - tworzy pliki XML ze ¼róde³ danych DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/DBIx/*
%{_mandir}/man3/*
