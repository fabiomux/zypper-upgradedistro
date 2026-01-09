#
# spec file for package zypper-upgradedistro-plugin
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           zypper-upgradedistro-plugin
Version:        1.2.0
Release:        0
%define mod_name zypper-upgradedistro
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       rubygem(zypper-upgraderepo)
Requires:       zypper >= 1.13.10
Url:            https://github.com/fabiomux/zypper-upgradedistro
Source:         %{mod_full_name}.tgz
Summary:        An interactive tool to perform the openSUSE Leap upgrade from command line
License:        GPL-3.0
Group:          System/Packages

%description
This is a simple interactive tool for the openSUSE Leap distribution
which detects a new stable version and performs the needed steps to
have a smoother upgrade procedure from command line.

%prep
%setup -q -n %{mod_name}

%build

%install
mkdir -p %{buildroot}/usr/lib/zypper/commands %{buildroot}/%{_mandir}/man8 %{buildroot}%{_bindir}
install -m 755 upgradedistro %{buildroot}%{_bindir}/
install -m 755 zypper-upgradedistro %{buildroot}/usr/lib/zypper/commands/
install -m 644 zypper-upgradedistro.8 %{buildroot}/%{_mandir}/man8/

%files
%defattr(-,root,root,-)
%{_bindir}/upgradedistro
/usr/lib/zypper
/usr/lib/zypper/commands
%{_mandir}/man8/*

%changelog
