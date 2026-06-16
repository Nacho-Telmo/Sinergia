FROM fedora:latest
RUN dnf install -y rpm-build rpm-devel rpmlint make python3 && dnf clean all
RUN mkdir -p /root/rpmbuild/{SOURCES,SPECS,RPMS,SRPMS,BUILD,BUILDROOT}
COPY app.py /root/rpmbuild/SOURCES/
COPY sinergia.spec /root/rpmbuild/SPECS/
RUN rpmbuild -ba /root/rpmbuild/SPECS/sinergia.spec
