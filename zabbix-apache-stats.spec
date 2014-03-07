Name:           zabbix-apache-stats
Version:        0.0.1
Release:        1%{?dist}
Summary:        Zabbix Apache Stat Collector

License:        GPL
Source0:        zabbix-apache-stats-%{version}.tar.gz

Requires:       zabbix20-agent
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
Zabbix Apache Stat Collector

%prep
%setup -q -c -n zabbix-apache-stats-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
ln -s %{python_sitelib}/fetch.py ${RPM_BUILD_ROOT}/usr/bin/zabbix-apache-stats

%files
/usr/bin/zabbix-apache-stats
%attr(0755, root, root) %{python_sitelib}/fetch.*
%{python_sitelib}/zabbix_apache_stats-*.egg-info

%changelog
* Fri Mar 07 2014 Shawn Siefkas <shawn.siefkas@meredith.com> - 0.0.1-1
- Initial Spec File
