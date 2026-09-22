import { useState, useEffect } from "react";
import { checkHealth } from "../api";

export default function Header() {
  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => {
    checkHealth()
      .then(() => setIsOnline(true))
      .catch(() => setIsOnline(false));
  }, []);

  return (
    <header className="flex items-center justify-between p-4 bg-gray-800 border-b border-gray-700">
      <h1 className="text-xl font-bold text-yellow-500">🎬 Cinema Booking</h1>
      <div className="flex items-center gap-2 text-sm">
        <span className={`w-3 h-3 rounded-full ${isOnline ? "bg-green-500" : "bg-red-500"}`}></span>
        <span>{isOnline ? "API Online" : "API Offline"}</span>
      </div>
    </header>
  );
}