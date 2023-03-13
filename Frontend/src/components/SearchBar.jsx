import React from 'react'
import { Link } from 'react-router-dom'
import { FiSearch } from "react-icons/fi"
import { MdFavorite} from "react-icons/md"
import { FaShoppingCart, FaUserAlt } from "react-icons/fa"
const SearchBar = () => {
  const links = [
    {
      name: "Category A", 
      to:"/categorya"
    },
    {
      name: "Category B", 
      to:"/categoryb"
    },
    {
      name: "Category C", 
      to:"/categoryc"
    },
    {
      name: "Category D", 
      to:"/categoryd"
    },

]

  return (
    <div className='bg-slate-600 px-20 flex justify-between items-center sticky'>
        <div className=''>
            
            <select className='text-lg border px-4'>
                  {links.map(link => (<option><Link to={link.to} className="">{link.name}</Link></option>))}
            </select>
              
        </div>
        <form className='flex items-center bg-white h-10 justify-between rounded-2xl p-4 my-3 w-1/2'>
            <input type="text" placeholder='Search anything you are looking for' className='w-full'/>
          <button className='pl-4'>
            <FiSearch  className='hover:scale-150 text-blue-600'/>
          </button>
        </form>
        <div className='flex justify-around text-blue-800'>
          <div>
            <MdFavorite className='text-4xl mr-4 cursor-pointer hover:scale-150'/>
          </div>
          <div>
            <FaShoppingCart className="text-4xl mr-4 cursor-pointer hover:scale-150"/>
          </div>
          <div>
            <FaUserAlt className="text-4xl cursor-pointer hover:scale-150"/>
          </div>
        </div>
    </div>
  )
}

export default SearchBar