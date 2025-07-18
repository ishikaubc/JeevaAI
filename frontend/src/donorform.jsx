import React, { useState } from "react";
import axios from "axios";

const DonorForm = () => {
  const [formData, setFormData] = useState({
    region: "",
    days_since_last_donation: "",
    willing_to_donate: 1,
  });

  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        region: formData.region,
        days_since_last_donation: parseInt(formData.days_since_last_donation),
        willing_to_donate: parseInt(formData.willing_to_donate),
      };
  
      const res = await axios.post("http://localhost:8000/jeevaAI/predict", payload);
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error(err);
      setPrediction("Prediction failed.");
    }
  };
  

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#fff5f5] p-4">
      <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-lg p-8 max-w-md w-full border-t-8 border-[#b30000]">
        <h1 className="text-2xl font-bold text-center text-[#b30000] mb-6">🩸 Donor Availability Predictor</h1>

        <label className="block mb-2 text-[#800000] font-semibold">Region</label>
        <input
          type="text"
          name="region"
          value={formData.region}
          onChange={handleChange}
          className="w-full p-2 mb-4 rounded bg-[#ffe6e6] border border-[#b30000] focus:outline-none focus:ring-2 focus:ring-[#b30000]"
        />

        <label className="block mb-2 text-[#800000] font-semibold">Days Since Last Donation</label>
        <input
          type="number"
          name="days_since_last_donation"
          value={formData.days_since_last_donation}
          onChange={handleChange}
          className="w-full p-2 mb-4 rounded bg-[#ffe6e6] border border-[#b30000] focus:outline-none focus:ring-2 focus:ring-[#b30000]"
        />

        <label className="block mb-2 text-[#800000] font-semibold">Willing to Donate</label>
        <select
          name="willing_to_donate"
          value={formData.willing_to_donate}
          onChange={handleChange}
          className="w-full p-2 mb-6 rounded bg-[#ffe6e6] border border-[#b30000] focus:outline-none focus:ring-2 focus:ring-[#b30000]"
        >
          <option value={1}>Yes</option>
          <option value={0}>No</option>
        </select>

        <button
          type="submit"
          className="bg-[#b30000] text-white w-full py-2 rounded font-semibold hover:bg-[#990000] transition-colors"
        >
          Predict
        </button>

        {prediction !== null && (
          <div className="mt-6 p-4 bg-[#ffe6e6] text-center text-[#800000] font-semibold rounded shadow-inner">
            Prediction: {prediction === 1 ? "Available" : prediction === 0 ? "Not Available" : prediction}
          </div>
        )}
      </form>
    </div>
  );
};

export default DonorForm;
