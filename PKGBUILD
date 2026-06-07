# Maintainer: TuNombre <tuemail@ejemplo.com>
pkgname=sinergia-dd-burner
pkgver=1.0.0
pkgrel=1
pkgdesc="Herramienta para quemar imágenes DD"
arch=('any')
license=('GPL')
depends=('python')

# Aquí indicamos que los archivos están en el repositorio (no en una carpeta sub-repositorio)
source=('app.py' 'dd-burner.png')
sha256sums=('SKIP' 'SKIP')

package() {
    # Crear carpetas necesarias
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/pixmaps"

    # Copiar archivos
    install -m644 "${srcdir}/app.py" "${pkgdir}/usr/lib/${pkgname}/main.py"
    install -m644 "${srcdir}/dd-burner.png" "${pkgdir}/usr/share/pixmaps/dd-burner.png"

    # Crear lanzador ejecutable
    echo -e "#!/bin/sh\npython /usr/lib/${pkgname}/main.py" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"
}
