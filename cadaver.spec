Name: cadaver
Version: 0.22.1
Release: 2
Summary: Command-line WebDAV client
License: GPL
Group: Applications/Internet
Source: http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
URL: http://www.webdav.org/cadaver/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: neon-devel >= 0:0.24.0-1 

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc NEWS FAQ THANKS TODO COPYING README ChangeLog
%{_mandir}/*/*

%changelog
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
