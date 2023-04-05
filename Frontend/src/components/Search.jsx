import React from 'react'
import { FiSearch } from "react-icons/fi"
import { MdFavorite} from "react-icons/md"
import { FaShoppingCart, FaUserAlt } from "react-icons/fa"
const Search = () => {

  return (
    <div className='bg-slate-600 px-20 flex justify-between items-center sticky top-0'>
        <div className='text-blue-800'>
            <FaUserAlt className="text-4xl cursor-pointer hover:scale-150"/>
              
        </div>
        <div className='flex items-center bg-white h-10 justify-between rounded-2xl p-4 my-3 w-1/2'>
            <input type="search" placeholder='Search anything you are looking for' className='w-full py-1.5 outline-none relative'/>
          <button className='pl-4'>
            <FiSearch  className='hover:scale-150 text-blue-600'/>
          </button>
        </div>
        <div className='flex justify-around text-blue-800'>
          <div>
            <MdFavorite className='text-4xl mr-4 cursor-pointer hover:scale-150'/>
          </div>
          <div>
            <FaShoppingCart className="text-4xl mr-4 cursor-pointer hover:scale-150"/>
          </div>
        </div>
    </div>
  )
}

export default Search