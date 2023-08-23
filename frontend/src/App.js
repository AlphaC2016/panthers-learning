import React, { useState } from 'react';

function App() {

  const [file, setFile] = useState(null)
  const [decompressed, setDecompressed] = useState()
  const [response, setResponse] = useState()

  const useFile = async () =>{
    if(file){
      setDecompressed(file.name)
      await fetch("https://ncnmjwtaooob5dzhmhhv3n52su.apigateway.il-jerusalem-1.oci.customer-oci.com/test/hello")
            .then((res)=>res.json()).then((json)=>setResponse(json))
    }
    
  }

  return (
    <div className="App">
      {!decompressed ? <div><input type='file' onChange={(e) => setFile(e.target.files[0])} />
                            <button onClick={useFile}>use file</button></div> : 
                            <div>
                              {/* <h1>{decompressed}</h1> */}
                              {console.log(response)}
                              {response !== undefined ? response.map((res)=><div>link: {res.link} / - /  score: {res.score}</div>) : <div>no data</div>}
                            </div>}
    </div>
  );
}

export default App;
