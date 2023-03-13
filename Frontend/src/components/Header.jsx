import React from 'react'
import { Link } from 'react-router-dom'

const Header = () => {
  return (
    <header className="px-20 py-3 flex items-center justify-between bg-slate-400">
        <div className="flex items-center hover:scale-125">
            <div className="font-black"><svg 
                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-8 h-8 text-blue-600 cursor-pointer">
                <path fillRule="evenodd" d="M1 2.75A.75.75 0 011.75 2h16.5a.75.75 0 010 1.5H18v8.75A2.75 2.75 0 0115.25 15h-1.072l.798 3.06a.75.75 0 01-1.452.38L13.41 18H6.59l-.114.44a.75.75 0 01-1.452-.38L5.823 15H4.75A2.75 2.75 0 012 12.25V3.5h-.25A.75.75 0 011 2.75zM7.373 15l-.391 1.5h6.037l-.392-1.5H7.373zM13.25 5a.75.75 0 01.75.75v5.5a.75.75 0 01-1.5 0v-5.5a.75.75 0 01.75-.75zm-6.5 4a.75.75 0 01.75.75v1.5a.75.75 0 01-1.5 0v-1.5A.75.75 0 016.75 9zm4-1.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" clipRule="evenodd" />
                </svg>
            </div>
            <div className="font-extrabold cursor-pointer text-2xl">
                <Link to="/">
                <span className="text-blue-600">DAN</span><span className="text-gray-600">BILL</span>
                </Link>
            </div>
        </div>
        <div className="font-bold">
            <ul className="flex text-gray-600">
                <Link to="/" className="px-4 cursor-pointer hover:scale-125 hover:underline underline-offset-8">HOME</Link>
                <Link to="/about" className="px-4 cursor-pointer hover:scale-125 hover:underline underline-offset-8">ABOUT</Link>
                <Link to="/product" className="px-4 cursor-pointer hover:scale-125 hover:underline underline-offset-8">PRODUCT</Link>
                <Link to="/faq" className="px-4 cursor-pointer hover:scale-125 hover:underline underline-offset-8">FAQ</Link>
            </ul>
        </div>
        <div className="flex font-bold text-gray-600">
            <Link to="/login" className="px-2 border-2 mx-2 rounded-md py-2 cursor-pointer shadow-md shadow-gray-600 hover:scale-125">LOG IN</Link>
            <Link to="/register" className="px-2 border-2 mx-2 rounded-md py-2 cursor-pointer shadow-md shadow-gray-600 hover:scale-125">REGISTER</Link>
        </div>
    </header>

    
  )
}

export default Header