#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Variable
%define	pnam	Magic
Summary:	Variable::Magic - Associate user-defined magic to variables from Perl
Summary(pl.UTF-8):	Variable::Magic - dowiązanie magii zdefiniowanej przez użytkownika do zmiennych w Perlu
Name:		perl-Variable-Magic
Version:	0.62
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.perl.com/CPAN/modules/by-module/Variable/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	588d94ec3d98dece878a776d161c1dda
URL:		https://metacpan.org/release/Variable-Magic
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Magic is Perl way of enhancing objects.

This mechanism let the user add extra data to any variable and hook
syntaxical operations (such as access, assignation or destruction)
that can be applied to it.

With this module, you can add your own magic to any variable without
the pain of the C API.

%description -l pl.UTF-8
Magia to perlowy sposób rozszerzania obiektów.

Ten mechanizm pozwala użytkownikowi dodać dodatkowe dane do dowolnej
zmiennej i przechwycić operacje składniowe (takie jak dostęp,
powiązanie czy destrukcję), które można na niej wykonać.

Przy użyciu tego modułu można dodawać własną magię do dowolnej
zmiennej unikając bólu API języka C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' samples/*.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p samples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Variable/Magic.pm
%dir %{perl_vendorarch}/auto/Variable/Magic
%attr(755,root,root) %{perl_vendorarch}/auto/Variable/Magic/Magic.so
%{_mandir}/man3/Variable::Magic.3pm*
%{_examplesdir}/%{name}-%{version}
