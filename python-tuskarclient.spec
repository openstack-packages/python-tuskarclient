Name:           python-tuskarclient
Version:        0.1.1
Release:        3%{?dist}
Summary:        Python client for the Tuskar API

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-tuskarclient
Source0:        https://github.com/openstack/python-tuskarclient/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-crypto >= 2.6
Requires:       python-babel
Requires:       python-iso8601
Requires:       python-prettytable
Requires:       python-keystoneclient
Requires:       python-requests
Requires:       python-simplejson
Requires:       python-six
Requires:       python-stevedore


%description
python-tuskarclient is a Python client and a command-line interface
for Tuskar <https://github.com/openstack/tuskar>.


%prep
%setup -q -n %{name}-%{version}
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
rm -rf  %{buildroot}/%{python2_sitelib}/python_tuskarclient*

%files
%{_bindir}/*
%{python2_sitelib}/tuskarclient*
%doc LICENSE README.rst

%changelog
* Fri Feb 28 2014 Jordan OMara <jomara@redhat.com> - 0.1.1-1
- added .egg-info

* Mon Feb 24 2014 Angus Thomas <athomas@redhat.com> - 0.1.0-2
- Replace explicit paths with macros
- Added LICENSE README.rst to docs

* Fri Feb 21 2014 Angus Thomas <athomas@redhat.com> - 0.1.0-1
- Initial package.
