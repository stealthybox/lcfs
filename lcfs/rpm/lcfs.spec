# Enable building from outside build system
%{!?lcfsrelease:%define lcfsrelease 0.0}
%{!?release:%define release 0}
%{!?rpmdescription: %define rpmdescription This package contains %summary.}

Name: %name
Version: %lcfsrelease
Release: %release
Summary: %summary
Group: LCFS Runtime Environment
License: Proprietary
Source: %{name}-%{version}-%{release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: %name
autoreqprov: no

%if 0%{?required:1}
Requires: %required
%endif

%if 0%{?required_rpms:1}
BuildRequires: %required_rpms
%endif

%description
  %rpmdescription

%prep
%setup -n %specsrcdir

%build

%if 0%{?kernelpath:1}
export KERNELPATH="%kernelpath"
%endif

%if 0%{?kernelother:1}
export KERNELOTHER="%kernelother"
%endif

make clean all

%install
mkdir -p ${RPM_BUILD_ROOT}/opt/pwx/bin
cp -f cstat ${RPM_BUILD_ROOT}/opt/pwx/bin
cp -f lcfs ${RPM_BUILD_ROOT}/opt/pwx/bin
cp -f lcfs-setup.sh ${RPM_BUILD_ROOT}/opt/pwx/bin

%check

%clean
/bin/rm -rf $RPM_BUILD_ROOT

%files
#%defattr(-,root,root,0755)
/opt/pwx/bin/cstat
/opt/pwx/bin/lcfs
/opt/pwx/bin/lcfs-setup.sh

%pre

%post

%postun

%preun
#if [ $1 = 0 ]; then
#fi

%changelog
* Sat Jan 16 2016 jrivera
- Initial spec file creation
