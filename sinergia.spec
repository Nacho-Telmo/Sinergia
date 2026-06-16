Name:           sinergia-dd-burner
Version:        1.0.2
Release:        1
Summary:        Sinergia DD Burner
BuildArch:      noarch
License:        GPL
URL:            https://github.com/Nacho-Telmo/Sinergia

%description
Sinergia DD Burner es una herramienta de la comunidad para grabar imágenes ISO/IMG usando dd.

%prep

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/sinergia-dd-burner

cp %{_sourcedir}/app.py %{buildroot}/usr/share/sinergia-dd-burner/

cat << 'INNER_EOF' > %{buildroot}/usr/bin/sinergia-dd-burner
#!/bin/bash
python3 /usr/share/sinergia-dd-burner/app.py "$@"
INNER_EOF

chmod 755 %{buildroot}/usr/bin/sinergia-dd-burner

%files
/usr/bin/sinergia-dd-burner
/usr/share/sinergia-dd-burner/app.py

%changelog
* Tue Jun 16 2026 Nacho <nacho@sinergia> - 1.0.2-1
- Versión inicial empaquetada para Fedora.
