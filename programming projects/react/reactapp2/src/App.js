import React from "react";
import "./App.css";
import Helloworld from "./Components/Helloworld";
import Basiclayout from "./Components/Basiclayout";

//should be have one only container
//also always rename your component starting capital letters

function App() {
  return (
    <div>
      <Helloworld name="asdn" />
      <Basiclayout />
    </div>
  );
}
export default App;
/*
//1. basic
//2. how to pass information
/*
======
new
======
*/

