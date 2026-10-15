import { useEffect, useState } from "react";

const App = () => {
  const [data,setData] = useState(null)

  useEffect(()=>{
    fetch("http://127.0.0.1:8000/").then(response => response.json()).then(json =>setData(json))
  },[])

  return (
    <div>
      <h1>API Connect</h1>
      {
        data ? (
          <p>
            Message: {data.message}
          </p>
        ): <p>Loading...</p>
      }
    </div>
  )
}

export default App