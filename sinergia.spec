Name:           sinergia-dd-burner
Version:        1.0.2
Release:        3
Summary:        Sinergia DD Burner
BuildArch:      noarch
License:        GPL
URL:            https://github.com/Nacho-Telmo/Sinergia

Requires:       python3-pyqt6

%description
Sinergia DD Burner es una herramienta de la comunidad para grabar imágenes ISO/IMG usando dd.

%prep
mkdir -p %{_builddir}/%{name}-%{version}

%install
# Creamos las carpetas de destino
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/sinergia-dd-burner
mkdir -p %{buildroot}/usr/share/applications

# Copiamos app.py desde las fuentes
cp %{_sourcedir}/app.py %{buildroot}/usr/share/sinergia-dd-burner/

# CORRECCIÓN: Copiamos TU archivo .desktop existente desde las fuentes de GitHub
# (Ajustá el nombre si en tu repo se llama distinto a "sinergia-dd-burner.desktop")
cp %{_sourcedir}/sinergia-dd-burner.desktop %{buildroot}/usr/share/applications/

# Lanzador para la terminal
cat << 'INNER_EOF' > %{buildroot}/usr/bin/sinergia-dd-burner
#!/bin/bash
python3 /usr/share/sinergia-dd-burner/app.py "$@"
INNER_EOF

chmod 755 %{buildroot}/usr/bin/sinergia-dd-burner

%files
/usr/bin/sinergia-dd-burner
/usr/share/sinergia-dd-burner/app.py
/usr/share/applications/sinergia-dd-burner.desktop

%changelog
* Tue Jun 16 2026 Nacho <nacho@sinergia> - 1.0.2-3
- Copiado archivo .desktop existente desde las fuentes para el menú de aplicaciones.
- Mantenida la dependencia de python3-pyqt6.
