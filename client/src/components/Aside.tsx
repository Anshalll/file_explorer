
import { motion } from "motion/react"

export default function Aside() {

  const BasicFiles = [
    {
        "name": "Desktop",
        "path": "",
        "icon": "./icons/icons8-desktop-folder-48.png"
    },
    {
        "name": "Documents",
        "path": "",
        "icon": "./icons/icons8-documents-48.png"
    },
    {
        "name": "Downloads",
        "path": "",
        "icon": "./icons/icons8-download-48.png"
    },
    {
        "name": "Movies",
        "path": "",
        "icon": "./icons/icons8-movies-folder-48.png"
    },
    {
        "name": "Songs",
        "path": "",
        "icon": "./icons/icons8-mp3-48.png"
    },
    {
        "name": "Videos",
        "path": "",
        "icon": "./icons/icons8-video-file-48.png"
    }
  ]

  return (
    <aside className='w-[20%] h-full bg-black p-[20px] gap-[20px] flex flex-col  overflow-y-auto'>
        {BasicFiles.map((value, index) => {
            return <motion.button   whileHover={{
                scale: 1.1,
                transition: { duration: 0.2 , ease: 'easeInOut'}
              }}  key={index} className=" text-white text-[12px] flex items-center w-full w-full gap-[20px]">
                <img src={value.icon} width={20} height={20} alt="loading" />
                <p>{value.name}</p>
            </motion.button>
        })}

    </aside>
  )
}
