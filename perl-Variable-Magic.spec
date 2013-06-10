#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Variable
%define	pnam	Magic
Summary:	Variable::Magic - Associate user-defined magic to variables from Perl
#Summary(pl.UTF-8):	
Name:		perl-Variable-Magic
Version:	0.52
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.perl.com/CPAN/modules/by-module/Variable/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3c3cb6b8adc20616f1e71af145ee73c1
URL:		http://search.cpan.org/dist/Variable-Magic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Magic is Perl way of enhancing objects.

This mechanism let the user add extra data to any variable and hook
syntaxical operations (such as access, assignation or destruction)
that can be applied to it.

With this module, you can add your own magic to any variable without
the pain of the C API.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
cp -a samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Variable/*.pm
%dir %{perl_vendorarch}/auto/Variable/Magic
%attr(755,root,root) %{perl_vendorarch}/auto/Variable/Magic/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
