import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/api/teams`)
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Teams</h1>
        <ul className="list-group">
          {teams.map(team => (
            <li key={team.id} className="list-group-item">{team.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Teams;