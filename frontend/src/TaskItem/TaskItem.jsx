import React from "react";
import "./TaskItem.css";
import { useState } from "react";
import { EditModal } from "../EditModal/EditModal";

function TaskItem({
  id,
  title,
  description,
  done,
  checkTask,
  onDelete,
  setTasks,
  tasks,
  setTaskDone,
}) {
  const [openModal, setOpenModal] = useState(false);

  const handleOpenModal = () => {
    setOpenModal(!openModal);
  };

  const modalEdit = (id) => {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const task = {
      id,
      title: title,
      description: description,
    };

    console.log(task);

    fetch(`http://localhost:5001/api/task/${id}`, {
      method: "PUT",
      body: JSON.stringify(task),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then(async (data) => {
        console.log(data);
        const tasks = await fetch("http://localhost:5001/api/tasks")
          .then((res) => res.json())
          .then((data) => data);
        setTasks(tasks);
        handleOpenModal();
        setTaskDone(tasks.every((task) => task.done === true));
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <li
      className={`list-group-item list-group-item-action justify-content-between align-items-stretch d-flex flex-row ${
        done ? "list-group-item-dark" : "list-group-item-light"
      }`}
      key={id}
    >
      <div className="w-50">
        <h5 className={`mb-1`}>{title}</h5>
        {/* <small>{createdAt}</small> */}

        <p className={`mb-1`}>{description}</p>
        <small>
          <i
            className="p-2 fs-5 text-success bi bi-pencil-square"
            onClick={handleOpenModal}
          ></i>
        </small>
        <small>
          <i
            onClick={() => onDelete(id)}
            className="p-2 fs-5 text-danger bi bi-trash-fill pe-auto"
          ></i>
        </small>
      </div>

      <div className="align-middle p-2">
        <small className="mt-5">
          <i
            onClick={() => checkTask(id)}
            className={`text-success fs-1 bi ${
              done ? "bi-check-circle-fill" : "bi-check-circle"
            }`}
          ></i>
        </small>
      </div>

      {/* Modal Edit  */}
      {!!openModal && (
        <EditModal>
          <div className="bg-white card" style={{ width: "500px" }}>
            <div className="text-end mx-auto justify-content-space d-flex p-3 card-header">
              <h3>Editar Tarea</h3>
              <div className="pr-3"></div>
            </div>
            <div>
              <form className="p-3">
                <div className="mb-3">
                  <input type="hidden" id="id" defaultValue={id} />
                  <label htmlFor="title" className="form-label">
                    Titulo
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="title"
                    defaultValue={title}
                    placeholder="Titulo de la tarea"
                  />

                  <label htmlFor="description" className="form-label">
                    Descripcion
                  </label>
                  <textarea
                    className="form-control"
                    id="description"
                    rows="3"
                    defaultValue={description}
                    placeholder="Descripcion de la tarea"
                  ></textarea>
                </div>
              </form>
            </div>
            <div className="d-flex justify-content-between text-end p-3">
              <button
                className="btn btn-primary text-end"
                onClick={() => modalEdit(id)}
              >
                Editar
              </button>

              <button
                className="btn btn-danger align-middle"
                onClick={handleOpenModal}
              >
                Cerrar
              </button>
            </div>
          </div>
        </EditModal>
      )}
    </li>
  );
}

export default TaskItem;
