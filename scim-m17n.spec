%define version	0.2.3

%define scim_version		1.4.5
%define m17n_lib_version	1.3.0

Summary:	A wrapper for m17n
Name:		scim-m17n
Version:	%{version}
Release:	%mkrel 3
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.net/projects/scim/
Source0:	http://freefr.dl.sourceforge.net/sourceforge/scim/%name-%version.tar.gz
Requires:	m17n-lib >= %{m17n_lib_version}
Requires:	scim-client = %{scim_api}
BuildRequires:	m17n-lib-devel >= %{m17n_lib_version}
BuildRequires:	scim-devel >= %{scim_version}
Obsoletes:	%mklibname %name 0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
A wrapper for m17n.

%prep
%setup -q

%build
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
