Name:           python-tuskarclient
Version:        XXX
Release:        XXX
Summary:        Python client for the Tuskar API

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-tuskarclient
Source0:        https://pypi.python.org/packages/source/p/python-tuskarclient/python-tuskarclient-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       python-babel
Requires:       python-cliff
Requires:       python-iso8601
Requires:       python-openstackclient
Requires:       python-prettytable
Requires:       python-keystoneclient
Requires:       python-pbr
Requires:       python-requests >= 2.5.2
Requires:       python-simplejson
Requires:       python-six >= 1.9.0
Requires:       python-stevedore


%description
python-tuskarclient is a Python client and a command-line interface
for Tuskar <https://github.com/openstack/tuskar>.


%prep
%setup -q -n %{name}-%{upstream_version}
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%{_bindir}/tuskar
%{python2_sitelib}/tuskarclient*
%{python2_sitelib}/python_tuskarclient*
%doc README.rst
%license LICENSE

%changelog
