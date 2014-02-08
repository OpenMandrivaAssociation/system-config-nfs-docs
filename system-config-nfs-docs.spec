Summary:	Documentation for configuring an NFS server
Name:		system-config-nfs-docs
Version:	1.0.9
Release:	3
License:	GPLv2+
Group:		Books/Howtos
URL:		https://fedorahosted.org/%{name}
Source0:	http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	docbook-dtd45-xml
BuildRequires:	rarian

# Until version 1.3.41, system-config-nfs contained online documentation.
# From version 1.3.42 on, online documentation is split off into its own
# package system-config-nfs-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes:	system-config-nfs < 1.3.42
Requires:	system-config-nfs >= 1.3.42
Requires:	rarian
Requires:	yelp
BuildArch:	noarch

%description
This package contains the online documentation for system-config-nfs which is
a graphical user interface for creating, modifying, and deleting nfs shares.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

%files
%doc COPYING
%doc %{_datadir}/omf/system-config-nfs
%doc %{_datadir}/gnome/help/system-config-nfs

%changelog
* Sat May 28 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.9-1mdv2011.0
+ Revision: 681297
- initial adopt from Fedora
- imported package system-config-nfs-docs

