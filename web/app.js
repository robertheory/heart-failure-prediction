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

const EXAMPLE_1 = {
  Age: 45,
  Sex: "M",
  ChestPainType: "ATA",
  RestingBP: 80,
  Cholesterol: 1,
  FastingBS: 0,
  RestingECG: "Normal",
  MaxHR: 100,
  ExerciseAngina: "N",
  Oldpeak: 1.5,
  ST_Slope: "Flat"
};

const EXAMPLE_2 = {
  Age: 60,
  Sex: "F",
  ChestPainType: "ASY",
  RestingBP: 85,
  Cholesterol: 1,
  FastingBS: 0,
  RestingECG: "LVH",
  MaxHR: 110,
  ExerciseAngina: "Y",
  Oldpeak: 2.0,
  ST_Slope: "Down"
};

function fillFormWithExample(example) {
  const form = document.getElementById('heartForm');
  form.Age.value = example.Age;
  form.Sex.value = example.Sex;
  form.ChestPainType.value = example.ChestPainType;
  form.RestingBP.value = example.RestingBP;
  form.Cholesterol.value = example.Cholesterol;
  form.FastingBS.value = example.FastingBS;
  form.RestingECG.value = example.RestingECG;
  form.MaxHR.value = example.MaxHR;
  form.ExerciseAngina.value = example.ExerciseAngina;
  form.Oldpeak.value = example.Oldpeak;
  form.ST_Slope.value = example.ST_Slope;
}

document.getElementById('heartForm').addEventListener('submit', handleFormSubmit);

document.getElementById('loadExample1').addEventListener('click', function () {
  fillFormWithExample(EXAMPLE_1);
});

document.getElementById('loadExample2').addEventListener('click', function () {
  fillFormWithExample(EXAMPLE_2);
});

document.getElementById('clearForm').addEventListener('click', function () {
  document.getElementById('heartForm').reset();
});