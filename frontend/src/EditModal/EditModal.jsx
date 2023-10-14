import "./EditModal.css";
import ReactDOM from "react-dom";

function EditModal({ children }) {
  return ReactDOM.createPortal(
    <div className="EditModalBg">{children}</div>,
    document.getElementById("modal")
  );
}

export { EditModal };
