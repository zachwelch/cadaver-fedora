Name: cadaver
Version: 0.19.1
Release: 2
Source: http://www.webdav.org/cadaver/cadaver-%{version}.tar.gz
Group: Applications/Internet
URL: http://www.webdav.org/cadaver/
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Summary: A command-line WebDAV client.
BuildPrereq: apache-devel, libxml2-devel, ncurses-devel, openssl-devel, readline-devel

%description
cadaver is a command-line WebDAV client. It supports file upload,
download, on-screen display, namespace operations (move/copy),
collection creation and deletion, and locking operations.

%prep
%setup -q

%build
%configure --with-ssl=%{_prefix} --enable-libxml
make

%clean
rm -fr $RPM_BUILD_ROOT

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-,root,root)
%doc ChangeLog COPYING* FAQ INSTALL INTEROP NEWS README THANKS TODO
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Fri Feb 22 2002 Nalin Dahyabhai <nalin@redhat.com>  0.19.1-2
- rebuild

* Wed Jan 23 2002 Nalin Dahyabhai <nalin@redhat.com>  0.19.1-1
- update to 0.19.1
- depend on libxml2 instead of libxml

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 0.17.0-3
- automated rebuild

* Thu Jul 12 2001 Nalin Dahyabhai <nalin@redhat.com> 0.17.0-2
- add a couple of missing build prerequisites
- enable use of libxml

* Wed May 22 2001 Nalin Dahyabhai <nalin@redhat.com> 0.17.0-1
- update to 0.17.0

* Fri Mar  2 2001 Tim Powers <timp@redhat.com>
- rebuilt against openssl-0.9.6-1

* Fri Jan 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 0.16.0

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Wed Nov  8 2000 Nalin Dahyabhai <nalin@redhat.com>
- initial Power Tools build
