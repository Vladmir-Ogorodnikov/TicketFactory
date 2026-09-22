export default function ReceiptView({ receipt, onBack }) {
  return (
    <div className="max-w-md mx-auto p-6 bg-gray-800 rounded-lg shadow-lg border border-yellow-600/50 relative overflow-hidden">
      {/* Декоративная "перфорация" билета */}
      <div className="absolute top-0 left-0 w-full h-4 bg-gray-900" style={{ maskImage: "radial-gradient(circle, transparent 6px, black 6px)", maskSize: "20px 20px", maskPosition: "top" }}></div>

      <div className="text-center mb-6 pt-4">
        <h2 className="text-2xl font-bold text-yellow-500">ВАШ ЧЕК</h2>
        <p className="text-xs text-gray-400 mt-1">ID: {receipt.receipt_id}</p>
      </div>

      <div className="space-y-3 mb-6">
        {receipt.tickets.map((ticket, idx) => (
          <div key={idx} className="flex justify-between items-center bg-gray-700/50 p-3 rounded border border-gray-600">
            <div>
              <span className="font-bold text-yellow-400">{ticket.ticket_type}</span>
              <span className="text-gray-400 text-sm ml-2">Ряд {ticket.row}, Место {ticket.number}</span>
            </div>
            <span className="font-mono">{ticket.price}$</span>
          </div>
        ))}
      </div>

      <div className="border-t border-dashed border-gray-600 pt-4 flex justify-between items-center">
        <span className="text-lg font-semibold">ИТОГО:</span>
        <span className="text-2xl font-bold text-yellow-500">{receipt.total_amount}$</span>
      </div>
      <p className="text-xs text-gray-500 text-center mt-4">{receipt.created_at}</p>

      <button onClick={onBack} className="w-full mt-6 bg-gray-700 hover:bg-gray-600 text-white font-semibold py-2 rounded transition">
        Купить ещё
      </button>
    </div>
  );
}