// Asegurarnos de que el DOM esté listo antes de ejecutar el script
document.addEventListener('DOMContentLoaded', () => {
    // Obtener el elemento con los datos JSON
    const dataElement = document.getElementById('dataStrings');

    // Verificar si el elemento existe y contiene texto
    if (dataElement && dataElement.textContent) {
        try {
            // Parsear el contenido JSON
            const strings = JSON.parse(dataElement.textContent);

            // Seleccionar el contenedor donde se insertarán los strings
            const header = document.getElementById('tableHeader');

            // Crear un fragmento de documento para evitar múltiples manipulaciones del DOM
            const fragment = document.createDocumentFragment();

            // Construir los elementos en el fragmento
            strings.forEach(text => {
                const span = document.createElement('span');
                span.textContent = text;
                fragment.appendChild(span);
            });

            // Insertar el fragmento completo en el DOM de una vez
            header.appendChild(fragment);
        } catch (error) {
            console.error('Error al parsear el JSON:', error);
        }
    } else {
        console.error('No se encontró el elemento con los datos o está vacío.');
    }
});
