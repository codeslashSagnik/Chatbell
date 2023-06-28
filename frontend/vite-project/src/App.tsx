import { useState } from 'react'
import Controller from './components/Controller'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <div className=""><Controller/></div>
  
      </div>
      
    </>
  )
}

export default App
