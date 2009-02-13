%define version	0.2.2

%define scim_version		1.4.5
%define m17n_lib_version	1.3.0

Summary:	A wrapper for m17n
Name:		scim-m17n
Version:	%{version}
Release:	%mkrel 4
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.net/projects/scim/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		scim-m17n-0.2.2-gcc4.3-patch
Requires:	m17n-lib >= %{m17n_lib_version}
Requires:	scim-client = %{scim_api}
BuildRequires:	m17n-lib-devel >= %{m17n_lib_version}
BuildRequires:	scim-devel >= %{scim_version}
BuildRequires:	automake, libltdl-devel
Obsoletes:	%mklibname %name 0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
A wrapper for m17n.

%prep
%setup -q
%patch0 -p0

%build
./bootstrap
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%scim_plugins_dir/IMEngine/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*
%scim_plugins_dir/IMEngine/*.so
