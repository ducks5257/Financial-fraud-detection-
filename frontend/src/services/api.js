const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ||
  "https://financial-fraud-detector-api.onrender.com";

export const predictTransaction = async (transactionData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(transactionData),
    });

    if (!response.ok) {
      if (response.status === 422) {
        throw new Error(
          "Validation Error: Please check that all 30 inputs are valid numbers."
        );
      }

      if (response.status === 500) {
        throw new Error(
          "Backend Error: The ML model encountered an error."
        );
      }

      throw new Error(
        `Error: Received status code ${response.status}`
      );
    }

    return await response.json();
  } catch (error) {
    if (
      error.name === "TypeError" &&
      error.message === "Failed to fetch"
    ) {
      throw new Error(
        "Network Error: Cannot connect to backend. Check the deployed API URL and CORS configuration."
      );
    }

    throw error;
  }
};