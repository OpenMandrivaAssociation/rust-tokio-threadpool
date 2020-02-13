# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate tokio-threadpool

Name:           rust-%{crate}
Version:        0.1.18
Release:        1%{?dist}
Summary:        Task scheduler backed by a work-stealing thread pool

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/tokio-threadpool
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Task scheduler backed by a work-stealing thread pool.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc CHANGELOG.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.1.18-1
- Update to 0.1.18

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Josh Stone <jistone@redhat.com> - 0.1.17-1
- Update to 0.1.17

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.1.16-1
- Update to 0.1.16

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 11:26:47 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.15-1
- Update to 0.1.15

* Fri Jun 21 20:16:44 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.14-2
- Regenerate

* Tue Apr 23 15:12:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.14-1
- Update to 0.1.14

* Sun Mar 24 19:35:46 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.13-1
- Update to 0.1.13

* Mon Mar 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.12-1
- Update to 0.1.12

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-3
- Update crossbeam dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Josh Stone <jistone@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Sat Dec 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9

* Thu Nov 08 2018 Josh Stone <jistone@redhat.com> - 0.1.8-2
- Adapt to new packaging

* Thu Oct 25 2018 Josh Stone <jistone@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Fri Sep 28 2018 Josh Stone <jistone@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Sat Sep 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Sat Jun 16 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Bump crossbeam-deque to 0.4

* Mon Jun 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Thu May 03 2018 Josh Stone <jistone@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Tue Apr 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Fri Mar 23 2018 Josh Stone <jistone@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Fri Mar 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package
