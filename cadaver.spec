Name: cadaver
Version: 0.19.1
Release: 6
Source: http://www.webdav.org/cadaver/cadaver-%{version}.tar.gz
Patch0: cadaver-0.19.1-libxml2418.patch
Group: Applications/Internet
URL: http://www.webdav.org/cadaver/
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Summary: A command-line WebDAV client.
BuildPrereq: libxml2-devel, ncurses-devel, openssl-devel, readline-devel

%description
cadaver is a command-line WebDAV client. It supports file upload,
download, on-screen display, namespace operations (move/copy),
collection creation and deletion, and locking operations.

%prep
%setup -q
%patch -p0 -b .lx2418

%build
%configure --with-ssl --with-libxml2
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
* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Nalin Dahyabhai <nalin@redhat.com>  0.19.1-4
- rebuild in new environment

* Mon Apr 15 2002 Joe Orton <jorton@redhat.com>  0.19.1-3
- fix compatibility with libxml 2.4.18 (#63358), remove apache-devel prereq

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
