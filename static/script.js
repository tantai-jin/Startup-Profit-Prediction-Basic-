document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const rndInput = document.getElementById("rnd_spend");
    const adminInput = document.getElementById("admin_cost");
    const marketingInput = document.getElementById("marketing_spend");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevent form from reloading the page

        const rndSpend = parseFloat(rndInput.value);
        const adminCost = parseFloat(adminInput.value);
        const marketingSpend = parseFloat(marketingInput.value);

        // Make POST request to Flask backend
        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    rnd_spend: rndSpend,
                    admin_cost: adminCost,
                    marketing_spend: marketingSpend,
                }),
            });

            const data = await response.json();

            if (data.success) {
                resultDiv.textContent = `Predicted Profit: ${data.predicted_profit}`;
            } else {
                resultDiv.textContent = `Error: ${data.error}`;
            }
        } catch (error) {
            resultDiv.textContent = `Error: ${error.message}`;
        }
    });
});
