# Maintainer: TuNombre <tuemail@ejemplo.com>
pkgname=sinergia-dd-burner
pkgver=1.0.0
pkgrel=1
pkgdesc="Herramienta GUI para quemar imágenes ISO utilizando el comando dd"
arch=('any')
url="https://github.com/Nacho-Telmo/Sinergia"  # <--- Esta es la URL que faltaba
license=('GPL')
depends=('python' 'python-pyqt6')

# Definimos los archivos locales que deben incluirse en el paquete
source=('app.py' 'dd-burner.png')
sha256sums=('SKIP' 'SKIP')

package() {
    # 1. Crear directorios necesarios
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/icons/hicolor/scalable/apps"
    install -d "${pkgdir}/usr/share/applications"

    # 2. Copiar archivos fuente al paquete
    # Se utiliza "${srcdir}" porque makepkg mueve los archivos allí al compilar
    cp "${srcdir}/app.py" "${pkgdir}/usr/lib/${pkgname}/main.py"
    cp "${srcdir}/dd-burner.png" "${pkgdir}/usr/share/icons/hicolor/scalable/apps/dd-burner.png"

    # 3. Crear el ejecutable en /usr/bin
    echo -e "#!/bin/sh\npython /usr/lib/${pkgname}/main.py" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    # 4. Crear el archivo .desktop
    cat <<EOF > "${pkgdir}/usr/share/applications/${pkgname}.desktop"
[Desktop Entry]
Name=Sinergia DD Burner
Comment=Herramienta para quemar imágenes DD
Exec=${pkgname}
Icon=dd-burner
Terminal=false
Type=Application
Categories=Utility;System;
EOF
}

