// Função para coletar dados do formulário e converter para o formato esperado
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

// Função para exibir alertas Bootstrap
function showAlert(type, message) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = `
    <div class="alert alert-${type}" role="alert">
      ${message}
    </div>
  `;
}

// Função para processar a resposta da API
function handlePredictionResult(result) {
  if (result['heart_disease'] === true) {
    showAlert('danger', '<strong>Alerta:</strong> Indícios de doença cardíaca detectados.');
  } else if (result['heart_disease'] === false) {
    showAlert('success', '<strong>Parabéns!</strong> Não foram detectados indícios de doença cardíaca.');
  } else {
    showAlert('warning', 'Resultado inesperado. Por favor, tente novamente.');
  }
}

// Função para enviar os dados para a API
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

// Função principal de manipulação do formulário
async function handleFormSubmit(event) {
  event.preventDefault();
  showAlert('info', 'Processando...');

  const form = event.target;
  const data = getFormData(form);

  try {
    const result = await submitPrediction(data);
    handlePredictionResult(result);
  } catch (error) {
    showAlert('danger', `Erro ao processar a requisição: ${error.message}`);
  }
}

// Adiciona o listener ao formulário
document.getElementById('heartForm').addEventListener('submit', handleFormSubmit);