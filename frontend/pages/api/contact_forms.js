export default function handler(req, res) {
  // Get data submitted in request's body.
  const body = req.body

  // Optional logging to see the responses
  // in the command line where next.js app is running.
  console.log('body: ', body)

  // Sends a HTTP success code
  res.status(200).json({ data: `${body.first} ${body.last}` })
}

