document.getElementById('heartForm').addEventListener('submit', async function (e) {
  e.preventDefault();
  const form = e.target;
  const data = {
    Age: Number(form.Age.value),
    Sex: form.Sex.value,
    ChestPainType: form.ChestPainType.value,
    RestingBP: Number(form.RestingBP.value),
    Cholesterol: Number(form.Cholesterol.value),
    FastingBS: Number(form.FastingBS.value),
    RestingECG: form.RestingECG.value,
    MaxHR: Number(form.MaxHR.value),
    ExerciseAngina: form.ExerciseAngina.value,
    Oldpeak: Number(form.Oldpeak.value),
    ST_Slope: form.ST_Slope.value
  };

  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = '';

  try {
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error('Erro ao conectar ao servidor.');
    }

    const result = await response.json();

    if (result['heart disease'] === true) {
      resultDiv.innerHTML = `
        <div class="alert alert-danger" role="alert">
          <strong>Alerta:</strong> Indícios de doença cardíaca detectados.
        </div>
      `;
    } else if (result['heart disease'] === false) {
      resultDiv.innerHTML = `
        <div class="alert alert-success" role="alert">
          <strong>Parabéns!</strong> Não foram detectados indícios de doença cardíaca.
        </div>
      `;
    } else {
      resultDiv.innerHTML = `
        <div class="alert alert-warning" role="alert">
          Resultado inesperado. Por favor, tente novamente.
        </div>
      `;
    }
  } catch (error) {
    resultDiv.innerHTML = `
      <div class="alert alert-danger" role="alert">
        Erro ao processar a requisição: ${error.message}
      </div>
    `;
  }
});