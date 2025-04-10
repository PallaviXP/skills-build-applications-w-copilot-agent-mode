import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/api/v1/users/`)
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