document.addEventListener("DOMContentLoaded", () => {
  const q = document.getElementById("searchHistory");
  if (!q) return;
  q.addEventListener("input", () => {
    const val = q.value.toLowerCase();
    document.querySelectorAll("tbody tr").forEach(tr => {
      tr.style.display = tr.textContent.toLowerCase().includes(val) ? "" : "none";
    });
  });
});
