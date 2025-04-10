import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(`https://effective-journey-6v49wjvrr75c5j5r-8000.app.github.dev\/api\/users\/`)
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Users</h1>
        <ul className="list-group">
          {users.map(user => (
            <li key={user.id} className="list-group-item">{user.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Users;