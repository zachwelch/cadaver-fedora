
Name: cadaver
Version: 0.20.5
Release: 6
Summary: Command-line WebDAV client
License: GPL
Group: Applications/Internet
Source: http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
URL: http://www.webdav.org/cadaver/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: libxml2-devel, openssl-devel, pkgconfig, readline-devel

%description
cadaver is a command-line WebDAV client, with support for file upload, 
download, on-screen display, in-place editing, namespace operations
(move/copy), collection creation and deletion, property manipulation, 
and resource locking.

%prep
%setup -q

%build
# force the XML parser to be libxml2; over-ride SSL version checks
if pkg-config openssl ; then
	CPPFLAGS=`pkg-config --cflags openssl`; export CPPFLAGS
	LDFLAGS=`pkg-config --libs openssl`; export LDFLAGS
fi
%configure --with-libxml2 --with-ssl --with-force-ssl --with-included-neon
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc NEWS FAQ THANKS TODO COPYING README ChangeLog
%{_mandir}/*/*

%changelog
* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.20.5-5
- rebuild

* Fri Nov 22 2002 Joe Orton <jorton@redhat.com> 0.20.5-4
- force use of bundled neon (#78260)

* Mon Nov  4 2002 Joe Orton <jorton@redhat.com> 0.20.5-3
- rebuild in new environment

* Fri Aug 30 2002 Joe Orton <jorton@redhat.com> 0.20.5-2
- update to 0.20.5; many bug fixes, minor security-related
 fixes, much improved SSL support, a few new features.

* Thu Aug 22 2002 Joe Orton <jorton@redhat.com> 0.20.4-1
- add --with-force-ssl

* Wed May  1 2002 Joe Orton <joe@manyfish.co.uk>
- add man page

* Sat Jan 19 2002 Joe Orton <joe@manyfish.co.uk>
- updated description

* Mon Nov 19 2001 Joe Orton <joe@manyfish.co.uk>
- Merge changes from Nalin Dahyabhai <nalin@redhat.com>.

* Fri Feb 11 2000 Joe Orton <joe@orton.demon.co.uk>
- Text descriptions modified

* Thu Feb 10 2000 Lee Mallabone <lee0@callnetuk.com>
- Initial creation.
