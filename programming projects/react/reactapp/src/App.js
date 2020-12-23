import React from "react"; //always needed
import Tweet from "./Tweet";

//first we create component
function Hello() {
  const sayHello = () => {
    console.log("hello");
  };

  //class is className in react
  return (
    <div>
      <h1>Hello React</h1>
      <button onClick={sayHello}>Hello</button>
      <Tweet />
    </div>
  );
}
//end of component
//then we export component
export default Hello;
