document.querySelectorAll(".clob-cell").forEach((cell) => {
    // Agrega un evento de clic a cada celda
    cell.addEventListener("click", () => {
      // Alterna la clase "expanded" al hacer clic
      cell.classList.toggle("expanded");
    });
  });