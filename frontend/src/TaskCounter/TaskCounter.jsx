function TaskCounter({ tasks }) {
  return (
    // Bootstrap Counter
    <div className="d-flex fs-4 flex-row justify-content-evenly">
      <div className="">
        <h4>Total Tareas:</h4>
        <h4>Tareas Completadas:</h4>
        <h4>Tareas Pendientes:</h4>
      </div>
      <div className="d-flex fs-5 flex-column">
        <p className="badge bg-secondary">{tasks.length}</p>
        <p className="badge bg-success">
          {tasks.filter((task) => task.done === true).length}
        </p>
        <p className="badge bg-primary">
          {tasks.filter((task) => task.done === false).length}
        </p>
      </div>
    </div>
  );
}

export { TaskCounter };
