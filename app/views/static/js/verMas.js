document.querySelectorAll('.ver-mas').forEach(button => {
  button.addEventListener('click', function() {
      const targetId = this.getAttribute('data-target');
      const subtabla = document.getElementById(targetId);
      if (subtabla.style.display === 'none') {
          subtabla.style.display = 'table-row';
          this.innerHTML = '<i class="bi bi-chevron-up"></i>'; // Cambia el ícono
      } else {
          subtabla.style.display = 'none';
          this.innerHTML = '<i class="bi bi-chevron-down"></i>'; // Cambia el ícono
      }
  });
});