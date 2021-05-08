import React from "react"
import ReactDom from "react-dom"

function Greet(){
  return (
    <div>
      <h1>Hello</h1>
      <h1>Hello</h1>
      <h1>Hello</h1>
    </div>
  );
}

ReactDom.render(<Greet/>,document.getElementById("root"));
