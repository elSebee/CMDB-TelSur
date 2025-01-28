function showTable(tableId, button) {
    // Esconde todas las tablas
    let tables = document.querySelectorAll('.table-home');
    tables.forEach(function(table) {
        table.style.display = 'none';
    });

    // Muestra la tabla seleccionada
    let table = document.getElementById(tableId);
    table.style.display = 'block';

    // Remueve la clase "active" de todos los botones
    let buttons = document.querySelectorAll('.btn-home');
    buttons.forEach(function(btn) {
        btn.classList.remove('active');
    });

    // Añade la clase "active" al botón seleccionado
    button.classList.add('active');
}

