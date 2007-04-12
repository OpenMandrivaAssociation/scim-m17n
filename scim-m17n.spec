%define version	0.2.2
%define release	%mkrel 1

%define scim_version		1.4.5
%define m17n_lib_version	1.3.0

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-m17n
Summary:	A wrapper for m17n
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		GPL
URL:			http://sourceforge.net/projects/scim/
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{version}
Requires:			m17n-lib >= %{m17n_lib_version}
Requires:			scim >= %{scim_version}
BuildRequires:		m17n-lib-devel >= %{m17n_lib_version}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		automake1.8, libltdl-devel

%description
A wrapper for m17n.


%package -n	%{libname}
Summary:	Scim-m17n library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
Scim-m17n library.


%prep
%setup -q
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ ! -x configure ]] && ./bootstrap

%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/scim-1.0/*/IMEngine/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/scim-1.0/*/IMEngine/*.so


