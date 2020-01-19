%global fontname vemana2000
%global fontconf 69-%{fontname}.conf

Name: %{fontname}-fonts
Version: 1.1.3
Release: 6%{?dist}
Summary: Unicode compliant OpenType font for Telugu

Group: User Interface/X
License: GPLv2+ with exceptions
URL: https://fedorahosted.org/pothana_vemana/

Source0: https://fedorahosted.org/releases/p/o/pothana_vemana/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: fontforge
BuildRequires: fontpackages-devel
Requires: fontpackages-filesystem

%description
A free OpenType font for Telugu created by
Dr. Tirumala Krishna Desikacharyulu. 

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
 %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{fontconf} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
 %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.3-6
- Mass rebuild 2013-12-27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Sandeep Shedmake <sshedmak@redhat.com> - 1.1.3-4
- Cleaned the spec file
- Removed BuildRoot
- Edited Source0 and BuildRequires

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 02 2011 Sandeep Shedmake <sshedmak@redhat.com> - 1.1.3-1
- Added Indian Rupee Sign (U+20B9)
- Modified URL to fedorahosted.org domain
- Updated Source0 link
- Added BuildRequires fontforge
- Modified doc section

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 14 2009 <sshedmak@redhat.com> - 1.1.2-1
- Fixed FSType, Preferred Styles, UniqueID and Fullname
- Fixed Invalid Glyph Names reported by fontlint
- with exceptions string added in License

* Tue Aug 31 2009 <sshedmak@redhat.com> - 1.1.1-2
- Changed the Pothana2000 strings to Vemana2000

* Tue Jun 23 2009 <sshedmak@redhat.com> - 1.1.1-1
- Initial packaging
