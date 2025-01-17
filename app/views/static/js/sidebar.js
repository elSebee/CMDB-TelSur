const toggleBtn = document.getElementById('toggle-btn');
const sidebar = document.getElementById('sidebar');
const navbar = document.getElementById('navbar');
const mainContent = document.getElementById('main-content');

toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('closed'); // Alterna el sidebar
    navbar.classList.toggle('sidebar-closed'); // Alterna el navbar
    mainContent.classList.toggle('sidebar-closed'); // Alterna el contenido principal
});
