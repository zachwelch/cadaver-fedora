Name: cadaver
Version: 0.22.3
Release: 4
Summary: Command-line WebDAV client
License: GPL
Group: Applications/Internet
Source: http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
URL: http://www.webdav.org/cadaver/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: neon-devel >= 0:0.24.0-1 
BuildPrereq: readline-devel

%description
cadaver is a command-line WebDAV client, with support for file upload, 
download, on-screen display, in-place editing, namespace operations
(move/copy), collection creation and deletion, property manipulation, 
and resource locking.

%prep
%setup -q

%build
%configure --with-neon=%{_prefix} LDFLAGS=-pie CFLAGS="$RPM_OPT_FLAGS -fpie"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%doc NEWS FAQ THANKS TODO COPYING README ChangeLog
%{_mandir}/*/*

%changelog
* Mon Jul 17 2006 Joe Orton <jorton@redhat.com> 0.22.3-4
- rebuild

* Tue May 16 2006 Karsten Hopp <karsten@redhat.de> 0.22.3-3
- buildrequires readline-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.22.3-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.22.3-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 0.22.3-2
- rebuild for neon 0.25.x

* Fri Jan  6 2006 Joe Orton <jorton@redhat.com> 0.22.3-1
- update to 0.22.3

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov  8 2005 Tomas Mraz <tmraz@redhat.com> 0.22.2-3
- rebuilt with new openssl

* Wed Mar  2 2005 Joe Orton <jorton@redhat.com> 0.22.2-2
- rebuild

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 0.22.2-1
- update to 0.22.2

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 0.22.1-4
- Rebuild for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 12 2004 Joe Orton <jorton@redhat.com> 0.22.1-2
- build as PIE

* Tue Apr 20 2004 Joe Orton <jorton@redhat.com> 0.22.1-1
- update to 0.22.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Oct  3 2003 Joe Orton <jorton@redhat.com> 0.22.0-1
- update to 0.22.0; use system neon

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.21.0-2
- rebuild

* Mon Jul 21 2003 Joe Orton <jorton@redhat.com> 0.21.0-1
- update to 0.21.0

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

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
