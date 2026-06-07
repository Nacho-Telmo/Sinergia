# Maintainer: Ignacio <Nacho-Telmo>
pkgname=sinergia-dd-burner
pkgver=1.0.0
pkgrel=1
pkgdesc="Grabador de imágenes ISO a unidades USB seguro y minimalista con interfaz oscura"
arch=('any')
url="https://github.com/Nacho-Telmo/Sinergia"
license=('GPL3')
depends=('python' 'python-pyqt6')
makedepends=('git')
source=("git+https://github.com/Nacho-Telmo/Sinergia.git")
sha256sums=('SKIP')

package() {
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/applications"
    install -d "${pkgdir}/usr/share/pixmaps"

    install -m644 "${srcdir}/Sinergia/app.py" "${pkgdir}/usr/lib/${pkgname}/main.py"
    cp -r "${srcdir}/Sinergia/assets" "${pkgdir}/usr/lib/${pkgname}/"

    cat << 'EOF' > "${pkgdir}/usr/bin/${pkgname}"
#!/bin/sh
exec python /usr/lib/sinergia-dd-burner/main.py "$@"
EOF
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    install -m644 "${srcdir}/Sinergia/dd-burner.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"

    cat << EOF > "${pkgdir}/usr/share/applications/${pkgname}.desktop"
[Desktop Entry]
Name=Sinergia DD Burner
Exec=${pkgname}
Icon=${pkgname}
Type=Application
Categories=Utility;
Comment=Escribe ISOs a unidades USB de forma segura
EOF
}
