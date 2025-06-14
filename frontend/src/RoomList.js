import React, { useEffect, useState } from 'react';
import API from '../api';

function RoomList() {
  const [rooms, setRooms] = useState([]);

  useEffect(() => {
    API.get('rooms/')
      .then(res => setRooms(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Available Rooms</h2>
      <ul>
        {rooms.map(room => (
          <li key={room.id}>{room.name} - Capacity: {room.capacity}</li>
        ))}
      </ul>
    </div>
  );
}

export default RoomList;
