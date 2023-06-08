import "../Modal/Modal.css";
import ReactDOM from "react-dom";

function EditModal({ children }) {
  return ReactDOM.createPortal(
    <div className="ModalBackground">{children}</div>,
    document.getElementById("modal")
  );
}

export { EditModal };
