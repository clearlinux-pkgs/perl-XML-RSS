#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-XML-RSS
Version  : 1.62
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-RSS-1.62.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-RSS-1.62.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-feed-perl/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
Summary  : 'creates and updates RSS files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-XML-RSS-license = %{version}-%{release}
Requires: perl-XML-RSS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(DateTime::Format::Mail)
BuildRequires : perl(DateTime::Format::W3CDTF)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(HTML::Entities)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(XML::Parser)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
All rights reserved.
This package is free software; you can redistribute it and/or
modify it under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-XML-RSS package.
Group: Development
Provides: perl-XML-RSS-devel = %{version}-%{release}
Requires: perl-XML-RSS = %{version}-%{release}

%description dev
dev components for the perl-XML-RSS package.


%package license
Summary: license components for the perl-XML-RSS package.
Group: Default

%description license
license components for the perl-XML-RSS package.


%package perl
Summary: perl components for the perl-XML-RSS package.
Group: Default
Requires: perl-XML-RSS = %{version}-%{release}

%description perl
perl components for the perl-XML-RSS package.


%prep
%setup -q -n XML-RSS-1.62
cd %{_builddir}
tar xf %{_sourcedir}/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
cd %{_builddir}/XML-RSS-1.62
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/XML-RSS-1.62/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-RSS
cp %{_builddir}/XML-RSS-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-RSS/38e94f89ec602e1a6495ef7c30477d01aeefedc9 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-XML-RSS/808cdef4c992763637fe5a5a7551c6cd5186080b || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::RSS.3
/usr/share/man/man3/XML::RSS::Private::Output::Base.3
/usr/share/man/man3/XML::RSS::Private::Output::Roles::ImageDims.3
/usr/share/man/man3/XML::RSS::Private::Output::Roles::ModulesElems.3
/usr/share/man/man3/XML::RSS::Private::Output::V0_9.3
/usr/share/man/man3/XML::RSS::Private::Output::V0_91.3
/usr/share/man/man3/XML::RSS::Private::Output::V1_0.3
/usr/share/man/man3/XML::RSS::Private::Output::V2_0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-RSS/38e94f89ec602e1a6495ef7c30477d01aeefedc9
/usr/share/package-licenses/perl-XML-RSS/808cdef4c992763637fe5a5a7551c6cd5186080b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
