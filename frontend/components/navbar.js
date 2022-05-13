import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'

const Navbar = () => {
  return (
    <>
    <div className="flex flex-wrap bg-blue-600 text-white font-bold text-xl items-center justify-between">
    <Image src="/images/logo.png" alt="Logo" width="140px" height="120px"/>

        <ul className="flex flex-wrap p-4">

            <li className="p-1 m-1 ">
               <Link href="/">
                <a>Home</a>
                </Link>
            </li>

            <li className="p-1 m-1 ">
               <Link href="/pros">
                <a>Pros</a>
                </Link>
            </li>

            <li className="p-1 m-1 ">
               <Link href="/contact">
                <a>Contact</a>
                </Link>
            </li>

        <li className="p-1 m-1 ">
               <Link href="/facilities">
                <a>Facilities</a>
                </Link>
            </li>

        <li className="p-1 m-1 ">
               <Link href="/admissions">
                <a>Admissions</a>
                </Link>
            </li>

        <li className="p-1 m-1 ">
               <Link href="/gallery">
                <a>Gallery</a>
                </Link>
            </li>

        </ul>
        
    </div>

    </>
  )
}

export default Navbar
