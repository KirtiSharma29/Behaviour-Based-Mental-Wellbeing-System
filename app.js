function showToast(message, type="info") {
  const el = document.getElementById("toast");
  if (!el) return alert(message);
  el.querySelector("#toastMsg").textContent = message;
  el.classList.remove("hidden");
  setTimeout(()=> el.classList.add("hidden"), 3200);
}
