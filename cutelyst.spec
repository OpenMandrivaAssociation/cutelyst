%define major 0
%define devname %mklibname cutelyst -d

Name: cutelyst
Version: 4.1.0
Release: 1
Source0: https://github.com/cutelyst/cutelyst/archive/refs/tags/v%{version}.tar.gz
Summary: C++ Web Framework built on top of Qt
URL: https://github.com/cutelyst/cutelyst
License: BSD-3-Clause
Group: System/Libraries
BuildRequires: cmake

%description
A C++ Web Framework built on top of Qt, using the simple approach of
Catalyst (Perl) framework.


%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%libpackages -D

cat >%{specpartsdir}/%{devname}.specpart <<EOF
%%%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
EOF

for i in $LIBPACKAGES; do
	echo "Requires: %{mklibname $i} = %{EVRD}" >>%{specpartsdir}/%{devname}.specpart
done

cat >>%{specpartsdir}/%{devname}.specpart <<EOF
%%%description -n %{devname}
Development files (Headers etc.) for %{name}.

A C++ Web Framework built on top of Qt, using the simple approach of
Catalyst (Perl) framework.

%%%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
EOF

%files
%{_bindir}/*
%{_libdir}/cutelyst4-qt6-plugins
%dir %{_datadir}/cutelyst4-qt6
%dir %{_datadir}/cutelyst4-qt6/translations
%{_datadir}/cutelyst4-qt6/translations/*.qm
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
