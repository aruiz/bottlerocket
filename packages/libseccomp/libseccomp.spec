Name: %{_cross_os}libseccomp
Version: 2.4.2
Release: 1%{?dist}
Summary: Library for enhanced seccomp
License: LGPL-2.1-only
URL: https://github.com/seccomp/libseccomp
Source0: https://github.com/seccomp/libseccomp/releases/download/v%{version}/libseccomp-%{version}.tar.gz
BuildRequires: %{_cross_os}glibc-devel

# Backports from upstream after 2.4.2 release
Patch0001: 0001-api-define-__SNR_ppoll-again.patch
Patch0002: 0002-tests-rely-on-__SNR_xxx-instead-of-__NR_xxx-for-sysc.patch

%description
%{summary}.

%package devel
Summary: Files for development using the library for enhanced seccomp
Requires: %{name}

%description devel
%{summary}.

%prep
%autosetup -n libseccomp-%{version} -p1

%build
%cross_configure
%make_build

%install
%make_install

%files
%license LICENSE
%{_cross_attribution_file}
%{_cross_libdir}/*.so.*
%exclude %{_cross_bindir}/scmp_sys_resolver
%exclude %{_cross_mandir}

%files devel
%{_cross_libdir}/*.a
%{_cross_libdir}/*.so
%{_cross_includedir}/*.h
%{_cross_pkgconfigdir}/*.pc
%exclude %{_cross_libdir}/*.la

%changelog
