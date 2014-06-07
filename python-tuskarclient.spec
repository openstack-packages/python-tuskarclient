Name:           python-tuskarclient
Version:        0.1.4
Release:        2%{?dist}
Summary:        Python client for the Tuskar API

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-tuskarclient
Source0:        https://pypi.python.org/packages/source/p/python-tuskarclient/python-tuskarclient-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

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

%files
%{_bindir}/*
%{python2_sitelib}/tuskarclient*
%{python2_sitelib}/python_tuskarclient*
%doc LICENSE README.rst

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Jordan OMara <jomara@redhat.com> - 0.1.4-1
- new src, 0.1.4 (jomara@redhat.com)

* Fri Apr 4 2014 Jordan OMara <jomara@redhat.com> - 0.1.3-1
- upgrading source

* Fri Mar 14 2014 Jordan OMara <jomara@redhat.com> - 0.1.1-2
- fixed .egg-info

* Fri Feb 28 2014 Jordan OMara <jomara@redhat.com> - 0.1.1-1
- added .egg-info

* Mon Feb 24 2014 Angus Thomas <athomas@redhat.com> - 0.1.0-2
- Replace explicit paths with macros
- Added LICENSE README.rst to docs

* Fri Feb 21 2014 Angus Thomas <athomas@redhat.com> - 0.1.0-1
- Initial package.
