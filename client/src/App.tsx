
import { useEffect, useState } from 'react'
import Layout from './Layout'
import {motion} from 'motion/react'
export default function App() {

  const [Data, setData] = useState([])
  const [PercentUsed, setPercentUsed] = useState<number[]>([])

  useEffect(() => {

    const FetchData = async () => {

      const response = await fetch("http://localhost:5000/getdata", {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      })


      if (!response.ok) {
        console.error("An error occured!")
        return

      }

      let data = await response.json()
      if (data?.data) {
        for (let a of data.data) {
          let usedper = (a.used / a.total) * 100;
          setPercentUsed((e) => [...e, Math.floor(usedper)])
        }
        setData(data.data)
      }


    }

    if (Data.length === 0) {
      FetchData()

    }

  }, [Data])

  return (

    <Layout>

    {Data.length > 0 ?   <div className='flex  gap-[20px] p-[20px]'>

        {Data.map((value, index) => {
          return <div key={index} className='flex hover:bg-gray-900 flex-col justify-center gap-[10px] bg-black p-[20px] w-[500px] rounded-lg h-[150px] rounded-lg items-start'>

            <div className='text-white flex w-full items-center gap-[20px]'>
              <img src="./icons/icons8-ssd-48.png" alt="Loading" />

              <p>{value["partition_name"]}</p>



            </div>
            {PercentUsed.map((value, id) => (
              id === index &&

              <div className='w-full bg-white' key={index}>

                <motion.div animate={{ width: [0, `${value}%`] }}  className={` h-[20px] flex bg-blue-500 `}>

                </motion.div>

              </div>
            ))}


            <div className='flex gap-[20px] text-white w-full items-center'>
              <p><span className='text-green-500'>Total</span> {Math.floor(value["total"])}GB</p>
              <p><span className='text-red-500'>Used</span> {Math.floor(value["used"])}GB</p>
              <p><span className='text-yellow-500'>Free</span> {Math.floor(value["free"])}GB</p>
            </div>

          </div>
        })}

      </div> :  
      <div className='w-full h-full flex items-center justify-center'>

        <motion.img src="../icons/loading_spinner.png" animate={{  }}  width={40} height={40} className="mix-blend-screen" alt="" /> 
      
      </div>

      }

    </Layout>

  )
}
