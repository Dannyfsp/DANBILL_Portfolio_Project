import React from 'react'
import { Link } from 'react-router-dom'
import andriod from '../assets/android.png'
import apple from "../assets/apple.png"
import dell from "../assets/dell.png"
import hp from "../assets/hp.png"
import lg from "../assets/lg.png"
import samsung from "../assets/samsung.png"

const About = () => {
  return (
    <div className="px-20">
        <div className="flex flex-col border shadow-md mx-20 my-10 px-20">
            <div className="flex items-center justify-center font-bold text-4xl mt-3">
              <h1 className="text-blue-700">Home of top-notch devices</h1>
            </div>
            <div className="flex min-h-10 justify-around my-4 mb-8">
                <div><img src={lg} alt="lg-img" className="w-10 h-10" /></div>
                <div><img src={hp} alt="hp-img" className="w-10 h-10" /></div>
                <div><img src={andriod} alt="android-img" className="w-10 h-10" /></div>
                <div><img src={apple} alt="apple-img" className="w-10 h-10 " /></div>
                <div><img src={dell} alt="dell-img" className="w-10 h-10" /></div>
                <div><img src={samsung} alt="samsung-img" className="w-10 h-10" /></div>
            </div>
        </div>
        <div className="flex flex-col items-center justify-center mx-20 my-8 px-20">
            <div className='flex font-bold text-xl'>
              <h1 className="text-blue-600">Buy with ease, Sell with ease 😊</h1>
            </div>
            <div className='text-xl flex flex-col items-center justify-center'>
              <p className='text-gray-700 font-semibold'>Are you looking for where to purchase your devices or where to sell your devices?</p>
              <p className='text-gray-700 font-semibold'>Worry no more cos we got you covered</p>
              <p className='text-gray-700 font-semibold'>Wait no longer and click the button below to Register!</p>
            </div>
            <div>
              <button className="w-full text-4xl text-white border-4 shadow-md rounded-full px-10 py-5 m-4 bg-blue-500 hover:scale-125 hover:bg-blue-700">
                 <Link to="/register">REGISTER</Link> 
              </button>
            </div>
        </div>
    </div>
  )
}

export default About