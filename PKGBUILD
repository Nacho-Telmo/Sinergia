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
# Descargamos directamente la rama principal (main) de tu GitHub
source=("git+https://github.com/Nacho-Telmo/Sinergia.git")
sha256sums=('SKIP') # Al usar Git directo, omitimos el hash estático

package() {
    # 1. Crear la estructura de directorios en el sistema ficticio de pacman
    install -d "${pkgdir}/usr/lib/${pkgname}"
    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/applications"
    install -d "${pkgdir}/usr/share/pixmaps"

    # 2. Instalar el script de Python y el ícono desde el clon de Git
    cp "${srcdir}/Sinergia/app.py" "${pkgdir}/usr/lib/${pkgname}/main.py"
    install -m644 "${srcdir}/Sinergia/dd-burner.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"

    # 3. Crear el script lanzador en /usr/bin
    cat << 'EOF' > "${pkgdir}/usr/bin/${pkgname}"
#!/bin/sh
exec python /usr/lib/sinergia-dd-burner/main.py "$@"
EOF
    chmod +x "${pkgdir}/usr/bin/${pkgname}"

    # 4. Instalar el archivo de escritorio .desktop oficial
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
