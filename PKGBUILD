# Maintainer: TuNombre <tuemail@ejemplo.com>
pkgname=sinergia-dd-burner
pkgver=1.0.0
pkgrel=1
pkgdesc="Herramienta para quemar imágenes DD"
arch=('any')
license=('GPL')
depends=('python')

# Quitamos 'source' porque los archivos ya están en el repo de git del AUR
source=()

package() {
    # Crear carpetas necesarias
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/pixmaps"

    # Copiamos desde el directorio de construcción ($startdir)
    # que es donde 'makepkg' clona tu repo
    install -m644 "${startdir}/app.py" "${pkgdir}/usr/lib/${pkgname}/main.py"
    install -m644 "${startdir}/dd-burner.png" "${pkgdir}/usr/share/pixmaps/dd-burner.png"

    # Crear lanzador ejecutable
    echo -e "#!/bin/sh\npython /usr/lib/${pkgname}/main.py" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"
}

