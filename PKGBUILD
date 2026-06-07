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
    # Crear carpetas de destino
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/pixmaps"

    # Buscamos los archivos dentro de la carpeta de fuentes ($srcdir)
    # Sea cual sea el nombre que git le haya dado a la carpeta
    find "${srcdir}" -type f -name "app.py" -exec install -m644 {} "${pkgdir}/usr/lib/${pkgname}/main.py" \;
    find "${srcdir}" -type f -name "dd-burner.png" -exec install -m644 {} "${pkgdir}/usr/share/pixmaps/dd-burner.png" \;

    # Crear el ejecutable
    echo -e "#!/bin/sh\npython /usr/lib/${pkgname}/main.py" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"
}

