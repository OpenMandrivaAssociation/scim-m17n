%define version	0.2.2

%define scim_version		1.4.5
%define m17n_lib_version	1.3.0

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Summary:	A wrapper for m17n
Name:		scim-m17n
Version:	%{version}
Release:	%mkrel 4
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.net/projects/scim/
Source0:	%{name}-%{version}.tar.bz2
Requires:	%{libname} = %{version}
Requires:	m17n-lib >= %{m17n_lib_version}
Requires:	scim >= %{scim_version}
BuildRequires:	m17n-lib-devel >= %{m17n_lib_version}
BuildRequires:	scim-devel >= %{scim_version}
BuildRequires:	automake, libltdl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%scim_plugins_dir/IMEngine/*.so
