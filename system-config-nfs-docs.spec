Summary: Documentation for configuring an NFS server
Name: system-config-nfs-docs
Version: 1.0.9
Release: %mkrel 1
URL: https://fedorahosted.org/%{name}
License: GPLv2+
Group: Books/Howtos
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Source0: http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: gnome-doc-utils
BuildRequires: docbook-dtd45-xml
BuildRequires: rarian

# Until version 1.3.41, system-config-nfs contained online documentation.
# From version 1.3.42 on, online documentation is split off into its own
# package system-config-nfs-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes: system-config-nfs < 1.3.42
Requires: system-config-nfs >= 1.3.42
Requires: rarian
Requires: yelp

%description
This package contains the online documentation for system-config-nfs which is
a graphical user interface for creating, modifying, and deleting nfs shares.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%doc %{_datadir}/omf/system-config-nfs
%doc %{_datadir}/gnome/help/system-config-nfs
