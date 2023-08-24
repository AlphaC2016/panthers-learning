import React, { useState } from 'react';


function App() {

  const [file, setFile] = useState(null)
  const [decompressed, setDecompressed] = useState()
  const [response, setResponse] = useState()
  const [state, setState] = useState(0)

  const background = () =>{
    
    <div className="d-flex flex-column justify-content-center w-100 h-100"></div>
  }

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
      setState(1)
      reader.onload = async (e) => {
        const res = await fetch("https://ncnmjwtaooob5dzhmhhv3n52su.apigateway.il-jerusalem-1.oci.customer-oci.com/test/putFile",{
        method: 'PUT',
        headers: {
          'Content-type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        },
        body: e.target.result

      })
      setResponse(await res)
      setState(2)
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
      {/* {background div} */}
      {background()}
      {/* title */}
      <div className='Header'><h1>Dive In</h1></div>

      <button className='ExtentionButton' onClick={()=>{}}>Add Extention</button>

      <div>
        <input type='file' onChange={(e) => setFile(e.target.files[0])} />
        <button onClick={useFile}>use file</button>
        {state === 1 ? <div className="ring">
                          Loading
                          <span></span>
                        </div> : <></>}
        {console.log(response)}
        {response ? response.map((res)=><div>link: {res.link} / - /  score: {res.score}</div>) : <></>}
        
      </div>
      
      {/* {!decompressed ? <div><input type='file' onChange={(e) => setFile(e.target.files[0])} />
                            <button onClick={useFile}>use file</button></div> : 
                            <div>
                              <h1>{state === 1 ? <div class="ring">
                                  Loading
                                  <span></span>
                                </div> : decompressed}</h1>
                              {console.log(response)}
                              {/* {response !== undefined ? response.map((res)=><div>link: {res.link} / - /  score: {res.score}</div>) : <div>no data</div>} }
                            </div>} */}
    </div>
  );
}

export default App;
