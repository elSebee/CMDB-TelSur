function autoResize(textarea) {
    textarea.style.height = "auto"; // Restablece la altura para recalcular correctamente
    textarea.style.height = (textarea.scrollHeight) + "px"; // Ajusta la altura según el contenido
}

// Ejecutar al cargar la página para ajustar si ya hay texto
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("textarea").forEach(autoResize);
});