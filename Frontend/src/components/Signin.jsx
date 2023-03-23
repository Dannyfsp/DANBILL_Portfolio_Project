import React from 'react'

const Signin = () => {
  return (
    <div className="border border-gray-300 rounded-lg shadow-lg mx-auto my-8 max-w-md p-8 w-full h-full mt-28">
        <div>
            <h1 className="font-semibold text-2xl text-center mb-10 text-gray-600 mt-4">LOGIN</h1>
         </div>
        <form>
            <div className="mb-5">
                <div><label>Email</label></div>
                <div><input type="email" placeholder='Enter your Email address' className="border w-full outline-none py-1"/></div>
            </div>
            <div className="mb-5">
                <div><label>Password</label></div>
                <div><input type="password" placeholder='Enter your password' className="border w-full outline-none py-1"/></div>
            </div>
            <button className="w-full border border-gray-200 shadow-sm bg-blue-500 py-3 text-white rounded-sm hover:bg-blue-700 mb-5">LOGIN</button>
        </form>
    </div>
  )
}

export default Signin