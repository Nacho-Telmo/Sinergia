FROM fedora:latest

# Instalar dependencias necesarias
RUN dnf install -y rpm-build rpm-devel rpmlint make python3 && dnf clean all

# Crear el árbol de directorios estándar para rpmbuild
RUN mkdir -p /root/rpmbuild/{SOURCES,SPECS,RPMS,SRPMS,BUILD,BUILDROOT}

# Copiar app.py a SOURCES y el .spec a SPECS
COPY app.py /root/rpmbuild/SOURCES/
COPY sinergia.spec /root/rpmbuild/SPECS/

# Ejecutar la compilación real del paquete binario y fuente
RUN rpmbuild -ba /root/rpmbuild/SPECS/sinergia.spec
