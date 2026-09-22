const API_URL = "http://localhost:8000";

export const checkHealth = async () => {
  const response = await fetch(`${API_URL}/health`);
  if (!response.ok) throw new Error("API недоступен");
  return response.json();
};

export const purchaseTickets = async (data) => {
  const response = await fetch(`${API_URL}/tickets/purchase`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || errorData.Error || "Ошибка при покупке");
  }
  return response.json();
};

export const getReceipt = async (receiptId) => {
  const response = await fetch(`${API_URL}/tickets/${receiptId}`);
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.Error || "Чек не найден");
  }
  return response.json();
};