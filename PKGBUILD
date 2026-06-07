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

    # BUSCAMOS EN TODOS LADOS: Si está en src, en src/Sinergia o en src/sinergia-dd-burner
    # Esta es una forma segura de encontrar el archivo sin importar el nombre de la carpeta:
    find "${srcdir}" -name "app.py" -exec install -m644 {} "${pkgdir}/usr/lib/${pkgname}/main.py" \;
    find "${srcdir}" -name "dd-burner.png" -exec install -m644 {} "${pkgdir}/usr/share/pixmaps/dd-burner.png" \;

    echo -e "#!/bin/sh\npython /usr/lib/${pkgname}/main.py" > "${pkgdir}/usr/bin/${pkgname}"
    chmod +x "${pkgdir}/usr/bin/${pkgname}"
}

