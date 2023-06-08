import React, { useState, useEffect } from "react";
import { TaskList } from "../TaskList/TaskList";
import { TaskCounter } from "../TaskCounter/TaskCounter";
import { Modal } from "../Modal/Modal";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [openModal, setOpenModal] = useState(false);

  const handleOpenModal = () => {
    setOpenModal(!openModal);
    // console.log(openModal);
  };

  useEffect(() => {
    fetch("http://localhost:5000/api/tasks")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setTasks(data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  // Update tasks useEffect
  useEffect(() => {
    console.log("tasks updated");
  }, [tasks]);

  const createTask = () => {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const task = {
      id: tasks[tasks.length - 1].id + 1,
      title: title,
      description: description,
    };

    console.log(task);

    fetch("http://localhost:5000/api/task", {
      method: "POST",
      body: JSON.stringify(task),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .catch((error) => {
        console.log(error);
      });
    setTasks([...tasks, task]);
    setOpenModal(!openModal);
  };

  return (
    <div className="App">
      <div className="p-2">
        <h1>Tasks</h1>
        <hr />
        <TaskCounter tasks={tasks} />
      </div>
      <div className="d-flex flex-row-reverse m-3">
        <button className="btn btn-primary" onClick={handleOpenModal}>
          {" "}
          + Nueva Tarea{" "}
        </button>
      </div>
      <div className="p-3">
        <TaskList tasks={tasks} setTasks={setTasks} />
      </div>

      {!!openModal && (
        <Modal>
          <div className="bg-white card" style={{ width: "500px" }}>
            <div className="text-end mx-auto justify-content-space d-flex p-3 card-header">
              <h3>Nueva Tarea</h3>
              <div className="pr-3"></div>
            </div>
            <div>
              <form className="p-3">
                <div className="mb-3">
                  <label htmlFor="title" className="form-label">
                    Titulo
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="title"
                    placeholder="Titulo de la tarea"
                  />

                  <label htmlFor="description" className="form-label">
                    Descripcion
                  </label>
                  <textarea
                    className="form-control"
                    id="description"
                    rows="3"
                    placeholder="Descripcion de la tarea"
                  ></textarea>
                </div>
              </form>
            </div>
            <div className="d-flex justify-content-between text-end p-3">
              <button className="btn btn-primary text-end" onClick={createTask}>
                Crear
              </button>

              <button
                className="btn btn-danger align-middle"
                onClick={handleOpenModal}
              >
                Cerrar
              </button>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
}

export default App;
