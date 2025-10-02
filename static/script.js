document.getElementById("predict-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const features = [
    parseFloat(document.getElementById("f1").value),
    parseFloat(document.getElementById("f2").value),
    parseFloat(document.getElementById("f3").value),
  ];

  const response = await fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ features }),
  });

  const data = await response.json();
  document.getElementById("result").textContent = `Prediction: ${data.prediction}`;
});