document.getElementById('generateBtn')?.addEventListener('click', async () => {
  const text = document.getElementById('userInput').value;
  const output = document.getElementById('aiOutput');
  if (!text || !text.trim()) {
    output.innerText = '⚠️ Please type a prompt first.';
    return;
  }
  output.innerText = '🤖 Engineer_Abuibraheem_AI is thinking...';
  try {
    const resp = await fetch('/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    const data = await resp.json();
    if (data.response) {
      output.innerText = '🤖 Engineer_Abuibraheem_AI: ' + data.response;
    } else {
      output.innerText = '❌ Error: ' + (data.error || 'No response');
    }
  } catch (err) {
    output.innerText = '⚠️ Connection error. Check console.';
    console.error(err);
  }
});
