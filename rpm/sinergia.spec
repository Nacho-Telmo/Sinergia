Name:           sinergia-dd-burner
Version:        1.0.0
Release:        1%{?dist}
Summary:        Herramienta para gestionar la grabación de imágenes DD
License:        GPLv3
URL:            https://github.com/Nacho-Telmo/Sinergia
Source0:        sinergia-dd-burner-1.0.0.tar.gz
BuildArch:      noarch

Requires:       python3

%description
Sinergia DD Burner es una utilidad para gestionar la grabación de imágenes DD de forma sencilla.

%prep
%setup -q -n sinergia-dd-burner-1.0.0

%build
# No se requiere compilación para scripts de Python

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/sinergia

install -m 0755 app.py %{buildroot}%{_bindir}/sinergia
install -m 0644 dd-burner.png %{buildroot}%{_datadir}/sinergia/
install -m 0644 demo.png %{buildroot}%{_datadir}/sinergia/

%files
%{_bindir}/sinergia
%{_datadir}/sinergia/dd-burner.png
%{_datadir}/sinergia/demo.png
%doc README.md LICENSE

%changelog
* Tue Jun 16 2026 Nacho Telmo <tu_email@ejemplo.com> - 1.0.0-1
- Versión inicial empaquetada en RPM
