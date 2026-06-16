FROM fedora:latest
RUN dnf install -y rpm-build rpm-devel rpmlint make python3
RUN mkdir -p /root/rpmbuild/{SOURCES,SPECS,RPMS,BUILD,BUILDROOT}
COPY app.py /root/
# Generamos el spec de forma simple
RUN echo -e 'Name: sinergia-dd-burner\nVersion: 1.0.2\nRelease: 1\nSummary: Sinergia DD Burner\nBuildArch: noarch\nLicense: GPL\n\n%description\nSinergia DD Burner\n\n%install\nmkdir -p %{buildroot}/usr/bin\nmkdir -p %{buildroot}/usr/share/sinergia-dd-burner\ncp /root/app.py %{buildroot}/usr/share/sinergia-dd-burner/\necho -e "#!/bin/bash\npython3 /usr/share/sinergia-dd-burner/app.py \\$@" > %{buildroot}/usr/bin/sinergia-dd-burner\nchmod 755 %{buildroot}/usr/bin/sinergia-dd-burner\n\n%files\n/usr/bin/sinergia-dd-burner\n/usr/share/sinergia-dd-burner/app.py' > /root/rpmbuild/SPECS/sinergia.spec
# Construimos y capturamos errores
RUN rpmbuild --define "_topdir /root/rpmbuild" -ba /root/rpmbuild/SPECS/sinergia.spec || (cat /root/rpmbuild/BUILD/build.log && exit 1)
