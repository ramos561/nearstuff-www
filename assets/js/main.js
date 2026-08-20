const form = document.querySelector("[data-contact-form]");
if (form) {
  const status = form.querySelector("[data-form-status]");
  const submit = form.querySelector('button[type="submit"]');

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const data = new FormData(form);
    const payload = {
      name: String(data.get("name") || "").trim(),
      email: String(data.get("email") || "").trim(),
      message: String(data.get("message") || "").trim()
    };

    status.className = "form-status";
    status.textContent = "A enviar mensagem…";
    submit.disabled = true;

    try {
      const response = await fetch("https://dxiz2vvqs4cxkploqr2eydgwiy0rwtva.lambda-url.eu-west-1.on.aws/", {
        method: "POST",
        body: JSON.stringify(payload)
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      form.reset();
      status.className = "form-status success";
      status.textContent = "Mensagem enviada com sucesso. Obrigado pelo contacto.";
    } catch (error) {
      console.error(error);
      status.className = "form-status error";
      status.textContent = "Não foi possível enviar a mensagem. Tenta novamente dentro de alguns instantes.";
    } finally {
      submit.disabled = false;
    }
  });
}
