import { useState } from "react";
import Header from "./components/Header";
import PurchaseForm from "./components/PurchaseForm";
import ReceiptView from "./components/ReceiptView";
import { purchaseTickets } from "./api";

function App() {
  const [receipt, setReceipt] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handlePurchase = async (data) => {
    setIsLoading(true);
    setError(null);
    try {
      const result = await purchaseTickets(data);
      setReceipt(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleBack = () => {
    setReceipt(null);
    setError(null);
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1 flex items-center justify-center p-4">
        {error && (
          <div className="max-w-md w-full mb-4 p-4 bg-red-900/50 border border-red-500 text-red-200 rounded-lg text-center">
            ⚠️ {error}
          </div>
        )}

        {receipt ? (
          <ReceiptView receipt={receipt} onBack={handleBack} />
        ) : (
          <PurchaseForm onSubmit={handlePurchase} isLoading={isLoading} />
        )}
      </main>
    </div>
  );
}

export default App;