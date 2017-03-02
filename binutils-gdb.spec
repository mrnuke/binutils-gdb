%global target  arc-elf32
Name:           %{target}
Version:        arc.2017.03.eng008
Release:        1%{?dist}
Summary:        Binutils and GDB with Synopsis ARC sprinkles
License:        GPLv3+
URL:            https://github.com/foss-for-synopsys-dwc-arc-processors/binutils-gdb.git
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  flex bison perl-podlators zlib-devel expat-devel

%description
Binutils and GDB with Synopsis ARC sprinkles.


%package binutils
Version:        2.28.51
Summary:        GNU Binutils for cross-compilation for %{target} target
License:        GPLv3+

%description binutils
This is a cross-compilation version of GNU Binutils, with Synopsis sprinkles,
which can be used to assemble and link binaries for the %{target} platform.


%package gdb
Version:        7.12.50
Summary:        GDB for (remote) debugging %{target} targets
License:        GPLv3+

%description gdb
This is a version of GDB, the GNU Project debugger, with Synopsis sprinkles,
for (remote) debugging %{target} binaries. GDB allows you to see and modify
what is going on inside another program while it is executing.


%prep
%autosetup


%build
rm -rf zlib
%configure --target=%{target} --program-prefix=%{target}-
# Don't waste time building the docs. This apparently disables makeinfo
echo "MAKEINFO = :" >> Makefile
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files binutils
%license COPYING*
%doc README
%{_prefix}/%{target}
%{_bindir}/%{target}-addr2line
%{_bindir}/%{target}-ar
%{_bindir}/%{target}-as
%{_bindir}/%{target}-c++filt
%{_bindir}/%{target}-elfedit
%{_bindir}/%{target}-gprof
%{_bindir}/%{target}-ld
%{_bindir}/%{target}-ld.bfd
%{_bindir}/%{target}-nm
%{_bindir}/%{target}-objcopy
%{_bindir}/%{target}-objdump
%{_bindir}/%{target}-ranlib
%{_bindir}/%{target}-readelf
%{_bindir}/%{target}-size
%{_bindir}/%{target}-strings
%{_bindir}/%{target}-strip
%{_mandir}/man1/%{target}-*.1.gz

# FIXME: These don't have the arc-elf32- prefix, so just ignore them
%exclude %{_datadir}/locale

# We don't want these as we are a cross version
%exclude %{_infodir}


%files gdb
%license gdb/COPYING
%doc gdb/README
%{_bindir}/%{target}-gdb
%{_mandir}/man5/%{target}-*.5.gz

# Conflicts with host gdb package
%exclude %{_includedir}/gdb
# Probably something important
%exclude %{_datadir}/gdb/syscalls
%exclude %{_datadir}/gdb/system-gdbinit


%changelog
* Mon Feb 27 2017 Alexandru Gagniuc <mr.nuke.me@gmail.com>
- Initial RPM release
