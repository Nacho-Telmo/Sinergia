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
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/pixmaps"

    # La carpeta 'Sinergia' es la que crea git al clonar
    install -m644 "${srcdir}/Sinergia/app.py" "${pkgdir}/usr/lib/${pkgname}/main.py"
    install -m644 "${srcdir}/Sinergia/dd-burner.png" "${pkgdir}/usr/share/pixmaps/dd-burner.png"

    echo -e "#!/bin/sh\npython /usr/lib/${pkgname}/main.py" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"
}

