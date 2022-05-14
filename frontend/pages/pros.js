import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import Navbar from '../components/navbar'
import {useState} from 'react'
import {useRouter} from 'next/router'

const myLoader = ({ src, width, quality }) => {
    return `${src}?w=${width}&q=${quality || 75}`
}

const Pros = ({ pros }) => {
    const router = useRouter()
        const handleSubmit = async (event) => {
            event.preventDefault()

            const data = {
              search: event.target.search.value,
            }

            const JSONdata = JSON.stringify(data)
            console.log(JSONdata);

            const endpoint = 'http://127.0.0.1:8000/api/v1/search/'

            const options = {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSONdata,
            }

            const response = await fetch(endpoint, options)
            const result = await response.json()
            router.push("/")
          }


  return (
    <>
    <Head>
      <title>Kyushuzumo - Pros</title>
        <meta charSet="utf-8" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
    </Head>

    <Navbar />

      <form className="flex p-2 m-2" onSubmit={handleSubmit}>
         <input
            type="text"
            placeholder="Search"
            name="search"
            className="
            w-full
            rounded
            py-3 m-2
            px-[14px]
            text-body-color text-base
            border border-[f0f0f0]
            outline-none
            focus-visible:shadow-none
            focus:border-primary
            "
            required
            />
              <button
                type="submit"
                className="
                w-full
                text-white
                bg-blue-600
                rounded
                border border-primary
                p-3 m-2
                transition
                hover:bg-blue-800
                max-w-min
                "
                >
             Search
             </button>

      </form>

          <div className="bg-gray-100 justify-center p-2 m-2 flex flex-wrap">
          {pros.map((pro) => (
                      <div key={pro.id}>
        <div className="p-2 m-2 border rounded bg-gray-50 flex flex-wrap justify-between">

        <Image 
            loader={myLoader}
            src={pro.image}
            alt="Picture of the pro"
            width={500}
            height={400}
        />

        <div className="p-2 m-2 grid grid-cols-2 bg-gray-50">

        <h1 className="text-3xl font-bold text-center p-2 m-2 col-span-2">{pro.name}</h1>
        <p className="bg-gray-200 text-gray-600 p-2 m-2 rounded col-span-1">Origin: {pro.place_of_birth}</p>
        <p className="bg-gray-200 text-gray-600 p-2 m-2 rounded col-span-1">DOB: {pro.date_of_birth}</p>
        <p className="bg-gray-200 text-gray-600 p-2 m-2 rounded col-span-1">Height: {pro.height}cm</p>
        <p className="bg-gray-200 text-gray-600 p-2 m-2 rounded col-span-1">Weight: {pro.weight} kg</p>
        <p className="bg-gray-200 text-gray-600 p-2 m-2 rounded col-span-1">Record: {pro.wins}-{pro.no_contest}-{pro.losses}</p>
        <p className="bg-gray-200 text-gray-600 p-2 m-2 rounded col-span-1">Rank: {pro.rank}</p>
        <p className="bg-gray-200 text-gray-600 p-2 m-2 rounded col-span-1 max-w-md">Championships: {pro.championships}</p>

    </div>
    </div>
    </div>

            ))}
          </div>
    </>
  )
}

// This gets called on every request
 export async function getStaticProps() {
  // Fetch data from external API
  const res = await fetch('http://127.0.0.1:8000/api/v1/pros/')
  const pros = await res.json()

// Pass data to the page via props
  return { props: { pros, }, }
}

export default Pros
