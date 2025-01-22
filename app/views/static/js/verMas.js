document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.btn-expand').forEach(button => {
      button.addEventListener('click', () => {
          const cardContent = button.parentElement.nextElementSibling;
          cardContent.classList.toggle('expanded');
          button.innerHTML = cardContent.classList.contains('expanded')
              ? '<i class="bi bi-caret-up-fill"></i>'
              : '<i class="bi bi-caret-down-fill"></i>';
      });
  });
});
