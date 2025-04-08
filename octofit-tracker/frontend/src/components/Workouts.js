import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/api/workouts`)
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Workouts</h1>
        <ul className="list-group">
          {workouts.map(workout => (
            <li key={workout.id} className="list-group-item">{workout.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Workouts;