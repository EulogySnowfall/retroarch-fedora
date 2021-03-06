Name:           libretro-bnes
Version:        1
Release:        3.0e30b99baf%{?dist}
Summary:        Libretro bnes core

Group:          Applications/Emulators
License:        GPLv3
URL:            https://github.com/libretro/bnes-libretro
Source0:        https://github.com/libretro/bnes-libretro/archive/0e30b99baf.tar.gz
Source1:        https://raw.githubusercontent.com/libretro/libretro-super/master/dist/info/bnes_libretro.info


%description
Libretro bnes core.


%prep
%setup -q -n bnes-libretro-0e30b99baf08fe40162d71097249e84a0c6c7c21


%build
make %{?_smp_mflags}


%install
install -D -m 0755 libretro.so \
  %{buildroot}%{_libexecdir}/libretro/bnes.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/bnes.info


%files
%doc README
%{_libexecdir}/libretro/


%changelog
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1-1.86b2aafbda
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.86b2aafbda
- Initial RPM release.

