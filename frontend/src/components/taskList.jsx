import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    axios.get('http://localhost:5000/tasks')
      .then(response => {
        setTasks(response.data);
        setLoading(false);
        setError(false);
      })
      .catch(error => {
        console.error('There was an error fetching the tasks!', error);
        setLoading(false);
        setError('Failed to fetch tasks. Please try again later.');
      });
  }, []);
  if (tasks.length === 0) return <div>No tasks found.</div>;
  if (error) return <div> {error} </div>;
  if (loading) return <div>Loading...</div>;



  // Основной рендеринг
  return (
    <div>
      <h1>Task List</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.title} - {task.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;