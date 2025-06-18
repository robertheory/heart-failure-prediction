
function getFormData(form) {
  return {
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
}

function showAlert(type, message) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = `
    <div class="alert alert-${type}" role="alert">
      ${message}
    </div>
  `;
}

function showResultWithBack(type, message) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = `
    <div class="alert alert-${type}" role="alert">
      ${message}
    </div>
    <button id="backBtn" class="btn btn-secondary w-100 mt-3">Voltar</button>
  `;
  document.getElementById('backBtn').onclick = restoreForm;
}

function handlePredictionResult(result) {
  if (result['heart_disease'] === true) {
    showResultWithBack('danger', '<strong>Alerta:</strong> Indícios de doença cardíaca detectados.');
  } else if (result['heart_disease'] === false) {
    showResultWithBack('success', '<strong>Parabéns!</strong> Não foram detectados indícios de doença cardíaca.');
  } else {
    showResultWithBack('warning', 'Resultado inesperado. Por favor, tente novamente.');
  }
}

async function submitPrediction(data) {
  const response = await fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (!response.ok) {
    throw new Error('Erro ao conectar ao servidor.');
  }

  return response.json();
}

function restoreForm() {
  document.getElementById('heartForm').reset();
  document.getElementById('heartForm').style.display = 'block';
  document.getElementById('result').innerHTML = '';
}

async function handleFormSubmit(event) {
  event.preventDefault();
  showAlert('info', 'Processando...');
  document.getElementById('heartForm').style.display = 'none';

  const form = event.target;
  const data = getFormData(form);

  try {
    const result = await submitPrediction(data);
    handlePredictionResult(result);
  } catch (error) {
    showResultWithBack('danger', `Erro ao processar a requisição: ${error.message}`);
  }
}

document.getElementById('heartForm').addEventListener('submit', handleFormSubmit);