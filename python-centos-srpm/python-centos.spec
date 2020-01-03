%global pypi_name centos

Name:		python-%{pypi_name}
Version:	0.1.1
Release:	2%{?dist}
Summary:	Python bindings for the CentOS account system, CBS and other services

Group:		Applications/System
License:	GPLv2
URL:		https://centos.org/
Source0:	python-centos-%{version}.tar.gz
BuildArch: noarch

BuildRequires:	python2-devel
BuildRequires:	python2-setuptools

%description
Provides python bindings for the infrastructure services in the CentOS
project

%package -n python2-%{pypi_name}
Summary:	Python bindings for the CentOS account system, CBS and other
Requires:   python2-pyOpenSSL
Requires:   python2-munch
Requires:   python2-requests
Requires:   python2-urllib3
Requires:   python2-lockfile
Requires:   python2-kitchen
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Provides python bindings for the infrastructure services in the CentOS
project

%prep
%setup -q -c -n %{pypi_name}-%{version}

%build
%{py2_build}

%install
%{py2_install}

%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%doc COPYING
%{python2_sitelib}/*

%changelog
* Fri Jan 3 2019 Nico Kadel-Garcia  <nkadel@gmail.com> 0.1.1-2
- Port to RHEL 8 and Fedora
- Specifically build as python2- package with python2- dependencies


* Tue Jul 05 2016 brian@bstinson.com 0.1.1-1
- Fix CentOSUserCert to verify as false if the cert is expired

* Tue Nov 10 2015 brian@bstinson.com 0.1.0-2
- Adding a hard dep on python-kitchen

* Wed Oct 28 2015 brian@bstinson.com 0.1.0-1
- Update to point to the prod location of FAS

* Thu Sep 03 2015 brian@bstinson.com 0.0.4-1
- Add the AccountSystem and a BR for python-fedora

* Tue Aug 11 2015 brian@bstinson.com 0.0.2-1
- Updated to dev version of library defaults 

* Sun Jul 26 2015 brian@bstinson.com 0.0.1-1
- First build


