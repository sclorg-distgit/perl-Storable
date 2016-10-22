%{?scl:%scl_package perl-Storable}

%global base_version 2.51

Name:           %{?scl_prefix}perl-Storable
Epoch:          1
Version:        2.56
Release:        366%{?dist}
Summary:        Persistence for Perl data structures
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Storable/
Source0:        http://www.cpan.org/authors/id/A/AM/AMS/Storable-%{base_version}.tar.gz
# Unbundled from perl 5.21.11
Patch0:         Storable-2.51-Upgrade-to-2.53.patch
# Unbundled from perl 5.24.0
Patch1:         Storable-2.53-Upgrade-to-2.56.patch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Run-time:
# Carp substitutes missing Log::Agent
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Fcntl is optional, but locking is good
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(IO::File)
# Log::Agent is optional
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests:
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(integer)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(threads)
BuildRequires:  %{?scl_prefix}perl(Safe)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional tests:
# Data::Dump not used
# Data::Dumper not used
BuildRequires:  %{?scl_prefix}perl(B::Deparse) >= 0.61
BuildRequires:  %{?scl_prefix}perl(Digest::MD5)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.8
BuildRequires:  %{?scl_prefix}perl(Hash::Util)
BuildRequires:  %{?scl_prefix}perl(Tie::Hash)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
# Carp substitutes missing Log::Agent
Requires:       %{?scl_prefix}perl(Carp)
Requires:       %{?scl_prefix}perl(Config)
# Fcntl is optional, but locking is good
Requires:       %{?scl_prefix}perl(Fcntl)
Requires:       %{?scl_prefix}perl(IO::File)

%{?perl_default_filter}

%description
The Storable package brings persistence to your Perl data structures
containing scalar, array, hash or reference objects, i.e. anything that
can be conveniently stored to disk and retrieved at a later time.

%prep
%setup -q -n Storable-%{base_version}
%patch0 -p1
%patch1 -p1
# Remove bundled modules
rm -rf t/compat
sed -i -e '/^t\/compat\//d' MANIFEST

%build
# Be ware hints/linux.pl removes "-ON" from CFLAGS if N > 2 because it can
# break the code.
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Storable*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1:2.56-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.56-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.56-1
- 2.56 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.53-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.53-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.53-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.53-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 1:2.53-1
- 2.53 bump in order to dual-live with perl 5.22

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:2.51-4
- Increase Epoch to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.51-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 07 2014 Petr Pisar <ppisar@redhat.com> - 2.51-1
- 2.51 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 2.45-1
- 2.45 bump

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.39-3
- Link minimal build-root packages against libperl.so explicitly

* Tue Jun 11 2013 Petr Pisar <ppisar@redhat.com> - 2.39-2
- Do not export private libraries

* Fri May 24 2013 Petr Pisar <ppisar@redhat.com> 2.39-1
- Specfile autogenerated by cpanspec 1.78.
