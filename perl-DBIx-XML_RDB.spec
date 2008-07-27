#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBIx
%define		pnam	XML_RDB
Summary:	DBIx::XML_RDB - Perl extension for creating XML from existing DBI datasources
Summary(pl.UTF-8):	DBIx::XML_RDB - rozszerzenie Perla do tworzenia XML-a z istniejących źródeł danych DBI
Name:		perl-DBIx-XML_RDB
Version:	0.05
Release:	8
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1eda5c997811350c2008c5966a02aa24
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-DBI
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::XML_RDB Perl module is a simple creator of XML data from DBI
datasources.  It allows you to easily extract data from a database,
and manipulate later using XML::Parser.

%description -l pl.UTF-8
Moduł Perla DBIx::XML_RDB jest prostym kreatorem danych w XML-u ze
źródeł danych DBI. Umożliwia proste wyodrębnienie danych z bazy i
późniejsza manipulację nimi za pomocą XML::Parser.

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
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/DBIx/*
%{_mandir}/man3/*
