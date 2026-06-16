Name:           sinergia-dd-burner
Version:        1.0.2
Release:        6
Summary:        Sinergia DD Burner
BuildArch:      noarch
License:        GPL
URL:            https://github.com/Nacho-Telmo/Sinergia

# Se elimina la dependencia estricta para evitar conflictos de nombres entre repositorios
# La aplicación requiere python3-qt6, el cual el usuario debe tener instalado en su sistema.
Requires:       python3-qt6

%description
Sinergia DD Burner es una herramienta de la comunidad para grabar imágenes ISO/IMG usando dd.

%prep
mkdir -p %{_builddir}/%{name}-%{version}

%install
# Creamos las carpetas de destino en el buildroot
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/sinergia-dd-burner
mkdir -p %{buildroot}/usr/share/applications

# Copiamos app.py desde las fuentes
cp %{_sourcedir}/app.py %{buildroot}/usr/share/sinergia-dd-burner/

# Creamos el lanzador de terminal de forma nativa
cat << 'INNER_EOF' > %{buildroot}/usr/bin/sinergia-dd-burner
#!/bin/bash
python3 /usr/share/sinergia-dd-burner/app.py "$@"
INNER_EOF

chmod 755 %{buildroot}/usr/bin/sinergia-dd-burner

# Grabamos el .desktop idéntico al que usa el .deb directamente en su lugar
cat << 'INNER_EOF' > %{buildroot}/usr/share/applications/sinergia-dd-burner.desktop
[Desktop Entry]
Type=Application
Name=Sinergia DD Burner
Comment=Graba imágenes ISO y IMG usando el comando dd
Exec=/usr/bin/sinergia-dd-burner
Icon=utilities-terminal
Terminal=false
Categories=Utility;System;
INNER_EOF

%files
/usr/bin/sinergia-dd-burner
/usr/share/sinergia-dd-burner/app.py
/usr/share/applications/sinergia-dd-burner.desktop

%changelog
* Tue Jun 16 2026 Nacho <nacho@sinergia> - 1.0.2-6
- Eliminada dependencia estricta para garantizar instalación universal.

* Tue Jun 16 2026 Nacho <nacho@sinergia> - 1.0.2-5
- Agregada macro condicional en Requires para compatibilidad nativa con openSUSE (python3-PyQt6).

* Tue Jun 16 2026 Nacho <nacho@sinergia> - 1.0.2-4
- Corregido error de copia del .desktop generándolo in-line en %install.
