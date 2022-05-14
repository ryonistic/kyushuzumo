import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import Navbar from '../components/navbar'


export default function Home() {
  return (
    <>
    <Head>
      <title>Kyushuzumo - Home</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
    </Head>

    <Navbar />
    <div className="p-2 m-2 2xl:grid 2xl:grid-cols-2 md:flex sm:flex xl:flex sm:flex-wrap md:flex-wrap xl:flex-wrap">

      <Image className="col-span-1 col-start-1" src="/images/banner.jpg" width="1440px" height="870px" alt="banner image"/>

      <div className="grid grid-cols-3 px-4 mx-4 col-start-2 col-span-1 ">
        <h1 className="font-bold text-3xl text-gray-800 col-span-1 col-start-2 p-2 text-center">Miyazuki Honbasho</h1>
        <p className="text-lg text-gray-700 col-span-3 col-start-1 max-w-4xl">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In fermentum et sollicitudin ac. Lorem ipsum dolor sit amet consectetur adipiscing elit duis. Sit amet tellus cras adipiscing enim eu turpis egestas. Eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus. Rhoncus urna neque viverra justo nec ultrices dui. Mauris ultrices eros in cursus turpis. Nisi porta lorem mollis aliquam ut porttitor leo a diam. Eu facilisis sed odio morbi. Feugiat nibh sed pulvinar proin gravida hendrerit lectus a. Dictum sit amet justo donec enim. Congue quisque egestas diam in arcu cursus. In iaculis nunc sed augue lacus viverra vitae congue eu. Posuere sollicitudin aliquam ultrices sagittis. Pharetra sit amet aliquam id diam maecenas ultricies. Id ornare arcu odio ut. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor. Massa ultricies mi quis hendrerit dolor magna eget est. Vitae proin sagittis nisl rhoncus mattis rhoncus urna neque. Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi.
        </p><p className="text-lg text-gray-700 col-span-3 col-start-1 max-w-4xl">
            Nibh mauris cursus mattis molestie a iaculis at erat pellentesque. Facilisi etiam dignissim diam quis enim. Duis tristique sollicitudin nibh sit amet commodo nulla facilisi nullam. Scelerisque felis imperdiet proin fermentum. Neque volutpat ac tincidunt vitae semper quis. Tellus at urna condimentum mattis. Arcu ac tortor dignissim convallis. Est lorem ipsum dolor sit amet consectetur. Enim eu turpis egestas pretium aenean. Enim neque volutpat ac tincidunt vitae semper quis lectus. Consequat interdum varius sit amet mattis vulputate enim nulla. Luctus venenatis lectus magna fringilla urna porttitor. Diam vel quam elementum pulvinar etiam non quam. Etiam non quam lacus suspendisse faucibus interdum posuere. Eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum.
          </p>
      </div>

    </div>
    
    <div className="flex flex-wrap justify-center">
    <Link href="/admissions">
    <a>
      <button className="p-4 m-2 font-semibold text-white bg-blue-600 rounded text-xl transition hover:bg-blue-800">Apply Now</button>
    </a>
    </Link>
    
    </div>
    <div className="p-2 m-2 flex flex-wrap">

    
    </div>
    </>
  )
}
