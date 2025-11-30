// Simple interactions: submit contact form via fetch to /contact
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const status = document.getElementById('contactStatus');
      status.innerText = 'Sending...';
      const payload = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value
      };
      try {
        const resp = await fetch('/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const data = await resp.json();
        if (data.success) {
          status.innerText = 'Message sent! I will reply soon.';
          form.reset();
        } else {
          status.innerText = 'Failed to send: ' + (data.error || 'Unknown');
        }
      } catch (err) {
        status.innerText = 'Error sending message. Check console.';
        console.error(err);
      }
    });
  }
});
