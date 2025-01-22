// Obtener elementos
const modal = document.getElementById('myModal');
const openModalBtn = document.getElementById('openModalBtn');
const closeModal = document.querySelector('.close');

// Mostrar el modal al hacer clic en el botón
openModalBtn.addEventListener('click', () => {
    modal.style.display = 'block';
});

// Cerrar el modal al hacer clic en la "X"
closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Cerrar el modal si el usuario hace clic fuera del contenido
window.addEventListener('click', (event) => {
    if (event.target === modal) {
    modal.style.display = 'none';
    }
});