import React, { useState } from 'react';
import API from '../api';

function ReservationForm() {
  const [data, setData] = useState({ room: '', date: '', time: '' });

  const handleSubmit = (e) => {
    e.preventDefault();
    API.post('reservations/', data)
      .then(res => alert('Reserved successfully!'))
      .catch(err => console.error(err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Room ID" onChange={e => setData({...data, room: e.target.value})} />
      <input placeholder="Date" onChange={e => setData({...data, date: e.target.value})} />
      <input placeholder="Time" onChange={e => setData({...data, time: e.target.value})} />
      <button type="submit">Reserve</button>
    </form>
  );
}

export default ReservationForm;
