%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     zenergy
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  BMI260 IMU Linux driver
License:  GPLv2
URL:      https://github.com/KyleGospo/zenergy

Source:   %{url}/archive/refs/heads/master.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
This is a kernel module driver for the Bosch BMI260 IMU. This module is based off of the existing kernel BMI160 implementation. The 260 appears to follow the same specifications as the 270, or close enough to work at least.

%prep
%setup -q -c %{name}-master

%files
%doc %{name}-master/README.md
%license %{name}-master/LICENSE

%changelog
{{{ git_dir_changelog }}}
