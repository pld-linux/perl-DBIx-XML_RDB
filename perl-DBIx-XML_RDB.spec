%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	XML_RDB
Summary:	DBIx::XML_RDB perl module
Summary(pl):	Modu³ perla DBIx::XML_RDB
Name:		perl-DBIx-XML_RDB
Version:	0.05
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1eda5c997811350c2008c5966a02aa24
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
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
%{perl_vendorlib}/DBIx/*
%{_mandir}/man3/*
