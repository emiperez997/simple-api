import TaskItem from "../TaskItem/TaskItem";

function TaskList({ tasks, setTasks }) {
  const onDelete = (id) => {
    fetch(`http://localhost:5000/api/task/${id}`, {
      method: "DELETE",
    })
      .then((res) => res.json())
      .then(async (data) => {
        console.log(data);
        const tasks = await fetch("http://localhost:5000/api/tasks")
          .then((res) => res.json())
          .then((data) => data.data);
        setTasks(tasks);
      })
      .catch((err) => console.log(err));
  };

  const checkTask = (id) => {
    const task = tasks.find((task) => task.id === id);

    if (task.done) {
      fetch(`http://localhost:5000/api/task/undone/${id}`, {
        header: {
          ContentType: "application/json",
        },
      })
        .then((res) => res.json())
        .then(async (data) => {
          console.log(data);
          const tasks = await fetch("http://localhost:5000/api/tasks")
            .then((res) => res.json())
            .then((data) => data.data);
          setTasks(tasks);
        })
        .catch((err) => console.log(err));
    } else {
      fetch(`http://localhost:5000/api/task/done/${id}`, {
        header: {
          ContentType: "application/json",
        },
      })
        .then((res) => res.json())
        .then(async (data) => {
          console.log(data);
          const tasks = await fetch("http://localhost:5000/api/tasks")
            .then((res) => res.json())
            .then((data) => data.data);
          setTasks(tasks);
        })
        .catch((err) => console.log(err));
    }
  };

  return (
    <ul className="list-group">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          id={task.id}
          title={task.title}
          description={task.description}
          done={task.done}
          checkTask={checkTask}
          onDelete={onDelete}
          setTasks={setTasks}
          tasks={tasks}
        />
      ))}
    </ul>
  );
}

export { TaskList };
