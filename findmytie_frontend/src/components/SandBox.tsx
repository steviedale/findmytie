import React from "react";

type Props = {};

const SandBox = (props: Props) => {
  return (
    // <button type="button" className="btn btn-secondary">
    //   <svg
    //     xmlns="http://www.w3.org/2000/svg"
    //     width="24"
    //     height="24"
    //     fill="currentColor"
    //     // fill="#111111"
    //     className="bi bi-plus"
    //     viewBox="0 0 16 16"
    //     // data-darkreader-inline-fill=""
    //     // style="--darkreader-inline-fill: currentColor;"
    //   >
    //     <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"></path>
    //   </svg>
    // </button>
    <div
      className="icon-demo mb-4 border rounded-3 d-flex align-items-center justify-content-center p-3 py-6"
      style={{ fontSize: "10em"}}
      role="img"
      aria-label="Plus - large preview"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        fill="currentColor"
        className="bi bi-plus"
        viewBox="0 0 16 16"
        data-darkreader-inline-fill=""
        // style="--darkreader-inline-fill: currentColor;"
      >
        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"></path>
      </svg>
    </div>
  );
};

export default SandBox;
