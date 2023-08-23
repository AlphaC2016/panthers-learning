import React, { useState } from 'react';

function App() {

  const [file, setFile] = useState(null)
  const [decompressed, setDecompressed] = useState()
  const [response, setResponse] = useState()

  function getBase64(file) {
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {
      console.log(reader.result);
    };
    reader.onerror = function (error) {
      console.log('Error: ', error);
    };
 }

  const useFile = async () =>{
    if(file){
      setDecompressed(file.name)
      const reader = new FileReader()
      reader.readAsArrayBuffer(file)
      reader.onload = async (e) => {
        const res = await fetch("https://ncnmjwtaooob5dzhmhhv3n52su.apigateway.il-jerusalem-1.oci.customer-oci.com/test/putFile",{
        method: 'PUT',
        headers: {
          'Content-type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        },
        body: e.target.result
      })
      setResponse(await res)
      }
      // await fetch("https://ncnmjwtaooob5dzhmhhv3n52su.apigateway.il-jerusalem-1.oci.customer-oci.com/test/hello")
      //       .then((res)=>res.json()).then((json)=>setResponse(json))
      console.log(file)
      console.log(reader.result)
      
      // getBase64(file)
    }
    
  }

  return (
    <div className="App">
      {!decompressed ? <div><input type='file' onChange={(e) => setFile(e.target.files[0])} />
                            <button onClick={useFile}>use file</button></div> : 
                            <div>
                              <h1>{decompressed}</h1>
                              {console.log(response)}
                              {/* {response !== undefined ? response.map((res)=><div>link: {res.link} / - /  score: {res.score}</div>) : <div>no data</div>} */}
                            </div>}
    </div>
  );
}

export default App;
