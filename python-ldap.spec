%define pyver  %(%{__python} -c 'import sys ; print sys.version[:3]')
%define openldap_version 2.1.22

Name:           python-ldap
Version:        2.0.6
Release:        4
Summary:        An object-oriented API to access LDAP directory servers.

Group:          System Environment/Libraries
License:        PSF - see LICENCE
URL:            http://python-ldap.sourceforge.net/
Source0:        http://dl.sf.net/sourceforge/python-ldap/python-ldap-2.0.6.tar.gz
Patch0:         python-ldap-2.0.6-rpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# the openldap from RHL <= 9 and RHEL <= 3 is too old for python-ldap
BuildRequires:  openldap-devel >= %{openldap_version}, openssl-devel
BuildRequires:  python-devel >= 2.2
Requires:       openldap >= %{openldap_version}
Requires:       python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")

%description
python-ldap provides an object-oriented API for working with LDAP within
Python programs.  It allows access to LDAP directory servers by wrapping the 
OpenLDAP 2.x libraries, and contains modules for other LDAP-related tasks 
(including processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%prep
%setup -q 
%patch -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --root=$RPM_BUILD_ROOT \
  --record=INSTALLED_FILES
sed 's|^\(.*\.pyo\)$|%ghost \1|' < INSTALLED_FILES > %{name}-%{version}.files
find $RPM_BUILD_ROOT%{_libdir}/python%{pyver}/site-packages/* -type d \
  | sed "s|^$RPM_BUILD_ROOT|%dir |" >> %{name}-%{version}.files

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}.files
%defattr(-,root,root,-)
%doc LICENCE CHANGES README TODO Demo

%changelog
* Tue Mar 22 2005 Warren Togami <wtogami@redhat.com> - 2.0.6-4
- add LICENCE (#150842)
- remove epochs
- simplify python reqs
- remove invalid rpath

* Wed Mar 16 2005 Dan Williams <dcbw@redhat.com> - 0:2.0.6-2
- rebuilt to pick up new libssl.so.5

* Tue Feb  8 2005 David Malcolm <dmalcolm@redhat.com> - 0:2.0.6-1
- 2.0.6

* Tue Nov 16 2004 Nalin Dahyabhai <nalin@redhat.com> - 0:2.0.1-3
- rebuild (#139161)

* Mon Aug 30 2004 David Malcolm <dmalcolm@redhat.com> - 0:2.0.1-2
- Rewrote description; added requirement for openldap

* Tue Aug 17 2004 David Malcolm <dmalcolm@redhat.com> - 0:2.0.1-1
- imported into Red Hat's packaging system from Fedora.us; set release to 1

* Wed Jun 30 2004 Panu Matilainen <pmatilai@welho.com> 0:2.0.1-0.fdr.1
- update to 2.0.1

* Sun Dec 07 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.0-0.fdr.0.4.pre16
- fix spec permissions + release tag order (bug 1099)

* Sat Dec  6 2003 Ville Skyttä <ville.skytta at iki.fi> 0:2.0.0-0.fdr.0.pre16.3
- Stricter python version requirements.
- BuildRequire openssl-devel.
- Explicitly build *.pyo, install them as %%ghost.
- Own more installed dirs.
- Remove $RPM_BUILD_ROOT at start of %%install.

* Wed Dec 03 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.0-0.fdr.0.pre16.2
- duh, build requires python-devel, not just python...

* Wed Dec 03 2003 Panu Matilainen <pmatilai@welho.com> 0:2.0.0-0.fdr.0.pre16.1
- Initial Fedora packaging.
