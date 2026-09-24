document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("predictForm");
  if (!form) return;
  form.addEventListener("submit", () => {
    const btn = document.getElementById("predictBtn");
    if (btn) {
      btn.disabled = true;
      btn.textContent = "Predicting...";
    }
  });
});
