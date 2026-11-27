const campoQuantita = document.getElementById("quantita-demo");
const pulsanteCalcola = document.getElementById("calcola-demo");
const risultatoDemo = document.getElementById("risultato-demo");

function euro(importo) {
  return importo.toFixed(2).replace(".", ",") + " €";
}

pulsanteCalcola.addEventListener("click", function () {
  const quantita = campoQuantita.valueAsNumber;

  if (!Number.isInteger(quantita) || quantita <= 0) {
    risultatoDemo.classList.add("errore");
    risultatoDemo.textContent = "Inserisci una quantità intera maggiore di zero.";
    return;
  }

  const prezzoUnitario = 4;
  const subtotale = prezzoUnitario * quantita;
  let sconto = 0;
  let messaggioSconto = "Sconto non applicato.";

  if (quantita >= 10) {
    sconto = subtotale * 0.10;
    messaggioSconto = "Sconto del 10% applicato.";
  } else {
    sconto = 0;
  }

  const prodottiDopoSconto = subtotale - sconto;
  risultatoDemo.classList.remove("errore");
  risultatoDemo.textContent = messaggioSconto
    + " Prodotti dopo lo sconto: " + euro(prodottiDopoSconto) + ".";
});
