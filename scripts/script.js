// Contact form handler
const form = document.getElementById("contact-form");
form.addEventListener("submit", e => {
  e.preventDefault();
  alert("Thank you! I will get back to you soon.");
  form.reset();
});

// Dark mode toggle
const toggleBtn = document.getElementById("darkToggle");
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});
