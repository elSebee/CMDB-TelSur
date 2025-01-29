document.addEventListener("DOMContentLoaded", function () {
    // Botón para agregar una nueva fila
    document.getElementById("btn-agregar").addEventListener("click", function () {
        // Clona la primera fila de campos
        const primeraFila = document.querySelector(".campos-fila");
        const nuevaFila = primeraFila.cloneNode(true);

        // Limpia los valores de los campos en la nueva fila
        nuevaFila.querySelectorAll("textarea, select").forEach(function (campo) {
            if (campo.tagName === "TEXTAREA") {
                campo.value = ""; // Limpia los inputs
            } else if (campo.tagName === "SELECT") {
                campo.selectedIndex = 0; // Reinicia los selects
            }
        });

        // Agrega la nueva fila al contenedor
        document.getElementById("campos-container").appendChild(nuevaFila);
    });

    // Delegación de eventos para eliminar una fila
    document.getElementById("campos-container").addEventListener("click", function (e) {
        if (e.target.closest(".btn-eliminar")) {
            const fila = e.target.closest(".campos-fila");
            if (document.querySelectorAll(".campos-fila").length > 1) {
                fila.remove(); // Elimina la fila solo si hay más de una
            } else {
                alert("No se puede eliminar el último formulario.");
            }
        }
    });
});
