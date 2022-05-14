import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import Navbar from '../components/navbar'
import {useState} from 'react'
import {useRouter} from 'next/router'

const Admissions = () => {
    const router = useRouter()
        const handleSubmit = async (event) => {
            event.preventDefault()

            const data = {
              name: event.target.name.value,
              email: event.target.email.value,
              phone: event.target.phone.value,
              experience_level: event.target.experience_level.value,
            }

            const JSONdata = JSON.stringify(data)
            console.log(JSONdata);

            const endpoint = 'http://127.0.0.1:8000/api/v1/admission/'

            const options = {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSONdata,
            }

            const response = await fetch(endpoint, options)
            const result = await response.json()
            alert(`Your Data was submitted, You will receive an email confirmation.`)
            router.push("/")
          }

  return (
    <>

    <Head>
      <title>Kyushuzumo - Contact</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
    </Head>

    <Navbar />
      <h1 className="p-2 m-2 font-bold text-3xl text-center">Admission form</h1>
      <div className="p-2 m-2 flex flex-wrap justify-center">
               <form onSubmit={handleSubmit}>
                  <div className="mb-6">
                     <input
                        type="text"
                        placeholder="Your Name"
                        name="name"
                        className="
                        w-full
                        rounded
                        py-3
                        px-[14px]
                        text-body-color text-base
                        border border-[f0f0f0]
                        outline-none
                        focus-visible:shadow-none
                        focus:border-primary
                        "
                        required
                        />
                  </div>
                  <div className="mb-6">
                     <input
                        type="email"
                        name="email"
                        placeholder="Your Email"
                        className="
                        w-full
                        rounded
                        py-3
                        px-[14px]
                        text-body-color text-base
                        border border-[f0f0f0]
                        outline-none
                        focus-visible:shadow-none
                        focus:border-primary
                        "
                        required
                        />
                  </div>
                  <div className="mb-6">
                     <input
                        type="text"
                        name="phone"
                        placeholder="Your Phone"
                        className="
                        w-full
                        rounded
                        py-3
                        px-[14px]
                        text-body-color text-base
                        border border-[f0f0f0]
                        outline-none
                        focus-visible:shadow-none
                        focus:border-primary
                        "
                        required
                        />
                  </div>

                   <div className="mb-6">
                     <input
                        type="text"
                        name="experience_level"
                        placeholder="Beginner/Intermediate/Advanced/Pro"
                        className="
                        w-full
                        rounded
                        py-3
                        px-[14px]
                        text-body-color text-base
                        border border-[f0f0f0]
                        outline-none
                        focus-visible:shadow-none
                        focus:border-primary
                        "
                        required
                        />
                  </div>
                      <button
                        type="submit"
                        className="
                        w-full
                        text-white
                        bg-blue-600
                        rounded
                        border border-primary
                        p-3
                        transition
                        hover:bg-blue-800
                        "
                        >
                     Send Message
                     </button>
 
              </form>

      </div>
      </>
  )
}

 
export default Admissions
