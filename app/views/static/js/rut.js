document.addEventListener('DOMContentLoaded', function () {
    const rutInput = document.getElementById('rut');
    if (rutInput) {
        rutInput.addEventListener('input', function (e) {
            let rutError = document.getElementById('rutError');

            // Limpiar el RUT (solo números y la letra 'k')
            let rut = e.target.value.replace(/[^0-9kK]/g, '');

            // Si el RUT está vacío, no hacer nada
            if (rut.length === 0) {
                rutError.style.display = 'none';
                e.target.value = '';
                return;
            }

            // Separar el cuerpo del dígito verificador
            let cuerpo = rut.slice(0, -1);
            let dv = rut.slice(-1).toUpperCase();

            // Formatear el cuerpo con puntos
            if (cuerpo.length > 0) {
                cuerpo = cuerpo.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
            }

            // Unir el cuerpo formateado con el dígito verificador
            let rutFormateado = `${cuerpo}-${dv}`;

            // Actualizar el valor del input
            e.target.value = rutFormateado;

            // Validar el RUT
            if (validarRUT(rutFormateado)) {
                rutError.style.display = 'none';
            } else {
                rutError.style.display = 'block';
            }
        });
    }
});

function validarRUT(rut) {
    // Limpiar el RUT
    rut = rut.replace(/[^0-9kK]/g, '');

    // Verificar longitud mínima
    if (rut.length < 2) return false;

    // Separar cuerpo y dígito verificador
    let cuerpo = rut.slice(0, -1);
    let dv = rut.slice(-1).toUpperCase();

    // Calcular el dígito verificador esperado
    let suma = 0;
    let multiplicador = 2;

    for (let i = cuerpo.length - 1; i >= 0; i--) {
        suma += parseInt(cuerpo.charAt(i)) * multiplicador;
        multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
    }

    let dvEsperado = 11 - (suma % 11);
    if (dvEsperado === 11) dvEsperado = '0';
    if (dvEsperado === 10) dvEsperado = 'K';

    // Comparar con el dígito verificador ingresado
    return dv === dvEsperado.toString();
}