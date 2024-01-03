#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error occurred: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  } else {
    const todosData = JSON.parse(body);

    // Create a map to store the count of completed tasks for each user
    const completedTasksByUser = new Map();

    // Iterate through the todos and count completed tasks for each user
    todosData.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksByUser.set(userId, (completedTasksByUser.get(userId) || 0) + 1);
      }
    });

    // Print users with completed tasks
    completedTasksByUser.forEach((completedTasks, userId) => {
      console.log(`${userId}: ${completedTasks}`);
    });
  }
});
