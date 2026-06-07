# Maintainer: TuNombre <tuemail@ejemplo.com>
pkgname=sinergia-dd-burner
pkgver=1.0.0
pkgrel=1
pkgdesc="Herramienta para quemar imágenes DD"
arch=('any')
license=('GPL')
depends=('python')

package() {
    # 1. Crear carpetas de destino
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/pixmaps"
    install -d "${pkgdir}/usr/share/applications"

    # 2. Buscar e instalar los archivos (usando find para ser flexible)
    find "${srcdir}" -type f -name "app.py" -exec install -m644 {} "${pkgdir}/usr/lib/${pkgname}/main.py" \;
    find "${srcdir}" -type f -name "dd-burner.png" -exec install -m644 {} "${pkgdir}/usr/share/pixmaps/dd-burner.png" \;

    # 3. Crear el ejecutable en /usr/bin
    echo -e "#!/bin/sh\npython /usr/lib/${pkgname}/main.py" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    # 4. Crear archivo .desktop para el menú de aplicaciones
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

