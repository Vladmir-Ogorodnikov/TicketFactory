import { useState } from "react";
import { v4 as uuidv4 } from "uuid"; // Установи: npm install uuid

export default function PurchaseForm({ onSubmit, isLoading }) {
  const [userId, setUserId] = useState(uuidv4());
  const [age, setAge] = useState(18);
  const [isVip, setIsVip] = useState(false);
  const [seats, setSeats] = useState([{ row: 1, number: 1 }]);

  const addSeat = () => setSeats([...seats, { row: 1, number: 1 }]);

  const updateSeat = (index, field, value) => {
    const newSeats = [...seats];
    newSeats[index][field] = parseInt(value) || 1;
    setSeats(newSeats);
  };

  const removeSeat = (index) => {
    if (seats.length > 1) {
      setSeats(seats.filter((_, i) => i !== index));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      user_id: userId,
      seats: seats.map(s => [s.row, s.number]),
      age: parseInt(age),
      vip_flag: isVip,
    });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-6 bg-gray-800 rounded-lg shadow-lg border border-gray-700">
      <h2 className="text-lg font-semibold mb-4 text-yellow-500">Покупка билетов</h2>

      <div className="mb-4">
        <label className="block text-sm text-gray-400 mb-1">User ID</label>
        <div className="flex gap-2">
          <input type="text" value={userId} onChange={(e) => setUserId(e.target.value)} className="flex-1 bg-gray-700 border border-gray-600 rounded px-3 py-2 text-sm" readOnly />
          <button type="button" onClick={() => setUserId(uuidv4())} className="px-3 py-2 bg-gray-600 rounded hover:bg-gray-500 text-sm">🔄</button>
        </div>
      </div>

      <div className="mb-4">
        <label className="block text-sm text-gray-400 mb-1">Возраст</label>
        <input type="number" value={age} onChange={(e) => setAge(e.target.value)} min="1" required className="w-full bg-gray-700 border border-gray-600 rounded px-3 py-2" />
      </div>

      <div className="mb-4">
        <label className="block text-sm text-gray-400 mb-2">Места</label>
        {seats.map((seat, index) => (
          <div key={index} className="flex gap-2 mb-2 items-center">
            <input type="number" placeholder="Ряд" value={seat.row} onChange={(e) => updateSeat(index, "row", e.target.value)} min="1" required className="w-20 bg-gray-700 border border-gray-600 rounded px-2 py-2 text-center" />
            <span className="text-gray-500">:</span>
            <input type="number" placeholder="Место" value={seat.number} onChange={(e) => updateSeat(index, "number", e.target.value)} min="1" required className="w-20 bg-gray-700 border border-gray-600 rounded px-2 py-2 text-center" />
            {seats.length > 1 && (
              <button type="button" onClick={() => removeSeat(index)} className="text-red-400 hover:text-red-300 px-2">✕</button>
            )}
          </div>
        ))}
        <button type="button" onClick={addSeat} className="text-sm text-yellow-500 hover:text-yellow-400 mt-1">+ Добавить место</button>
      </div>

      <div className="mb-6 flex items-center gap-2">
        <input type="checkbox" id="vip" checked={isVip} onChange={(e) => setIsVip(e.target.checked)} className="w-4 h-4 accent-yellow-500" />
        <label htmlFor="vip" className="text-sm">VIP зал</label>
      </div>

      <button type="submit" disabled={isLoading} className="w-full bg-yellow-600 hover:bg-yellow-500 text-white font-bold py-3 rounded transition disabled:opacity-50 disabled:cursor-not-allowed">
        {isLoading ? "Обработка..." : "Купить билеты"}
      </button>
    </form>
  );
}