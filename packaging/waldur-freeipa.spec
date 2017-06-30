Name: waldur-freeipa
Summary: FreeIPA client plugin for Waldur MasterMind
Group: Development/Libraries
Version: 0.2.0
Release: 1.el7
License: MIT
Url: https://waldur.com
Source0: waldur-freeipa-%{version}.tar.gz

Requires: waldur-core > 0.141.0
Requires: python-freeipa >= 0.1.2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
Waldur FreeIPA plugin enables linking of Waldur account with FreeIPA profile.

%prep
%setup -q -n waldur-freeipa-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Mon Jun 19 2017 Jenkins <jenkins@opennodecloud.com> - 0.2.0-1.el7
- New upstream release

* Fri May 26 2017 Jenkins <jenkins@opennodecloud.com> - 0.1.0-1.el7
- New upstream release

* Thu May 25 2017 Victor Mireyev <victor@opennodecloud.com> - 0.1.0-1
- Initial version of the package.
