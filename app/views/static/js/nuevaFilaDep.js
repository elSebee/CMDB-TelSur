document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("btn-agregar").addEventListener("click", function () {
        const primeraFila = document.querySelector(".campos-fila");
        const nuevaFila = primeraFila.cloneNode(true);

        nuevaFila.querySelectorAll("textarea, select").forEach(function (campo) {
            if (campo.tagName === "TEXTAREA") {
                campo.value = "";
            } else if (campo.tagName === "SELECT") {
                campo.selectedIndex = 0;
            }
        });

        document.getElementById("campos-container").appendChild(nuevaFila);
    });

    document.getElementById("campos-container").addEventListener("click", function (e) {
        if (e.target.closest(".btn-eliminar")) {
            const fila = e.target.closest(".campos-fila");
            if (document.querySelectorAll(".campos-fila").length > 1) {
                fila.remove();
            } else {
                alert("No se puede eliminar el último formulario.");
            }
        }
    });
});

function enviar_formularios() {
    let formData = new FormData();
    formData.append("csrf_token", document.querySelector("input[name='csrf_token']").value);

    document.querySelectorAll(".campos-fila").forEach((fila, index) => {
        formData.append(`id_ci_origen[${index}]`, fila.querySelector("[name='id_ci_origen']").value);
        formData.append(`tipo_relacion[${index}]`, fila.querySelector("[name='tipo_relacion']").value);
        formData.append(`id_ci_destino[${index}]`, fila.querySelector("[name='id_ci_destino']").value);
        formData.append(`id_servicio[${index}]`, fila.querySelector("[name='id_servicio']").value);
    });

    console.log("Enviando datos:", [...formData]);

    fetch(`${window.location.origin}/dependencias/agregar/nuevo`, {  // URL corregida
        method: "POST",
        credentials: "include",
        body: formData, // El body debe ser FormData directamente
        cache: "no-cache",
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        window.location.href = data.redirect;  // Redirige a la nueva página
    })
    .catch(error => {
        console.error("Error al enviar:", error);
    });
}