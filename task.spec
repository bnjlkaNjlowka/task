Name: task
Version: 1.0
Release: 1
Summary: A simple thing
License: GPL
Source0: task-1.0.tar.gz

%description
cool

%global debug_package %{nil}

%prep
%autosetup

%build
make

%install
mkdir $RPM_BUILD_ROOT/usr
mkdir $RPM_BUILD_ROOT/usr/bin
install task-1.0 $RPM_BUILD_ROOT/usr/bin

%files
%defattr(-,root,root)
/usr/bin/task-1.0

%clean
rm -rf $RPM_BUILD_ROOT
