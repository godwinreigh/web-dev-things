import React from "react";
import "../App.css";

//normal
/*
function HelloWorld(props) {
  return (
    <h1>Hello World {props.name} </h1>
  )
}
*/

//class based component
class HelloWorld extends React.Component {
  render() {
    return (
      <div className="head-container">
        <div className="column1">
          <h1 className="hello"> Hello {this.props.name}</h1>
        </div>
        <div className="column2">
          <h1 className="hello2">This is column 2</h1>
        </div>
      </div>
    );
  }
}

export default HelloWorld;
